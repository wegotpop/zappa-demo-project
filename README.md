# POP Zappa demo

Build and deploy your own Zappa AWS Lambda web service

## Requirements

* Python 3.6.1

## Virtualenv setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r dev_requirements.txt

## Test the application

Run: `python app/app.py`

The visit http://localhost:5000

You should see a JSON document that reads "Hello world!"

## Deploy the application

Edit the `zappa_settings.yaml` file can change the project name (I would suggest changing POP to your POP username).

Run: `zappa deploy dev`

Zappa will now create some resources on AWS. It will then spit out a link to your new application. Put the link in the browser to see your internet-deployed application!

## Modifying the application

Add a new key-value to the payload dictionary in the application.

Update the deployment: `zappa update dev`

Reload the URL, your change should be visible