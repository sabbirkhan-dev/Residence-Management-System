# Residence Management System (RMS)

A modern web-based Residence / Mess Management System built with Django.

## Overview

Residence Management System (RMS) helps manage members, meals, deposits, bazar expenses, and monthly reports for residential hostels, bachelor messes, student accommodations, and shared living environments.

The system is designed to replace traditional Excel-based meal management with a clean and user-friendly web application.

---

## Features

### Dashboard

* Total Members Overview
* Daily Breakfast Count
* Daily Dinner Count
* Quick Navigation
* Summary Cards

### Member Management

* Add New Members
* Update Member Information
* Member Status Management
* Room Number Tracking
* Member Profiles

### Meal Management

* Daily Meal Entry
* Breakfast Tracking
* Dinner Tracking
* Custom Meal Quantity Support
* Date-wise Meal Records
* Meal Edit & Delete

### Deposits Management

* Member Deposits
* Deposit History
* Monthly Deposit Tracking
* Deposit Summary

### Bazar Management

* Bazar Expense Tracking
* Purchase Records
* Expense History
* Monthly Cost Calculation

### Monthly Reports

* Total Meal Calculation
* Meal Rate Calculation
* Total Deposits
* Total Expenses
* Member-wise Balance Sheet
* Payable / Receivable Report

### Member Profile

Each member can view:

* Total Meals
* Total Deposits
* Monthly Expenses
* Meal Cost
* Balance
* Receivable Amount
* Payable Amount

---

## Technology Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons

### Database

* SQLite (Development)

---

## Project Structure

```text
Residence_Management_System/
│
├── accounts/
├── dashboard/
├── members/
├── meals/
├── deposits/
├── bazar/
├── reports/
│
├── templates/
├── static/
│
├── config/
├── manage.py
└── db.sqlite3
```

---

## Future Improvements

* Month-wise Accounting System
* Automated Meal Rate Calculation
* Internet Bill Distribution
* Cooker Cost Distribution
* Utility Cost Distribution
* PDF Report Export
* Excel Report Export
* User Authentication & Roles
* Mobile Responsive Enhancements
* Notification System

---

## Screenshots

Dashboard

* Total Members
* Today's Breakfast
* Today's Dinner
* Navigation Sidebar

Meals Management

* Daily Meal Records
* Meal Tracking
* Meal Summary

Monthly Reports

* Excel-like Calculation Engine
* Member-wise Reports
* Deposit & Expense Summary

---

## Installation

Clone Repository

```bash
git clone https://github.com/your-username/residence-management-system.git
```

Create Virtual Environment

```bash
python -m venv env
```

Activate Virtual Environment

```bash
env\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Migrations

```bash
python manage.py migrate
```

Run Development Server

```bash
python manage.py runserver
```

Open Browser

```text
http://127.0.0.1:8000/
```

---

## Author

**Sabbir Khan**

Python Developer | Django Developer

GitHub: https://github.com/your-github-username

---

## License

This project is created for educational and personal learning purposes.
