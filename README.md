# Appointment Booking System

## Overview

The Appointment Booking System is a Python-based application designed to manage appointment bookings between patients and service providers.

This project focuses on demonstrating software quality assurance and testing practices through a test-driven development approach.

## Objectives

* Allow users to create and book appointments.
* Prevent double booking.
* Allow users to cancel appointments.
* Validate appointment information.
* Check provider availability.

## Features

* Create appointments
* Book appointments
* Cancel appointments
* Prevent conflicting bookings
* Validate appointment dates and times
* Prevent appointments from being booked in the past
* Track appointment status
* Check provider availability

## Testing Approach

This project follows **Test-Driven Development (TDD)** using the **Red-Green-Refactor** cycle.

### Red

Write a test that fails and identifies the required behaviour.

### Green

Write the minimum code required to make the test pass.

### Refactor

Improve the implementation while keeping all tests passing.

## QA Testing

The project includes:

* **Unit testing** – testing individual functions and behaviours.
* **Positive testing** – verifying that valid inputs and operations work correctly.
* **Negative testing** – verifying that invalid inputs and operations are rejected.
* **Boundary-value testing** – testing limits such as `00:00`, `23:59`, and today's date.
* **Validation testing** – checking invalid dates, times, and required fields.
* **Integration testing** – testing the complete appointment workflow.
* **Regression testing** – re-running the test suite after changes to ensure existing functionality still works.
* **Test coverage** – measuring how much of the code is exercised by the test suite.

### Test Results

The project currently contains **23 automated tests**.

All tests pass successfully:

**23 passed**

Test coverage:

**100%**

```text
Name                        Stmts   Miss  Cover
-----------------------------------------------
appointment.py                 39      0   100%
tests\test_appointment.py     101      0   100%
-----------------------------------------------
TOTAL                         140      0   100%
```

## Technology Stack

* Python
* pytest
* Coverage.py
* Git
* GitHub

## Project Status

**Core functionality complete**

The application has been tested using unit, positive, negative, boundary, validation, integration, and regression testing.

## Future Improvements

Possible future improvements include:

* REST API
* Database integration
* API testing
* Authentication and authorization
* User interface
* Appointment persistence
