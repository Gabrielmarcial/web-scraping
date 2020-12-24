from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import shutil
import os

# Abrindo o navegador
url = 'http://www.snirh.gov.br/hidroweb/serieshistoricas'

region = 'ACRE'

source = 'ANA'

chrome_options = Options()
chrome_options.add_argument('--headless')
prefs = {"profile.default_content_settings.popups": 0,
         "download.default_directory": 'C:\\Users\\jorgi\\Desktop\\Foursafe\\hidraweb\\dados',
         "directory_upgrade": True}
chrome_options.add_experimental_option("prefs", prefs)
browser = Chrome(chrome_options=chrome_options)

browser.get(url)

# Selecionando as opções
option_selecting = browser.find_elements_by_class_name("mat-form-field-infix")
option_selecting[0].click()

# Pluviometricas para tipo de estação
pluviometrica = browser.find_element_by_xpath("//mat-option[@value='P']//span")
pluviometrica.click()

# Escolhendo uma Região em especifico
option_selecting[6].click()
time.sleep(3)

regions = browser.find_elements_by_tag_name('mat-option')

for c in range(0, len(regions)):
    if region == regions[c].text:
        print(regions[c].text)
        # rgs[c].click()
        browser.execute_script('arguments[0].click()', regions[c])
        break

time.sleep(3)

# Consultando os dados
consulting_data = browser.find_element_by_xpath("//button[@class='mat-flat-button mat-primary']//span")
consulting_data.click()

# criando o dataframe
dataset = pd.DataFrame(columns=['Código', 'Nome_da_Estação', 'Estado', ' Município',
                                'Responsável_pela_Estação', ' Latitude_da_Estação ', ' Longitude_da_Estação'])

# selecionando 100 opções
selecting = browser.find_element_by_class_name('mat-paginator-page-size-select')
selecting.click()
time.sleep(2)
seleting_100 = browser.find_elements_by_tag_name('mat-option')
seleting_100[3].click()

# Selecionado o número de paginas
pagnum_mat = browser.find_element_by_class_name('mat-paginator-range-label')
pagnum_text = str(pagnum_mat.text)
pagnum_text.split('/')
pag_num = int(pagnum_text.split('/')[1])
num_pages = int(pag_num / 100)

# coletando os dados pagina por pagina
for page in range(0, num_pages + 1):

    # clicando nos links com os dados
    time.sleep(3)
    link_tbody = browser.find_element_by_tag_name('tbody')
    links_tr = link_tbody.find_elements_by_tag_name('tr')

    for j in range(0, len(links_tr)):
        try:
            link_td = links_tr[j].find_elements_by_tag_name('td')
            link = link_td[1].find_element_by_tag_name('a')
            link.click()

            # coletando os dados
            d = browser.find_element_by_tag_name('app-dados-estacao-convencional-dialogo')
            da = d.find_elements_by_tag_name('div')

            # Para coletar o responsavel especifico
            if da[28].text == source:
                data = []
                data.append(da[4].text)  # codigo da estação
                data.append(da[7].text)  # nome da estação
                data.append(da[22].text)  # estado
                data.append(da[25].text)  # municipio
                data.append(da[28].text)  # responsável
                data.append(da[34].text)  # latitude
                data.append(da[37].text)  # logitude

                # colocando os dados no df
                dataset.loc[len(dataset)] = data

            # fechar
            close_mat = d.find_element_by_tag_name('mat-card-actions')
            close_div = close_mat.find_element_by_tag_name('div')
            close = close_div.find_element_by_tag_name('button')
            close.click()
        except Exception as e:
            print("ERROR-%s" % e)

    # mudar de páginas
    time.sleep(3)
    nextpage_mat = browser.find_element_by_tag_name("mat-paginator")
    next_page = nextpage_mat.find_elements_by_tag_name('button')
    next_page[1].click()

dataset.to_csv('Dados_hidroweb.csv')

# movendo para a pasta correta
shutil.move('Dados_hidroweb.csv', 'dados')
print(dataset)# Visualizando o dataset

# colocando os codigos no link para download dos dados historicos de chuvas 
download = 'http://www.snirh.gov.br/hidroweb/rest/api/documento/convencionais?tipo=3&documentos='
for i in range(0, len(dataset['Código'])):
    if i == 0:
        download = download + str(dataset['Código'][i])
    else:
        download = download + ',' + str(dataset['Código'][i])
print(download)
# baixando o arquivo
time.sleep(4)
browser.get(download)

# aguardando o arquivo baixar
folder_archive = False

while folder_archive == False:
    folder_archive = os.path.exists(
        'C:\\Users\\jorgi\\Desktop\\Foursafe\\history_load\\download\\Medicoes_convencionais.zip')

