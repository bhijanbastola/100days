"""
Question: File Read and Write

Write a Program that Uses Functions write_to_file and read_from_file:

write_to_file(filename, content): Writes content to a file named filename. If the file doesn't exist, it should be created.
read_from_file(filename): Reads and prints the content of a file named filename. Call write_to_file to write "Hello, Python!" to a file named "greetings.txt", then call read_from_file to read and print the content of this file.
"""
with open("filename.txt", "a") as file:
    file.write("Hello 100 days challenge\n")

with open("filename.txt", "r") as file:
    content = file.read()
    print(content)