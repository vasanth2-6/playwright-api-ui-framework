# Test Strategy – AutomationExercise.com

## Objective

The objective of this testing effort is to validate the core functionality of AutomationExercise.com by covering critical user journeys and API endpoints.

## Scope

### In Scope

* Homepage validation
* Product search
* Product details
* Add product to cart
* Remove product from cart
* Product APIs
* Brand APIs
* Search product APIs

### Out of Scope

* Performance testing
* Security testing
* Accessibility testing
* Mobile application testing
* Cross-browser testing

## Risk Areas

### Risk 1 – Shopping Cart Functionality

Any issue in cart operations can directly impact customer purchases and business revenue.

### Risk 2 – Product Search

Incorrect search results can prevent users from finding products.

### Risk 3 – API Availability

API failures can affect integrations and frontend functionality.

## Test Approach

### UI Testing

Automated using:

* Playwright
* Pytest

### API Testing

Automated using:

* Requests
* Pytest

## Test Environment

* Windows 11
* Python 3.13
* Chromium Browser
* AutomationExercise.com

## Entry Criteria

* Application is accessible.
* Test environment is configured.
* Dependencies are installed.

## Exit Criteria

* All automated tests executed.
* No critical blockers.
* Test report generated.

## Future Enhancements

* Implement full Page Object Model
* Data-driven testing
* Parallel execution
* Cross-browser testing
* CI/CD enhancements
