# Final Exam Grade Calculator Web App Deployed to Azure using CI/CD
### Status ..
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![run-tests](../../actions/workflows/build_deploy.yml/badge.svg)](../../actions/workflows/build_deploy.yml)
![up badge](https://img.shields.io/website-up-down-green-red/http/webapp-xiezc3pdz7pmo.azurewebsites.net.svg)

This repo contains the source code for a Final Exam Grade Calculator,
something that many college (and high school) students use.

This calculator allows you to calculate the required Final Exam grade to meet
a desired course grade, based on the current course grade and the weight of
the final exam (the percent of the course grade determined by the final).

The app is deployed using GitHub CI/CD to Azure. The website can be found here:
https://webapp-xiezc3pdz7pmo.azurewebsites.net/. The site is hosted with
Microsoft's free tier Azure plan for students, so I can't guarantee anything
with regards to uptime.

## Running Locally

1. If you have not already, install a Python version that supports Streamlit
(as of 2024-04-18, Python 3.8 to 3.12).
2. Create a Python virtual environment: `python -m venv <environment name>`
3. Activate the virtual environment:
    - Windows Command Prompt: `<environment name>\Scripts\activate.bat`
    - Windows Powershell: `<environment name>\Scripts\Activate.ps1`
    - UNIX-Like: `source <environment name>/bin/activate` - you may have to
        use a different file to match your shell
4. Then, run `pip install -r requirements.txt` to install all the requirements.
5. Execute `streamlit run src/app.py`
