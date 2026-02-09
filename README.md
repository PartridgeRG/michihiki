# Michihiki

Michihiki is a small web service I operate as a hands-on DevOps training environment.

The goal of this repository is to demonstrate operational competence: deploying, maintaining, monitoring, and recovering a live service.

The application itself is intentionally simple. The focus of this project is system operation, reliability, and automation rather than feature development.

## What this repository demonstrates

- Linux service operation
- Deployment and configuration management
- Log inspection and troubleshooting
- Backup and restore procedures
- Monitoring and alerting
- Automation with Python
- Infrastructure provisioning with Terraform
- Continuous integration and deployment

## System Overview

Michihiki is a minimal task-tracking web application used as a controlled production-style environment.

It serves as a platform for operating a complete service stack, including:

- web application
- database
- reverse proxy
- containerized deployment
- monitoring and health checks
- automated deployment
- cloud infrastructure

## Operational Documentation

This repository includes full operational runbooks:

- DEPLOYMENT.md — provisioning and deployment from a clean system
- TROUBLESHOOTING.md — diagnosing service failures
- FAILURE_RECOVERY.md — backup and disaster recovery procedures
- ARCHITECTURE.md — system design and decisions

## Purpose

This repository functions as a public operations log and a portfolio of practical DevOps experience. It documents how a service is deployed, monitored, maintained, and restored after failure.

## Scripts

### hello_system.py

Minimal diagnostic script that prints operating system, OS release, CPU architecture, and Python version.  
Used to verify the execution environment during setup and troubleshooting.

**Usage**
```bash
python3 scripts/hello_system.py
```


