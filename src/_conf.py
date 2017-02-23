# -*- coding: utf-8 -*-  

"""
_conf.py
~~~~~~~~

Provides Viki configuration information.

:license: Apache2, see LICENSE for more details. 
"""

__config_home__ = "/usr/local/viki"
__config_jobs_dir__ = __config_home__ + "/" + "jobs"
__config_filename__ = "viki.json"
__config_file_path__ = __config_home__ + "/" + __config_filename__
__logfile_path__ = __config_home__ + "/" + "logs"

__all__ = ["__config_home__", "__config_jobs_dir__", "__config_filename__", "__config_file_path__", "__logfile_path__" ]