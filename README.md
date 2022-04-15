# Coding Problem

## Description
Construct a simple Store class that has a collection of Incidents and an "incident_status" method.

An Incident is something that happens in the store that must be reported and solved, for example “the floor in the fruit area is dirty” and someone needs to clean it (this is the action needed to solve it). Also an Incident has an status that can be “open” if the incident has been reported but not solved or “solved” if the case has been solved.

The incident_status method of the Store class receives 2 dates and returns the following:
- The number of “open” cases between those dates.
- The number of “solved” cases between those dates.
- The average solution time between those dates (include only the solved cases).
- The current maximum solution time between those dates (include open cases using the current time).

## Tech
---------
* Python version: 3.10

## How to use
To run the app run the following command
```bash
python main.py
```

## Running tests
To run tests, run the following command
```bash
python test.py
```

## Unit tests
The unit tests carried out were built based on the main functionality of the applications, which is the incident_status method, taking into account different types of data.

