import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

import passs

fromaddr = "naveenkatta719@gmail.com"
password = passs.password
#toaddr = "shrey.saxena@sequelstring.com"
toaddr = "abhishek891999@gmail.com"
# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hi, This is an emergency flight booking to be done for International Client Meeting. Please do it as soon as possible !"
df=pd.read_csv("Updated_MMT.csv")
nam=df.Name
nam=list(nam)

# string to store the body of the mail
body =f"Dear Shrey Sir,\n Ticket has been Successfully Booked"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "Updated_MMT.csv"
attachment = open(filename, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())


# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,password)

# Converts the Multipart msg into a string
text = msg.as_string()

server.send_message(msg)

server.quit()

print("Updated Mail has Been Sent....! ")