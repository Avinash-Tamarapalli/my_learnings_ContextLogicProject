import smtplib as smt
#ulurhnepfmbfeywm
# How to use it
# Open the “Mail” app.
# Open the “Settings” menu.
# Select “Accounts” and then select your Google Account.
# Replace your password with the 16-character password shown above.
# Just like your normal password, this app password grants 
# complete access to your Google Account. You won't need to remember it,
#  so don't write it down or share it with anyone.
obj = smt.SMTP("smtp.gmail.com",587)
obj.ehlo()
obj.starttls()
obj.login("avinash12082001@gmail.com","ulurhnepfmbfeywm")

subject = "Sending Email through Python, Test -1"

body = "Hi Yeshwant this email is send to you by writing a Python code!!!"

message = f"Subject: {subject}\n\n{body}"

mail_list = ["188r1a03g3@gmail.com",
             "vagvalayashwant@gmail.com"]

obj.sendmail('avinash12082001@gmail.com',mail_list,message)

print("mail sent")

obj.quit()