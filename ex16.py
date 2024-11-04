from sys import argv

script, filename = argv
print(f"we will erase {filename}")

input('?')

target = open(filename, 'w')
print(f"tuncating now {"......" * 10}")

target.truncate()

print("i will ask u for 3 lines")
l1 = input("l1 :")
l2 = input("l2 :")
l3 = input("l3 :")
#
target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")

print(l1,l2,l3)

target.close()
