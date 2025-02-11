#pro 22
# date : 11-02-2025

filename = "numbers.txt"

with open(filename, "w") as file:
     while True:
         numbers = input("Enter numbers [ press ENTER to exit. ]")

         if not numbers:
             break
         file.write(numbers + "\n")

print(f"Numbers are written to { filename }.")
            
