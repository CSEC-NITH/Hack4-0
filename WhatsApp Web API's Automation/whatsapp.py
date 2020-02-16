import time
import datetime as dt
import json
import os
import requests
import shutil
import pickle
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlencode
from bs4 import BeautifulSoup


def goto_main():
    try:
        driver.refresh()
        Alert(driver).accept()
    except Exception as e:
        print(e)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '._2zCfw')))


def dp_click_back():
    time.sleep(1)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span")
    python_button.click()
    return


def dp_click():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[1]/div/img")
    python_button.click()
    return


def view_dp():
    dp_click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[1]/div")
    python_button.click()
    time.sleep(10)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[3]/div/div/div[1]/div[2]")
    python_button.click()
    dp_click_back()
    return


def remove_dp():
    dp_click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[4]/div")
    python_button.click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    dp_click_back()
    return


'''def upload_dp():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[1]/div/img")
    python_button.click()
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[1]/div/div/div/div/div/img")
    python_button.click()
    time.sleep(3)
    driver.find_element_by_id("app").send_keys("C://Users/lenovo/Desktop/image.png")
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span")
    python_button.click()
    time.sleep(3)'''


def change_name():
    time.sleep(3)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(20):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("Enter new name: ")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return


def change_about():
    time.sleep(3)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("Enter new about: ")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return


def view_archived():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(5)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/header/div/div[1]/button/span")
    python_button.click()
    return


def view_starred():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(5)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/div/div/header/div/div[1]/button/span")
    python_button.click()
    return


def setting():
    time.sleep(3)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    return


def setting_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    return


def notification():
    setting()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[2]")
    python_button.click()
    return


def notificaton_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    setting_back()
    return


def notification_sound():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[1]/div[1]/div")
    python_button.click()
    notificaton_back()
    return


def notification_Desktop_alerts():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[2]/div[2]")
    python_button.click()
    notificaton_back()
    return


def notification_show_previews():
    notification()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[1]/span/div/span/div/div/div/div[3]/div[2]")
    python_button.click()
    notificaton_back()
    return


def group_chat_dots():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name: ")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/div/span")
    python_button.click()
    return


def group_info():
    group_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[1]/div")
    python_button.click()
    return


def group_info_back():
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button/span")
    python_button.click()
    return


def change_group_name():
    group_info()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/div[1]/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("Enter new group name: ")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    group_info_back()
    return


def change_group_desc():
    group_info()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/div/span[2]/div/span")
    python_button.click()
    time.sleep(2)
    actions = ActionChains(driver)
    for i in range(40):
        actions.send_keys(Keys.BACKSPACE).perform()
    name = input("Enter new group description: ")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    group_info_back()
    return


def mute_group():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[3]/label/input")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div[2]")
    python_button.click()
    return


def unmute_group():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    return


def clear_group_chat():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


def exit_group_chat():
    time.sleep(2)
    group_chat_dots()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]]")
    python_button.click()
    return


def individual_chat_dots():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name: ")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/div/span")
    python_button.click()
    return


def individual_info():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[1]/div")
    python_button.click()


def individual_chat_mute():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[3]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath(
        "//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/form/ol/li[3]/label/input")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[3]/div[2]")
    python_button.click()
    return


def individual_clear_chat():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[4]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


def individual_delete_chat():
    individual_chat_dots()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='main']/header/div[3]/div/div[3]/span/div/ul/li[5]/div")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()
    return


"--------------------------------------------------------------satyam-----------------------------------------------------------------------------------"


def logout():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    time.sleep(2)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div")
    python_button.click()
    return


def group_creation():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
    python_button.click()
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div")
    python_button.click()
    no = int(input("Enter number of participants: "))
    for x in range(no):
        actions = ActionChains(driver)
        num = int(input("Enter a number to add: "))
        actions.send_keys(num)
        actions.send_keys(Keys.ENTER).perform()

    python_button = driver.find_element_by_xpath(
        "//*[@id=\"app\"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span")
    python_button.click()
    actions = ActionChains(driver)
    name = input("enter the name of group")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return


def blocking():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name: ")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    time.sleep(1)
    python_button = driver.find_element_by_xpath("//*[@id=\"main\"]/header")
    python_button.click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath(
        "//*[@id=\"app\"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[6]/div/div[2]/div/span")
    python_button.click()
    time.sleep(1)
    python_button = driver.find_element_by_xpath("//*[@id=\"app\"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]")
    python_button.click()


