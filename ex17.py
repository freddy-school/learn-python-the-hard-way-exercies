from os import truncate, write
from sys import argv
from os.path import exists

script, from_file, to_file = argv

to_w_file = open(from_file)
indat = to_w_file.read()

print(f"how big wrigfht {len(indat)}")

out_file = open(to_file, 'w')
out_file.write(indat)

print("done")
out_file.close()
to_w_file.close()
