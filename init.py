from tkinter import Tk, Label, PhotoImage, Button
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.opera.options import Options as opera_options
from selenium.webdriver.edge.options import Options as edge_options
from File import print_debug, found_data
#/msg(-size:str -txt:str -title:str -link:str -lock:bool -version:str -show:bool)

class pop_up:
    class cls_option:
            def __init__(self, option):
                self.size = option[option.index("size:")+5: option.index("-", option.index("size:"))-1]
                self.txt = option[option.index("txt:")+4: option.index("-", option.index("txt:"))-1]
                self.title = option[option.index("title:")+6: option.index("-", option.index("title:"))-1]
                self.link = option[option.index("link:")+5: option.index("-", option.index("link:"))-1]
                self.lock = int( option[option.index("lock:")+5: option.index("-", option.index("lock:"))-1])
            
            def print_self(self):
                print("size:",self.size)
                print("txt:",self.txt)
                print("title:",self.title)
                print("link:",self.link)
                print("lock:",self.lock)

    def __init__(self, string):
        self.command = string[string.index("/")+1 : string.index("{")]
        self.option = self.cls_option(string[string.index("{")+1 : string.index("}")]+" -")
    
    def start_root(self):
        self.root = Tk()
        self.root.title(self.option.title)
        self.root.resizable(False, False)
        self.root.geometry(self.option.size)
        self.root.iconphoto(True, PhotoImage(file = "asset/VoltaireTaMere_icon[PNG].png"))
        self.root.configure(bg='#23272A')

        Label(self.root, text=self.option.txt, bg='#23272A', fg='#ffffff', font=('Helvetica', '10',"bold")).pack()

        Button(self.root,
                        text="  OK  ",
                        command=lambda: [self.open_link(), self.root.destroy()],  
                        bg="#a2d417",
                        fg="#ffffff",
                        activebackground  ="#a2d417",
                        bd=0).pack()
    
    def open_link(self):
        if self.option.link != "None":
            webbrowser.open_new(self.option.link)

    def print_self(self):
        print("command:", self.command)
        self.option.print_self()

def init():
    open("./file/DEBUG.txt","w",encoding="utf-8").close()
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
                e = pop_up("/msg{-txt:aucun moteur\n de recherche detecté \n(chrome, opera ou firefox) -title:VoltaireTaMere -link:https://www.google.com/intl/fr_fr/chrome/ -lock:0 -size:180x90}")
                e.start_root()
                e.root.mainloop()
                exit()
    return
    v_driver.get("https://sites.google.com/view/voltairetamere/init")
    v_driver.implicitly_wait(1)
    init_command = v_driver.find_element_by_class_name("yaqOZd").text
    print("init_command:", init_command)
    v_driver.close()
    if init_command[init_command.index("version:")+8:] != found_data("./file/version.txt","version","str"):
        init_command = "/msg{-txt:VoltaireTaMere doit être\n mis à jour -title:VoltaireTaMere -link:https://sites.google.com/view/voltairetamere/accueil -lock:1 -size:180x70}"

    if init_command != "version:"+found_data("./file/version.txt","version","str"):
        w = pop_up(init_command)
        w.start_root()
        w.root.mainloop()
        if w.option.lock:
            exit()