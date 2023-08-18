from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Cosco:
    def __init__(self, browser:webdriver.Chrome):
        self.browser = browser
        
    def run(self,key:str):
        ret = ['Cosco', key, 'Não Encontrado',[]]
        try:
            self.browser.get('https://elines.coscoshipping.com/ebusiness/cargoTracking?trackingType=CONTAINER&number='+ key)
            all = self.waitForElement(By.CLASS_NAME,'singleCNTRBody')
            if len(all) != 0:
                for element in all:
                    infos = element.find_elements(By.CSS_SELECTOR,'div.ivu-col')
                    line = []
                    for info in infos:
                        current = info.find_elements(By.XPATH, ".//*")
                        line.append({"label":current[0].text.strip(),"value":current[1].text.strip()})
                    ret[3].append(line)
                ret[2] = 'Encontrado'
        except:{}
        return ret
    # espera 5 seg ou tempo passado na varievel 'maxTries' por um elemento na tela
    def waitForElement(self, _type, className, maxTries = 5):
        _try = 0
        all = []
        while (len(all) == 0) :
            if _try > maxTries:
                break
            all = self.browser.find_elements(_type, className)
            _try += 1
            time.sleep(1)
        return all