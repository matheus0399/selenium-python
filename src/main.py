from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chromium.options import ChromiumOptions
from cosco import Cosco
from msc import MSC
from maersk import Maersk
import json

# # CRIAÇÃO DO NAVEGADOR
serv =  Service(ChromeDriverManager().install())

chromeOptions = ChromiumOptions()
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument('--disable-blink-features=AutomationControlled')
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])

browser = webdriver.Chrome(options=chromeOptions,service=serv)
cosco = Cosco(browser)
msc = MSC(browser)
maersk = Maersk(browser)
# # LOOP PARA COLETA DAS INFORMAÇÕES
containers = [
    'TRHU2004679','CMAU0514215','TTNU8678224','HAMU1324924','SEGU9972152'
]
found = []
for container in containers:
    found.append(cosco.run(container))
    found.append(msc.run(container))
    found.append(maersk.run(container))
    
# Escreve o resultado em um arquivo json
json_object = json.dumps(found, indent=4, ensure_ascii=False)
 
with open("infos.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)
    
# # comando pra rodar o arquivo -> python main.py