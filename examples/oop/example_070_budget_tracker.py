class BudgetTracker:
    def __init__(self):
        self.name = "BudgetTracker"
        self.status = "Initialized"
        self.data = []

    def add_item(self, item):
        self.data.append(item)
        print(f"Item '{item}' added to {self.name}.")

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)
            print(f"Item '{item}' removed from {self.name}.")
        else:
            print(f"Item '{item}' not found in {self.name}.")

    def display_items(self):
        print(f"Items in {self.name}:")
        for item in self.data:
            print(f"- {item}")

    def clear_items(self):
        self.data.clear()
        print(f"All items cleared from {self.name}.")

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

# Ejemplo de uso
obj = BudgetTracker()
obj.add_item("Ejemplo 1")
obj.add_item("Ejemplo 2")
obj.display_items()
obj.set_status("Activo")
print("Estado actual:", obj.get_status())
print("FIN")
