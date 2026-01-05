import os
import socket
from datetime import datetime
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import psutil

load_dotenv()

CPU_THRESHOLD=20
MEMORY_THRESHOLD=20

cpu=psutil.cpu_percent(interval=1)
memory=psutil.virtual_memory().percent

if cpu<CPU_THRESHOLD and memory<MEMORY_THRESHOLD:
    exit()

EMAIL_USER=os.getenv("EMAIL")
EMAIL_PASSWORD=os.getenv("PASSWORD")
RECIVER_MAIL=os.getenv("RECIVER_MAIL")

msg=EmailMessage()

msg["From"]=EMAIL_USER
msg["To"]=RECIVER_MAIL
msg["Subject"]="EC2 Resource cpu and memory usage alerts"
msg.set_content(f"EC2 usage report for CPU Usage: {cpu}, EC2 usage report MEMORY Usage: {memory}, Hostname for EC2: {socket.gethostname()}, Time: {datetime.now()}")

with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.send_message(msg)

print("Alert email")
