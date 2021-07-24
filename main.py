import smtplib
#have to set security to lower settings in gmail to allow gmail to send
my_email = ""
my_password = ""

connection = smtplib.SMTP("smtp.gmail.com")
#encrypts email
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="bob@bob.com", msg="Subject:Hello\n\nThis is the body of the email.")
connection.close()

