from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MSC:
    def __init__(self, browser:webdriver.Chrome):
        self.browser = browser
        
    def run(self,key:str):
        ret = ['MSC', key, 'Não Encontrado',[]]
        try:
            self.browser.get('https://www.msc.com/en/track-a-shipment')
            input = self.waitForElement(By.CSS_SELECTOR,'[id="trackingNumber"]')[0]
            # escreve a chave no input em tela
            for char in key:
                input.send_keys(char)
                time.sleep(0.02)
            input.submit()
            all = self.waitForElement(By.CLASS_NAME,'msc-flow-tracking__port', 10)
            headers = []
            if len(all) > 0:
                all_headers = self.waitForElement(By.CSS_SELECTOR,'.msc-flow-tracking__tracking .data-heading')
                for hd in all_headers:
                    headers.append(hd.text.strip())
                for element in all:
                    infos = element.find_elements(By.CSS_SELECTOR,'.msc-flow-tracking__cell:not(.msc-flow-tracking__cell--one)')
                    line = []
                    for i in range(len(infos)):
                        line.append({"label":headers[i], "value": infos[i].text.strip()})
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