# Docker CI/CD Pipeline Project

## Current Status
This repository contains the foundational setup for a Docker-based CI/CD pipeline using GitLab CI/CD. So far, the following have been implemented:

- Building Docker images and saving build artifacts.
- Running integration tests.
- Running User Acceptance Tests (UAT).
- Running performance tests using Gatling.
- Automated verification that all tests pass before proceeding.
- Automated Git tagging upon successful test completion.
- Pushing Docker images to a container registry (e.g., GitLab Registry, AWS ECR).

## Work In Progress
- Deployment to Kubernetes (via Helm or kubectl).
- Integration with monitoring and notification tools (Slack, Grafana, etc.).

## Important Note
This project is currently a work in progress and may not be fully completed or maintained in the future. Contributions and improvements are welcome, but there is no guarantee that all planned features will be implemented.

## How to Use
1. Push your code changes to the GitLab repository.
2. The GitLab CI/CD pipeline will automatically trigger and execute the defined stages.
3. Monitor the pipeline status and test results directly within GitLab.

---

Thank you for checking out this project. Feel free to explore and contribute!
