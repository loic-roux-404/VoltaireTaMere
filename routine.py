from Question import Question, found_matche, found_good_one
from File import print_debug
from selenium.webdriver.common.by import By

def test_Feature(Feature, driver): #test la presence d'une feature
    try:
        driver.find_element_by_class_name(Feature)
        return True
    except:
        return False

def BOT(driver, data, test_blanc):
        print_debug("[BOT] ####### WORKING #######","white")

        if not(test_blanc):
            audio = test_Feature("sentenceAudioReader", driver)
            if test_Feature("popupContent", driver):
                try:
                    driver.find_element_by_id("btn_fermer").click()
                except:
                    print_debug("[BOT] FAILED TO EXECUTE FEATURE IN","red")
                    return "feature_in"
        else:
            audio = False
        
        try:
            Phrase = driver.find_element_by_class_name("sentence").text
        except:
            return "no_sentence"
        
        print_debug("[BOT] PHRASE: "+str(Phrase),"white")
        question = found_matche(Phrase, data)

        if question.matche != "":
            if audio:
                driver.find_element_by_xpath("//input[@class='gwt-TextBox writingExerciseSpan']").send_keys(question.corr_in_matche.replace("@",""))
                driver.find_element_by_id("btn_pas_de_faute").click()
                print_debug("[BOT] EXECUTION AUDIO DONE","green")
            else:
                try:
                    driver.find_elements_by_xpath("//span[@class = 'pointAndClickSpan'][.='"+ question.err_in_phrase +"']")[ found_good_one(question.phrase, question.matche, question.err_in_phrase) ].click()
                    print_debug("[BOT] EXECUTION CLICK DONE","green")
                except:
                    if "…" in question.err_in_phrase:
                        driver.find_elements_by_xpath("//span[@class = 'pointAndClickSpan'][.='"+ question.err_in_phrase.replace("…","") +"']")[ found_good_one(question.phrase, question.matche, question.err_in_phrase.replace("…","")) ].click()
                    else:
                        print_debug("[BOT] FAILED TO EXECUTE CAN'T TOUCH: "+str(question.err_in_phrase),"red")
                        return "can't_touche &"+str(question.err_in_phrase)
        else:
            if audio:
                print_debug("[BOT] FAILED TO EXECUTE NO MATCH FOUND\n","yellow")
                return "not_found"
            else:
                try:
                    driver.find_element_by_class_name("noMistakeButton").click()
                    print_debug("[BOT] EXECUTION NO MISTAKE DONE","green")
                except:
                    return []
        
        print(question.err_list)
        return question.err_list

def MANUAL(driver, data, test_blanc):
    if not(test_blanc):
        audio = test_Feature("sentenceAudioReader", driver)
        if test_Feature("popupContent", driver):
            try:
                driver.find_element_by_id("btn_fermer").click()
            except:
                print_debug("[BOT] FAILED TO EXECUTE FEATURE IN","red")
                return "feature_in"
    else:
        audio = False
    
    try:
        Phrase = driver.find_element_by_class_name("sentence").text
    except:
        return "no_sentence"
    
    print_debug("[BOT] PHRASE: "+str(Phrase),"white")
    question = found_matche(Phrase, data)

    if question.matche != "":
        if audio:
            return question.corr_in_matche
        else:
            return question.err_in_phrase
    else:
        if audio:
            return "not_found"
        else:
            return "no_error"
    
    print(question.err_list)
    return question.err_list
