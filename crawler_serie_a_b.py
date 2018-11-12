from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver

base_url = "https://globoesporte.globo.com/futebol"
url_serie_a = "{}/brasileirao-serie-a/".format(base_url)
url_serie_b = "{}/brasileirao-serie-b/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_serie_a)
bs_obj = bs(ff.page_source, 'html.parser')

arrows = ff.find_elements_by_class_name('lista-jogos__navegacao--setas')
left_arrow = arrows[0]
right_arrow = arrows[1]

for i in range(38):
    left_arrow.click()

for i in range(38):

    bs_obj = bs(ff.page_source, 'html.parser')

    round = bs_obj.find('span', {'class':'lista-jogos__navegacao--rodada'})
    print(round.text)
    
    boxes = bs_obj.find_all('div', {'class' :'jogo theme'})
    for box in boxes:
        home_team = box.find('div', {'class':'placar__equipes placar__equipes--mandante'})
        home_team_sigla = home_team.find('span', {'class', 'equipes__sigla'}).text
        home_team = home_team.find('span', {'class':'equipes__nome'}).text

        guest_team = box.find('div', {'class':'placar__equipes placar__equipes--visitante'})
        guest_team_sigla = guest_team.find('span', {'class', 'equipes__sigla'}).text
        guest_team = guest_team.find('span', {'class':'equipes__nome'}).text
        
        info = box.find('div', {'class':'jogo__informacoes'})
        date = info.find('span', {'class':'jogo__informacoes--data'}).text.strip()
        local = info.find('span', {'class':'jogo__informacoes--local'}).text.strip()
        time = info.find('span', {'class':'jogo__informacoes--hora'}).text.strip()

        print('\n{} x {}\n{} {} {}\n'.format(home_team, guest_team, date, time, local))

    right_arrow.click()
