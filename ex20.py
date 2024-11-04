#
# from sys import argv
# script, input_file = argv
#
#
# def print_all(f):
#     print(f.read())
#
# current_file = open(input_file)
# print_all(current_file)
#




from os import read
from sys import argv

script, file = argv

def print_all(f):
    print(f.read())

def undo(f):
    f.seek(0)

def print_a_line(line_num, f):
    print(f.readline(line_num))
    
curent_file = open(file)
print_all(curent_file)
line_num = 3


print_a_line({line_num , curent_file} * 10)

