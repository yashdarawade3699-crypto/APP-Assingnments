file = open("input.txt", "r")

lines = file.readlines()
file.close()

print("Total number of lines:", len(lines))

first_two = lines[:2]

file = open("output.txt", "w")
file.writelines(first_two)
file.close()

print("First two lines written to output.txt")