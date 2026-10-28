
from models import LibraryItem


class InventoryManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added.")

        if item.item_id in self.items:
            raise ValueError("An item with this ID already exists.")

        self.items[item.item_id] = item
        print(f"Added successfully: {item.title}")

    def display_items(self):
        if not self.items:
            print("Inventory is empty.")
            return

        print("\n" + "=" * 90)
        print(f"{'ID':<10} {'TITLE':<22} {'TYPE':<15} {'PRICE':<12} {'STATUS':<15}")
        print("-" * 90)

        for item in self.items.values():
            print(
                f"{item.item_id:<10} "
                f"{item.title[:21]:<22} "
                f"{type(item).__name__:<15} "
                f"₹{item.price:<11.2f} "
                f"{'Checked out' if item.is_checked_out else 'Available':<15}"
            )

        print("=" * 90)

    def checkout_item(self, item_id):
        item = self.items.get(item_id)

        if item is None:
            print("Error: Item ID not found.")
            return

        try:
            item.checkout()
            print(f"Checked out successfully: {item.title}")
        except ValueError as error:
            print(f"Error: {error}")

    def return_item(self, item_id, days_late=0):
        item = self.items.get(item_id)

        if item is None:
            print("Error: Item ID not found.")
            return

        if not isinstance(days_late, int) or isinstance(days_late, bool) or days_late < 0:
            print("Error: Late days must be a non-negative integer.")
            return

        try:
            fee = item.calculate_fee(days_late)
            item.return_item()
            print(f"Returned successfully: {item.title}")
            print(f"Late fee: ₹{fee:.2f}")
        except ValueError as error:
            print(f"Error: {error}")

    def generate_audit_report(self):
        print("\n========== INVENTORY AUDIT REPORT ==========")
        print(f"Total items: {len(self.items)}")
        print(f"Available: {sum(not item.is_checked_out for item in self.items.values())}")
        print(f"Checked out: {sum(item.is_checked_out for item in self.items.values())}")

        for item in self.items.values():
            print(f"\n{item}")
            print(f"  Details: {item.display_metadata()}")
            print(f"  Price: ₹{item.price:.2f}")
            print(f"  Representation: {repr(item)}")

        print("============================================")


def main():
    from models import Book, Magazine, DigitalMedia

    inventory = InventoryManager()

    inventory.add_item(
        Book("B101", "Python Basics", 450, "John Smith", 320)
    )
    inventory.add_item(
        Magazine("M101", "Tech Monthly", 120, "Issue 25", 60)
    )
    inventory.add_item(
        DigitalMedia("D101", "Python Course", 299, 500, "Personal")
    )

    while True:
        print("\n===== SMART INVENTORY SYSTEM =====")
        print("1. Display inventory")
        print("2. Check out item")
        print("3. Return item")
        print("4. Generate audit report")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            inventory.display_items()

        elif choice == "2":
            item_id = input("Enter item ID: ").strip()
            inventory.checkout_item(item_id)

        elif choice == "3":
            item_id = input("Enter item ID: ").strip()
            try:
                days_late = int(input("Enter late days (0 if none): "))
                inventory.return_item(item_id, days_late)
            except ValueError:
                print("Error: Please enter a whole number for late days.")

        elif choice == "4":
            inventory.generate_audit_report()

        elif choice == "5":
            print("Thank you for using Smart Inventory System!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
