# import smtplib
#
# my_email = "santoshkumarmeher13@gmail.com"
# password = "ikwpccbxcnpwpsty"
# # receiver_email = "s7327894942@gmail.com"
#
# if password is None:
#     raise ValueError("Email password not set.")
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.ehlo()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="s7327894942@gmail.com",
#         msg="Subject:Hello\n\n This is message"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second
# week_day = now.weekday()
# print(f"{year}/{month}/{day} ({week_day}) {hour}:{minute}:{second}")
# birthday = dt.datetime(day=5,month=3,year=1999)
# print(birthday)



import datetime as dt
import random
import smtplib

MY_EMAIL = "santoshkumarmeher13@gmail.com"
PASSWORD = "ikwpccbxcnpwpsty"
# RECEIVER = "s7327894942@gmail.com"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)

    if PASSWORD is None:
        raise ValueError("Email password not set.")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.ehlo()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="s7327894942@gmail.com",
            msg=f"Subject:Monday Motivation\n\n {quote}"
        )


