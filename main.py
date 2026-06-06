"""Expense Tracker (CSV / JSON)

A modern Tkinter dashboard to record, search and analyse daily expenses.
This file contains the main application. Internship and author details
are kept in the repository documentation (README.md).
"""

import csv
import json
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_FILE = os.path.join(DATA_DIR, "expenses.csv")
JSON_FILE = os.path.join(DATA_DIR, "expenses.json")
FIELDNAMES = ["date", "category", "description", "amount"]
# Display/header form for CSV files (Titlecase) — kept separate so the on-disk
# CSV headers look friendly while internal keys remain lowercase.
CSV_HEADERS = ["Date", "Category", "Description", "Amount"]

# ---------------------------------------------------------------------------
# Theme — flat, modern, dashboard-style
# ---------------------------------------------------------------------------
COLORS = {
    "bg":            "#F4F6FA",   # app background
    "sidebar":       "#1E2A38",   # dark sidebar
    "sidebar_hover": "#2C3E50",
    "sidebar_text":  "#ECF0F1",
    "header":        "#2563EB",   # accent / header
    "header_text":   "#FFFFFF",
    "card":          "#FFFFFF",
    "border":        "#E5E7EB",
    "text":          "#1F2937",
    "muted":         "#6B7280",
    "primary":       "#2563EB",
    "success":       "#10B981",
    "danger":        "#EF4444",
    "warning":       "#F59E0B",
    "table_alt":     "#F9FAFB",
}

FONT_TITLE   = ("Segoe UI", 18, "bold")
FONT_SUB     = ("Segoe UI", 11)
FONT_BODY    = ("Segoe UI", 10)
FONT_LABEL   = ("Segoe UI", 10, "bold")
FONT_NAV     = ("Segoe UI", 11)
FONT_KPI     = ("Segoe UI", 20, "bold")


