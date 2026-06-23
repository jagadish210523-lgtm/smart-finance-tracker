import os
import csv
from datetime import datetime  # Changed from 'import datetime' to prevent now() module crashes

class Expense_Tracker:
    def __init__(self, filename="expense.csv"):
        self.filename = filename
        self.expense = []
        self.income = []
        self.load_data()

    # ==================== CHANGED: NEW CSV LOAD DATA ====================
    def load_data(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                try:
                    next(reader)  # Skip the CSV header row
                except StopIteration:
                    return

                self.income = []
                self.expense = []

                for row in reader:
                    if len(row) == 5:
                        date_val, amount_val, type_val, cat_val, desc_val = row
                        
                        entry = {
                            "date": date_val,
                            "amount": float(amount_val),
                            "category": cat_val,
                            "description": desc_val
                        }

                        if type_val == "Income":
                            entry["id"] = len(self.income) + 1
                            self.income.append(entry)
                        elif type_val == "Expense":
                            entry["id"] = len(self.expense) + 1
                            self.expense.append(entry)
        except Exception as e:
            print(f"[WARNING] Error loading CSV file: {e}")

    # ==================== CHANGED: NEW CSV SAVE DATA ====================
    def save_data(self):
        try:
            with open(self.filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                # Header row to match the data fields
                writer.writerow(["Date", "Amount", "Type", "Category", "Description"])

                for inc in self.income:
                    writer.writerow([inc["date"], f"{inc['amount']:.2f}", "Income", inc["category"], inc["description"]])

                for exp in self.expense:
                    writer.writerow([exp["date"], f"{exp['amount']:.2f}", "Expense", exp["category"], exp["description"]])
        except Exception as e:
            print(f"Failed to save data: {e}")

    # ==================== YOUR ORIGINAL CODE CONTINUES ====================
    # Note: Added 'category' here so it matches the 3 inputs sent by main()
    def add_income(self, amount, category, description):
       if amount <= 0:
          print(f"[FAILED] Income must be greater than 0")
          return False
       income_entry = {
          "id": len(self.income) + 1,
          "amount": float(amount),
          "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "category": category.strip().capitalize(),
          "description": description.strip().capitalize()
       }
       self.income.append(income_entry)
       self.save_data()
       print("[SUCCESS] Income is added successfully!")
       return True

    def add_expense(self, amount, category, description):  # Fixed parameter order to match main()
       if amount <= 0:
          print(f"[FAILED] Invalid expense. Try again!")
          return False
       expense_entry = {
          "id": len(self.expense) + 1,
          "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "category": category.strip().capitalize(),
          "amount": float(amount),
          "description": description.strip().capitalize()
       }
       self.expense.append(expense_entry)
       self.save_data()
       print(f"[SUCCESS] Expense is added")
       return True

    def view_transaction(self):
       if not self.income and not self.expense:
          print(f"No Records Found")
          return
       print("\n" + "=" * 80)
       print(f"{'TYPE':<10} {'ID':<5} {'Date':<21} {'Category':<15} {'Amount ($)':<12} {'Description'}")
       print("=" * 80)
       for inc in self.income:
          print(f"{'INCOME':<10} {inc['id']:<5} {inc['date']:<21} {inc['category']:<15} {inc['amount']:<12.2f} {inc['description']}")
       for exp in self.expense:
          print(f"{'EXPENSE':<10} {exp['id']:<5} {exp['date']:<21} {exp['category']:<15} {exp['amount']:<12.2f} {exp['description']}")
       print("="*80)

    def calculate_total_income(self):
       return sum(item["amount"] for item in self.income)

    def calculate_total_expense(self):
       return sum(item["amount"] for item in self.expense)

    def display_balance(self):
       total_income = self.calculate_total_income()
       total_expense = self.calculate_total_expense()
       net_balance = total_income - total_expense
       print(f"\n" + "-" * 30)
       print(f"FINANCIAL SUMMARY")
       print(f"-" * 30)
       print(f"Total Income: {total_income}")
       print(f"Total Expense: {total_expense}")
       print(f"Current Balance: {net_balance}")

def main():
   tracker = Expense_Tracker()
   while True:
      print("\n=== EXPENSE TRACKER ===")
      print("1. Add Income")
      print("2. Add Expense")
      print("3. View Transaction")
      print("4. Display Balance")
      print("5. Exit")
      choice = input("Enter Your Choice: ").strip()  # Kept string input to avoid menu bypass crash
      
      if choice == "1":
         try:
            amt = float(input("Enter Income: "))
            cat = input("Enter income category(Salary/Side income): ")
            desc = input("Enter short description: ")
            tracker.add_income(amt, cat, desc)
         except ValueError:
            print(f"[INVALID] Please enter valid amount")
      elif choice == "2":
         try:
            amt = float(input("Enter Expense: "))
            cat = input("Expense Type(Rent/Food/Bills): ")
            desc = input("Enter short description: ")
            tracker.add_expense(amt, cat, desc)
         except ValueError:
            print(f"[INVALID] Please enter valid expense")
      elif choice == "3":
         tracker.view_transaction()
      elif choice == "4":
         tracker.display_balance()
      elif choice == "5":
         print(f"Thanks for using Expense tracker")
         break
      else:
         print(f"Invalid! Please choose between 1-5")

if __name__ == "__main__":
    main()