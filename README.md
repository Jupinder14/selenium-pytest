# Automated e2e tests using Selenium with python and pytest

This project contains automated tests for carbohydrate calculator using python-behave
This is the link to application: https://www.calculator.net/carbohydrate-calculator.html

### To run tests locally

In order to run tests manually, first install requirements from project root

`pip install -r requirements.txt`

To run tests

`pytest --alluredir=reports/allure-results`

### Tests running in pipeline

A workflow is added to run with Github Actions every time a new change is made.
You can check the workflow file under .github/workflows

On every pull request, the workflow will run an it can be seen on Github Actions page.
https://github.com/Jupinder14/selenium-pytest/actions

### Reporting

An Allure report is deployed to github pages on every test run.
You can check the latest report at https://jupinder14.github.io/selenium-pytest

