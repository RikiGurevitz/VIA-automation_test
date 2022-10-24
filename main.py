from telnetlib import EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sign_up(name, password):
    driver.find_element(By.ID, 'signin2').click()
    driver.implicitly_wait(500)
    driver.find_element(By.ID, 'sign-username').send_keys(name)
    driver.find_element(By.ID, 'sign-password').send_keys(password)
    driver.implicitly_wait(600)
    driver.find_element(By.CSS_SELECTOR, '#signInModal > div > div > div.modal-footer > button.btn.btn-primary').click()
    try:
       # wait for the alert
        WebDriverWait(driver, 5).until(EC.alert_is_present(), 'wait for alert')
        alert = driver.switch_to.alert
        # approve the alert
        alert.accept()
    except TimeoutException:
        pass
    driver.implicitly_wait(600)
    log_in(name, password)


def buy_the_phone_and_tests():
    driver.implicitly_wait(5000)
    driver.find_element(By.CSS_SELECTOR, '#tbodyid > div:nth-child(3) > div > div > h4 > a').click()
    driver.implicitly_wait(100)
    driver.find_element(By.CSS_SELECTOR, '#tbodyid > div.row > div > a').click()
    driver.implicitly_wait(100)
    url = driver.current_url
    list_check = []
    # check rhe cart
    nexus6_id = url.split('=', 1)[1].split('#')[0]
    driver.find_element(By.ID, 'cartur').click()
    driver.implicitly_wait(100)
    list_len = driver.find_elements(By.CSS_SELECTOR, '#tbodyid > tr')
    nexus6_name = driver.find_element(By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(2)').text
    nexus6_price = driver.find_element(By.CSS_SELECTOR, '#tbodyid > tr > td:nth-child(3)').text

    if len(list_len) == 1:
        list_check.append(1)
    else:
        list_check.append(0)
    if nexus6_id == '3':
        list_check.append(1)
    else:
        list_check.append(0)
    if nexus6_name == "Nexus 6":
        list_check.append(1)
    else:
        list_check.append(0)
    if nexus6_price == '650':
        list_check.append(1)
    else:
        list_check.append(0)

    if list_check.count(list_check[0]) == len(list_check):
        print('the tests are correct')
    else:
        print('the tests are not correct')


def log_in(name, password):
    driver.find_element(By.ID, 'login2').click()
    driver.implicitly_wait(500)
    user_name = driver.find_element(By.ID, 'loginusername')
    user_name.send_keys(name)
    user_password = driver.find_element(By.ID, 'loginpassword')
    user_password.send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ' #logInModal > div > div > div.modal-footer > button.btn.btn-primary').click()
    driver.implicitly_wait(200)
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present(), 'wait for alert')
        alert = driver.switch_to.alert
        if 'Wrong password.' in alert.text or 'User does not exist.' in alert.text:
            alert.accept()
            driver.implicitly_wait(300)
            user_name.clear()
            user_password.clear()
            driver.find_element(By.CSS_SELECTOR,
                                '#logInModal > div > div > div.modal-footer > button.btn.btn-secondary').click()
            driver.implicitly_wait(300)
            sign_up(name, password)
        else:
            alert.accept()
            driver.implicitly_wait(100)
            driver.find_element(By.CSS_SELECTOR,
                                'logInModal > div > div > div.modal-footer > button.btn.btn-primary').click()
    except TimeoutException:
        pass


# --------main
# open the broser
driver = webdriver.chrome.webdriver.WebDriver(executable_path='C:/automation/drivers/chromedriver.exe')
driver.maximize_window()
# get into the url adress
url = "https://www.demoblaze.com/"
driver.get(url)
log_in('r^9xxxxx', '778889$$___')
driver.implicitly_wait(300)
buy_the_phone_and_tests()
driver.implicitly_wait(300)

driver.close()
