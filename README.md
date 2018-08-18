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
