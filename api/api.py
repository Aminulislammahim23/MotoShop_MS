import csv
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

class MotoShopAPI:

    def __init__(self):
        self.users = self.load_csv("users.csv")
        self.inventory = self.load_csv("inventory.csv")
        self.sales = self.load_csv("sales.csv")

    # -----------------------------
    # CSV LOAD
    # -----------------------------
    def load_csv(self, filename):
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            return []

        with open(path, mode="r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    # -----------------------------
    # CSV SAVE
    # -----------------------------
    def save_csv(self, filename, data):
        path = os.path.join(DATA_DIR, filename)

        if len(data) == 0:
            return

        with open(path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    # -----------------------------
    # USERS CRUD
    # -----------------------------
    def add_user(self, user):
        self.users.append(user)
        self.save_csv("users.csv", self.users)

    # -----------------------------
    # INVENTORY CRUD
    # -----------------------------
    def add_inventory(self, item):
        self.inventory.append(item)
        self.save_csv("inventory.csv", self.inventory)

    def update_inventory(self, item_id, updated_data):
        for item in self.inventory:
            if item["id"] == item_id:
                item.update(updated_data)
                break
        self.save_csv("inventory.csv", self.inventory)

    def delete_inventory(self, item_id):
        self.inventory = [i for i in self.inventory if i["id"] != item_id]
        self.save_csv("inventory.csv", self.inventory)

    # -----------------------------
    # SALES CRUD
    # -----------------------------
    def add_sale(self, sale):
        self.sales.append(sale)
        self.save_csv("sales.csv", self.sales)
