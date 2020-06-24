from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import random


class ProjetoWeb:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.automatic_downloads": 1,
            "profile.default_content_settings.popups": 0,
        })
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )
        self.linkSite = 'https://cursoautomacao.netlify.app'

    def Iniciar(self):
        self.acessarSite()
        self.selecionarRadioButton()
        self.digitarDinamicamente()
        self.liberarAcesso()
        self.finalizarPrograma()

    def acessarSite(self):
        self.driver.get(self.linkSite)

    def selecionarRadioButton(self):
        try:
            opcao = input(
                'Qual opção deseja selecionar? (windows 10/Mac/Linux)')
            opcao_radio_button = self.wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, f'//input[@value="{opcao}"]')))
            opcao_radio_button.click()
        except Exception:
            print('Favor informar uma opção válida. (windows 10/Mac/Linux)')
            self.selecionarRadioButton()

    def digitarDinamicamente(self):
        try:
            texto = input('Gentileza digitar o seu comentário: ')
            campo_texto = self.wait.until(expected_conditions.element_to_be_clickable(
                (By.XPATH, '//textarea[@placeholder="digite seu texto aqui"]')))
            self.digitarComoPessoa(texto, campo_texto)
        except Exception:
            print('Desculpe, não foi possível digitar o seu texto.')

    def liberarAcesso(self):
        try:
            liberar_acesso = input(
                'Quais acessos devem ser liberados? * Para mais de um acesso, gentileza digitar os números separados por vírgula. ')
            niveis = liberar_acesso.split(',')
            for nivel in niveis:
                opcao_liberar_acesso = self.wait.until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, f'//input[@id="acessoNivel{nivel}Checkbox"]')))
                opcao_liberar_acesso.click()
                sleep(2)
        except Exception:
            print('Gentileza digitar apenas números separados por vírgula.')
            self.liberarAcesso()

    def finalizarPrograma(self):
        finalizar_programa = input(
            'Gostaria de executar o programa novamente? (s/n)')
        if finalizar_programa == 's':
            curso.Iniciar()
        elif finalizar_programa == 'n':
            print('Finalizando o programa...')
            sleep(3)
            print('Programa Finalizado!')
        else:
            print('Gentileza digitar "s" ou "n"')
            self.finalizarPrograma()

    def digitarComoPessoa(self, texto, elemento):
        for letter in texto:
            elemento.send_keys(letter)
            sleep(random.randint(1, 5) / 30)


curso = ProjetoWeb()
curso.Iniciar()
