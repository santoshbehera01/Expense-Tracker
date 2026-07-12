# Project Documentation — Expense Tracker

## 1. Overview

Expense Tracker is a desktop application developed using Python and Tkinter that helps users record, manage, analyze, and export daily expenses. The application stores data in both CSV and JSON formats, ensuring reliable data persistence and easy access.

---

## 2. Objectives

- Manage daily expenses efficiently.
- Store data using CSV and JSON files.
- Provide expense analysis and reporting.
- Demonstrate GUI development and file handling in Python.

---

## 3. Architecture

```text
User Interface (Tkinter)
          │
          ▼
Application Logic
          │
          ▼
Data Storage
(CSV + JSON)
```

### Core Modules

- Expense Management
- Input Validation
- CSV Storage
- JSON Storage
- Dashboard & Reports

---

## 4. Technologies Used

| Component | Technology |
|------------|------------|
| Language | Python 3 |
| GUI Framework | Tkinter |
| Data Storage | CSV, JSON |
| Tools | Git, GitHub, VS Code |

---

## 5. Key Features

- Dashboard with expense statistics
- Add and delete expenses
- View all expense records
- Search expenses by category
- Category wise spending summary
- CSV export functionality
- Automatic data persistence
- User friendly interface

---

## 6. Data Storage

The application maintains records in:

```text
data/
├── expenses.csv
└── expenses.json
```

Files are automatically created during the first application launch.

---

## 7. Validation & Error Handling

- Required fields validation
- Numeric amount validation
- Exception handling for file operations
- User friendly error messages

---

## 8. Future Enhancements

- Budget Management
- Charts & Analytics
- PDF/Excel Export
- Dark Mode
- Cloud Backup

---

## 9. Conclusion

Expense Tracker demonstrates practical implementation of Python GUI development, file handling, data persistence, and software design principles. It provides a simple and effective solution for managing personal expenses through a modern desktop interface..