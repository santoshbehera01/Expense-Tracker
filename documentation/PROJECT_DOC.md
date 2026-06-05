# Project Documentation — Expense Tracker (Desktop Edition)

## 1. Introduction

The **Expense Tracker** is a professional desktop application built with
Python and Tkinter. It allows a user to record, organize and analyse
personal expenses through a clean, modern dashboard interface. Data is
persisted to **CSV** and **JSON**, so it is portable and easy to inspect.

The project was built as part of a **6-week Python internship** by
**Santosh Kumar (Intern ID: CT06DN868)** and is intended to showcase
practical software-engineering skills — modular code, validation,
exception handling, file I/O, and UI/UX design.

## 2. Objectives

- Deliver a real, dashboard-style desktop application (not a CLI script).
- Demonstrate clean, modular, PEP 8–compliant Python.
- Practice persistent storage in both CSV and JSON formats.
- Provide a friendly user experience with validation and clear dialogs.
- Produce a deliverable that is **GitHub-ready** and **LinkedIn-worthy**.

## 3. Architecture

```
┌───────────────────────── main.py ─────────────────────────┐
│                                                           │
│  ┌─── Storage layer ───┐    ┌──── Validation ────┐         │
│  │ ensure_files()      │    │ validate_date()    │         │
│  │ load_expenses()     │    │ validate_amount()  │         │
│  │ save_expenses()     │    └────────────────────┘         │
│  └─────────────────────┘                                   │
│                                                           │
│  ┌─────────────── ExpenseTrackerApp (Tk) ──────────────┐   │
│  │  Sidebar  │   Header   │   Content (switchable):    │   │
│  │           │            │  • Dashboard               │   │
│  │           │            │  • Add Expense             │   │
│  │           │            │  • All Expenses            │   │
│  │           │            │  • Search                  │   │
│  │           │            │  • Summary                 │   │
│  │           │            │  • Export                  │   │
│  │           │            │  Status bar                │   │
│  └─────────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────────┘
```

- **Storage layer** is pure functions on CSV / JSON files.
- **Validation helpers** are small, testable, and reused everywhere.
- **`ExpenseTrackerApp`** is a `tk.Tk` subclass that owns the window,
  the ttk styles, the sidebar, the header, the content area and the
  status bar. Each section is built lazily on navigation.

## 4. Features

| # | Feature                | Description                                                  |
|---|------------------------|--------------------------------------------------------------|
| 1 | Dashboard              | KPI cards + recent expenses table                            |
| 2 | Add Expense            | Form with date, category, description, amount + validation   |
| 3 | View Expenses          | Treeview with scrollbar, alternate row colors                |
| 4 | Search                 | Case-insensitive category filter with subtotal               |
| 5 | Delete Expense         | Multi-select aware, confirmation dialog                      |
| 6 | Total Expenses         | Always visible in the status bar                             |
| 7 | Category-wise Summary  | Amount, % share, and ASCII bar per category                  |
| 8 | Export to CSV          | Save a copy anywhere via a native file dialog                |
| 9 | CSV & JSON storage     | Every write mirrors data to both files                       |
|10 | Auto-create files      | `data/expenses.csv` and `data/expenses.json` on first launch |

## 5. Working Procedure

1. The user launches `python main.py`.
2. `ensure_files()` creates the `data/` folder and both data files if
   they are missing.
3. The Tkinter window opens with the dashboard.
4. The user clicks any sidebar item — the content area is rebuilt for
   that section.
5. Add/Delete actions call `load_expenses()`, mutate the list, then call
   `save_expenses()` which writes **both** CSV and JSON.
6. The status bar is refreshed after every navigation to show the
   live total.

## 6. UI / UX Decisions

- **Sidebar** uses a dark navy palette (`#1E2A38`) for high contrast and
  a "real product" feel, with hover states and an active highlight.
- **Header** uses an accent blue (`#2563EB`) and a friendly date label.
- **KPI cards** use white surfaces with a 1-pixel border for a modern,
  flat look (no heavy shadows that often look dated on Tk).
- **Treeview** styling overrides the default platform theme via `clam`
  so the app looks consistent on Windows, macOS and Linux.
- **Buttons** are implemented as flat `Label` widgets so we have full
  control over color and hover state — Tk's native buttons cannot be
  styled this freely on every OS.

## 7. Code Quality

- PEP 8 formatting, type-friendly function signatures.
- Each feature is a single function or method (`_build_dashboard`,
  `_build_add_form`, …).
- Storage and validation helpers are decoupled from the UI.
- I/O is wrapped in `try/except OSError` with user-facing message boxes.
- No third-party dependencies — runs out of the box.

## 8. Future Enhancements

- Charts (matplotlib) embedded in the dashboard.
- Monthly budgets and overspend alerts.
- Date-range filters and inline edit of rows.
- Excel + PDF export.
- Dark-mode toggle.
- Package as a single-file `.exe` with PyInstaller.

## 9. Conclusion

The Expense Tracker shows how Python and Tkinter can be used to build
a polished, modular desktop application that goes well beyond a typical
beginner script. It balances clean engineering with strong UX, making
it a strong portfolio piece and a solid foundation for further growth.
