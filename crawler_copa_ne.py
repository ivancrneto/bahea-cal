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
url_copa_nordeste = "{}/copa-do-nordeste/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_copa_nordeste)
bs_obj = bs(ff.page_source, 'html.parser')

seta_fase_esq = ff.find_element_by_class_name('gui-icon-arrow-left-highlight')
seta_fase_dir = ff.find_element_by_class_name('gui-icon-arrow-right-highlight')

for i in range(5):
    seta_fase_esq.click()
    sleep(1)

## Preliminar

bs_obj = bs(ff.page_source, 'html.parser')
fase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
print(fase, "\n")

boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

print_matches(boxes)

## Primeira fase

seta_fase_dir.click()

bs_obj = bs(ff.page_source, 'html.parser')
fase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
print(fase, "\n")

setas_grupo_esq = ff.find_elements_by_class_name('gui-icon-arrow-left-highlight')
setas_grupo_dir = ff.find_elements_by_class_name('gui-icon-arrow-right-highlight')

setas_grupo_esq.pop(0)
setas_grupo_dir.pop(0)

for i in range(6):
    for seta in setas_grupo_esq:
        seta.click()

for i in range(6):
    bs_obj = bs(ff.page_source, 'html.parser')
    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})
    
    print_matches(boxes)

    for seta in setas_grupo_dir:
        seta.click()

## Mata-mata

for i in range(3):
    seta_fase_dir.click()

    bs_obj = bs(ff.page_source, 'html.parser')
    fase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
    print(fase, "\n")
    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

    print_matches(boxes)

