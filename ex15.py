from sys import argv

script, file_name = argv

text = open(file_name, encoding = 'utf-8')

print(f"file {file_name}'s contents :")

print(text.read())
text.close()
print("Type the file name once again.")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())
text_again.close()
