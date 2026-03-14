#I'm using this site whith dummy emails for educational purposes: https://ethereal.email/create
import smtplib

my_email = "teresa.kling@ethereal.email"
password = "u2Mvsrc12RtK2ddP5r"
#in normal case (for example gmail adress) it has to be used with new app + app password etc

# with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="teresa.kling@ethereal.email", msg="Subject: Hello\n\n "
#                                                                                         "content content\n\n z wyrazami szacunku")


#"monday motivational quote" - in my case suterday
import datetime as dt
import random

now = dt.datetime.now()

if now.weekday() == 5:
    with open("quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="teresa.kling@ethereal.email",
                            msg="Subject: Your motivation for today!!!\n\n"
                                "Hi!\n Here is your quote for today:\n\n"
                                f"{quote}\n"
                                "Have a nice day!")