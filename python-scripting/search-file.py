# import os

# for dirname,dirpath,filename in os.walk("/etc/ufw"):
#     for file in filename:
#         if file=="ufw.conf":
#             print(os.path.join(dirname,file))



import os

import argparse


my_parser=argparse.ArgumentParser(description="Read the log file")
my_parser.add_argument("pathname",
                       help="Please enter the logfile to parse")
# my_parser.add_argument("filesearch",
#                        help="Please enter the logfile to parse")


args=my_parser.parse_args()

# for dirname,dirpath,filename in os.walk(args.pathname):
#     for file in filename:
#         if file==args.filesearch:
#             print(os.path.join(dirname,file))


for dirname,dirpath,filename in os.walk(args.pathname):
    for file in filename:
        if file.endswith(".conf"):
            print(os.path.join(dirname,file))
