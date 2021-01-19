from termcolor import colored

def print_debug(string, color):
    print(colored(string,color))
    f = open(".\\file\\DEBUG.txt","a",encoding="utf-8")
    f.write(string+"\n")
    f.close()

class Module:
    def __init__(self,path):
        self.path = path
        self.data = self.extract()
        self.test_blanc = self.path == ".\\Modules\\Supérieur\\Module11.txt" or self.path == ".\\Modules\\pont_Supérieur\\Module9.txt"
    
    def extract(self):
        try:
            File = open(self.path, "r", encoding="utf-8")
        except:
            print_debug("[Module] erreur no file found","red")
            return []
        data_File = File.read()+"€"
        try:
            data_File = data_File[data_File.index("[\"java.util.ArrayList"):data_File.index("€")].replace("\\x3Cbr/\\x3E","\",\"")
        except:
            print_debug("[Module] erreur fichier vide","red")
            return []

        data = []
        i = 0
        extrt = " "
        
        while extrt != "":
            extrt = data_File[ data_File.find("\"",i) : data_File.find("\"", i+data_File.find("\"")+1) ]

            if "\\x3C" in extrt:
                data += [extrt.replace("\"","")
                                .replace("\\x3CB\\x3E", "<")
                                .replace("\\x3C/B\\x3E", ">")
                                .replace("\\x27","'")
                                .replace("\\xA0"," ")
                                .replace("\\x26#x2011;","-")
                                .replace("\\x3Cspan class\\x3Dsmallcaps\\x3E","")
                                .replace("\\x3C!-- smallcaps end --\\x3E\\x3C/span\\x3E","")
                                .replace("\\x3CSUP\\x3E","")
                                .replace("\\x3C/SUP\\x3E","")
                                .replace("a) ","")
                                .replace("b) ","")
                                .replace("\\x3CI\\x3E","")
                                .replace("\\x3C/I\\x3E","")
                                .replace("\\x3Cbr/\\x3E","")]       
            i += len(extrt)
        
        File.close()
        if data != []:
            print_debug("[Module] Fichier ["+ self.path + "] chargé\n","green")
        else:
            print_debug("[Module] erreur data vide","red")
        return data
    
    def print_class(self):
        print_debug("[Module] path: "+ str(self.path),"white")
        print_debug("[Module] data: "+ str(self.data),"white")
        print_debug("[Module] test_blanc: "+ str(self.test_blanc),"white")