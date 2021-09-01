# Code challenge - The eye

## Objective
The objective of this repo is to code the challenge in [the-eye.md](the-eye.md)

## Assumptions && Decisions
- I assumed that Session and Application entities doesn't needed to be modeled because there aren't not enough information about both. 
- Even though only Create operation were required for this challenge, I maintained Read, Update and Delete operations possible to the Event model.
- Assuming 'The Eye' will communicate over HTTPS and by a frontend application.
- I did a load test to assure 'The Eye' can handle at least 100 requests/s as required.
- To avoid race conditions, I used `select_for_update` method on viewset implementation. There are other approaches to solve that like `F()` expressions.
- I used sqlite3 as database to focus only on the challenge requirements. For production environment, we could choose a robust database like MySQL, PostgreSQL, etc.
- `select_for_update` just work for big databases like Postgres, MySQL. So I'm assuming one of them would be used for this application instead of sqlite3
- Assuming all the tests will run in a CI/CD pipeline.


## Requirements
- Pipenv
- Python3
- make


## Setup
To setup the project and download dependencies just run:
```
make setup
```
Expected output:
```
➜  ca-code-assigment git:(main) ✗ make setup
pipenv install --dev
Creating a virtualenv for this project...
Pipfile: /Users/fernandoteles/Documents/ca-code-assigment/Pipfile
Using /usr/bin/python3 (3.8.2) to create virtualenv...
⠼ Creating virtual environment...created virtual environment CPython3.8.2.final.0-64 in 847ms
  creator CPython3macOsFramework(dest=/Users/fernandoteles/.local/share/virtualenvs/ca-code-assigment-pAKBM2TQ, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/fernandoteles/Library/Application Support/virtualenv)
    added seed packages: pip==21.2.3, setuptools==57.4.0, wheel==0.37.0
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/fernandoteles/.local/share/virtualenvs/ca-code-assigment-pAKBM2TQ
Installing dependencies from Pipfile.lock (382326)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 46/46 — 00:00:45
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
pipenv run python application/manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, drf_api_logger, sessions, the_eye
Running migrations:
  No migrations to apply.
pipenv shell
Launching subshell in virtual environment...
 . /Users/fernandoteles/.local/share/virtualenvs/ca-code-assigment-pAKBM2TQ/bin/activate
➜  ca-code-assigment git:(main) ✗  . /Users/fernandoteles/.local/share/virtualenvs/ca-code-assigment-pAKBM2TQ/bin/activate
```

## Loadtest with [Locust](https://locust.io/)

[Loadtest output](application/the_eye/tests/load_test_report.html) run against django test server:
```
(ca-code-assigment) ➜  ca-code-assigment git:(main) ✗ locust -f application/the_eye/tests/load_test.py
[2021-08-31 21:04:05,893] Fernandos-MacBook-Pro.local/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
[2021-08-31 21:04:05,909] Fernandos-MacBook-Pro.local/INFO/locust.main: Starting Locust 2.1.0
[2021-08-31 21:05:06,695] Fernandos-MacBook-Pro.local/INFO/locust.runners: Ramping to 150 users at a rate of 50.00 per second
[2021-08-31 21:05:08,703] Fernandos-MacBook-Pro.local/INFO/locust.runners: All users spawned: {"WebsiteUser": 150} (150 total users)
KeyboardInterrupt
2021-09-01T00:09:15Z
[2021-08-31 21:09:15,123] Fernandos-MacBook-Pro.local/INFO/locust.main: Running teardowns...
[2021-08-31 21:09:15,123] Fernandos-MacBook-Pro.local/INFO/locust.main: Shutting down (exit code 1), bye.
[2021-08-31 21:09:15,123] Fernandos-MacBook-Pro.local/INFO/locust.main: Cleaning up runner...
 Name                                                                              # reqs      # fails  |     Avg     Min     Max  Median  |   req/s failures/s
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 POST /events/                                                                       4769    15(0.31%)  |      98       7    2753      24  |   91.87    0.29
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 Aggregated                                                                          4769    15(0.31%)  |      98       7    2753      24  |   91.87    0.29

Response time percentiles (approximated)
 Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 POST     /events/                                                                               24     38     58     84    310    480    860   1100   1900   2800   2800   4769
--------|--------------------------------------------------------------------------------|---------|------|------|------|------|------|------|------|------|------|------|------|
 None     Aggregated                                                                             24     38     58     84    310    480    860   1100   1900   2800   2800   4769

Error report
 # occurrences      Error
----------------------------------------------------------------------------------------------------------------------------------------------------------------
 14                 POST /events/: ConnectionError(MaxRetryError("HTTPConnectionPool(host='127.0.0.1', port=8080): Max retries exceeded with url: /events/ (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x1085b5760>: Failed to establish a new connection: [Errno 54] Connection reset by peer'))"))
 1                  POST /events/: ConnectionError(ProtocolError('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer')))
----------------------------------------------------------------------------------------------------------------------------------------------------------------
```


## Tests
To run the tests uses:
```
make tests
```

Expected output:
```
(ca-code-assigment) ➜  ca-code-assigment git:(main) ✗ make test
pushd application &&\
	pytest &&\
	popd
~/Documents/ca-code-assigment/application ~/Documents/ca-code-assigment
================================================================================ test session starts ================================================================================
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.10.0, pluggy-1.0.0 -- /Users/fernandoteles/.local/share/virtualenvs/ca-code-assigment-pAKBM2TQ/bin/python
cachedir: .pytest_cache
django: settings: application.settings (from ini)
rootdir: /Users/fernandoteles/Documents/ca-code-assigment, configfile: pytest.ini
plugins: cov-2.12.1, django-4.4.0
collected 2 items

the_eye/tests/event_model_tests.py::EventModelTestCase::test_can_create_event_model PASSED                                                                                    [ 50%]
the_eye/tests/event_viewset_tests.py::EventViewSetTests::test_create_event PASSED                                                                                             [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
the_eye/__init__.py                        0      0   100%
the_eye/admin.py                           1      0   100%
the_eye/migrations/0001_initial.py         6      0   100%
the_eye/migrations/__init__.py             0      0   100%
the_eye/models.py                          9      0   100%
the_eye/serializers.py                     6      0   100%
the_eye/tests/__init__.py                  0      0   100%
the_eye/tests/event_model_tests.py        10      0   100%
the_eye/tests/event_viewset_tests.py      14      0   100%
the_eye/views.py                           7      0   100%
--------------------------------------------------------------------
TOTAL                                     53      0   100%


================================================================================ slowest 5 durations ================================================================================
0.56s setup    application/the_eye/tests/event_model_tests.py::EventModelTestCase::test_can_create_event_model
0.37s call     application/the_eye/tests/event_viewset_tests.py::EventViewSetTests::test_create_event
0.10s call     application/the_eye/tests/event_model_tests.py::EventModelTestCase::test_can_create_event_model
0.00s teardown application/the_eye/tests/event_viewset_tests.py::EventViewSetTests::test_create_event
0.00s setup    application/the_eye/tests/event_viewset_tests.py::EventViewSetTests::test_create_event
=========================================================================== 2 passed, 2 warnings in 1.59s ===========================================================================
~/Documents/ca-code-assigment
```


## Run
To run the code use:
```
make run
```
Expected output:
```
(ca-code-assigment) ➜  ca-code-assigment git:(main) ✗ make run
python application/manage.py runserver 0.0.0.0:8080
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 31, 2021 - 22:42:03
Django version 3.2.6, using settings 'application.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
```

