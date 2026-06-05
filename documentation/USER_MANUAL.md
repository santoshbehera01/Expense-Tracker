# User Manual — Expense Tracker

## 1. Starting the application

1. Open a terminal in the project folder.
2. Run:
   ```bash
   python main.py
   ```
3. The application window opens at the **Dashboard**.

## 2. Window layout

- **Sidebar (left)** — navigation between sections.
- **Header (top)** — current section title and today's date.
- **Content (center)** — the active section.
- **Status bar (bottom)** — live total and storage file paths.

## 3. Adding an expense

1. Click **Add Expense** in the sidebar.
2. Fill in:
   - **Date** — format `YYYY-MM-DD` (today's date is pre-filled).
   - **Category** — pick from the dropdown or type your own.
   - **Description** — short text.
   - **Amount** — non-negative number.
3. Click **Save Expense**.
4. A confirmation dialog appears; the form resets for the next entry.

Validation rules:
- All fields are required.
- Invalid date format → error dialog.
- Negative or non-numeric amount → error dialog.

## 4. Viewing all expenses

1. Click **All Expenses**.
2. Scroll through the table.
3. To delete a record:
   - Click the row to select it (Ctrl/Shift-click for multi-select).
   - Click **🗑 Delete Selected** and confirm.
4. Click **🔄 Refresh** to reload from disk.

## 5. Searching

1. Click **Search**.
2. Type a category (e.g. `Food`) and press **Search** or hit Enter.
3. Matching rows appear in the table; the **subtotal** appears at the
   bottom-right.

## 6. Category-wise summary

1. Click **Summary**.
2. Each row shows the category, total amount, percentage share, and a
   visual bar.
3. The **Grand Total** is shown at the bottom-right.

## 7. Exporting to CSV

1. Click **Export CSV**.
2. Click **⬇ Export to CSV**.
3. Choose a destination and filename, then click **Save**.
4. A confirmation dialog shows the saved path.

## 8. Where is my data stored?

- `data/expenses.csv` — primary store, human-readable.
- `data/expenses.json` — mirror in JSON.

Both files are created automatically on first launch and updated on
every add/delete.

## 9. Troubleshooting

| Problem                                | Fix                                                                 |
|----------------------------------------|---------------------------------------------------------------------|
| `ModuleNotFoundError: _tkinter`        | Install Tk: `sudo apt install python3-tk` (Linux).                  |
| Window does not open on a headless box | The app needs a display; run it on a real desktop session.          |
| Amount rejected                        | Use a non-negative number, e.g. `120` or `49.99`.                   |
| Date rejected                          | Use `YYYY-MM-DD`, e.g. `2025-06-05`.                                |
| Lost data file                         | Just relaunch; an empty `data/expenses.csv` & `.json` are recreated.|
