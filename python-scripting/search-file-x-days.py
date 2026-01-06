import os
from datetime import datetime

current_date=datetime.now()
max_age=10

for dirpath, dirname, filepath in os.walk("/etc"):
    for file in filepath:
        comp_path = os.path.join(dirpath,file)
        file_stat=os.stat(comp_path)
        # print(file_stat)
        file_ctime=file_stat.st_ctime
        file_creation_date=datetime.fromtimestamp(file_ctime)
        diff_in_days=(current_date-file_creation_date).days
        if diff_in_days > max_age:
            print(comp_path, diff_in_days)
