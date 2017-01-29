#!/usr/bin/env python3

import os
import subprocess
import json
import uuid

class Jobs():
    """ Jobs library for viki """

    ## Jobs internals

    def __init__(self):
        """ Initialize jobs handler """

        # Change to just /home/viki eventually
        self.home = "/usr/local/viki"

        # Path to the jobs directory relative to self.home
        self.jobspath = self.home + "/" + "jobs"

        # Name of job configuration file
        self.jobConfigFile = "config.json"

    def _writeJobFile(self, file, text):
        """ _writeJobFile
        Takes a filename and textblob and
        attempts to write the text to that file
        """
        if not file or not text:
            return False

        with open(file, 'w') as fileObj:
            fileObj.write(text)

        return fileObj.close()

    def _readJobFile(self, file):
        """ _readJobFile
        Takes a filename and returns the string
        contents of that file or False if it does not exist
        """
        if not file:
            return False

        with open(file, 'r') as fileObj:
            ret = fileObj.read()
            fileObj.close()

        return ret

    def _runShellCommand(self, command, file):
        """ _runShellCommand
        string:command Shell command to run
        string:file path Where the command results (stdout) are stored
        Runs the given command and stores results in a file
        Returns Tuple (True|False, Return code)
        """
        print('----> _runShellCommand')
        print('----> Arg: command: ' + command)
        print('----> Arg: output file: ' + file)

        # This fixes Popen not correctly storing the output of
        # echo "some string" in the output file
        command = "'" + command + "'"
        print('----> command with single quotes: ' + command)

        # Generate output file for run results
        outputFile = open(file, 'a')

        process = subprocess.Popen(
            command,
            stdout=outputFile,
            stderr=subprocess.STDOUT,
            shell=True
        )

        while process.poll() is None:
            # Not finished
            pass

        # Close the file before exiting
        outputFile.close()

        # Get return code
        returnCode = process.poll()
        print('----> return code: ' + str(returnCode))

        return True if returnCode == 0 else False, returnCode

    def _dirtyRmRf(self, dir):
        """ Executes a quick and dirty rm -rf dirName """

        # Use subprocess because its easier to let bash do this than Python
        removeTmp = subprocess.call('rm -rf ' + dir, shell=True)


    ## Job functions

    def getJobs(self):
        """
        List jobs in ~/viki/jobs
        Takes no parameters
        """
        message = "Ok"
        success = "1"
        name = "jobs"
        jobsList = []

        try:

            # Get all job dirs
            jobsList = os.listdir(self.jobspath)

        except OSError as error:
            message = error.message
            success = "0"

        ret = { "success":success, "message":message, "name":name, "jobs":jobsList }

        return ret


    def getJobByName(self, name):
        """
        Get details of a single job by name
        string:name Name of specific job
        """
        success = "1"
        message = "Ok"
        contents = {}

        try:

            if name is None:
                raise ValueError('Missing required field: jobName')

            jobDir = self.jobspath + "/" + name

            if os.path.isdir(jobDir):
                with open(jobDir + "/" + self.jobConfigFile, 'r') as jobFile:
                    contents = jobFile.read()
            else:
                raise OSError('Job directory not found')

        except (OSError, ValueError) as error:
            success = "0"
            message = error.message

        return { "success":success, "message":message, "job":name, "exec":contents }


    def createJob(self, newName, jsonText):
        """ Adds a job """
        message = "Job created successfully"
        success = "1"

        try:

            jobDir = self.jobspath + "/" + newName
            jobFilename = jobDir + "/" + self.jobConfigFile

            # Remove existing job conf
            if os.path.exists(jobFilename):
                self._dirtyRmRf(jobFilename)

            # Create Json array for _writeJobFile
            jsonObj = json.loads(jsonText)
            jsonObj['runNumber'] = 0
            jsonObj['lastSuccessfulRun'] = 0
            jsonObj['lastFailedRun'] = 0
            jsonObj['name'] = newName
            jsonText = str(jsonObj)

            # Create job file
            self._writeJobFile(jobFilename, jsonText)

        except json.JSONDecoderError as error:
            message = error.message
            success = "0"

        ret = {"success":success, "message":message}

        return ret


    def updateJob(self, name):
        """ Update an existing job """
        success = "1"
        #message = "Run successful"
        message = "-- Under Construction --"

        return { "success":success, "message":message }


    def runJob(self, name):
        """ Run a specific job """
        success = "1"
        message = "Run successful"
        returnCode = 0

        # Create job directory and file path names
        jobDir = self.jobspath + "/" + name
        jobConfigJsonFile = jobDir + "/" + "config.json"

        try:

            # Check job directory exists
            # Otherwise raise OSError
            if not os.path.isdir(jobDir):
                raise OSError('Job not found')

            # Check config json file exists
            # Otherwise raise OSError
            if not os.path.isfile(jobConfigJsonFile):
                raise OSError('Job file not found')

            # Read the file and load the json inside it
            # Otherwise raise OSError
            jobJson = json.loads(self._readJobFile(jobConfigJsonFile))
            if jobJson is False or jobJson is None:
                raise OSError('Job file could not be read')

            # Generate a tmp directory to work in
            # Use uuid4() because it creates a truly random uuid
            # and doesnt require any arguments and uuid1 uses
            # the system network addr.
            tmpCwd = "/tmp/viki-" + str(uuid.uuid4())
            print('----> tmpdir: ' + tmpCwd)
            os.mkdir(tmpCwd)

            # Create filename path for output file
            # todo: Move this to store the output in a new directory
            # where it will not get removed after each run
            fileName = tmpCwd + "/" + "output.txt"

            # Grab the json array "steps" from
            # jobs/jobName/config.json file
            jobSteps = jobJson['steps']

            # Execute them individually
            # If any of these steps fail then we stop execution
            for step in jobSteps:

                # Debug output file **remove me eventually**
                fileName = "/usr/local/viki/jobs/testoutput.txt"

                successBool, returnCode = self._runShellCommand(step, fileName)

                if not successBool:
                    print('----> Job step failed: ' + str(step))
                    print('    ---> with exit code: ' + str(returnCode))
                    raise SystemError('Build step failed')

            # Clean up tmp workdir
            self._dirtyRmRf(tmpCwd)

        except OSError as error:
            message = error.message
            success = "0"
        except subprocess.CalledProcessError as error:
            message = error.message
            success = "0"
        except SystemError as error:
            message = error.message
            success = "0"

        return { "success":success, "message":message, "returnCode":returnCode }