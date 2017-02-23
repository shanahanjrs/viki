# -*- coding: utf-8 -*-  

""" 
app.py
 ~~~~~~~~~~~~~~~~

  This module implements the App class for main application details and system checks / maintenance.
:license: Apache2, see LICENSE for more details. 
"""

# --- Imports

import os
import src._version
import src._conf


class App():
    """ Application library for viki """

    def __init__(self):
        """ Initialize Application configuration
        Uses 2 main files; _version, and _conf
        """

        # Provide version
        self.version = src._version.__version__

        # Viki home directory
        self.home = src._conf.__config_home__

        # Path to the jobs directory
        self.jobs_path = src._conf.__config_jobs_dir__

        # Name of viki conf file
        self.job_config_filename = src._conf.__config_filename__

        # Abs path to conf file
        self.job_config_path = src._conf.__config_file_path__

        # Abs path to logs file
        self.logfile_path = src._conf.__logfile_path__

        # File permissions
        self.file_perms = 0o755


    def check_system_setup(self):
        """ This will be run every time viki starts up
        It will check to make sure the home directory exists,
        the configuration file in viki-home exists, and
        that the jobs directory exists.
        If those are not setup correctly you will need to run viki with sudo to create them.
        """
        dirs = [self.home, self.jobs_path, self.job_config_path]

        for j in dirs:
            if not os.path.exists(j):
                return False

        return True


    def create_home_dir(self):
        """ Creates the home directory """
        print('Creating home directory...')

        if not self.home:
            return False

        if os.path.exists(self.home):
            return False

        os.mkdir(self.home, mode=self.file_perms)

        return True


    def generate_config_file(self):
        """ Generates a starter viki configuration file """
        print('Generating configuration file...')

        if not self.job_config_path:
            return False

        if os.path.exists(self.job_config_path):
            return False

        tmp_conf_file = """
        {
            "name": "viki"
        }
        """

        with open(self.job_config_path, mode='w', encoding='utf-8') as conf_file_obj:
            conf_file_obj.write(tmp_conf_file)
            conf_file_obj.close()

        os.chmod(self.job_config_path, mode=self.file_perms)

        return True


    def generate_log_file(self):
        """ Generates a blank viki log file """
        print('Generating log file...')

        if not self.logfile_path:
            return False

        if os.path.exists(self.logfile_path):
            return False

        tmp_logfile = ''

        with open(self.logfile_path, mode='w', encoding='utf-8') as logfile_obj:
            logfile_obj.write(tmp_logfile)
            logfile_obj.close()

        os.chmod(self.logfile_path, mode=self.file_perms)

        return True


    def create_jobs_dir(self):
        """ Create the jobs directory under viki home """
        print('Creating jobs directory...')

        if not self.jobs_path:
            return False

        if os.path.exists(self.jobs_path):
            return False

        os.mkdir(self.jobs_path, mode=self.file_perms)

        return True