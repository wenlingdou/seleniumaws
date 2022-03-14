from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome('/Users/mike_coddy/GitHub/python_cctb/moodle_app/chromedriver')

# create a Chrome driver instance, specify the path to chromedriver file
# this give a DeprecationWarning
# driver = webdriver.Chrome('../chromedriver.exe')
#s = Service(executable_path='../chromedriver.exe')
#driver = webdriver.Chrome(service=s)

#---------------------------------------------------------------------------------------------------------
# Moodle Test Automation Plan
# launch to home page - validate we are on homepage

# navigate to login page - validate we are on login page
# login with admin account - validate we are on Dashboard page

# navigate to add new user page _ Site Adminiatration > User >Add New User - validate we are on Add new user page
# populate new user form fields using Faker library fake random data
# submit a new user form

# validate new user added
# search for new user using email - validate new is found
# logout of admin account
# login as a new user - validate a new user can login
# logout of new user account
# login with admin account
# search for a new user using email address
# delete new user

def setUp():
    print(f'Launch {locators.app} App')
    print(f'--------------------------------------------------')

    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # navigate to Moodle App website
    driver.get(locators.moodle_url)
    # check Moodle URL and home page title are as expected
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_homepage_title:
        print(f'HoHoHo! {locators.app} App website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('-----------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

def log_in(username, password):
    if driver.current_url == locators.moodle_url:   # check we are on home page
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_url and driver.title == locators.moodle_login_title:
            print(f'{locators.app} App login page is displayed! Continue to login.')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()  # method 1 using ID
            # locators XPATH practice------------------------------------------
            #driver.find_element(By.XPATH, '//button[contains(., "Log in")]').click()  #method2-using XPATH
            #driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]').click()  # method3-using XPATH
            #driver.find_element(By.XPATH, '//button[contains(@id, "loginbtn")]').click() # method 4 using XPATH + id
            #driver.find_element(By.XPATH, '//button[@id="loginbtn"]').click()  # method 5 using XPATH + id
            #driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()  # method 6 using * + id
            #driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()  # method 7 using CSS_SELECTOR
            #driver.find_element(By.CSS_SELECTOR, 'button[id="loginbtn"').click()  #method 8 using CSS_SELECTOR

            #---------------------------------------------------------------------------------------
            # validate login successfully Dashboard page is disable.
            if driver.current_url == locators.moodle_dashboard_url and driver.title == locators.moodle_dashboard_title:
                assert driver.current_url == locators.moodle_dashboard_url
                assert driver.title == locators.moodle_dashboard_title
                print(f'Login is successful. {locators.app} Dashboard is displayed - Page Title: {driver.title}')
            else:
                print(f'Dashboard is not displayed. Check your code or website and try again.')

def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'-----------Log out successful. {datetime.datetime.now()}')

################ '//span[contains(.,"")]'
def create_new_user():
    # navigate to 'Add a new user' form
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    linkcheck = driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    print(f'----------User link is displayed: {linkcheck}')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # validate we are on "Add a new user" page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_addnewuser_title
    print(f'-----navigate to add new user page title: {locators.moodle_addnewuser_title}')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.firstname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.lastname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_value('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.5)

    #upload picture
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    img_path = ['Server files', 'mp_courses', 'Category introduction', '51zLZbEVSTL._AC_SL1200_.jpg']
    for path in img_path:
        driver.find_element(By.LINK_TEXT, path).click()
        sleep(0.5)

    # select radio button
    # method 1 - click the radio button
    #driver.find_element(By.XPATH, '//input[@value="4"]').click()
    # method 2 - click the label attached to radio button
    driver.find_element(By.XPATH, '//label[contains(., "Create an alias/shortcut to the file")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(text(), "Select this file")]').click()
    sleep(0.25)

    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_descp)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.firstname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.lastname)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middlename)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.firstname)
    sleep(0.25)

    # populate list of interests
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    sleep(0.25)

    # Add multiple interests using for loop
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + '\n')
        #driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(Keys.ENTER)
        sleep(0.25)

    # for i in range(3):
    #     driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(locators.fake.job() + '\n')
    #     sleep(0.25)
    # populate optional fields
    #driver.find_element(By.LINK_TEXT, 'Optional').click()
    driver.find_element(By.XPATH, '//a[text()="Optional"]').click()

    for i in range(len(locators.lst_opt)):
        fld, fid, val = locators.lst_opt[i], locators.lst_ids[i], locators.lst_val[i]
        #print(f'Populate Optional Field: {fld}')
        driver.find_element(By.ID, fid).send_keys(val)
        sleep(0.25)

##################################################################
    # press submit button to complete the registration
    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'*----------New User {locators.new_username}/{locators.new_password}/{locators.email} is added______*')
#######################################################

def search_user():
    print('*--------------------SEARCH-------------------------------------*')
    if locators.moodel_users_mainpage_url in driver.current_url and driver.title == locators.moodle_users_mainpage_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users')
        print(f'---------Browse list of users page is displayed.')
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() and driver.find_element(By.NAME, 'email').is_displayed():
            sleep(0.25)
            print(f'Search for user by email {locators.email}')
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            sleep(0.25)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            sleep(0.25)
            driver.implicitly_wait(5)

            try:
                assert driver.find_element(By.XPATH, f'//td[contains(., "{locators.fullname}")]/../td[contains(., "{locators.email}")]').is_displayed()
                # capture user Moodle System ID
                href = driver.find_element(By.LINK_TEXT, locators.fullname).get_attribute("href")
                # global user_system_id
                locators.sysid = href[href.find('=') + 1 : href.rfind('&')]
                print(f'*-----User {locators.fullname}/ {locators.email} / System id: {locators.sysid}is found! -*')
            except NoSuchElementException as nse:
                print(' --- Element is not found')
                print(f'*----------The user {locators.fullname}/ {locators.email} is not exist.---------*')


def check_newuser_login():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.fullname}")]').is_displayed():
            sleep(0.25)
            print(f'*----User with the name {locators.fullname} is confirmed.-----*')

def delete_user():
    print('*-------------DELETE--------------------*')
    # navigate to Site Administration > User Browse list of user
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)

    # search for the user
    search_user()

    # delete user
    assert driver.find_element(By.XPATH, f'//td[contains(., "{locators.fullname}")]/../td/a[contains(@href, "delete={locators.sysid}")]').is_displayed()
    driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]/../td/a[contains(@href, "delete={locators.sysid}")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[text()="Delete"]').click()
    sleep(0.25)
    print(f'----User {locators.email}, System ID: {locators.sysid} is deleted at: {datetime.datetime.now()}---')

    # confirm delete
    search_user()


# setUp()
# log_in(locators.admin_username, locators.admin_password)
# create_new_user()
# search_user()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_newuser_login()
# log_out()
# log_in(locators.admin_username, locators.admin_password)
# delete_user()
# log_out()
# tearDown()