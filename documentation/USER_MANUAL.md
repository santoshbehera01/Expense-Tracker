# User Manual — Expense Tracker

**Project Name:** Expense Tracker (CSV / JSON)
**Intern Name:** Santosh Kumar Behera
**Intern ID:** CITS2854
**Duration:** 6 Weeks

---

## 1. Starting the Application

1. Open a terminal in the project folder.
2. Run:

   ```bash
   python main.py
   ```

3. The application window opens at the **Dashboard**.

---

## 2. Window Layout

- **Sidebar (Left):** Navigation between application sections.
- **Header (Top):** Displays the current section title and today's date.
- **Content Area (Center):** Displays the selected feature page.
- **Status Bar (Bottom):** Shows the total expense amount and storage information.

---

## 3. Adding an Expense

1. Click **Add Expense** from the sidebar.
2. Fill in the following details:

   - **Date** — Format: `YYYY-MM-DD`
   - **Category** — Select from the dropdown or enter your own.
   - **Description** — Brief expense description.
   - **Amount** — Enter a non-negative numeric value.

3. Click **Save Expense**.
4. A confirmation message will appear, and the form will reset.

### Validation Rules

- All fields are mandatory.
- Invalid date format displays an error message.
- Negative or non-numeric amounts are rejected.

---

## 4. Viewing All Expenses

1. Click **All Expenses**.
2. Browse all stored expense records in the table.
3. To delete an expense:

   - Select one or more rows.
   - Click **🗑 Delete Selected**.
   - Confirm the deletion.

4. Click **🔄 Refresh** to reload data from storage.

---

## 5. Searching Expenses

1. Click **Search**.
2. Enter a category name (e.g., `Food`).
3. Press **Search** or hit **Enter**.
4. Matching expenses will be displayed.
5. The subtotal for matching records appears at the bottom.

---

## 6. Category-wise Summary

1. Click **Summary**.
2. View spending grouped by category.
3. Each category displays:

   - Total Amount
   - Percentage Share
   - Visual Expense Bar

4. The **Grand Total** is displayed at the bottom.

---

## 7. Exporting Data to CSV

1. Click **Export CSV**.
2. Click **⬇ Export to CSV**.
3. Select a destination folder.
4. Enter a filename and click **Save**.
5. A confirmation message will display the saved location.

---

## 8. Data Storage

The application automatically stores data in the following files:

### CSV Storage

```text
data/expenses.csv
```

### JSON Storage

```text
data/expenses.json
```

Both files are automatically created when the application is launched for the first time and are updated whenever expenses are added or deleted.

---

## 9. Troubleshooting

| Issue                                  | Recommended Solution                                                  |
|-----------------------------------------|----------------------------------------------------------------------|
| `ModuleNotFoundError: _tkinter`         | Install Tkinter using `sudo apt install python3-tk` (Linux systems). |
| Application window does not open        | Ensure the application is running in a desktop environment with GUI support. |
| Invalid amount entered                  | Enter a valid non-negative numeric value such as `120` or `49.99`.   |
| Invalid date format                     | Use the format `YYYY-MM-DD` (Example: `2026-06-05`).                 |
| Missing or deleted data files           | Restart the application. Required CSV and JSON files will be recreated automatically. |
---

## 10. Conclusion

The Expense Tracker application provides a simple and efficient way to manage daily expenses through a modern desktop interface. Users can record, search, analyze, and export expense data while maintaining reliable storage in both CSV and JSON formats.

This project was developed as part of the **Python Programming Internship Program** at **CODTECH IT Solutions Pvt. Ltd.** and demonstrates practical implementation of Python GUI development, file handling, data management, and software engineering best practices.
