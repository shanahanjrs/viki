#!/usr/bin/env python3

"""
Viki daemon
~~~~~~~~~~~

The automation framework

Usage:
    jobs
    job/<jobName>
    job/<jobName>/run

Maintainer:
    John Shanahan <shanahan.jrs@gmail.com>

License:
    Apache 2.0
    http://www.apache.org/licenses/LICENSE-2.0

"""


# --- Imports


try:
    from flask import Flask, request, jsonify, render_template
    from src.job.job import Job
    from src.application.app import App
    import os
    import sqlite3
    import logging
except ImportError as error:
    exit('ImportError: ' + str(error))


# --- Setup


debug = True

# --- Classes / globals


app = Flask(__name__)
viki_app = App()
job = Job()
version = viki_app.version

home_directory = "/usr/local/viki"
log_dir = "/usr/local/viki/logs"
log_file = log_dir + "/" + "viki.log"
log_level = logging.WARNING

# Sqlite
# sqlite_file = "/path/to/sqlite3/file"

# sqlite_connection = sqlite3.connect(sqlite_file)
# sqlite = sqlite_connection.cursor()


# --- Routes


@app.route("/")
def root():
    """ Home """
    logging.info('--> Func:root')

    ret = {"name": "viki", "version": version}

    return render_template('home.html', data=ret)


# --- Import other Routes (Api, custom routes)


# main api
from src.blueprints import api_blueprint
app.register_blueprint(api_blueprint.api_blueprint)


# Custom route blueprints go here.
# from src.blueprints import YOURBLUEPRINT
# app.register_blueprint(YOURBLUEPRINT.BLUEPRINTNAME)


# --- Main


if __name__ == "__main__":

    # --- Pre
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)

    logging.basicConfig(filename=log_file, level=log_level)

    # --- Start
    if debug:
        # Set debug options
        app.debug = True
        log_level = logging.DEBUG

    app.run()