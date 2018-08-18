# rover

Simple fetch from API and log to stdout - tests CI/CD with AWS

## App

This application builds a very simple serverless function to fetch data from an external API and log it. However, in order to do this, it requires libraries not part of the standard serverless runtime.

## So what?

This over simple app needs a comparable build process to much more sophisticated apps including dozens of libraries, automated tests, and serverless function packaging.

## The plan

1. Write simple behavior tests
1. Write code to make tests pass
1. Configure pipeline to perform CI/CD

### Tools to explore

- AWS CodeBuild
- AWS CodePipeline
- AWS CodeDeploy
- AWS Lambda

# Installation

1. Clone this repository
1. Run `pipenv sync --dev`
1. Run `pipenv shell`

## Testing

This project leverages the gherkin style testing implementation offered by the excellent [python `behave`](https://pypi.org/project/behave/) library.

To execute the tests, run `behave`.

### Code Coverage

1. To execute the tests with code coverage run `coverage run --omit features/steps/steps.py --source='.' -m behave`
1. Examine the coverage with `coverage report`
