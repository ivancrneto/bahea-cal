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
url_copa_brasil = "{}/copa-do-brasil/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_copa_brasil)
bs_obj = bs(ff.page_source, 'html.parser')

left_arrow = ff.find_element_by_class_name('gui-icon-arrow-left-highlight')
right_arrow = ff.find_element_by_class_name('gui-icon-arrow-right-highlight')

for i in range(8):
    left_arrow.click()
    sleep(1)

for i in range(8):
    sleep(1)
    bs_obj = bs(ff.page_source, 'html.parser')
    phase = bs_obj.find('span', {'class':'tabela-navegacao-seletor-ativo'}).text
    print(phase, "\n")

    boxes = bs_obj.find_all('div', {'class':'placar-jogo'})

    print_matches(boxes)

    right_arrow.click()
    