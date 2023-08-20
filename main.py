import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.vagas.com.br/vagas-de-python'

response = requests.get(url) 


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.title.text
    print(title)
        
    list_name = []
    list_empresas = []
    list_nivel = []
    list_local = []
    list_data = []
    list_desc = []

    name_divs = soup.find_all('a', class_='link-detalhes-vaga')
    for name in name_divs:
        description_name = name.get_text()
        list_name.append(description_name[13:])
        
    empresa_divs = soup.find_all('span', class_='emprVaga')
    for empresa in empresa_divs:
        description_emprsa = empresa.get_text()
        list_empresas.append(description_emprsa[11:])

    nivel_divs = soup.find_all('span', class_='emprVaga')
    for nivel in nivel_divs:
        description_nivel = nivel.get_text()
        list_nivel.append(description_nivel[11:])
        
    local_divs = soup.find_all('span', class_='vaga-local')
    for local in local_divs:
        description_local = local.get_text()
        list_local.append(description_local[13:])

    data_divs = soup.find_all('span', class_='data-publicacao')
    for div in data_divs:
        description_data = div.get_text()
        list_data.append(description_data)
        
    desc_divs = soup.find_all('div', class_='detalhes')
    for desc in desc_divs:
        description_desc = desc.get_text()
        list_desc.append(description_desc)

    
    
dataframe = {
  'Cargo': list_name,
  'Empresa': list_empresas,
  'Nível': list_nivel,
  'Local': list_local,
  'Descrição': list_desc
}

df = pd.DataFrame(dataframe)
    
df.to_excel('output.xlsx', index=True)
    