def chat_selection():
    time.sleep(5)
    python_button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    python_button.click()
    actions = ActionChains(driver)
    name = input("enter the name of chat to select")
    actions.send_keys(name)
    actions.send_keys(Keys.ENTER).perform()
    return


'''
#def dropdown():
    #time.sleep(4)
   # chat_selection()
    #img = driver.find_element_by_class_name("_19RFN")
    #actionChains = ActionChains(driver)
    #actionChains.double_click(img).perform()
    #return
'''

'''def archive():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[1]/div")
    python_button.click()
    return


def mute_notifs():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[2]/div")
    python_button.click()
    return


def exit_group():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return


def pin_chat():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[4]/div")
    python_button.click()
    return'''


'''
def mark_unread():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[5]/div")
    python_button.click()
    return


def delete_chat():
    #dropdown()
    python_button = driver.find_element_by_xpath("//*[@id='app']/div/span[4]/div/ul/li[3]/div")
    python_button.click()
    return'''


'''def viewing_status():
    python_button = driver.find_element_by_xpath("//*[@id='side']/header/div[2]/div/span/div[1]/div/span")
    python_button.click()
    chat_selection()
    return'''

"-----------------------------------------------------------priyanka-------------------------------------------------------------------------------"


def send_messages():
    action = ActionChains(driver)
    time.sleep(5)
    button = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/input")
    button.click()
    name = input("Enter the name: ")
    action.send_keys(name)
    action.send_keys(Keys.ENTER).perform()
    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    button.click()
    message = input("Enter the message: ")
    action1 = ActionChains(driver)
    action1.send_keys(message)
    action1.send_keys(Keys.ENTER).perform()


def unread_user_names():
    time.sleep(8)
    scrolls = 100
    initial = 10
    user_names = []
    for i in range(0, scrolls):
        driver.execute_script("document.getElementById('pane-side').scrollTop={}".format(initial))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for i in soup.find_all("div", class_="_2WP9Q"):
            if i.find("div", class_="_1ZMSM"):
                username = i.find("div", class_="_3H4MS").text
                user_names.append(username)
        initial += 10
    user_names = list(set(user_names))
    return user_names


def get_last_message_for(name):
    # name = input("Enter name: ")
    messages = list()
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for i in soup.find_all("div", class_="FTBzM"):
        message = i.find("div", class_="_12pGw")
        if message:
            messages.append(message.text)
    messages = list(filter(None, messages))
    print(messages)


def send_picture():
    name = input("Enter name: ")
    caption = input("Enter a nice caption: ")
    picture_location = "/home/bolt/Pictures/201320.jpg"
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    try:
        attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
        send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'
        attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'
        attach_btn = driver.find_element_by_xpath(attach_xpath)
        attach_btn.click()
        time.sleep(1)
        attach_img_btn = driver.find_element_by_xpath(attach_type_xpath)
        attach_img_btn.send_keys(picture_location)
        time.sleep(1)
        if caption:
            caption_xpath = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]"
            send_caption = driver.find_element_by_xpath(caption_xpath)
            send_caption.send_keys(caption)
        send_btn = driver.find_element_by_xpath(send_file_xpath)
        send_btn.click()

    except (NoSuchElementException, ElementNotVisibleException) as e:
        print(str(e))


def send_document():
    name = input("Enter name: ")
    document_location = "/home/bolt/Documents/file.pdf"
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    try:
        attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
        send_file_xpath = '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span'
        attach_type_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input'
        attach_btn = driver.find_element_by_xpath(attach_xpath)
        attach_btn.click()
        time.sleep(1)
        attach_img_btn = driver.find_element_by_xpath(attach_type_xpath)
        attach_img_btn.send_keys(document_location)
        time.sleep(1)
        send_btn = driver.find_element_by_xpath(send_file_xpath)
        send_btn.click()
        time.sleep(3)

    except (NoSuchElementException, ElementNotVisibleException) as e:
        print(str(e))


def get_last_seen():
    name = input("Enter the name: ")
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(name + Keys.ENTER)
    time.sleep(2)
    last_seen = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/div[2]/span")
    print(last_seen.text)


