# ============================================
# api_client.py - MotoShop Client Console
# ============================================

import requests

API_BASE = "http://127.0.0.1:8000"


# -------- 1) CALL: ADD PRODUCT --------
def call_add_product():
    try:
        data = {
            "id": int(input("Enter Product ID: ")),
            "name": input("Enter Product Name: "),
            "price": float(input("Enter Price: ")),
            "qty": int(input("Enter Quantity: "))
        }

        response = requests.post(f"{API_BASE}/add_product", json=data)
        result = response.json()

        print("\nResponse:", result)
        print("Product Added:", result["product"])

    except Exception as e:
        print("Error:", e)


# -------- 2) CALL: LIST PRODUCTS --------
def call_list_products():
    try:
        response = requests.get(f"{API_BASE}/list_products")
        result = response.json()

        print("\nTotal Products:", result["total"])
        for p in result["products"]:
            print(p)

    except Exception as e:
        print("Error:", e)


# -------- 3) CALL: SEARCH PRODUCT --------
def call_search_product():
    try:
        name = input("Enter Product Name to Search: ")

        response = requests.get(f"{API_BASE}/search_product", params={"name": name})
        result = response.json()

        print("\nSearch Name:", result["search_name"])
        print("Found:", result["found"])
        print("Results:", result["results"])

    except Exception as e:
        print("Error:", e)


# -------- 4) CALL: TOTAL INVENTORY VALUE --------
def call_total_value():
    try:
        response = requests.get(f"{API_BASE}/total_value")
        result = response.json()

        print("\nTotal Value:", result["total_inventory_value"])
        print("Product Count:", result["product_count"])

    except Exception as e:
        print("Error:", e)


# -------- MENU --------
def menu():
    print("\n==============================")
    print("     MotoShop API CLIENT      ")
    print("==============================")
    print("1. Add Product")
    print("2. List Products")
    print("3. Search Product")
    print("4. Total Inventory Value")
    print("5. Exit")
    print("==============================")


# -------- MAIN LOOP --------
def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            call_add_product()
        elif choice == "2":
            call_list_products()
        elif choice == "3":
            call_search_product()
        elif choice == "4":
            call_total_value()
        elif choice == "5":
            print("Exiting client...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
