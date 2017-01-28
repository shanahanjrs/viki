#!/usr/bin/env python3

import os

class Jobs():
    """ Jobs library for viki """

    ## Jobs internals

    def __init__(self):
        """ Initialize jobs handler """

        # Change to just /home/viki eventually
        self.home = "/usr/local/viki"

        # Path to the jobs directory relative to self.home
        self.jobspath = self.home + "/" + "jobs"

        # Name of a jobs config file
        self.jobConfigFile = 'config.json'

    def _writeJobFile(self, file, text):
        if not file or not text:
            return False

        with open(file, 'w') as fileObj:
            fileObj.write(text)

        return fileObj.close()


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


    def createJob(self, name, jsonText):
        """ Adds a job """

        jobDir = self.jobspath + "/" + name
        jobFilename = jobDir + "/" + jsonText

        # Remove existing job dir and files if it exists
        if os.path.exists(jobDir):

            for file in os.listdir(jobDir):

                # If file
                if os.path.isfile(jobDir + "/" + file):
                    os.remove(jobDir + "/" + file)

                # If directory
                if os.path.isdir(jobDir + "/" + file):
                    os.rmdir(jobDir + "/" + file)

            # Then the now-empty directory
            os.remove(jobDir)

        # Create job directory
        os.makedirs(jobDir)
        self._writeJobFile(jobFilename, jsonText)

        ret = {"success":"1", "message":"Job created"}
        return ret


    def updateJob(self, name):
        """ Update an existing job """
        success = "1"
        message = "Run successful"

        return { "success":success, "message":message }


    def runJob(self, name):
        """ Run a specific job """
        success = "1"
        message = "Run successful"


        return { "success":success, "message":message }