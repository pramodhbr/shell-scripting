#Platform is used to execute the script in both linux and windows

import platform
import os

if platform.system() == "Linux":
    os.system("ls")
elif platform.system == "Windows":
    os.system("Dir")
else:
    print("Unsupported platform")
