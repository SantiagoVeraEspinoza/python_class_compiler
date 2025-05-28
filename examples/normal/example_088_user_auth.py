# User Auth

def user_auth_main():
    data = []
    status = "Initialized"

    def add_item(item):
        data.append(item)
        print(f"Item '{item}' added.")

    def remove_item(item):
        if item in data:
            data.remove(item)
            print(f"Item '{item}' removed.")
        else:
            print(f"Item '{item}' not found.")

    def display_items():
        print("Current items:")
        for item in data:
            print(f"- {item}")

    def clear_items():
        data.clear()
        print("All items cleared.")

    def set_status(new_status):
        nonlocal status
        status = new_status
        print(f"Status set to '{status}'")

    def get_status():
        return status

    # Example usage
    add_item("Ejemplo 1")
    add_item("Ejemplo 2")
    display_items()
    set_status("Activo")
    print("Estado actual:", get_status())

user_auth_main()
print("FIN")
