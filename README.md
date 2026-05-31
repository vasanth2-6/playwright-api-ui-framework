# Automation Exercise QA Framework

## Overview

This project contains UI and API automation tests for AutomationExercise.com using Playwright, Pytest, and Requests.

## Tech Stack

* Python 3.13
* Playwright
* Pytest
* Requests
* GitHub Actions

## Project Structure

project/
├── tests/
│ ├── ui/
│ └── api/
├── pages/
├── docs/
├── .github/workflows/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

## UI Tests

1. Homepage Validation
2. Product Search
3. Product Details
4. Add To Cart
5. Remove From Cart

## API Tests

1. Products API
2. Brands API
3. Search Product API

## Installation

pip install -r requirements.txt

playwright install

## Run Tests

pytest -v

## Generate HTML Report

pytest --html=report.html --self-contained-html

## Future Improvements

* Page Object Model implementation
* Data-driven testing
* Parallel execution
* Cross-browser execution
* Docker support
* Jenkins integration
