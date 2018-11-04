from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver

url = "https://globoesporte.globo.com/futebol/brasileirao-serie-a/"

ff = webdriver.Firefox()
ff.get(url)
bs_obj = bs(ff.page_source, 'html.parser')

boxes = bs_obj.find_all('div', {'class' :'jogo theme'})

for box in boxes:
    mandante = box.find('div', {'class':'placar__equipes placar__equipes--mandante'})
    mandante = mandante.find('span', {'class':'equipes__nome'}).text
    
    visitante = box.find('div', {'class':'placar__equipes placar__equipes--visitante'})
    visitante = visitante.find('span', {'class':'equipes__nome'}).text
    
    info = box.find('div', {'class':'jogo__informacoes'})
    data = info.find('span', {'class':'jogo__informacoes--data'}).text.strip()
    local = info.find('span', {'class':'jogo__informacoes--local'}).text.strip()
    hora = info.find('span', {'class':'jogo__informacoes--hora'}).text.strip()

    print('\n{} x {}\n{} {} {}\n'.format(mandante, visitante, data, hora, local))

