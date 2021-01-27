from selenium import webdriver
import webbrowser
from GUI import GUI, Login
from File import print_debug
from tkinter import Tk, Label, PhotoImage, Button
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.opera.options import Options as opera_options
from selenium.webdriver.edge.options import Options as edge_options

class pop_up:
    def __init__(self, size, msg, link):
        self.root = Tk()
        self.root.title("VoltaireTaMere")
        self.root.resizable(False, False)
        self.root.geometry(size)
        self.root.iconphoto(True, PhotoImage(file = "asset\\new_VoltaireTaMere_icon[PNG].png"))
        self.root.configure(bg='#23272A')

        Label(self.root, text=msg, bg='#23272A', fg='#ffffff', font=('Helvetica', '10',"bold")).pack()

        Button(self.root,
                        text="  OK  ",
                        command=lambda: [webbrowser.open_new(link), self.root.destroy()],  
                        bg="#a2d417",
                        fg="#ffffff",
                        activebackground  ="#a2d417",
                        bd=0).pack()

open(".\\file\\DEBUG.txt","w",encoding="utf-8").close()

try:
    option = chrome_options()
    option.add_argument ("--headless")
    v_driver = webdriver.Chrome(options=option)
except:
    print_debug("[v_driver] don't detect Chrome","yellow")
    try:
        option = firefox_options()
        option.add_argument ("--headless")
        v_driver = webdriver.Opera(options=option)
    except:
        print_debug("[v_driver] don't detect Opera","yellow")
        try:
            option = opera_options()
            option.add_argument ("--headless")
            v_driver = webdriver.Firefox(options=option)
        except:
            print_debug("[v_driver] CANT FIND COMPATIBLE DRIVER -> EXIT","red")
            pop_up("200x50","aucun moteur de\nrecherche detecté","https://www.google.com/intl/fr_fr/chrome/").root.mainloop()
            exit()

v_driver.get("https://sites.google.com/view/voltairetamere/version")
v_driver.implicitly_wait(1)
print_debug("[VERSION] "+open(".\\file\\version.txt", "r",encoding="utf-8").read(), "white")

if v_driver.find_element_by_class_name("yaqOZd").text != open(".\\file\\version.txt", "r",encoding="utf-8").read():
    v_driver.close()
    pop_up("300x100","VoltaireTaMere require une \nmise à jour.\nMerci de reinstaller cette nouvelle versions\n","https://sites.google.com/view/voltairetamere/accueil").root.mainloop()
    exit()
v_driver.close()

flog = open(".\\file\\log.txt","r", encoding="utf-8")
log = flog.read()
print_debug("[LOGIN] log: "+log,"white")

try:
    logIn = log[log.index("login:") : log.index("mdp:")].replace("login:","")
    mdp = log[log.index("mdp:") :].replace("mdp:","")
except:
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
            print_debug("[DRIVER] CANT FIND COMPATIBLE DRIVER -> EXIT","red")
            pop_up("200x70","aucun moteur de\nrecherche detecté","https://www.google.com/intl/fr_fr/chrome/").root.mainloop()
            exit()

driver.get("https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet-voltaire.fr/choix-parcours/&applicationCode=pv")
driver.implicitly_wait(1)
driver.find_element_by_id("user_pseudonym").send_keys(logIn)
driver.find_element_by_id("user_password").send_keys(mdp)
driver.find_element_by_id("login-btn").click()

gui = GUI(driver)
gui.Menu_1(gui.BG1)
gui.root.mainloop()