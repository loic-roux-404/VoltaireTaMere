import os
from tkinter import Button, Label, Tk, Entry, Listbox, Text, Menubutton, Menu, PhotoImage, StringVar, IntVar, Toplevel
from time import sleep
from File import Module, print_debug, found_data, connect, write_data
from routine import BOT, MANUAL
from threading import Thread
from Question import auto_learning

class GUI:
    def __init__(self,driver):
        self.root = Tk()
        self.root.title("VoltaireTaMere")
        self.root.resizable(False, False)
        self.root.geometry('600x350')
        self.root.iconphoto(True, PhotoImage(file = "asset\\VoltaireTaMere_icon[PNG].png"))
        self.root.configure(bg='#23272A')
        
        self.Auto_off = PhotoImage(file = "asset\\Boutton_Auto_off.png")
        self.Auto_on = PhotoImage(file = "asset\\Boutton_Auto_on.png")
        self.Manual = PhotoImage(file = "asset\\Boutton_Manuel.png")
        self.back = PhotoImage(file = "asset\\Boutton_Retour.png")
        self.load_file = PhotoImage(file = "asset\\Boutton_Load.png")
        self.Quitter = PhotoImage(file = "asset\\boutton_Quitter.png")
        self.BG1 = PhotoImage(file = "asset\\Menu_1.png")
        self.BG2 = PhotoImage(file = "asset\\Menu_2.png")
        self.BG3 = PhotoImage(file = "asset\\Menu_3.png")

        self.driver = driver
        self.module = Module("")
        self.bot_on = False

        self.accuracy = IntVar()
        self.time_next = IntVar()
        self.accuracy.set(found_data("./file/options.txt", "accuracy", "int"))
        self.time_next.set(found_data("./file/options.txt", "accuracy", "int"))
        
        self.number_q = 0
        self.prgm = StringVar()
        self.niveau = StringVar()

        self.fond = Label(self.root, image=None, bg= '#23272A')
        self.btn_pont_sup = Button(self.root, text = "PONT\nSUPÉRIEUR",
                            command=lambda : [self.prgm.set("pont_Supérieur"),
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Test\\ Blanc"),
                                                self.Menu_Unpack(),self.Menu_2(self.BG2)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_sup = Button(self.root, text = "SUPÉRIEUR",
                            command=lambda : [self.prgm.set("Supérieur"), 
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Module\\ 9 Module\\ 10 Test\\ Blanc"), 
                                                self.Menu_Unpack(), self.Menu_2(self.BG2)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_exc = Button(self.root, text = "EXCELLENCE",
                            command=lambda : [self.prgm.set("Excellence"),
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Module\\ 9 Module\\ 10 Module\\ 11 Module\\ 12 Verbes\\ Pronominaux\\ II"), 
                                                self.Menu_Unpack(), self.Menu_2(self.BG2)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_cus = Button(self.root, text = "CUSTOM",
                            bg="#a2d417",
                            command=lambda :[self.prgm.set("CUS"),self.niveau.set(""),self.Menu_Unpack(),self.Menu_3(self.BG3)],
                            activebackground  ="#ffffff",
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_auto =  Button(self.root, 
                        image=self.Auto_off,
                        command= self.switch_bot,
                        bg="#a2d417",
                        activebackground  ="#a2d417",
                        bd=0)
        self.btn_manual =  Button(self.root, 
                        image=self.Manual,
                        command= lambda: Thread(target=self.ROUTINE_MANUAL).start(),
                        bg="#23272A",
                        activebackground  ="#23272A",
                        bd=0)
        self.btn_load_file =  Button(self.root, 
                        image=self.load_file,
                        command=self.init_module,
                        bg="#23272A",
                        activebackground  ="#23272A",
                        bd=0)
        self.btn_back =  Button(self.root, 
                        image=self.back,
                        command=lambda: [self.Menu_Unpack(),self.Menu_1(self.BG1)],
                        bg="#23272A",
                        activebackground  ="#23272A",
                        bd=0)
        self.btn_quit =  Button(self.root, 
                        image=self.Quitter,
                        command=self.root.destroy,  
                        bg="#23272A",
                        activebackground  ="#23272A",
                        bd=0)
        self.listB_Module = Listbox(self.root,
                        exportselection=0,
                        listvariable = self.niveau, 
                        selectmode = "single",
                        activestyle = "none",
                        height = 14,
                        width = 21,
                        bd = 0,
                        bg = "#2C2F33",
                        fg = "#ffffff",
                        selectbackground = "#a2d417",
                        font=('Helvetica', '10'))
        self.log = Text (self.root,
                        height = 12,
                        width=47,
                        bg="#2C2F33",
                        fg="#ffffff",
                        bd=0,
                        font=('Helvetica', '10'))
        self.log.tag_config("green",foreground = "#40ff46")
        self.log.tag_config("red",foreground = "#ff4040")
        self.log.tag_config("yellow", foreground = "#f5ff40")
        self.log.tag_config("cyan", foreground = "#00ffff")
        self.log.tag_config("magenta", foreground = "#ff00ff")
        self.log.tag_config("white", foreground = "#ffffff")
        self.menuAide = Menubutton(self.root, 
                            text='Aide', 
                            width='6', 
                            fg='#ffffff',
                            bg='#2c2e30', 
                            activebackground='#a2d417',
                            bd = 0)
        self.SousMenuAide = Menu(self.menuAide, fg='#ffffff', bg='#2c2e30',activebackground='#a2d417')
        self.SousMenuAide.add_command(label='Notice', command = lambda: os.startfile(".\\file\\NOTICE.pdf"))
        self.SousMenuAide.add_command(label='réinitialiser Login', command = lambda: [Login(self.driver, self.root)])
        self.menuAide.configure(menu=self.SousMenuAide)

        self.menuOption = Menubutton(self.root, 
                            text='Option', 
                            width='6', 
                            fg='#ffffff',
                            bg='#2c2e30', 
                            activebackground='#a2d417',
                            bd = 0)
        self.SousMenuOption = Menu(self.menuOption, fg='#ffffff', bg='#2c2e30',activebackground='#a2d417')
        self.SousMenuOption.add_command(label='OverClock', command = lambda : [self.time_next.set(1), print_debug("[MAIN] Overclock ON", "yellow"), 
                                                                            self.log.insert("end","Overclock ON\n", "yellow")])
        self.SousMenuOption.add_command(label='options', command = lambda : [self.Menu_Unpack(), self.Menu_4()])
        self.menuOption.configure(menu=self.SousMenuOption)
        self.option_auto_login = Button(self.root, text = "auto login",
                            command=lambda : [self.log.delete(1.0,"end"), self.input_data.place_forget(),
                                            self.log.insert("end", "L'auto login permet de se connecter automatiquement a son compte projet voltaire lors du démarage"),
                                            self.switch_auto_login.place(x=320, y=30)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 2,
                            width = 20,
                            font=('Helvetica', '10'))
        self.option_accuracy = Button(self.root, text = "précision",
                            command=lambda : [self.switch_auto_login.place_forget(), self.log.delete(1.0,"end"), 
                                            self.set_accurate_buffer(), self.input_data.place(x=320, y=30),
                                            self.log.insert("end","Définit le pourcentage de bonnes réponses")],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 2,
                            width = 20,
                            font=('Helvetica', '10'))
        self.option_time = Button(self.root, text = "temps d'attente",
                            command=lambda : [self.switch_auto_login.place_forget(), self.log.delete(1.0,"end"), 
                                            self.set_time_buffer(), self.input_data.place(x=320, y=30),
                                            self.log.insert("end","définit le temps d'attente entre chaque question")],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 2,
                            width = 20,
                            font=('Helvetica', '10'))

        self.switch_auto_login = Button(self.root, text = "",
                            command=None,
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 1,
                            width = 10,
                            font=('Helvetica', '10'))

        self.time_buffer = StringVar()
        self.time_buffer.set(found_data("./file/options.txt","time","int"))
        self.accurate_buffer = StringVar()
        self.accurate_buffer.set(found_data("./file/options.txt","accuracy","int"))

        self.input_data = Entry (self.root,
                            textvariable = None,
                            bg="#2C2F33",
                            fg="#ffffff",
                            width = 11,
                            bd=1,
                            font=('Helvetica', '10')) 
    
    def auto_login_switch(self):
        if found_data("./file/options.txt","auto_login", "int"):
            self.switch_auto_login["bg"] = "#a2d417"
            self.switch_auto_login["text"] = "activer"
            self.switch_auto_login["command"] = lambda: [write_data("./file/options.txt","auto_login",0), self.auto_login_switch()]
        else:
            self.switch_auto_login["bg"] = "#2C2F33"
            self.switch_auto_login["text"] = "desactiver"
            self.switch_auto_login["command"] = lambda: [write_data("./file/options.txt","auto_login",1), self.auto_login_switch()]

    def Menu_1(self, BG):
        self.fond["image"] = BG
        self.fond.pack()
        self.btn_pont_sup.place(x=22, y=170)
        self.btn_sup.place(x=174, y=170)
        self.btn_exc.place(x=326, y=170)
        self.btn_cus.place(x=478, y=170)
        self.btn_quit.place(x=478, y=307)
        self.menuAide.place(x=555, y=0)
        self.menuOption.place(x=510, y=0)
    def Menu_2(self, BGaff):
        self.fond["image"] = BGaff
        self.log["width"] = 47
        self.btn_auto["bg"] = "#a2d417"
        self.btn_auto["activebackground"] = "#a2d417"
        self.fond.pack()
        self.btn_load_file.place(x=30, y=308)
        self.btn_manual.place(x=255, y=60)
        self.btn_auto.place(x=402, y=60)
        self.btn_back.place(x=477, y=309)
        self.log.place(x=255, y=105)
        self.listB_Module.place(x=32, y=60)
        self.listB_Module.selection_set(0)
        self.menuAide.place(x=555, y=0)
        self.menuOption.place(x=510, y=0)
    def Menu_3(self, BGaff):
        self.fond["image"] = BGaff
        self.log["width"] = 79
        self.btn_auto["bg"] = "#23272A"
        self.btn_auto["activebackground"] = "#23272A"
        self.fond.pack()
        self.btn_load_file.place(x=30, y=308)
        self.btn_manual.place(x=30, y=63)
        self.btn_auto.place(x=156, y=63)
        self.btn_back.place(x=477, y=309)
        self.log.place(x=30, y=103)
        self.menuAide.place(x=555, y=0)
        self.menuOption.place(x=500, y=0)
        os.startfile(".\\Modules\\Custom\\Module1.txt")
    def Menu_4(self):
        self.btn_back["command"] = lambda: [ self.Menu_Unpack(),self.Menu_1(self.BG1), 
                                            write_data("./file/options.txt","time", self.time_buffer.get()),
                                            write_data("./file/options.txt","accuracy", self.accurate_buffer.get()),
                                            self.accuracy.set(found_data("./file/options.txt", "accuracy", "int")),
                                            self.time_next.set(found_data("./file/options.txt", "accuracy", "int"))]
        self.auto_login_switch()
        self.log["width"] = 58
        self.log["bg"] = "#23272A"
        self.btn_back.place(x=477, y=309)
        self.menuAide.place(x=555, y=0)
        self.option_auto_login.place(x=0, y=10)
        self.option_accuracy.place(x=0, y=65)
        self.option_time.place(x=0, y=120)
        self.log.place(x=180, y=80)

    def set_time_buffer(self):
        self.input_data["textvariable"] = self.time_buffer
    def set_accurate_buffer(self):
        self.input_data["textvariable"] = self.accurate_buffer

    def Menu_Unpack(self):
        self.log["bg"] = "#2C2F33"
        self.log.delete(1.0,"end")
        self.bot_on = False
        self.btn_auto["image"]= self.Auto_off
        self.btn_back["command"] = lambda: [self.Menu_Unpack(),self.Menu_1(self.BG1)]
        self.input_data.place_forget()
        self.switch_auto_login.place_forget()
        self.fond.pack_forget()
        self.btn_load_file.place_forget()
        self.btn_manual.place_forget()
        self.btn_auto.place_forget()
        self.btn_back.place_forget()
        self.listB_Module.place_forget()
        self.log.place_forget()
        self.btn_pont_sup.place_forget()
        self.btn_sup.place_forget()
        self.btn_exc.place_forget()
        self.btn_cus.place_forget()
        self.btn_quit.place_forget()
        self.menuAide.place_forget()
        self.menuOption.place_forget()
        self.option_auto_login.place_forget()
        self.option_accuracy.place_forget()
        self.option_time.place_forget()

    def init_module(self):
        try:
            self.module = Module(".\\Modules\\"+ self.prgm.get() + "\\Module"+ str(self.listB_Module.curselection()[0] + 1)+ ".txt")
        except:
            self.module = Module(".\\Modules\\Custom\\Module1.txt")
        
        if self.module.data == []:
            self.log.insert("end","erreur aucun fichier chargé\n","red")
        else:
            self.log.insert("end","fichier correctement chargé\n","green")

    def switch_bot(self):
        if self.bot_on:
            self.bot_on = False
            self.btn_auto["image"]=self.Auto_off
        elif self.module.data != []:
            self.bot_on = True
            self.btn_auto["image"]=self.Auto_on
            self.td = Thread(target=self.ROUTINE_BOT)
            self.td.start()
        else:
            self.log.insert("end","erreur aucun fichier chargé\n","red")
            print_debug("AUCUN  FICHIER CHARGÉ","red")

    def ROUTINE_BOT(self):
        if self.accuracy.get() < 0:
            self.accuracy.set(0)
            write_data("./file/options.txt","accuracy",0)
            print_debug("[option] accuracy valeur interdite", "red")
        if self.time_next.get() < 1:
            self.time_next.set(1)
            write_data("./file/options.txt","time",1)
            print_debug("[option] time valeur interdite", "red")

        while self.bot_on:
            self.log.delete(1.0,"end")
            return_tag = BOT(self.driver, self.module.data, self.module.test_blanc, self.accuracy.get())
            print_debug("return_tag: "+str(return_tag)+"\n","yellow")
            if type(return_tag) != list:
                if return_tag == "feature_in":
                    self.log.insert("end","Merci de fermer la Pop-up\n","yellow")
                elif "can't_touche" in return_tag:
                    self.log.insert("end","Je n'arrive pas a toucher: "+ return_tag[return_tag.index("&")+1 : len(return_tag)] +"\n","yellow")
                elif return_tag == "not_found":
                    self.log.insert("end","je trouve pas sorry UwU\n","yellow")  
                break
            
            self.number_q += 1
            if self.module.test_blanc == False:
                if self.driver.find_elements_by_xpath("//span[@title='Mauvaise réponse']") != [] and return_tag != ["auto_fail"]:
                    text = self.driver.find_elements_by_xpath("//span[@class = 'answerWord']/span[@class = 'pointAndClickSpan']")[1].text
                    if return_tag == []:
                        auto_learning().add_match( self.driver.find_element_by_class_name("sentence").text, text)
                    else:
                        auto_learning().add_data( return_tag, text)
                    self.log.insert("end","erreur détéctée apprentissage...\n","green")

                self.driver.find_element_by_class_name("nextButton").click()

            self.log.insert("end","["+str(self.number_q)+"]: Clique fait !\n","green")
            self.log.insert("end",open(".\\file\\VTMtext.txt","r",encoding="utf-8").read())
            self.log.insert("end","\n\nWaiting...\n","green")
            i = 0
            while i < self.time_next.get() and self.bot_on:
                sleep(1)
                i += 1

        self.bot_on = False
        self.btn_auto["image"]=self.Auto_off
        self.time_next.set(found_data("./file/options.txt", "time", "int"))
        print_debug("[BOT_ROUTINE] I am a bot, and this action was performed automatically.\nI answered "+str(self.number_q)+" questions","green")
        self.log.insert("end","I am a bot, and this action was performed automatically.\nI answered "+str(self.number_q)+" questions\n","green")
        self.number_q = 0
        return 0

    def ROUTINE_MANUAL(self):
        self.log.delete(1.0,"end")
        return_tag = MANUAL(self.driver, self.module.data, self.module.test_blanc)
        if return_tag == "feature_in":
            self.log.insert("end","Merci de fermer la Pop-up\n","yellow")
        elif return_tag == "not_found":
            self.log.insert("end","je trouve pas sorry UwU\n","yellow")
        elif return_tag == "no_error":
            self.log.insert("end","pas de faute :D\n","green")
        else:
            self.log.insert("end","la faute est: "+ return_tag + "\n","green")
        
        self.log.insert("end",open(".\\file\\VTMtext.txt","r",encoding="utf-8").read())
        
class Login:
    def __init__(self, driver, parent=None):
        os.startfile(".\\file\\NOTICE.pdf")
        if parent == None:
            self.root = Tk()
        else:
            self.root = Toplevel(parent)
            self.root.iconphoto(True, PhotoImage(file = "asset\\VoltaireTaMere_icon[PNG].png"))
        self.driver =  driver
        self.root.title("VoltaireTaMere")
        self.root.resizable(False, False)
        self.root.geometry('240x180')
        self.root.configure(bg='#23272A')

        self.flog = open(".\\file\\log.txt","w", encoding="utf-8")
        self.User = StringVar()
        self.Mdp = StringVar()
        self.a = Label (self.root,
            text="Entrée vos identifiants Projet Voltaire",
            bg="#23272A",
            fg="#ffffff",
            font=('Helvetica', '10'))
        self.a.place(x=12, y=10)
        self.b = Label (self.root,
                text="E-mail:",
                bg="#23272A",
                fg="#ffffff",
                font=('Helvetica', '10'))
        self.b.place(x=12, y=40)
        self.c = Entry (self.root,
                textvariable = self.User,
                bg="#2C2F33",
                fg="#ffffff",
                width = 30,
                bd=1,
                font=('Helvetica', '10'))
        self.c.place(x=15, y=65)
        self.d = Label (self.root,
                text="Mot de passe:",
                bg="#23272A",
                fg="#ffffff",
                font=('Helvetica', '10'))
        self.d.place(x=12, y=90)
        self.e = Entry (self.root,
                textvariable = self.Mdp,
                bg="#2C2F33",
                fg="#ffffff",
                width = 30,
                bd=1,
                font=('Helvetica', '10'))
        self.e.place(x=15, y=115)
        self.f = Button (self.root,
                text="Valider",
                command= self.register,
                fg="#ffffff",
                bg="#8BC34A",
                font=('Helvetica', '12'),
                bd=0,)
        self.f.place(x=15, y=145)
        self.g = Button (self.root,
                text="Désactiver",
                command= self.unactive,
                fg="#ffffff",
                bg="#8BC34A",
                font=('Helvetica', '12'),
                bd=0,)
        self.g.place(x=145, y=145)
    
    def register(self):
        self.flog.write("login:"+self.User.get()+"\nmdp:"+self.Mdp.get()+"\n")
        self.flog.close()
        self.root.destroy()
        connect(self.driver)
    
    def unactive(self):
        self.flog.write("login:*\nmdp:*\n")
        self.flog.close()
        self.root.destroy()
    