from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Maersk:
    def __init__(self, browser:webdriver.Chrome):
        self.browser = browser
    # não foi possivel programar o processo pq nenhum dos exemplos constam no site
    def run(self,key:str):
        ret = ret = ['Maersk', key, 'Não Encontrado',[]]
        try:
            self.browser.get('https://www.maersk.com/tracking/' + key)
        except:{}
        return ret