# SWEproject
[![TeamGlab](https://circleci.com/gh/TeamGlab/SWEproject.svg?style=shield)](https://app.circleci.com/pipelines/github/TeamGlab/SWEproject)

# Run locally:
(The following steps assume python/pip 3 by default, but you may have to replace each occurence with python3/pip3)
1. Make sure you have Python 3 installed on your machine
2. Make sure you have Django installed (pip install django should be sufficient, though you may want to use a virtual environment)
3. Go into the top level UFSailWebsite directory (`cd UFSailWebsite`)
4. Run `python manage.py runserver`
5. Navigate to http://localhost:8000 (or http://127.0.0.1:8000) in your browser

# Testing notes:
CircleCI is set up to automatically run tests and store the results. You can see these online on the tests tab under a job\
(for example, see https://app.circleci.com/pipelines/github/TeamGlab/SWEproject/20/workflows/bfcde501-457b-4c01-8375-648470840b26/jobs/21/tests)

You can also view the xml output on the artifacts tab\
(for example, see https://app.circleci.com/pipelines/github/TeamGlab/SWEproject/20/workflows/bfcde501-457b-4c01-8375-648470840b26/jobs/21/artifacts)

To run locally, cd into UFSailWebsite and run `python manage.py test`\
You can append `-v 2` to this command in order to see test cases listed (and some other information)
