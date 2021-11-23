from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

amazonDic = {
    "site":"https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
    "login":'#ap_email',  # CSS_SELECTOR
    "password":'#ap_password',  # CSS_SELECTOR
    "btnLoginProceed": '//*[@id="signInSubmit"]',  # XPATH
    "linkConsole": "https://www.amazon.com.br/Microsoft-Console-Xbox-Series-S/dp/B08JN2VMGX/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=xbox+one&qid=1637157767&sr=8-6&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147",
    "addCartBtn": '//*[@id="add-to-cart-button"]',  # XPATH
    "warranty": "#attachSiNoCoverage > span:nth-child(1) > input:nth-child(1)",  # CSS_SELECTOR
    "closeOrder": '//*[@id="hlb-ptc-btn-native"]',  # CSS_SELECTOR
    "toBuy": '//*[@id="submitOrderButtonId"]/span/input'  # XPATH
             }

kabumDic = {
    "site": "https://www.kabum.com.br/login",
    "login": '.jss2 > div:nth-child(2) > input:nth-child(1)',  # CSS_SELECTOR
    "password": '.jss7 > div:nth-child(2) > input:nth-child(1)',  # CSS_SELECTOR
    "btnLoginProceed": '#botaoLogin',  # CSS_SELECTOR
    "linkConsole": "https://www.kabum.com.br/produto/128561/console-microsoft-xbox-series-s-512gb-branco-rrs-00006",
    "addCartBtn": '//*[@id="blocoValores"]/div[2]/button',  # XPATH
    "closeOrder": '//*[@id="__next"]/div[1]/div/div[2]/div[2]/div/div/div[4]/button[1]',
    "frete": '//*[@id="sellersContainer"]/div/div/div[3]/form/div[4]/label/input',  # XPATH
    "btnPayment": '//*[@id="buttonGoToPayment"]',  # XPATH
    "creditCard": '//*[@id="botaoFormaDePagamentoCartaoCredito"]',
 
}

magaludic = {
    "site": "https://sacola.magazineluiza.com.br/#/cliente/login/?next=https%3A//www.magazineluiza.com.br/%3Fpartner_id%3D974%26gclid%3DCjwKCAiAnO2MBhApEiwA8q0HYUujR9kBf7GNMNHu2HvJj8vVLOqA_c-GUV9Dqn_y6K5109pM7QWMDRoChowQAvD_BwE%26gclsrc%3Daw.ds&origin=magazineluiza",
    "login": 'input-login-00f09e78',  # ID
    "password": '#input-password-ed29d128',  # CSS_SELECTOR
    "btnLoginProceed": 'button.LoginBox-form-continue:nth-child(3)',  # CSS_SELECTOR
    "linkConsole": "https://www.magazineluiza.com.br/console-xbox-series-s-512gb-ssd-midia-digital/p/hkb206dfdd/ga/xbss/",
    "addCartBtn": '//*[@id="blocoValores"]/div[2]/button',  # XPATH
    "closeOrder": '//*[@id="__next"]/div[1]/div/div[2]/div[2]/div/div/div[4]/button[1]',
    "frete": '//*[@id="sellersContainer"]/div/div/div[3]/form/div[4]/label/input',  # XPATH
    "btnPayment": '//*[@id="buttonGoToPayment"]',  # XPATH
    "creditCard": '//*[@id="botaoFormaDePagamentoCartaoCredito"]',
}
chooseSite = input('choose the website you want to buy(Amazon, Kabum, Magalu): ').upper()
if chooseSite == 'AMAZON':
    path_dic = amazonDic  # Váriavel vai receber o valor do diconário da loja que o usuário decidir fazer a compra.

elif chooseSite == 'KABUM':
    path_dic = kabumDic
    nameCard = input('Type the name printed on the card: ')
    #numberCard = int(input('Enter the card number: '))
    #expirationDate = int(input('Type in the expiration date: '))

elif chooseSite == 'MAGALU':
    path_dic = magaludic

duration = 20
site = webdriver.Chrome()  # Abrindo o browser.
site.get(path_dic["site"])  # Acessando o site da loja escolhida para realizar a compra,
site.maximize_window()

# Função para efetuar o login do usuário no site escolhido da compra. 

def logar(email, password, siteChoose):
    if siteChoose == 'AMAZON':
        login = site.find_element(By.CSS_SELECTOR, path_dic["login"]).click()
        login = WebDriverWait(site, duration).until(EC.presence_of_element_located((By.CSS_SELECTOR, path_dic["login"]))).send_keys(email)

        proceedBtnLogin = WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()

        passwordSite = WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path_dic["password"]))).click()
        passwordSite = WebDriverWait(site, duration).until(EC.presence_of_element_located((By.CSS_SELECTOR, path_dic["password"]))).send_keys(password)
  
        proceedBtnPassword = site.find_element(By.XPATH, path_dic["btnLoginProceed"]).click()
    
    elif siteChoose == 'KABUM':
        login = site.find_element(By.CSS_SELECTOR, path_dic["login"]).click()
        login = WebDriverWait(site, duration).until(EC.presence_of_element_located((By.CSS_SELECTOR, path_dic["login"]))).send_keys(email)

        passwordSite = WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path_dic["password"]))).click()
        passwordSite = WebDriverWait(site, duration).until(EC.presence_of_element_located((By.CSS_SELECTOR, path_dic["password"]))).send_keys(password)

        proceedBtnPassword = site.find_element(By.CSS_SELECTOR, path_dic["btnLoginProceed"]).click()
    
    elif siteChoose == 'MAGALU':
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.ID, path_dic["login"]))).click()
       # WebDriverWait(site, duration).until(EC.presence_of_element_located((By.ID, path_dic["login"]))).send_keys(email)
    

# Função para abrir uma nova aba com o produto escolhido.
def newTab():
    site.execute_script("window.open('');")
    site.switch_to.window(site.window_handles[1])
    site.get(path_dic["linkConsole"])

# Função para finalizar a compra do produto.
def addCart(siteChoose):
    if siteChoose == 'AMAZON':
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["addCartBtn"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path_dic["warranty"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["closeOrder"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["toBuy"]))).click()
    
    if siteChoose == 'KABUM':
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["addCartBtn"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["closeOrder"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["frete"]))).click()
        WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["btnPayment"]))).click()

def creditCard(cardName):
    selectCreditCardOption = WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["creditCard"]))).click()
    WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.ID, 'nomeImpressoCartaoCredito'))).click()
    #WebDriverWait(site, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'nomeImpressoCartaoCredito')))
    #WebDriverWait(site, 20).until(EC.element_to_be_clickable((By.ID, 'nomeImpressoCartaoCredito'))).send_keys(cardName)
    #nameCardPrintedSelect = WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.ID, 'nomeImpressoCartaoCredito'))).click()
    #WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.ID, 'nomeImpressoCartaoCredito'))).send_keys(cardName)

logar('renatopessoa__@hotmail.com','nrb20252', chooseSite)
newTab()
addCart(chooseSite)

if chooseSite == 'KABUM':
    creditCard(nameCard)