# ---------------------------------------------------------------------------
# Storage layer
# ---------------------------------------------------------------------------
def ensure_files() -> None:
    """Create data folder & files if missing."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(CSV_FILE):
        # Create CSV with friendly Titlecase headers (one-line header only)
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)


def load_expenses() -> list:
    """Read expenses from the CSV store."""
    ensure_files()
    rows = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for raw in reader:
                # Normalize headers to lowercase internal keys so code works
                row = {(k or "").strip().lower(): v for k, v in raw.items()}
                try:
                    row["amount"] = float(row.get("amount", 0) or 0)
                except (TypeError, ValueError):
                    row["amount"] = 0.0
                rows.append(row)
    except OSError as exc:
        messagebox.showerror("Storage Error", f"Could not read CSV:\n{exc}")
    return rows


def save_expenses(expenses: list) -> None:
    """Persist expenses to BOTH CSV and JSON."""
    try:
        # Write CSV using friendly Titlecase headers while mapping internal
        # lowercase keys to the on-disk header names.
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            for e in expenses:
                row = {h: e.get(h.lower(), "") for h in CSV_HEADERS}
                writer.writerow(row)
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=4)
    except OSError as exc:
        messagebox.showerror("Storage Error", f"Could not save data:\n{exc}")


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
def validate_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(value: str) -> bool:
    try:
        v = float(str(value).strip())
        return v >= 0
    except (ValueError, TypeError):
        return False


# ---------------------------------------------------------------------------
# Main application
# ---------------------------------------------------------------------------
class ExpenseTrackerApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Expense Tracker - Personal Finance Manager")
        self.geometry("1180x720")
        self.minsize(960, 600)
        self.configure(bg=COLORS["bg"])

        ensure_files()
        self._configure_styles()
        self._build_layout()
        self._show_section("dashboard")

    # ------------------------------------------------------------------
    # ttk styling
    # ------------------------------------------------------------------
    def _configure_styles(self) -> None:
        style = ttk.Style(self)
        # 'clam' is the most theme-able built-in
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            background=COLORS["card"],
            fieldbackground=COLORS["card"],
            foreground=COLORS["text"],
            rowheight=30,
            font=FONT_BODY,
            borderwidth=0,
        )
        style.configure(
            "Treeview.Heading",
            background=COLORS["primary"],
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=8,
            relief="flat",
        )
        style.map("Treeview.Heading", background=[("active", COLORS["primary"])])
        style.map(
            "Treeview",
            background=[("selected", COLORS["primary"])],
            foreground=[("selected", "white")],
        )

        style.configure(
            "Modern.TEntry",
            fieldbackground="white",
            bordercolor=COLORS["border"],
            lightcolor=COLORS["border"],
            darkcolor=COLORS["border"],
            padding=6,
        )
        style.configure(
            "Modern.TCombobox",
            fieldbackground="white",
            padding=6,
        )

    # ------------------------------------------------------------------
    # Layout: sidebar + header + content
    # ------------------------------------------------------------------
    def _build_layout(self) -> None:
        # Sidebar
        self.sidebar = tk.Frame(self, bg=COLORS["sidebar"], width=240)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="  💰 Expense Tracker",
            bg=COLORS["sidebar"],
            fg=COLORS["sidebar_text"],
            font=("Segoe UI", 16, "bold"),
            anchor="w",
            padx=18,
        ).pack(fill="x", pady=(22, 6))

        tk.Label(
            self.sidebar,
            text="  Personal Finance",
            bg=COLORS["sidebar"],
            fg="#9CA3AF",
            font=("Segoe UI", 9),
            anchor="w",
            padx=18,
        ).pack(fill="x", pady=(0, 20))

        nav_items = [
            ("dashboard",  "📊  Dashboard"),
            ("add",        "➕  Add Expense"),
            ("view",       "📋  All Expenses"),
            ("search",     "🔍  Search"),
            ("summary",    "📈  Summary"),
            ("export",     "⬇   Export CSV"),
        ]
        self._nav_buttons = {}
        for key, label in nav_items:
            btn = tk.Label(
                self.sidebar,
                text=label,
                bg=COLORS["sidebar"],
                fg=COLORS["sidebar_text"],
                font=FONT_NAV,
                anchor="w",
                padx=22,
                pady=12,
                cursor="hand2",
            )
            btn.pack(fill="x")
            btn.bind("<Button-1>", lambda _e, k=key: self._show_section(k))
            btn.bind("<Enter>", lambda _e, b=btn: b.configure(bg=COLORS["sidebar_hover"]))
            btn.bind("<Leave>", lambda _e, b=btn: self._restore_nav_bg(b))
            self._nav_buttons[key] = btn

        # Header
        self.header = tk.Frame(self, bg=COLORS["header"], height=70)
        self.header.pack(side="top", fill="x")
        self.header.pack_propagate(False)
        self.header_title = tk.Label(
            self.header,
            text="Dashboard",
            bg=COLORS["header"],
            fg=COLORS["header_text"],
            font=FONT_TITLE,
            padx=24,
        )
        self.header_title.pack(side="left", pady=18)

        self.header_date = tk.Label(
            self.header,
            text=datetime.now().strftime("%A, %d %B %Y"),
            bg=COLORS["header"],
            fg="#DBEAFE",
            font=FONT_SUB,
            padx=24,
        )
        self.header_date.pack(side="right", pady=22)

        # Content area
        self.content = tk.Frame(self, bg=COLORS["bg"])
        self.content.pack(side="top", fill="both", expand=True)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        self.statusbar = tk.Label(
            self,
            textvariable=self.status_var,
            bg="#111827",
            fg="#E5E7EB",
            anchor="w",
            padx=14,
            font=("Segoe UI", 9),
        )
        self.statusbar.pack(side="bottom", fill="x")

    def _restore_nav_bg(self, btn: tk.Label) -> None:
        active_key = getattr(self, "_active_section", None)
        if self._nav_buttons.get(active_key) is btn:
            btn.configure(bg=COLORS["sidebar_hover"])
        else:
            btn.configure(bg=COLORS["sidebar"])

    # ------------------------------------------------------------------
    # Section switching
    # ------------------------------------------------------------------
    def _show_section(self, key: str) -> None:
        self._active_section = key
        for k, btn in self._nav_buttons.items():
            btn.configure(bg=COLORS["sidebar_hover"] if k == key else COLORS["sidebar"])

        for widget in self.content.winfo_children():
            widget.destroy()

        builders = {
            "dashboard": self._build_dashboard,
            "add":       self._build_add_form,
            "view":      self._build_view_table,
            "search":    self._build_search,
            "summary":   self._build_summary,
            "export":    self._build_export,
        }
        titles = {
            "dashboard": "Dashboard",
            "add":       "Add Expense",
            "view":      "All Expenses",
            "search":    "Search Expenses",
            "summary":   "Category-wise Summary",
            "export":    "Export Data",
        }
        self.header_title.configure(text=titles.get(key, "Dashboard"))
        builders.get(key, self._build_dashboard)()
        self._refresh_status()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _refresh_status(self) -> None:
        rows = load_expenses()
        total = sum(float(r["amount"]) for r in rows)
        self.status_var.set(
            f"  {len(rows)} expense(s) • Total: ₹ {total:,.2f}   |   Files: data/expenses.csv • data/expenses.json"
        )

    @staticmethod
    def _card(parent: tk.Misc, **pack_opts) -> tk.Frame:
        card = tk.Frame(
            parent,
            bg=COLORS["card"],
            highlightthickness=1,
            highlightbackground=COLORS["border"],
        )
        card.pack(**pack_opts)
        return card

    # ------------------------------------------------------------------
    # Section: Dashboard (KPIs + recent table)
    # ------------------------------------------------------------------
    def _build_dashboard(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        rows = load_expenses()
        total = sum(float(r["amount"]) for r in rows)
        cats = {r.get("category", "—") for r in rows}
        top_cat = "N/A"
        if rows:
            sums: dict = {}
            for r in rows:
                sums[r.get("category", "")] = sums.get(r.get("category", ""), 0) + float(r["amount"])
            top_cat = max(sums, key=sums.get) if sums else "N/A"

        kpi_row = tk.Frame(wrap, bg=COLORS["bg"])
        kpi_row.pack(fill="x")

        def kpi(parent, label, value, color):
            card = tk.Frame(parent, bg=COLORS["card"],
                            highlightthickness=1, highlightbackground=COLORS["border"])
            card.pack(side="left", expand=True, fill="both", padx=8, ipadx=10, ipady=14)
            tk.Label(card, text=label, bg=COLORS["card"], fg=COLORS["muted"],
                     font=FONT_SUB, anchor="w").pack(fill="x", padx=18, pady=(6, 4))
            tk.Label(card, text=value, bg=COLORS["card"], fg=color,
                     font=FONT_KPI, anchor="w").pack(fill="x", padx=18)

        kpi(kpi_row, "Total Spent",   f"₹ {total:,.2f}", COLORS["primary"])
        kpi(kpi_row, "Total Entries", str(len(rows)),     COLORS["success"])
        kpi(kpi_row, "Categories",    str(len(cats)),     COLORS["warning"])
        kpi(kpi_row, "Top Category",  top_cat,            COLORS["danger"])

        # Recent expenses table
        tk.Label(wrap, text="Recent Expenses", bg=COLORS["bg"],
                 fg=COLORS["text"], font=("Segoe UI", 13, "bold")).pack(
            anchor="w", pady=(22, 8))

        table_card = self._card(wrap, fill="both", expand=True)
        if not rows:
            tk.Label(table_card, text="No expenses found. Add your first expense.",
                     bg=COLORS["card"], fg=COLORS["muted"], font=FONT_SUB,
                     padx=18, pady=28, anchor="center").pack(expand=True)
        else:
            tree = self._make_tree(table_card)
            for row in rows[-10:][::-1]:
                tree.insert("", "end",
                            values=(row.get("date", ""), row.get("category", ""),
                                    row.get("description", ""), f"{float(row.get('amount', 0)):.2f}"))

    # ------------------------------------------------------------------
    # Section: Add expense form
    # ------------------------------------------------------------------
    def _build_add_form(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        card = self._card(wrap, fill="x", ipadx=10, ipady=10)
        inner = tk.Frame(card, bg=COLORS["card"])
        inner.pack(padx=26, pady=22, fill="x")

        tk.Label(inner, text="New Expense", bg=COLORS["card"],
                 fg=COLORS["text"], font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))

        # Fields
        def field(row, label, widget):
            tk.Label(inner, text=label, bg=COLORS["card"], fg=COLORS["text"],
                     font=FONT_LABEL).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 14))
            widget.grid(row=row, column=1, sticky="ew", pady=8)

        inner.columnconfigure(1, weight=1)

        date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        cat_var  = tk.StringVar()
        desc_var = tk.StringVar()
        amt_var  = tk.StringVar()

        date_entry = ttk.Entry(inner, textvariable=date_var, style="Modern.TEntry")
        cat_combo  = ttk.Combobox(
            inner, textvariable=cat_var, style="Modern.TCombobox",
            values=["Food", "Travel", "Shopping", "Bills", "Health",
                    "Entertainment", "Education", "Other"],
        )
        desc_entry = ttk.Entry(inner, textvariable=desc_var, style="Modern.TEntry")
        amt_entry  = ttk.Entry(inner, textvariable=amt_var,  style="Modern.TEntry")

        field(1, "Date (YYYY-MM-DD)", date_entry)
        field(2, "Category",          cat_combo)
        field(3, "Description",       desc_entry)
        field(4, "Amount (₹)",        amt_entry)

        # Actions
        btn_row = tk.Frame(inner, bg=COLORS["card"])
        btn_row.grid(row=5, column=0, columnspan=2, sticky="e", pady=(18, 0))

        def submit():
            date = date_var.get().strip()
            cat  = cat_var.get().strip()
            desc = desc_var.get().strip()
            amt  = amt_var.get().strip()

            if not all([date, cat, desc, amt]):
                messagebox.showwarning("Missing fields", "Please fill in all fields.")
                return
            if not validate_date(date):
                messagebox.showerror("Invalid date", "Use the format YYYY-MM-DD.")
                return
            if not validate_amount(amt):
                messagebox.showerror("Invalid amount", "Amount must be a non-negative number.")
                return

            expenses = load_expenses()
            expenses.append({
                "date": date,
                "category": cat.title(),
                "description": desc,
                "amount": round(float(amt), 2),
            })
            save_expenses(expenses)
            messagebox.showinfo("Saved", "Expense added successfully.")
            cat_var.set(""); desc_var.set(""); amt_var.set("")
            date_var.set(datetime.now().strftime("%Y-%m-%d"))
            self._refresh_status()

        self._flat_button(btn_row, "Reset",
                          lambda: (cat_var.set(""), desc_var.set(""), amt_var.set(""),
                                   date_var.set(datetime.now().strftime("%Y-%m-%d"))),
                          bg=COLORS["card"], fg=COLORS["text"],
                          border=COLORS["border"]).pack(side="right", padx=(8, 0))
        self._flat_button(btn_row, "Save Expense", submit,
                          bg=COLORS["primary"], fg="white").pack(side="right")

    # ------------------------------------------------------------------
    # Section: View all expenses + delete
    # ------------------------------------------------------------------
    def _build_view_table(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        toolbar = tk.Frame(wrap, bg=COLORS["bg"])
        toolbar.pack(fill="x", pady=(0, 12))

        tk.Label(toolbar, text="All recorded expenses",
                 bg=COLORS["bg"], fg=COLORS["muted"],
                 font=FONT_SUB).pack(side="left")

        table_card = self._card(wrap, fill="both", expand=True)
        tree = self._make_tree(table_card)
        rows = load_expenses()
        for idx, row in enumerate(rows):
            tree.insert("", "end", iid=str(idx),
                        values=(row["date"], row["category"],
                                row["description"], f"{float(row['amount']):.2f}"))

        def delete_selected():
            sel = tree.selection()
            if not sel:
                messagebox.showinfo("Select a row", "Please select an expense to delete.")
                return
            if not messagebox.askyesno("Confirm", "Delete selected expense?"):
                return
            current = load_expenses()
            for iid in sorted([int(s) for s in sel], reverse=True):
                if 0 <= iid < len(current):
                    current.pop(iid)
            save_expenses(current)
            self._show_section("view")

        self._flat_button(toolbar, "🗑  Delete Selected", delete_selected,
                          bg=COLORS["danger"], fg="white").pack(side="right")
        self._flat_button(toolbar, "🔄  Refresh",
                          lambda: self._show_section("view"),
                          bg=COLORS["card"], fg=COLORS["text"],
                          border=COLORS["border"]).pack(side="right", padx=8)

    # ------------------------------------------------------------------
    # Section: Search by category
    # ------------------------------------------------------------------
    def _build_search(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        bar = self._card(wrap, fill="x", ipady=8)
        inner = tk.Frame(bar, bg=COLORS["card"])
        inner.pack(fill="x", padx=18, pady=14)

        tk.Label(inner, text="Search by category:", bg=COLORS["card"],
                 fg=COLORS["text"], font=FONT_LABEL).pack(side="left")

        query_var = tk.StringVar()
        entry = ttk.Entry(inner, textvariable=query_var, style="Modern.TEntry", width=32)
        entry.pack(side="left", padx=12)

        table_card = self._card(wrap, fill="both", expand=True, pady=(12, 0))
        tree = self._make_tree(table_card)

        subtotal_var = tk.StringVar(value="Subtotal: ₹ 0.00")
        tk.Label(wrap, textvariable=subtotal_var, bg=COLORS["bg"],
                 fg=COLORS["text"], font=("Segoe UI", 11, "bold")).pack(
            anchor="e", pady=(10, 0))

        def run_search():
            for i in tree.get_children():
                tree.delete(i)
            query = query_var.get().strip().lower()
            if not query:
                subtotal_var.set("Subtotal: ₹ 0.00")
                return
            total = 0.0
            for r in load_expenses():
                if r.get("category", "").lower() == query:
                    tree.insert("", "end", values=(r["date"], r["category"],
                                                  r["description"],
                                                  f"{float(r['amount']):.2f}"))
                    total += float(r["amount"])
            subtotal_var.set(f"Subtotal: ₹ {total:,.2f}")

        self._flat_button(inner, "Search", run_search,
                          bg=COLORS["primary"], fg="white").pack(side="left")
        entry.bind("<Return>", lambda _e: run_search())

    # ------------------------------------------------------------------
    # Section: Category-wise summary
    # ------------------------------------------------------------------
    def _build_summary(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        rows = load_expenses()
        summary: dict = {}
        for r in rows:
            summary[r["category"]] = summary.get(r["category"], 0) + float(r["amount"])
        total = sum(summary.values())

        card = self._card(wrap, fill="both", expand=True)
        cols = ("category", "amount", "share", "bar")
        tree = ttk.Treeview(card, columns=cols, show="headings", height=14)
        tree.heading("category", text="Category")
        tree.heading("amount",   text="Amount (₹)")
        tree.heading("share",    text="Share")
        tree.heading("bar",      text="")
        tree.column("category", width=200, anchor="w")
        tree.column("amount",   width=160, anchor="e")
        tree.column("share",    width=100, anchor="e")
        tree.column("bar",      width=400, anchor="w")
        tree.tag_configure("odd",  background=COLORS["table_alt"])
        tree.tag_configure("even", background=COLORS["card"])

        for i, (cat, amt) in enumerate(sorted(summary.items(), key=lambda x: -x[1])):
            share = (amt / total * 100) if total else 0
            bar = "█" * int(share / 2)
            tree.insert("", "end", values=(cat, f"{amt:,.2f}", f"{share:.1f}%", bar),
                        tags=("odd" if i % 2 else "even",))

        tree.pack(fill="both", expand=True, padx=2, pady=2)

        footer = tk.Frame(wrap, bg=COLORS["bg"])
        footer.pack(fill="x", pady=(12, 0))
        tk.Label(footer, text=f"Grand Total: ₹ {total:,.2f}",
                 bg=COLORS["bg"], fg=COLORS["text"],
                 font=("Segoe UI", 12, "bold")).pack(side="right")

    # ------------------------------------------------------------------
    # Section: Export
    # ------------------------------------------------------------------
    def _build_export(self) -> None:
        wrap = tk.Frame(self.content, bg=COLORS["bg"])
        wrap.pack(fill="both", expand=True, padx=24, pady=20)

        card = self._card(wrap, fill="x", ipadx=10, ipady=10)
        inner = tk.Frame(card, bg=COLORS["card"])
        inner.pack(padx=26, pady=22, fill="x")

        tk.Label(inner, text="Export your expenses", bg=COLORS["card"],
                 fg=COLORS["text"], font=("Segoe UI", 14, "bold")).pack(anchor="w")
        tk.Label(inner,
                 text="Save a copy of your data as a CSV file anywhere on your computer.",
                 bg=COLORS["card"], fg=COLORS["muted"],
                 font=FONT_SUB).pack(anchor="w", pady=(4, 18))

        def export_csv():
            path = filedialog.asksaveasfilename(
                title="Export expenses as CSV",
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv")],
                initialfile="expenses_export.csv",
            )
            if not path:
                return
            try:
                with open(path, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
                    writer.writeheader()
                    for e in load_expenses():
                        writer.writerow({h: e.get(h.lower(), "") for h in CSV_HEADERS})
                messagebox.showinfo("Exported", f"Data exported to:\n{path}")
            except OSError as exc:
                messagebox.showerror("Export failed", str(exc))

        self._flat_button(inner, "⬇  Export to CSV", export_csv,
                          bg=COLORS["primary"], fg="white").pack(anchor="w")

    # ------------------------------------------------------------------
    # Generic widgets
    # ------------------------------------------------------------------
    def _make_tree(self, parent: tk.Misc) -> ttk.Treeview:
        cols = ("date", "category", "description", "amount")
        tree = ttk.Treeview(parent, columns=cols, show="headings", height=14)
        tree.heading("date",        text="Date")
        tree.heading("category",    text="Category")
        tree.heading("description", text="Description")
        tree.heading("amount",      text="Amount (₹)")
        tree.column("date",        width=120, anchor="w")
        tree.column("category",    width=140, anchor="w")
        tree.column("description", width=420, anchor="w")
        tree.column("amount",      width=140, anchor="e")

        sb = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=sb.set)
        tree.pack(side="left", fill="both", expand=True, padx=2, pady=2)
        sb.pack(side="right", fill="y")
        return tree

    @staticmethod
    def _flat_button(parent, text, command, bg, fg, border=None) -> tk.Label:
        """A simple flat 'button' built from a Label for full color control."""
        btn = tk.Label(parent, text=f"  {text}  ", bg=bg, fg=fg,
                       font=("Segoe UI", 10, "bold"),
                       padx=18, pady=8, cursor="hand2")
        if border:
            btn.configure(highlightthickness=1, highlightbackground=border)
        btn.bind("<Button-1>", lambda _e: command())

        def on_enter(_e):
            btn.configure(bg=_shade(bg, -10))
        def on_leave(_e):
            btn.configure(bg=bg)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn


def _shade(hex_color: str, delta: int) -> str:
    """Lighten/darken a hex color by `delta` (-100..100)."""
    try:
        h = hex_color.lstrip("#")
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        r = max(0, min(255, r + delta))
        g = max(0, min(255, g + delta))
        b = max(0, min(255, b + delta))
        return f"#{r:02X}{g:02X}{b:02X}"
    except Exception:
        return hex_color


# ---------------------------------------------------------------------------
def main() -> None:
    try:
        app = ExpenseTrackerApp()
        app.mainloop()
    except tk.TclError as exc:
        print(f"GUI could not start (no display?): {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
