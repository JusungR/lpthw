from sys import argv

script, file_name = argv

print(f"We are going to erase {file_name}.")
print(f"If you don't wnat to, press ctrl + C")
print(f"If you do want to, hit RETURN")

input("?")

print("Opening the file....")
object = open(file_name, 'w', encoding = 'utf-8')

print("Truncating thefile. Good bye!")
object.truncate()

print("Now I'm goig to ask you for threee lines.")
line1 = input("line1 :")
line2 = input("line2 :")
line3 = input("line3 :")

object.write(line1)
object.write("\n")
object.write(line2)
object.write("\n")
object.write(line3)
object.write("\n")

print("And finally, we close it")
object.close()
