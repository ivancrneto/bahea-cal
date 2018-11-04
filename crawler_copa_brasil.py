from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

def print_matches(boxes):
    for box in boxes:
        info = box.find('div', {'class':'placar-jogo-informacoes'}).text

        mandante = box.find('span', {'class':'placar-jogo-equipes-item placar-jogo-equipes-mandante'})
        mandante_sigla = mandante.find('span', {'class':'placar-jogo-equipes-sigla'}).text
        mandante = mandante.find('span', {'class':'placar-jogo-equipes-nome'}).text

        visitante = box.find('span', {'class':'placar-jogo-equipes-item placar-jogo-equipes-visitante'})
        visitante_sigla = visitante.find('span', {'class':'placar-jogo-equipes-sigla'}).text
        visitante = visitante.find('span', {'class':'placar-jogo-equipes-nome'}).text
        
        output = '{} x {}\n{}\n'.format(mandante, visitante, info)
        print(output)

base_url = "https://globoesporte.globo.com/futebol"
url_copa_brasil = "{}/copa-do-brasil/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_copa_brasil)
bs_obj = bs(ff.page_source, 'html.parser')

seta_fase_esq = ff.find_element_by_class_name('gui-icon-arrow-left-highlight')
seta_fase_dir = ff.find_element_by_class_name('gui-icon-arrow-right-highlight')

for i in range(8):
    seta_fase_esq.click()
    sleep(1)

for i in range(8):
    sleep(1)
    bs_obj = bs(ff.page_source, 'html.parser')
    fase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
    print(fase, "\n")

    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

    print_matches(boxes)

    seta_fase_dir.click()
    