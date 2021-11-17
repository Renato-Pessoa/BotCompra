from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


amazonDic = {
    "site":"https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&",
    "login":'email',
    "password":'//*[@id="ap_password"]',
    "linkPs5": "https://www.amazon.com.br/Microsoft-Console-Xbox-Series-S/dp/B08JN2VMGX/ref=sr_1_6?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=xbox+one&qid=1637157767&sr=8-6&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147",
    "addCartBtn": "add-to-cart-button",
    "warranty": "#attachSiNoCoverage > span:nth-child(1) > input:nth-child(1)",
    "closeOrder": '//*[@id="hlb-ptc-btn-native"]',
    "toBuy": '//*[@id="submitOrderButtonId"]/span/input'
             }
duration = 20

path_dic = amazonDic  # Váriavel vai receber o valor do diconário da loja que o usuário decidir fazer a compra.
site = webdriver.Chrome()  # Abrindo o browser.
site.get(path_dic["site"])  # Acessando o site da loja escolhida para realizar a compra,
site.maximize_window()

# Função para efetuar o login do usuário no site escolhido da compra. 
def logar(email, password):
    login = site.find_element(By.NAME, path_dic["login"]).send_keys(email) 

    proceedBtnLogin = site.find_element_by_xpath('//*[@id="continue"]').click()

    passwordSite = site.find_element(By.XPATH, path_dic["password"]).send_keys(password)
  
    proceedBtnPassword = site.find_element_by_xpath('//*[@id="signInSubmit"]').click()

# Função para abrir uma nova aba com o produto escolhido.
def newTab():
    site.execute_script("window.open('');")
    site.switch_to.window(site.window_handles[1])
    site.get(path_dic["linkPs5"])

# Função para finalizar a compra do produto.
def addCart():
    site.find_element(By.ID, path_dic["addCartBtn"]).click()
    WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path_dic["warranty"]))).click()
    WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["closeOrder"]))).click()
    WebDriverWait(site, duration).until(EC.element_to_be_clickable((By.XPATH, path_dic["toBuy"]))).click()

logar('bot.ps5.unit@gmail.com','testebot123456')
newTab()
addCart()