from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

def print_matches(boxes):
    for box in boxes:
        info = box.find('div', {'class':'placar-jogo-informacoes'}).text

        home_team = box.find('span', {'class':'placar-jogo-equipes-item placar-jogo-equipes-mandante'})
        home_team_sigla = home_team.find('span', {'class':'placar-jogo-equipes-sigla'}).text
        home_team = home_team.find('span', {'class':'placar-jogo-equipes-nome'}).text

        guest_team = box.find('span', {'class':'placar-jogo-equipes-item placar-jogo-equipes-visitante'})
        guest_team_sigla = guest_team.find('span', {'class':'placar-jogo-equipes-sigla'}).text
        guest_team = guest_team.find('span', {'class':'placar-jogo-equipes-nome'}).text
        
        output = '{} x {}\n{}\n'.format(home_team, guest_team, info)
        print(output)
        
base_url = "https://globoesporte.globo.com/futebol"
url_copa_nordeste = "{}/copa-do-nordeste/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_copa_nordeste)
bs_obj = bs(ff.page_source, 'html.parser')

left_arrow = ff.find_element_by_class_name('gui-icon-arrow-left-highlight')
right_arrow = ff.find_element_by_class_name('gui-icon-arrow-right-highlight')

for i in range(5):
    left_arrow.click()
    sleep(1)

## Preliminar

bs_obj = bs(ff.page_source, 'html.parser')
phase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
print(phase, "\n")

boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

print_matches(boxes)

## Primeira fase

right_arrow.click()

bs_obj = bs(ff.page_source, 'html.parser')
phase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
print(phase, "\n")

left_arrows_group = ff.find_elements_by_class_name('gui-icon-arrow-left-highlight')
right_arrows_group = ff.find_elements_by_class_name('gui-icon-arrow-right-highlight')

left_arrows_group.pop(0)
right_arrows_group.pop(0)

for i in range(6):
    for arrow in left_arrows_group:
        arrow.click()

for i in range(6):
    bs_obj = bs(ff.page_source, 'html.parser')
    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})
    
    print_matches(boxes)

    for arrow in right_arrows_group:
        arrow.click()

## Mata-mata

for i in range(3):
    right_arrow.click()

    bs_obj = bs(ff.page_source, 'html.parser')
    phase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
    print(phase, "\n")
    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

    print_matches(boxes)

