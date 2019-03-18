from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying file {from_file} to {to_file}.")

# we could do these two on one line, how?
in_file = open(from_file)
in_data = in_file.read()

print(f"This data is {len(in_data)} byte long.")

print(f"Does the output_file is exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL+C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(in_data)

print("All right, well done.")

in_file.close()
out_file.close()
