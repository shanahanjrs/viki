from modules.jobs import Jobs
import uuid

job = Jobs()

### Test private functions

def test_quote_string_single_quotes():

    test_variables = [
        'x', '"x', 'x""x', ' -- x', '\'\'\n'
    ]

    for var in test_variables:
        assert job._quote_string(var) == "'" + var + "'"


def test_quote_string_double_quotes():

    test_variables = [
        'x', '"x', 'x""x', ' -- x', '\'\'\n'
    ]

    for var in test_variables:
        assert job._quote_string(var, SingleQuote=False) == '"' + var + '"'


def test_write_job_file():

    job_file_path = '/tmp/pytest-job-file.txt'
    job_file_text = 'This is a test message'

    assert job._write_job_file(job_file_path, job_file_text) is not None


def test_read_job_file():

    job_file_path = '/tmp/pytest-job-file.txt'
    job_file_text = 'This is a test message'

    assert job._read_job_file(job_file_path) is not None

    assert job._dirty_rm_rf(job_file_path) is not None


def test_run_shell_command():

    command = "echo Shanahanjrs @0xJRS"
    tmp_filename = '/tmp/pytest-job-run-file.txt'

    assert job._run_shell_command(command, tmp_filename) == (True, 0)

    assert job._dirty_rm_rf(tmp_filename) is not None

### Test public functions

def test_get_jobs():

    assert job.get_jobs()["success"] == 1


def test_create_job():

    job_name = 'viki-pytest-job-00'
    job_steps = ["echo Shanahanjrs", "pwd", "uname -a"]
    job_config = {"description":"This is my test job", "steps":job_steps}

    assert job.create_job(job_name, job_config)["success"] == 1


def test_get_job_by_name():

    job_name = 'viki-pytest-job-00'

    assert job.get_job_by_name(job_name)["success"] == 1


def test_update_job_by_name():

    job_name = 'viki-pytest-job-00'

    assert job.update_job(job_name)["message"] == "-- Under Construction --"


def test_delete_job_by_name():

    job_name = 'viki-pytest-job-00'

    assert job.delete_job(job_name)["success"] == 1
