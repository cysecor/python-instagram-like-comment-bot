from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import random


def hand_typed_comment(comment, field):
    for i, v in enumerate(comment):
        field.send_keys(v)
        sleep(random.random() / 3)


binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary, executable_path="/home/kali/Desktop/geckodriver")
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys("***************")
password_input.send_keys("***************")


login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

not_now_btn = browser.find_element_by_xpath("//button[text()='Not Now']")
not_now_btn.click()

sleep(2)

not_now_btn = browser.find_element_by_xpath("//button[text()='Not Now']")
not_now_btn.click()

sleep(2)

browser.get('https://www.instagram.com/explore/tags/pentesting/')

sleep(3)

posts = browser.find_elements_by_css_selector("a[href*='/p/']")
links = [elem.get_attribute('href') for elem in posts]

comments = ["Nice job!", "Wow! So cool!", "Awesome!", "Superb!", "You have some skills!"]

for link in links:
    random_time_addon = random.random()

    browser.get(link)
    sleep(3 + random_time_addon)

    like_btn = browser.find_element_by_css_selector(".fr66n .wpO6b")
    like_btn.click()
    sleep(0.5 + random_time_addon)

    like_btn = browser.find_element_by_css_selector("._15y0l .wpO6b")
    like_btn.click()
    sleep(0.5 + random_time_addon)

    comment_textarea = browser.find_element_by_css_selector("textarea")
    hand_typed_comment(random.choice(comments), comment_textarea)
    sleep(0.5 + random_time_addon)

    submit_comment = browser.find_element_by_xpath("//button[text()='Post']")
    submit_comment.click()
    sleep(2 + random_time_addon)



#browser.close()