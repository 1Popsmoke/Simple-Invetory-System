class InventorySystem: # this is like the blueprint it has the methods used in creating this system e.g. functions, while loops, if....Else
    def __init__(self):
        self.inventory = {} # here the Items are saved temporarily in a list
        #f = open("myfile.txt", "x")
        #f.close()

    def add_item(self): # function add of the system
        """Add a new item or update the quantity of an existing item."""
        item_name = input("Enter item name: ").strip()
        if item_name in self.inventory:
            print(f"{item_name} already exists in inventory.") # *f* is the file being created in InvetortSystem that store items
            update = input("Do you want to update the quantity? (y/n): ").strip().lower()
            if update == 'y':
                quantity = int(input("Enter quantity to add: "))
                self.inventory[item_name]['quantity'] += quantity
                print(f"Updated {item_name} quantity to {self.inventory[item_name]['quantity']}.")
                
        else:
            quantity = int(input(f"Enter quantity of {item_name}: "))
            price = float(input(f"Enter price of {item_name}: "))
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
            print(f"Added {quantity} of {item_name} to inventory.")
                
           
    def remove_item(self): # function remove of the system
        """Remove a certain quantity of an item from the inventory."""
        item_name = input("Enter item name to remove: ").strip()
        if item_name in self.inventory:
            quantity = int(input(f"Enter quantity of {item_name} to remove: "))
            if self.inventory[item_name]['quantity'] >= quantity: # here if the number of items in the invetory is greater than the quantity the user wants to strip
                self.inventory[item_name]['quantity'] -= quantity # the user can successfully strip the quantity
                if self.inventory[item_name]['quantity'] == 0:
                    del self.inventory[item_name]  # Remove the item if quantity reaches 0
                print(f"Removed {quantity} of {item_name}. New quantity: {self.inventory[item_name]['quantity']}.")
            else:
                print(f"Error: Not enough {item_name} in inventory to remove {quantity}.")
        else:
            print(f"{item_name} not found in inventory.")

    def view_inventory(self): #  function View of the system
        """Display all the items in the inventory."""
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\nInventory List:")
            for item, details in self.inventory.items():
                print(f"Item: {item}, Quantity: {details['quantity']}, Price: str ${details['price']:.2f}")

    def update_item(self): # function Update of the system
        """Update the price or quantity of an existing item."""
        item_name = input("Enter item name to update: ").strip()
        if item_name in self.inventory:
            update = input("Do you want to update the price or quantity? (p/q): ").strip().lower()
            if update == 'p':
                new_price = float(input(f"Enter new price for {item_name}: "))
                self.inventory[item_name]['price'] = new_price
                print(f"Updated {item_name} price to ${new_price:.2f}.")
            elif update == 'q':
                new_quantity = int(input(f"Enter new quantity for {item_name}: "))
                self.inventory[item_name]['quantity'] = new_quantity
                print(f"Updated {item_name} quantity to {new_quantity}.")
            else:
                print("Invalid option.")
        else:
            print(f"{item_name} not found in inventory.")

def main():  # function of the main class
    system = InventorySystem()  # returns statements which calls the fuctions and method used
    
    while True:
        print("\nSimple Inventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. View inventory")
        print("4. Update item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            system.add_item()
        elif choice == '2':
            system.remove_item()
        elif choice == '3':
            system.view_inventory()
        elif choice == '4':
            system.update_item()
        elif choice == '5':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": # this specific line of code allows the whole code to execute
    main()
