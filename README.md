# Expense Tracker (CSV / JSON) — Desktop Edition

A modern, dashboard-style **Expense Tracker desktop application** built with
Python and Tkinter. It looks and feels like a real desktop product —
sidebar navigation, colored header, KPI cards, professional tables, and
a status bar — while storing data safely in both **CSV** and **JSON**.

---

## Intern Details

| Field        | Value                              |
|--------------|------------------------------------|
| Project Name | **Expense Tracker (CSV / JSON)**   |
| Intern Name  | **Santosh Kumar**                  |
| Intern ID    | **CT06DN868**                      |
| Duration     | **6 Weeks**                        |
| Stack        | Python 3.8+ • Tkinter • CSV • JSON |

---

## Features

- 📊 **Dashboard** with KPI cards (Total Spent, Entries, Categories, Top Category)
- ➕ **Add Expense** — form with date, category, description, amount
- 📋 **All Expenses** — professional Treeview table with scrollbar
- 🔍 **Search** expenses by category, with subtotal
- 🗑️ **Delete** any selected expense
- 📈 **Category-wise Summary** with visual share bars
- ⬇️ **Export to CSV** to any location on disk
- 💾 **Dual storage** — every change is written to `data/expenses.csv` and `data/expenses.json`
- 🛟 **Auto-create** data folder & files on first run
- 🛡️ **Validation** — non-negative amounts, valid `YYYY-MM-DD` dates, friendly dialogs
- 🎨 **Modern UI** — sidebar nav, hover states, status bar, colored header, flat buttons

---

## Technologies Used

| Layer        | Tech                                          |
|--------------|-----------------------------------------------|
| Language     | Python 3.8+                                   |
| GUI          | Tkinter + ttk (Treeview, Combobox, Entry)     |
| Storage      | CSV and JSON (standard library)               |
| OS support   | Windows • macOS • Linux                       |
| Dependencies | None (standard library only)                  |

---

## Folder Structure

```
ExpenseTracker/
│
├── main.py                       # Main Tkinter application
├── data/
│   ├── expenses.csv              # CSV store (auto-created)
│   └── expenses.json             # JSON store (auto-created)
├── assets/
│   └── icons/                    # App icons (optional)
├── screenshots/                  # Place your UI screenshots here
├── documentation/
│   ├── PROJECT_DOC.md            # Full project documentation
│   └── USER_MANUAL.md            # Step-by-step user manual
├── README.md                     # This file
└── requirements.txt              # Dependency notes
```

---

## Installation Guide

### 1. Prerequisites

- **Python 3.8+** (Tkinter is bundled on Windows and macOS).
- On Debian/Ubuntu Linux install Tk once:
  ```bash
  sudo apt install python3-tk
  ```

### 2. Get the project

```bash
git clone https://github.com/<your-username>/ExpenseTracker.git
cd ExpenseTracker
```

### 3. (Optional) virtual environment

```bash
python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows
```

### 4. Run the app

```bash
python main.py
```

The data folder and files will be created automatically on first launch.

---

## Usage Instructions

1. Launch the app — the **Dashboard** opens by default with KPIs and the
    10 most recent expenses.
2. Use the **left sidebar** to navigate:
   - **Add Expense** — fill the form and click *Save Expense*.
   - **All Expenses** — see every record; select a row and click
     *Delete Selected* to remove it.
   - **Search** — type a category (e.g. `Food`) and press *Search* or
     Enter; the subtotal appears at the bottom-right.
   - **Summary** — view a category-wise breakdown with share bars.
   - **Export CSV** — save a copy of your data anywhere on disk.
3. The **status bar** at the bottom always shows the live total and the
   storage file paths.

---

## Screenshots

> Add your screenshots to the `screenshots/` folder.

```
screenshots/
├── 01_dashboard.png
├── 02_add_expense.png
├── 03_all_expenses.png
├── 04_search.png
└── 05_summary.png
```

Embed in your GitHub README like:

```markdown
![Dashboard](screenshots/01_dashboard.png)
```

---

## Sample Data

### `data/expenses.csv`

```csv
date,category,description,amount
2025-06-01,Food,Lunch with team,450.00
2025-06-02,Travel,Metro card recharge,200.00
2025-06-03,Shopping,Notebook and pens,180.50
2025-06-04,Food,Groceries,1250.75
2025-06-05,Bills,Internet bill,799.00
```

### `data/expenses.json`

```json
[
    {"date": "2025-06-01", "category": "Food", "description": "Lunch with team", "amount": 450.0},
    {"date": "2025-06-02", "category": "Travel", "description": "Metro card recharge", "amount": 200.0},
    {"date": "2025-06-03", "category": "Shopping", "description": "Notebook and pens", "amount": 180.5}
]
```

---

## Future Improvements

- Charts and graphs (matplotlib / plotly) inside the dashboard.
- Monthly **budgets** and **alerts** when overspending.
- Filtering by **date range** in addition to category.
- **Edit** an existing expense from the table.
- Export to **Excel** and **PDF** reports.
- **Dark mode** toggle.
- Cloud sync with Google Sheets or Firebase.
- Package as a single-file executable using `pyinstaller`.

---

## Author

**Santosh Kumar** — Intern ID `CT06DN868`
Built during a **6-week Python internship** as a portfolio-grade
desktop project, suitable for **GitHub** and **LinkedIn** showcases.
