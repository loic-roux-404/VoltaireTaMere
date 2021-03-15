from GUI import GUI, Login
from File import print_debug, found_data, connect
from init import init, pop_up
from selenium import webdriver
from os import path
import subprocess
init()

try:
    ch_output = subprocess.Popen(["chromedriver"])
    driver = webdriver.Chrome()
except:
    print_debug("[DRIVER] don't detect Chrome", "yellow")

driver.implicitly_wait(1)

if open("./file/log.txt","r", encoding="utf-8").read() == "" or open("./file/log.txt","r", encoding="utf-8").read() == "None":
    Login(driver).root.mainloop()
else:
    connect(driver)

gui = GUI(driver)
gui.Menu_1(gui.BG1)
gui.root.mainloop()