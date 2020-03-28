# If you want to run this program, you will have to install this:
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# If the link doesn't work, type in ChromeDriver and you'll probably get the link.
# Once you have the ChromeDriver all set up, if you're on Mac or Linux, in your terminal, type:
# cp chromedriver /usr/local/bin
# Note that you can only run this program in Chrome!


# Imports
from selenium import webdriver

# Content
browser = webdriver.Chrome()
browser.get("github.com")

signin_link = browser.find_element_by_link_text("Sign In")
signin_link.click()

# Do not try this test account. If you want to try, sign in with any account of yours
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("user123")
password_box = browser.find_element_by_id("password")
password_box.send_keys("thisisapassword")

assert "user123" in browser.page_source

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "user123" in link_label
