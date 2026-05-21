# ELT API Pipeline

## Overview
Simple ELT pipeline that extracts user data from a public API, loads raw data into PostgreSQL, and performs SQL transformations.

## Tech Stack
- Python
- PostgreSQL
- pandas
- SQLAlchemy

## Workflow
API → PostgreSQL Raw Table → SQL Transformations

## Features
- API extraction
- Raw data loading
- SQL transformations
- PostgreSQL integration

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run pipeline
python extract.py