import json
import os

class FinanceManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {"transactions": []}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_income(self, value, description):
        self.data["transactions"].append({
            "type": "income",
            "value": value,
            "description": description
        })
        self.save_data()

    def add_expense(self, value, description):
        self.data["transactions"].append({
            "type": "expense",
            "value": value,
            "description": description
        })
        self.save_data()

    def get_balance(self):
        balance = 0
        for t in self.data["transactions"]:
            if t["type"] == "income":
                balance += t["value"]
            else:
                balance -= t["value"]
        return balance

    def list_transactions(self):
        print("\n📊 TRANSAÇÕES:")
        for i, t in enumerate(self.data["transactions"], 1):
            print(f"{i}. {t['type']} - R$ {t['value']} - {t['description']}")
