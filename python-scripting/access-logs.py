logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
import re
from collections import Counter
import csv
import argparse


my_parser=argparse.ArgumentParser(description="Read the log file")
my_parser.add_argument("logfile",
                       help="Please enter the logfile to parse", type=argparse.FileType('r'))



args=my_parser.parse_args()


def read_file(logfile):
    with args.logfile as f:
        log=f.read()
        ip_list=re.findall(logreg,log)
        return ip_list
    
def read_count():
    ip_list=read_file(args.logfile)
    ip_count=Counter(ip_list)
    return ip_count.items()

def csv_writer():
    counter=read_count()
    with open("ip_count.csv",'w') as f:
        fwriter=csv.writer(f)
        fwriter.writerow(["IP_ADDRESS","COUNT"])
        for items,val in counter:
            fwriter.writerow([items,val])

if __name__=="__main__":
    csv_writer()
