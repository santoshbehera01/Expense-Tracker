# User Manual — Expense Tracker

## 1. Starting the Application

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

3. The application will launch and open the **Dashboard** page.

---

## 2. Interface Overview

The application consists of four main sections:

- **Sidebar Navigation** — Access different features.
- **Header Section** — Displays the current page title.
- **Content Area** — Shows the selected page content.
- **Status Bar** — Displays application status and information.

---

## 3. Adding an Expense

1. Navigate to **Add Expense**.
2. Enter the following details:

   - Date (`YYYY-MM-DD`)
   - Category
   - Description
   - Amount

3. Click **Save Expense**.

The expense will be validated and stored automatically.

### Validation Rules

- All fields are required.
- Amount must be a valid non-negative number.
- Date must follow the format `YYYY-MM-DD`.

---

## 4. Viewing Expenses

1. Open **All Expenses**.
2. Browse expense records in the table.
3. Select a record to delete if needed.
4. Click **Refresh** to reload data.

---

## 5. Searching Expenses

1. Open **Search**.
2. Enter a category name.
3. Click **Search** or press **Enter**.
4. Matching records will be displayed instantly.

---

## 6. Expense Summary

The **Summary** page provides:

- Category wise expense totals
- Spending distribution
- Overall expense analysis
- Grand total calculation

This helps users understand spending patterns more effectively.

---

## 7. Exporting Data

1. Open **Export CSV**.
2. Click **Export to CSV**.
3. Choose a destination folder.
4. Save the exported file.

The exported CSV file can be opened in Excel, Google Sheets, or other spreadsheet applications.

---

## 8. Data Storage

Expense records are stored automatically in:

```text
data/
├── expenses.csv
└── expenses.json
```

Both files are created automatically during the first application launch.

---

## 9. Troubleshooting

| Issue | Solution |
|---------|----------|
| Application does not start | Verify Python 3.8+ is installed correctly. |
| Tkinter module missing | Install Tkinter (`sudo apt install python3-tk` on Linux). |
| Invalid amount entered | Enter a valid numeric value. |
| Invalid date format | Use `YYYY-MM-DD` format. |
| Missing data files | Restart the application; files will be recreated automatically. |

---

## 10. Features at a Glance

- Dashboard Overview
- Add Expense
- View All Expenses
- Search Expenses
- Expense Summary
- CSV Export
- CSV & JSON Storage
- Input Validation
- User Friendly Interface

---

## 11. Conclusion

Expense Tracker is a desktop application designed to simplify personal expense management. It allows users to record, organize, analyze, and export financial data through a clean and intuitive interface while demonstrating practical use of Python, Tkinter, file handling, and data persistence techniques.