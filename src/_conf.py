"""
Provides Viki configuration information.
"""

__config_home__ = "/usr/local/viki"
__config_jobs_dir__ = __config_home__ + "/" + "jobs"
__config_filename__ = "viki.json"
__config_file_path__ = __config_home__ + "/" + __config_filename__
__logfile_path__ = __config_home__ + "/" + "logs"

__all__ = ["__config_home__", "__config_jobs_dir__", "__config_filename__", "__config_file_path__", "__logfile_path__" ]