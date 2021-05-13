from bs4 import BeautifulSoup
import requests
import pandas as pd

lista_noticias = []
url = 'https://canaltech.com.br/ultimas/'

site = requests.get(url)
soup = BeautifulSoup(site.content, 'html.parser')

# pegando a noticia
noticias = soup.findAll('article', class_='col-xs-12 col-sm-6 col-md-4')

for noticia in noticias:
    # captando o titilo
    noticia_titulo = noticia.find(
        'h3', class_='title titulo-listagem').get_text()
    # pegando o link
    noticia_link_2 = noticia.find(
        "a", class_='jc list-item type-artigo timeline-fade')
    noticia_link = (
        'https://canaltech.com.br{}').format(noticia_link_2['href'])
    # pegando a categoria
    noticia_categoria = noticia.find('span', class_='catag').get_text()
    # print(noticia_titulo)
    # print(noticia_categoria)
    # print("https://canaltech.com.br" + noticia_link['href'])
    lista_noticias.append([noticia_titulo, noticia_categoria, noticia_link])
noticias_df = pd.DataFrame(lista_noticias, columns=[
                           'Título', 'Categoria', 'Link'])

noticias_df.to_excel('Tabela de ultimas noticias canaltech.xlsx', index=False)
