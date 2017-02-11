#!/usr/bin/env python3

import src._version
import src._conf

class App():
    """ Jobs library for viki """

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

        # Name of viki configuration file
        self.job_config_filename = src._conf.__config_filename__