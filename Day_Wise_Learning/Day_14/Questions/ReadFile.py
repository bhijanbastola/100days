
try:
    with open("data.txt", "r") as file:
        content = file.read()

except FileNotFoundError as e:
    print(f"The data.txt file doesn't exist")

finally:
    print(f"Program Execution Completed")