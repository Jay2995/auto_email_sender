import smtplib;
import datetime as dt;
import random;

now_date = dt.datetime.now();
my_email = "youremail@gmail.com";
password = "your app password";

def rand_quote():
    random_msg = random.choice(quotes);
    print(random_msg);
    return(random_msg);

with open('quotes.txt', 'r') as file:
    lines = file.readlines();
quotes = [line.strip() for line in lines ];



if now_date.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls();
        connection.login(user=my_email, password=password);
        connection.sendmail(
            from_addr= my_email,
            to_addrs= "receiverEmail@proton.me",
            msg = f"Subject: inspirational msg \n\n {rand_quote()}");









