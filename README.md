# Smart Finance Tracker

A robust, Object-Oriented Command Line Interface (CLI) application built using pure Python to manage personal finances. This application allows users to log income and expenses, persist data locally, and view automated financial health summaries.

## 🚀 Key Features
*   **Persistent Local Storage:** Automatic data serialization and deserialization using native CSV handling.
*   **Object-Oriented Architecture:** Built using clean, maintainable, and modular Python class structures.
*   **Data Sanitization:** Input filtering including automatic string formatting, type checking, and boundary validation (e.g., preventing negative values).
*   **Real-time Ledger Analytics:** Dynamic balance calculation and tabular formatting of your entire transaction history.

## 🛠️ Tech Stack
*   **Language:** Python 3.x (Core modules only)
*   **Built-in Libraries Used:** `os`, `csv`, `datetime`

## ⚙️ How It Works
The application implements an explicit schema definition for transactions:
`[Date, Amount, Type, Category, Description]`

It splits data streams in memory into separate state arrays for optimization, while keeping files perfectly synchronized via automated overwrite handlers on every mutating operation.

## 💻 Installation & Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd smart-finance-tracker
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```
