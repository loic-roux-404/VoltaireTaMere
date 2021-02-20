import difflib
from File import print_debug

class Question:
    def __init__(self, Phrase, close_matche):
        self.phrase_No_change = Phrase
        self.phrase = Phrase.replace("‑","-").replace("-","- ").replace(",","").replace(".","").replace("'","' ")
        self.matche = close_matche.replace("‑","-").replace("-","- ").replace(",","").replace(".","").replace("'","' ")
        self.corr_in_matche =  close_matche[close_matche.find("<") : close_matche.find(">")].replace("<","").replace(">","")
        self.err_list = []
        self.err_in_phrase = self.find_err()

    def find_err(self):
        if self.matche == "":
            print_debug("[find_err] No Close Match","yellow")
            return ""

        Words_err = ""
        extrt = " "
        i = 0
        while extrt != "":
            extrt = self.matche[self.matche.find("<",i) : self.matche.find(">",i) ].replace("<","").replace(">","") 
            try:
                if self.matche[self.matche.find(">",i)+1] == "-":
                    extrt += "-"
            except:
                None

            i = self.matche.find(">",i)+1

            if extrt != "" and extrt not in Words_err:
                Words_err += extrt+" "

        Words_err = split_Word(Words_err)
        list_String_Err = split_Word(self.phrase)
        list_String_Corr = split_Word(self.matche.replace("<","").replace(">",""))
        print_debug("[find_err] err: "+str(Words_err),"cyan")
        print_debug("[find_err] phrase: "+str(list_String_Err),"cyan")
        print_debug("[find_err] matche: "+str(list_String_Corr),"cyan")

        for i in range(0,len(list_String_Corr)):

            if list_String_Corr[i] in list_String_Err:
                list_String_Err[ list_String_Err.index( list_String_Corr[i] ) ] = ""
                list_String_Corr[i] = ""
        
        list_String_Err = [list_String_Err[i] for i in range(0,len(list_String_Err)) if list_String_Err[i] != ""]
        list_String_Corr = [list_String_Corr[i] for i in range(0,len(list_String_Corr)) if list_String_Corr[i] != ""]

        for i in range(0, len(list_String_Corr)):
            if list_String_Corr[i].replace("…","") not in Words_err:
                print_debug("[find_err] Words_err: "+str(Words_err),"cyan")
                print_debug("[find_err] list_String_Corr: "+str(list_String_Corr),"cyan")
                print_debug("[find_err] list_String_Err: "+str(list_String_Err),"cyan")
                print_debug("[find_err] Close Match INCORRECT\n","yellow")
                return ""

        if list_String_Corr == [] and list_String_Err == []:
            print_debug("[find_err] Close Match INCORRECT\n","yellow")
            return ""

        print_debug("[find_err] Close Match CORRECT","green")

        if list_String_Err == []:
            list_String_Err = Words_err

        if "'" in list_String_Err[0]:
            try:
                list_String_Err[0] = list_String_Err[1]
            except:
                list_String_Err[0] =  list_String_Err[0][ 0 : list_String_Err[0].find("'")]
            

        if "-" in list_String_Err[0]:
            list_String_Err[0] = list_String_Err[0][ 0 : list_String_Err[0].find("-")]
        
        print_debug("[find_err] Words_err: "+str(Words_err),"cyan")
        print_debug("[find_err] list_String_Corr: "+str(list_String_Corr),"cyan")
        print_debug("[find_err] list_String_Err: "+str(list_String_Err),"cyan")
        self.err_list = list_String_Err

        if len(list_String_Err) > 1:
            return list_String_Err[ auto_learning().memory_data(list_String_Err) ]
        else:
            return list_String_Err[0]
    
    def print_class(self):
        print_debug("[Question] phrase:"+self.phrase,"white")
        print_debug("[Question] match:"+self.matche,"white")
        print_debug("[Question] corr_in_matche"+self.corr_in_matche,"white")
        print_debug("[Question] err_in_phrase"+self.err_in_phrase,"white")

