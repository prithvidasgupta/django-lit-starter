# Django + Lit Starter Project

# Prerequisites
- Python 3.11+
- NodeJS 20+
- A modern web browser (Firefox/Chrome)
- Homebrew (to run `brew` commands) (on Mac)
- (Optional) Postman REST API Client

Use tools like `pyenv` and `nvm` to easily manage Python and NodeJS runtimes.

This project will use Django and Lit elements to generate a simple hello world page that changes message on random reloads and a counter button.

Run these commands in exact sequence for installation of libraries

1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd js && npm i && cd ..`
5. `sudo chmod 755 build-js`
6. (MacOS only) `brew install watch`

Run the hello world Django+Lit starter project using `python manage.py runserver`.

The terminal logs still look weird but that is not something to worry about (atleast right now).

Check out `manage.py` and `build-js` to see how I built the Lit component using esbuild.

Some code for Django taken/inspired from the MDN tutorial and `csev/dj4e-samples`.
