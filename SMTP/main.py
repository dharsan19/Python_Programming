import smtplib

my_email = ""
my_password = ""

with smtplib.SMTP("smtp.google.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
