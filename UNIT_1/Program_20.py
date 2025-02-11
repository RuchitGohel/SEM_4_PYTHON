# pro_20 :
# date : 11-02-25
# Write a program to take user input and store it in a  text file.

filename = "name.txt"

with open(filename, "w") as file:
    while True:
        name = input("Enter name [ press Enter to exit. ]:")

        if not name:
            break
        file.write(name+"\n")

print(f"Names are written to { filename }")
