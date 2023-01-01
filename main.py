import pandas
import datetime as dt
import smtplib
import random
import os

# __________________________________________CHOOSING RANDOM TEMPLATE_________________________________
message_body = ''


def random_template():
    global message_body
    random_file = random.choice(os.listdir('letter_templates'))
    with open(f'letter_templates/{random_file}', 'r') as template:
        body_as_list = template.readlines()
        body_as_list[0] = f"Dear {data_dict['name']}\n"

    with open(f'letter_templates/{random_file}', 'w') as template_file:
        template_file.writelines(body_as_list)

    with open(f'letter_templates/{random_file}', 'r') as final_file:
        body = final_file.read()
        message_body = body


# __________________________________________EMAIL SETTINGS____________________________________________

def send_email():
    MY_MAIL = ''
    PASSWORD = ''
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=data_dict['email'],
                            msg=f'Subject:HAPPY BIRTHDAY\n\n{message_body}')


# ___________________________________________DATA_____________________________________________________

data = pandas.read_csv('birthdays.csv')
data_as_dict = data.to_dict(orient='records')

today = dt.datetime.now()
for data_dict in data_as_dict:
    if data_dict['month'] == today.month and data_dict['day'] == today.day:
        random_template()
        send_email()

