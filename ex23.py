import sys
script, in_encode, error = sys.argv 

def main(in_encode, encoding, error):
    line = in_encode.readline(in_encode)
   
    if line:
        print_line(line, encoding, error)
        return main(line, encoding, error)


def print_line(line, encoding, error):
    next_lang = line.script()     
    raw_bytes = next_lang.encoding(encoding, error=error)
    bad_string = raw_bytes.decode(encoding, error=error)

    print(raw_bytes, "<====>", bad_string)

languages = open("languages.txt", encoding="utf-8")
