from selenium import webdriver
from GUI import GUI, Login
from File import print_debug

open(".\\file\\DEBUG.txt","w",encoding="utf-8").close()

flog = open(".\\file\\log.txt","r", encoding="utf-8")
log = flog.read()
print_debug("[LOGIN] log: "+log,"white")

if log == "":
    flog.close()
    log_gui = Login()
    log_gui.root.mainloop()
    flog = open(".\\file\\log.txt","r", encoding="utf-8")
    log = flog.read()

logIn = log[log.index("login:") : log.index("mdp:")].replace("login:","")
mdp = log[log.index("mdp:") :].replace("mdp:","")
flog.close()
print_debug("[LOGIN] log: "+logIn+" "+mdp,"white")

try:
    driver = webdriver.Chrome()
except:
    print_debug("[DRIVER] don't detect Chrome","yellow")
    try:
        driver = webdriver.Opera()
    except:
        print_debug("[DRIVER] don't detect Opera","yellow")
        try:
            driver = webdriver.Firefox()
        except:
            print_debug("[DRIVER] don't detect Firefox","yellow")
            try:
                driver = webdriver.Edge()
            except:
                print_debug("[DRIVER] CANT FIND DRIVER -> EXIT","red")
                exit()

driver.get("https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet-voltaire.fr/choix-parcours/&applicationCode=pv")
driver.implicitly_wait(1)
driver.find_element_by_id("user_pseudonym").send_keys(logIn)
driver.find_element_by_id("user_password").send_keys(mdp)
driver.find_element_by_id("login-btn").click()

gui = GUI(driver)
gui.Menu_1(gui.BG1)
gui.root.mainloop()
driver.close()