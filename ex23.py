import sys

script, input_encoding, error = sys.argv

def main(language_file,encoding, errors) :
    line = language_file.readline()

    if line :
        line_output(line, encoding, errors)
        return main(language_file,encoding,errors)


def line_output(line, encoding, errors) :
    next_language = line.strip()
    raw_bytes = next_language.encode(encoding, errors=errors)
    cooked_bytes = raw_bytes.decode(encoding, errors= errors)

    print(raw_bytes,"<=====>",cooked_bytes)

languages = open("languages.txt", encoding = "utf=8")

main(languages,input_encoding,error)
