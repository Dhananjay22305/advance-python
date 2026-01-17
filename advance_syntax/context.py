password = input("Enter your password: ")

with open("file.txt", "w") as file:
    file.write(password)
