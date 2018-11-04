from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver

base_url = "https://globoesporte.globo.com/futebol"
url_serie_a = "{}/brasileirao-serie-a/".format(base_url)
url_serie_b = "{}/brasileirao-serie-b/".format(base_url)

ff = webdriver.Firefox()
ff.get(url_serie_a)
bs_obj = bs(ff.page_source, 'html.parser')

setas = ff.find_elements_by_class_name('lista-jogos__navegacao--setas')
seta_esq = setas[0]
seta_dir = setas[1]

for i in range(38):
    seta_esq.click()

for i in range(38):

    bs_obj = bs(ff.page_source, 'html.parser')

    rodada = bs_obj.find('span', {'class':'lista-jogos__navegacao--rodada'})
    print(rodada.text)
    
    boxes = bs_obj.find_all('div', {'class' :'jogo theme'})
    for box in boxes:
        mandante = box.find('div', {'class':'placar__equipes placar__equipes--mandante'})
        mandante_sigla = mandante.find('span', {'class', 'equipes__sigla'}).text
        mandante = mandante.find('span', {'class':'equipes__nome'}).text

        visitante = box.find('div', {'class':'placar__equipes placar__equipes--visitante'})
        visitante_sigla = visitante.find('span', {'class', 'equipes__sigla'}).text
        visitante = visitante.find('span', {'class':'equipes__nome'}).text
        
        info = box.find('div', {'class':'jogo__informacoes'})
        data = info.find('span', {'class':'jogo__informacoes--data'}).text.strip()
        local = info.find('span', {'class':'jogo__informacoes--local'}).text.strip()
        hora = info.find('span', {'class':'jogo__informacoes--hora'}).text.strip()

        print('\n{} x {}\n{} {} {}\n'.format(mandante, visitante, data, hora, local))

    seta_dir.click()
