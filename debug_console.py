import os
from Question import Question, auto_learning
from File import Module
from selenium import webdriver
from routine import BOT, MANUAL

module_load = None
driver_ = None

def split_Word(String):
    List_From_String = [String[0 : String.find(" ")]]
    i = len(String[0 : String.find(" ")])
    word = " "

    while word != "":
        word = String[String.find(" ",i) : String.find(" ", String.find(" ",i)+1) ].replace(" ","")
        List_From_String += [word]
        i += len(word)+1
        
    List_From_String[len(List_From_String)-2] += String[len(String)-1].replace(" ","")
    return List_From_String[0: len(List_From_String)-1]

class cmd:
    class info:
        def info(self):
            print("/*******************\\")
            print("run: run basic process")
            print("load: load driver or file of module")
            print("open_file: open file in file foldier")
            print("learning: run process of auto learning")
            print("\\*******************/")

    class run:
        def info(self):
            print("/*******************\\")
            print("question: test error detetction process")
            print("bot: run bot routine one time")
            print("manual: run manual routine one time")
            print("\\*******************/")
        def question(self):
            Question(input("sentence>"), input("match>"))
        def bot(self):
            global module_load
            global driver_
            if module_load == None:
                print("VoltaireTaMere_debug>no module load")
            elif driver_ == None:
                print("VoltaireTaMere_debug>no driver load")
            else:
                BOT(driver_, module_load.data, False)
        def manual(self):
            global module_load
            global driver_
            if module_load == None:
                print("VoltaireTaMere_debug>no module load")
            elif driver_ == None:
                print("VoltaireTaMere_debug>no driver load")
            else:
                MANUAL(driver_, module_load.data, False)
        def meven(self):
            print("t'es trop BG")

    class load:
        def info(self):
            print("/*******************\\")
            print("module: load extraction data process from path")
            print("driver: load driver and connect")
            print("\\*******************/")
        def module(self):
            global module_load
            module_load = Module(input("path>"))
        def driver(self):
            global driver_
            driver_ = webdriver.Chrome()
            driver_.get("https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet-voltaire.fr/choix-parcours/&applicationCode=pv")
            driver_.implicitly_wait(1)
            flog = open(".\\file\\log.txt","r+", encoding="utf-8")
            log = flog.read()
            logIn = log[log.index("login:") : log.index("mdp:")].replace("login:","")
            mdp = log[log.index("mdp:") : len(log)].replace("mdp:","")
            flog.close()
            driver_.find_element_by_id("user_pseudonym").send_keys(logIn)
            driver_.find_element_by_id("user_password").send_keys(mdp)
            driver_.find_element_by_id("login-btn").click()
    
    class open_file:
        def debug(self):
            os.startfile(".\\file\\DEBUG.txt")
        def log(self):
            os.startfile(".\\file\\log.txt")
        def learning_data(self):
            os.startfile(".\\file\\auto_learning_data.txt")
        def learning_match(self):
            os.startfile(".\\file\\auto_learning_match.txt")
    
    class learning:
        def info(self):
            print("/*******************\\")
            print("learn_match: add match in mermory")
            print("learn_data: add error in memory")
            print("memory_data: try to find error in memory")
            print("memory_match: try to find match in memory")
            print("\\*******************/")
        def learn_match(self):
            auto_learning().add_match(input("sentence>"), input("err>"))
        def learn_data(self):
            auto_learning().add_data(input("list>"), input("err>"))
        def memory_data(self):
            print(auto_learning().memory_data(input("list>")))
        def memory_match(self):
            print(auto_learning().memory_match(input("sentence>")))

while  1:
    command = input("VoltaireTaMere_debug>")
    if command == "stop":
        if driver_ != None:
            driver_.close()
        exit()
    if command == "info":
        command += " info"
    try:
        command = split_Word(command)
        getattr(getattr(cmd(), command[0]), command[1])("")
    except:
        print("unknown command, try \"info\" for more informations")
