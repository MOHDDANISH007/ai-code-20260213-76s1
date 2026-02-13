def hello(name: str):
    if not isinstance(name, str) or not name.strip():
        print("Error: Invalid user name.")
        return

    print(f"Hello, {name}!")
hello("al zaid")