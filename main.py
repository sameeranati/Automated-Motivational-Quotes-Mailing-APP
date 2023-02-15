import datetime as dt
import random
import smtplib
file=open("/home/sameeranati/birthdaywisher/quotes.txt")
s=file.readlines()
date=dt.datetime(year=2022,month=11,day=21)
x=date.weekday()

my_email="sameeranati@gmail.com"
my_password="gxyyolcscmjlylvo"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=my_password)
if x==0:
    connection.sendmail(from_addr=my_email, to_addrs="sameera_nati@yahoo.co.in",msg=f"Subject: motivationalquote\n\n {random.choice(s)}")
connection.close()

