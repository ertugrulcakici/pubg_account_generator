import json
from random import choices
from time import sleep

import clipboard
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from logger import Logger

DEBUG = True

signInMail = ""
password = ""
username = ""


# read json from a file and import login datas and set them
with open("data.json", "r") as jsonFile:
    data = json.load(jsonFile)
    signInMail = data["signInMail"]
    password = data["password"]
    username = data["username"]


class app():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe", options=option)
        self.driver.maximize_window()
        self.logger = Logger(printing=DEBUG)

    def get_random_username():
        return username.join(choices("1234567890", k=3))

    def register(self):
        self.driver.get("https://accounts.pubg.com/register")
        self.logger.log("Logged into pubg.com for registering")
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-register/app-internal-page/div/div/div/div/app-register-form/div[2]/div[2]/div/form/div/div/div[2]/div/app-email-input/div/input").send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-register/app-internal-page/div/div/div/div/app-register-form/div[2]/div[2]/div/form/div/div/div[2]/div/app-password-input[1]/div/input").send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-register/app-internal-page/div/div/div/div/app-register-form/div[2]/div[2]/div/form/div/div/div[2]/div/app-password-input[2]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("/html/body/app-root/div/app-register/app-internal-page/div/div/div/div/app-register-form/div[2]/div[2]/div/form/div/div/div[2]/div/app-username-input/div/input").send_keys(
            username)
        self.driver.execute_script(
            'document.getElementsByName("month")[0].click()')
        chain = ActionChains(self.driver)
        chainend = ActionChains(self.driver)
        chainend.send_keys(Keys.TAB)
        chainend.send_keys(Keys.SPACE)
        chainyear = ActionChains(self.driver)
        chainyear.send_keys(Keys.DOWN)
        chain.send_keys(Keys.ENTER)
        chain.perform()
        self.driver.execute_script(
            'document.getElementsByName("day")[0].click()')
        chain.perform()
        self.driver.execute_script(
            'document.getElementsByName("year")[0].click()')
        [chainyear.perform() for i in range(20)]
        chain.perform()
        chainend.perform()
        self.driver.execute_script(
            'document.getElementsByClassName("button is-link is-primary")[0].click()')
        __import__("os").system(
            "start https://mail.google.com/mail/u/0/#inbox")

    def login_and_delete_account(self):
        self.driver.get("https://accounts.pubg.com/login")
        self.logger.log("Logging into pubg.com for logging in")
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-login/app-internal-page/div/div/div/div/app-login-form/form/div/div[2]/app-email-input/div/input").send_keys(signInMail)
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-login/app-internal-page/div/div/div/div/app-login-form/form/div/div[2]/app-password-input/div/input").send_keys(password)
        self.driver.execute_script(
            'document.getElementsByClassName("button is-link is-primary loginBtn")[0].click()')
        sleep(3)
        self.logger.log("logged in")
        self.driver.get("https://accounts.pubg.com/personal-info")
        self.driver.execute_script(
            'document.getElementsByClassName("accordion-content inactive")[4].className = "accordion-content active";')
        self.driver.execute_script(
            'document.getElementsByClassName("button is-link is-primary")[6].click()')
        self.driver.find_element_by_xpath(
            "/html/body/app-root/div/app-personal-info/app-internal-page/div/div/div/div/div/div[5]/app-delete-form/div/div[2]/section/app-password-input/div/input").send_keys(password)
        self.driver.execute_script(
            'document.getElementsByClassName("button is-link is-primary")[8].click()')
        sleep(3)
        self.logger.log("account deleted")


if __name__ == "__main__":
    myapp = app()
    myapp.login_and_delete_account()
    myapp.register()
    clipboard.copy(password)
