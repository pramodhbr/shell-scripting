

# try:
#     open("/etc")

# except Exception as e:
#     print(e)

############ Method 1 #############
# import os

# filename="/etc/hosts"

# if os.path.exists(filename) and os.path.isfile(filename):
#     print("File exist")
# else:
#     print("File doesnot exist")
# print(os.path.exists("/etc/hosts"))
# print(os.path.isfile("/etc/hosts"))
# print(os.path.isdir("/etc"))


############## Method 2 ############
import pathlib

filename="/etc/hosts"

path=pathlib.Path(filename)

print(path.exists())
print(path.is_file())
print(path.is_dir())
