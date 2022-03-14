import datetime
from faker import Faker
fake = Faker(locale='en_CA')

#----------------------------Moodle Web App DATA PARAMETERS-------------
app = 'Moodle'
moodle_url = 'http://52.39.5.126/'
moodle_homepage_title = 'Software Quality Assurance Testing'
moodle_login_url = 'http://52.39.5.126/login/index.php'
moodle_login_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashboard_url = 'http://52.39.5.126/my/'
moodle_dashboard_title = 'Dashboard'
moodle_addnewuser_title = 'SQA: Administration: Users: Accounts: Add a new user'
moodel_users_mainpage_url = 'http://52.39.5.126/admin/user.php'
moodle_users_mainpage_title = 'SQA: Administration: Users: Accounts: Browse list of users'
admin_username = 'wenlingdou'
admin_password = 'DWLdwl*916'

new_username = fake.user_name()
new_password = fake.password()
firstname = fake.first_name()
lastname = fake.last_name()
middlename = fake.first_name()
fullname = f'{firstname} {lastname}'
email = fake.email()

list_of_interests = [fake.job(), fake.job(), fake.job()]

moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.current_country()
description = f'User added by {admin_username} via Python Selenium Automated script {datetime.datetime.now()}'
              #fake.sentence(nb_words=100)
pic_descp = f'Image submitted by {fullname}'
sysid = ''
webpage = fake.url()
icq_num = fake.pyint(111111, 999999)
id_skype = new_username
id_aim = f'{new_username}{fake.pyint(111,999)}'
id_yahoo = fake.user_name()
id_msn = fake.user_name()
id_idnumber = fake.pyint(1111111, 9999999)
id_institution = fake.company()
id_department = fake.catch_phrase()
phonenum1 = fake.phone_number()
phonenum2 = fake.phone_number()
address = fake.address().replace("\n", " ")

lst_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID',
           'ID number', 'Institution', 'Department', 'Phone', 'Mobile phone', 'Address']
lst_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim', 'id_yahoo', 'id_msn', 'id_idnumber',
           'id_institution', 'id_department', 'id_phone1', 'id_phone2', 'id_address']
lst_val = [webpage, icq_num, id_skype, id_aim, id_yahoo, id_msn, id_idnumber,
           id_institution, id_department, phonenum1, phonenum2, address]

