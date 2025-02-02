# inventory_management_system.py

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price):
        """Add a new item or update the quantity and price of an existing item."""
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
            self.items[item_name]['price'] = price
            print(f"Updated {item_name}: {quantity} units added. New price: ${price}.")
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
            print(f"Added new item: {item_name}, Quantity: {quantity}, Price: ${price}.")

    def update_item(self, item_name, quantity=None, price=None):
        """Update the quantity and/or price of an existing item."""
        if item_name in self.items:
            if quantity is not None:
                self.items[item_name]['quantity'] = quantity
            if price is not None:
                self.items[item_name]['price'] = price
            print(f"Item {item_name} updated.")
        else:
            print(f"Item {item_name} not found.")

    def remove_item(self, item_name):
        """Remove an item from the inventory."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Item {item_name} has been removed from inventory.")
        else:
            print(f"Item {item_name} not found.")

    def view_inventory(self):
        """View all items in the inventory."""
        if not self.items:
            print("Inventory is empty.")
            return
        print("\nInventory List:")
        for item_name, details in self.items.items():
            print(f"Item: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']}")

    def search_item(self, item_name):
        """Search for an item by name."""
        if item_name in self.items:
            details = self.items[item_name]
            print(f"Item: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']}")
        else:
            print(f"Item {item_name} not found in inventory.")


def main():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Search Item")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            item_name = input("Enter item name: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            price = float(input("Enter price per unit: ").strip())
            inventory.add_item(item_name, quantity, price)
        elif choice == '2':
            item_name = input("Enter item name to update: ").strip()
            quantity = input("Enter new quantity (leave empty to skip): ").strip()
            price = input("Enter new price (leave empty to skip): ").strip()

            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            inventory.update_item(item_name, quantity, price)
        elif choice == '3':
            item_name = input("Enter item name to remove: ").strip()
            inventory.remove_item(item_name)
        elif choice == '4':
            inventory.view_inventory()
        elif choice == '5':
            item_name = input("Enter item name to search: ").strip()
            inventory.search_item(item_name)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
