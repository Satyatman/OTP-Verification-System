import os
import math
import random
import smtplib
# Generating a six-digit random number and storing it in a variable
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg = otp
# Connecting to GMAIL using SMTP. email and password are stored as env variables for privacy.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
email, pwd = os.environ.get('EMAIL_HOST'), os.environ.get('EMAIL_PWD')
s.login(email, pwd)
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
# Verifying if the OTP entered matches the OTP sent.
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
