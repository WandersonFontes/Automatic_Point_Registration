from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from random import randrange
import subprocess as s
import time


class Ponto:
    def __init__(self):
        tempo = randrange(3, 5)
        s.call(['notify-send','Ei!','Seu registro será realizado em  '+str(tempo)+' minutos!'])
        time.sleep(tempo*60)
        self.driver = Chrome()

    def acessar(self, url):
        # print('Acessar Rélogio de Ponto...')
        driver = self.driver
        driver.maximize_window()
        driver.get(url)  # Abertura da página
        time.sleep(4)  # tempo para página ser carregada no navegador
        # print('Acessado com sucesso!')
        #driver.quit();
    def login(self):
        # print('Realizando login...')
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_name('usuario').send_keys()#Usuário
        time.sleep(1)
        driver.find_element_by_name('senha').click()
        time.sleep(1)
        driver.find_element_by_name('senha').send_keys()#Senha
        time.sleep(1)
        driver.find_element_by_id('login').click()
        time.sleep(2)
        # print('Login feito com sucesso!')
    def regristrar(self):
        # print('Registrando ponto eletrônico...')
        driver = self.driver
        driver.find_element_by_class_name('icon-clock').click()
        time.sleep(2)
        driver.find_element_by_id('registrar').click()
        # print('Regsitro realizado com sucesso!')
        time.sleep(3)
        driver.close()
        s.call(['notify-send','Pronto','Regsitro realizado com sucesso!'])


test = Ponto()
test.acessar('https://www.secullum.com.br/Ponto4Web/1335679674')
test.login()
test.regristrar()
