import os
from tkinter import Button, Label, Tk, Entry, Listbox, Text, Menubutton, Menu, PhotoImage, StringVar, IntVar
from time import sleep
from File import Module, print_debug
from routine import BOT, MANUAL
from threading import Thread
from Question import auto_learning

class GUI:
    def __init__(self,driver):
        self.root = Tk()
        self.root.title("VoltaireTaMere")
        self.root.resizable(False, False)
        self.root.geometry('600x350')
        self.root.iconphoto(True, PhotoImage(file = "asset\\new_VoltaireTaMere_icon[PNG].png"))
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

        self.time_next = IntVar()
        self.time_next.set(9)
        self.number_q = 0
        self.prgm = StringVar()
        self.niveau = StringVar()

        self.fond = Label(self.root, image=None, bg= '#23272A')
        self.btn_pont_sup = Button(self.root, text = "PONT\nSUPÉRIEUR",
                            command=lambda : [self.prgm.set("pont_Supérieur"),
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Test\\ Blanc"),
                                                self.Menu_Unpack(),self.Menu_2(self.BG2,self.BG1)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_sup = Button(self.root, text = "SUPÉRIEUR",
                            command=lambda : [self.prgm.set("Supérieur"), 
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Module\\ 9 Module\\ 10 Test\\ Blanc"), 
                                                self.Menu_Unpack(), self.Menu_2(self.BG2,self.BG1)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_exc = Button(self.root, text = "EXCELLENCE",
                            command=lambda : [self.prgm.set("Excellence"),
                                                self.niveau.set("Module\\ 1 Module\\ 2 Module\\ 3 Module\\ 4 Module\\ 5 Module\\ 6 Module\\ 7 Module\\ 8 Module\\ 9 Module\\ 10 Module\\ 11 Module\\ 12 Verbes\\ Pronominaux\\ II"), 
                                                self.Menu_Unpack(), self.Menu_2(self.BG2,self.BG1)],
                            bg="#a2d417",
                            highlightthickness=2,
                            bd=0,
                            height = 6,
                            width = 12,
                            font=('Helvetica', '10',"bold"))
        self.btn_cus = Button(self.root, text = "CUSTOM",
                            bg="#a2d417",
                            command=lambda :[self.prgm.set("CUS"),self.niveau.set(""),self.Menu_Unpack(),self.Menu_3(self.BG3,self.BG1)],
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
                        command=None,
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
        self.SousMenuAide.add_command(label='réinitialiser Login', command = lambda: [ self.root.destroy(), Login()])
        self.SousMenuAide.add_command(label='OverClock', command = lambda : [self.time_next.set(1), print_debug("[MAIN] Overclock ON", "yellow"), self.log.insert("end","Overclock ON\n", "yellow")])
        self.menuAide.configure(menu=self.SousMenuAide)

    def Menu_1(self, BG):
        self.fond["image"] = BG
        self.fond.pack()
        self.btn_pont_sup.place(x=22, y=170)
        self.btn_sup.place(x=174, y=170)
        self.btn_exc.place(x=326, y=170)
        self.btn_cus.place(x=478, y=170)
        self.btn_quit.place(x=478, y=307)
        self.menuAide.place(x=555, y=0)
    def Menu_2(self, BGaff,BG1,):
        self.fond["image"] = BGaff
        self.btn_back["command"]=lambda : [self.Menu_Unpack(),self.Menu_1(BG1)]
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
    def Menu_3(self, BGaff,BG1):
        self.fond["image"] = BGaff
        self.btn_back["command"]=lambda : [self.Menu_Unpack(),self.Menu_1(BG1)]
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
        os.startfile(".\\Modules\\Custom\\Module1.txt")
    def Menu_Unpack(self):
        self.log.delete(1.0,"end")
        self.bot_on = False
        self.btn_auto["image"]= self.Auto_off
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
    
    def init_module(self):
        try:
            self.module = Module(".\\Modules\\"+ self.prgm.get() + "\\Module"+ str(self.listB_Module.curselection()[0] + 1)+ ".txt")
        except:
            self.module = Module(".\\Modules\\Custom\\Module1.txt")
        
        if self.module == []:
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
            print_debug("AUCUN  FICHIER CHARGÉ","red")

    def ROUTINE_BOT(self):
        print(self.bot_on)
        while self.bot_on:
            self.log.delete(1.0,"end")
            return_tag = BOT(self.driver, self.module.data, self.module.test_blanc)
            print_debug("return_tag: "+str(return_tag)+"\n","yellow")
            self.number_q += 1
            if type(return_tag) != list:
                if return_tag == "feature_in":
                    self.log.insert("end","Merci de fermer la Pop-up\n","yellow")
                elif "can't_touche" in return_tag:
                    self.log.insert("end","Je n'arrive pas a toucher: "+ return_tag[return_tag.index("&")+1 : len(return_tag)] +"\n","yellow")
                elif return_tag == "not_found":
                    self.log.insert("end","je trouve pas sorry UwU\n","yellow")  
                break
                
            if self.module.test_blanc == False:
                if self.driver.find_elements_by_xpath("//span[@title='Mauvaise réponse']") != []:
                    text = self.driver.find_elements_by_xpath("//span[@class = 'answerWord']/span[@class = 'pointAndClickSpan']")[1].text
                    if return_tag == []:
                        auto_learning().add_match( self.driver.find_element_by_class_name("sentence").text, text)
                    else:
                        auto_learning().add_data( return_tag, text)
                    self.log.insert("end","erreur détéctéee apprentissage...\n","green")

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
        self.time_next.set(10)
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
    def __init__(self):
        os.startfile(".\\file\\NOTICE.pdf")
        self.root = Tk()
        self.root.title("VoltaireTaMere")
        self.root.resizable(False, False)
        self.root.geometry('240x180')
        self.root.iconphoto(True, PhotoImage(file = "asset\\new_VoltaireTaMere_icon[PNG].png"))
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
        self.f.place(x=90, y=145)
    
    def register(self):
        self.flog.write("login:"+self.User.get()+"mdp:"+self.Mdp.get())
        self.flog.close()
        self.root.destroy()