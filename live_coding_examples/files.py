import os.path

file_name = "log_file.txt"

if not os.path.exists(file_name):
    file = open(file_name, "x")
    file.write("Sample log")
    file.close()


file = open(file_name, "rt")
log = file.read()
print(file.seek(0, 0))
print(file.seek(5))
print(file.seek(0, 2))
print(log)