def participants_for_group():
    group_name = input("Enter the name of group: ")
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(group_name + Keys.ENTER)
    try:
        click_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "._19vo_ > span:nth-child(1)")))
        click_menu.click()
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException as e:
        print("None")
    except Exception as e:
        print("None")
    time.sleep(2)
    group_participants = driver.find_element_by_xpath("//*[@id=\"main\"]/header/div[2]/div[2]/span")
    print("Group members: " + group_participants.text)
    button = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]")
    button.click()


'''def get_group_participants():
    group_name = input()
    participants_count_for_group(group_name)
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(group_name + Keys.ENTER)
    try:
        click_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#main > header > div._1WBXd > div._2EbF- > div > span")))
        click_menu.click()
    except TimeoutException:
        raise TimeoutError("Your request has been timed out! Try overriding timeout!")
    except NoSuchElementException as e:
        return "None"
    except Exception as e:
        return "None"
    participants = []
    scrollbar = driver.find_element_by_css_selector(
        "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div")
    for v in range(1, 70):
        print(v)
        driver.execute_script('arguments[0].scrollTop = ' + str(v * 300), scrollbar)
        time.sleep(0.10)
        elements = driver.find_elements_by_tag_name("span")
        for element in elements:
            try:
                html = element.get_attribute('innerHTML')
                soup = BeautifulSoup(html, "html.parser")
                for i in soup.find_all("span", class_="_3TEwt"):
                    if i.text not in participants:
                        participants.append(i.text)
                        print(i.text)
            except Exception as e:
                pass
        elements = driver.find_elements_by_tag_name("div")
        for element in elements:
            try:
                html = element.get_attribute('innerHTML')
                soup = BeautifulSoup(html, "html.parser")
                for i in soup.find_all("div", class_="_25Ooe"):
                    j = i.find("span", class_="_1wjpf")
                    if j:
                        j = j.text
                        if "\n" in j:
                            j = j.split("\n")
                            j = j[0]
                            j = j.strip()
                            if j not in participants:
                                participants.append(j)
                                print(j)
            except Exception as e:
                pass
    return participants'''


def join_group(self, invite_link):
    driver.get(invite_link)
    try:
        Alert(driver).accept()
    except:
        print("No alert Found")
    join_chat = driver.find_element_by_css_selector("#action-button")
    join_chat.click()
    WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')))
    join_group = driver.find_element_by_xpath(
        '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]')
    join_group.click()


def get_invite_link_for_group(self, groupname):
    search = driver.find_element_by_css_selector("._2zCfw")
    search.send_keys(groupname + Keys.ENTER)
    driver.find_element_by_css_selector("#main > header > div._5SiUq > div._16vzP > div > span").click()
    try:
        # time.sleep(3)
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")))
        invite_link = driver.find_element_by_css_selector(
            "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div > div > div:nth-child(5) > div:nth-child(3) > div._3j7s9 > div > div")
        invite_link.click()
        WebDriverWait(driver, self.timeout).until(EC.presence_of_element_located(
            (By.ID, "group-invite-link-anchor")))
        link = driver.find_element_by_id("group-invite-link-anchor")
        return link.text
    except:
        print("Cannot get the link")


def demonstration():
    print("Unread Messages from: ")
    user_names = unread_user_names()
    print(user_names)
    time.sleep(5)
    print("Last messages are: ")
    for x in range(len(user_names)):
        print(user_names[x])
        get_last_message_for(user_names[x])
    print("Reply to the message: ")
    send_messages()
    print("Blocking this number: ")
    blocking()
    print("Creating a group: ")
    group_creation()
    print("Data of group")
    participants_for_group()
    print("Posting a message and media(image & documents) in a group")
    send_picture()
    send_document()
    print("Logging out: ")
    logout()


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=./User_Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://web.whatsapp.com/')
    print("")
    demonstration()
    # send_messages()
    # unread_user_names()
    # get_last_message_for()
    # send_picture()
    # send_document()
    # get_status()
    # get_last_seen()
    # individual_clear_chat()
    # view_dp()
    # remove_dp()
    # group_creation()
    # blocking()
    # participants_for_group()

    '''participants_count_for_group()
    get_group_participants()
    create_group()
    join_group()
    get_invite_link_for_group()'''
