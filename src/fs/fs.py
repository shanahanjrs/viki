# -*- coding: utf-8 -*-  

""" 
fs.py
 ~~~~~

Filesystem library - internal to Viki
:license: Apache2, see LICENSE for more details. 
"""

import ast
import os
import subprocess
import json
import uuid

class Fs():
    """ Filesystem library for viki """

    debug = False

    def __init__(self):
        """ Initialize jobs handler
        Vars for use:
        home: Viki's home directory. Usually /usr/local/viki
        jobs_path: Path to Viki's jobs directory. Usually /usr/local/viki/jobs
        job_config_filename: Name of the config for each individual job. Usually 'config.json'
        """

        # TODO Move this to a central place so all classes can use it

        # Change to just /home/viki eventually
        self.home = "/usr/local/viki"

        # Path to the jobs directory relative to self.home
        self.jobs_path = self.home + "/" + "jobs"

        # Path to the jobs STDOUT file
        self.job_output_file = "output.txt"

        # Name of job configuration file
        self.job_config_filename = "config.json"


    # --- Main library


    def write_job_file(self, file, text):
        """ _write_job_file
        Takes a filename and textblob and
        attempts to write the text to that file
        """

        if not file or not text:
            return False

        # This will not work if the directory does not exist
        with open(file, 'w') as file_obj:
            file_obj.write(json.dumps(text))
            file_obj.close()

        return True


    def read_job_file(self, file):
        """ _read_job_file
        Takes a job name (abs path) and returns the string version of .../jobs/job_name/config.json
        Filename must be the full path of the file, not just the name
        contents of that file or False if it does not exist
        """
        if not file:
            return False

        if not os.path.exists(file):
            return False

        with open(file, 'r') as file_obj:
            ret = file_obj.read()
            file_obj.close()

        return ret


    def dirty_rm_rf(self, dir):
        """ Executes a quick and dirty rm -rf dirName
        Use subprocess because its easier to let bash do this than Python
        """
        subprocess.call(
            [b'/bin/bash', b'-c', 'rm -rf ' + dir]
        )

        return True


    def job_exists(self, job_name):
        """ Simple internal function to quickly tell you if
        a job actually exists or not
        """
        return os.path.exists(self.jobs_path + '/' + job_name)


    def read_last_run_output(self, output_file_path):
        """ _read_last_run_output
        Takes output_file_path (abs path) and returns the entire output of the last job run's output
        """
        if not output_file_path:
            return False

        output_filename = output_file_path.split('/')[-1]

        # Check the file exists and is actually named correctly
        if not os.path.exists(output_file_path) or output_filename != self.job_output_file:
            return False

        with open(output_file_path, 'r') as file_obj:
            ret = file_obj.read()
            file_obj.close()

        return ret