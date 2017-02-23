# -*- coding: utf-8 -*-  

""" 
api_blueprint.py
 ~~~~~~~~~~~~~~~~

  This module implements the main Job api for Viki.
:license: Apache2, see LICENSE for more details. 
"""

# --- Imports

from flask import Blueprint, jsonify, request
from src.job.job import Job

# --- Vars
blueprint_name = 'api_blueprint'
template_folder_name = 'templates'

job = Job()

api_blueprint = Blueprint(blueprint_name, __name__,
                          template_folder=template_folder_name)

# --- Api endpoints

@api_blueprint.route("/jobs")
def jobs():
    """ List all jobs """

    ret = jsonify(job.get_jobs())

    return ret


@api_blueprint.route("/job/<string:job_name>", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def get_job(job_name):
    """ Show single job details by name """

    ret = None

    if request.method == 'GET':
        # Retrieve a jobs details
        ret = job.get_job_by_name(job_name)

    if request.method == 'POST':
        # Requires "application/json" mime type and valid JSON body
        # containing description, and steps
        job_config = str(request.get_json())
        ret = job.create_job(job_name, job_config)

    if request.method == 'PUT':
        # Requires "application/json" mime type and valid JSON body
        # containing field/s to be updated
        ret = job.update_job(job_name)

    if request.method == 'DELETE':
        # Deletes a job from the repository
        ret = job.delete_job(job_name)

    if ret is None:
        ret = {"success":0, "message":"Failed"}

    return jsonify(ret)


@api_blueprint.route("/job/<string:job_name>/run", methods = ['POST'])
def run_job(job_name):
    """ Run specific job by name """

    return jsonify(job.run_job(job_name))


@api_blueprint.route("/the3laws")
def the_three_laws():
    """ The three laws of robotics """
    return jsonify('A robot may not injure a human being or, through inaction, allow a human being to come to harm. ' +
        'A robot must obey the orders given it by human beings except where such orders would conflict with the First Law. ' +
        'A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.')