def split_Word(String):
    List_From_String = [String[0 : String.find(" ")]]
    i = len(String[0 : String.find(" ")])
    word = " "

    while word != "":
        word = String[String.find(" ",i) : String.find(" ", String.find(" ",i)+1) ].replace(" ","")
        List_From_String += [word]
        i += len(word)+1
        
    List_From_String[len(List_From_String)-2] += String[len(String)-1].replace(" ","").replace("?","").replace("!","").replace("»","").replace("«","")
    return List_From_String[0: len(List_From_String)-1]  
    
def found_matche(Phrase, data):
    matches = difflib.get_close_matches(Phrase, data) + auto_learning().memory_match(Phrase)

    print_debug("[found_matche] close matches: "+str(matches),"white")
    if matches != []:

        for i in range(0, len(matches)):
            if "<" in matches[i]:
                question = Question(Phrase, matches[i])

                if question.err_in_phrase != "":
                    print_debug("[found_matche] CLOSE MATCH FOUND: "+str(matches[i]),"white")
                    print_debug("[found_matche] ERROR: "+str(question.err_in_phrase),"green")
                    return question

    print_debug("[found_matche] NO CLOSE MATCH FOUND","white")
    print_debug("[found_matche] NO ERROR","green")
    return Question(Phrase, "")

def found_good_one(phrase, match, err_in_phrase):
    nmb_presence = phrase.count(err_in_phrase)
    match = split_Word(match)
    if nmb_presence != 1:
        i = 0
        j = 0
        while "<" not in match[i] and i < len(match):
            if match[i].replace("\'"," ").replace("-"," ") == err_in_phrase:
                j += 1
            i += 1
        return j
    else:
        return 0

class auto_learning():
    def add_data(self, list_err, real_err):
        print_debug("[auto_learning] failed to locate error, learning...", "yellow")
        f = open(".\\file\\auto_learning_data.txt", "a", encoding="utf-8")
        f.write(str(list_err) + " " + real_err + "\n")
        f.close()

    def memory_data(self, input_list):
        f = open(".\\file\\auto_learning_data.txt", "r", encoding="utf-8")
        memory_data = f.read()
        memory_data_list = []
        extr = " "
        i = 0
        while extr != "":
            extr = memory_data[ memory_data.find("[", i) : memory_data.find("]", i)+1 ]
            memory_data_list += [extr]
            i = memory_data.find("\n",i+1)
        
        memory_call = difflib.get_close_matches(str(input_list), memory_data_list)
        
        f.close()
        if memory_call != []:
            learning = difflib.get_close_matches( memory_data[ memory_data.find(memory_call[0])+len(memory_call[0])+1 : memory_data.find("\n", memory_data.find(memory_call[0]) )], input_list)
            if learning != []:
                print_debug("[auto_learning] found error in memory","magenta")
                return input_list.index(learning[0])
            else:
                print_debug("[auto_learning] no error found in memory","magenta")
                return 0
        else:
            print_debug("[auto_learning] no error found in memory","magenta")
            return 0
    
    def add_match(self, sentence, real_err):
        print_debug("[auto_learning] failed to found match, learning...", "yellow")
        f = open(".\\file\\auto_learning_match.txt", "a", encoding="utf-8")
        sentence = " "+sentence
        try:
            sentence = sentence[ :sentence.index(" "+real_err)] + " <@" + real_err + ">" + sentence[ sentence.index(" "+real_err)+len(real_err)+1:] + "\n"
        except:
            try:
                sentence = sentence[ :sentence.index("'"+real_err)] + "'<@" + real_err + ">" + sentence[ sentence.index("'"+real_err)+len(real_err)+1:] + "\n"
            except:
                sentence = sentence[ :sentence.index("-"+real_err)] + "-<@" + real_err + ">" + sentence[ sentence.index("-"+real_err)+len(real_err)+1:] + "\n"
        f.write(sentence[1:])
        f.close()
    
    def memory_match(self, sentence):
        f = open(".\\file\\auto_learning_match.txt", "r", encoding="utf-8")
        memory_match = f.read()
        memory_match_list = []
        extr = " "
        i = 0
        while extr != "":
            extr = memory_match[ i : memory_match.find("\n", i) ]
            memory_match_list += [extr]
            i += len(extr)+1
        
        return difflib.get_close_matches(sentence, memory_match_list)