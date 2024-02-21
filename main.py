import smtplib;
import datetime as dt;
import random;
import csv;
import pandas as pd;

my_email = "youremail@gmail.com";
password = "your app password";

now_date = dt.datetime.now();

now_month = now_date.month;
now_weekday = now_date.day;
today= (now_month,now_weekday);

file = pd.read_csv('birthdays.csv');


birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in file.iterrows()};

if today in birthday_dict:
    birthday_person = birthday_dict[today];
    print(birthday_person);
    random_number = random.randint(1,3);
    file_path = f"letters/letter_{random_number}.txt";
    with open(file_path) as letter_file:
        contents = letter_file.read()
        edited_text = contents.replace("[NAME]", birthday_person['name']);
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls();
        connection.login(user=my_email, password=password);
        connection.sendmail(
            from_addr = my_email,
            to_addrs= f"{birthday_person.email}",
            msg  = f"Subject: Happy Birthday\n\n {edited_text}"
        );


        
