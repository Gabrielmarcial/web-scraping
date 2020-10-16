from selenium.webdriver import Chrome
import time
# Abrindo o navegador
url = 'http://www.snirh.gov.br/hidroweb/serieshistoricas'
regiao = str(input('qual a região:'))
browser = Chrome()
browser.get(url)


# Selecionando as opções
a = browser.find_elements_by_class_name("mat-form-field-infix")
a[0].click()

#Pluviometricas para tipo de estação
b = browser.find_element_by_xpath("//mat-option[@value='P']//span")
b.click()

#Escolhendo a Região RIO DE JANEIRO

#a[6].click()
#time.sleep(11)
#rg = browser.find_element_by_xpath("//mat-option[@id='mat-option-34']//span")
# como tem um elemento logo abaixo do span ele não realiza o click com o comando 'rg.click()'
# para resolver o problema foi usado o comando abaixo
#browser.execute_script('arguments[0].click()', rg)

# Escolhendo uma Região em especifico
a[6].click()
time.sleep(5)

#regiao = str(input('qual a região:'))

rgs = browser.find_elements_by_tag_name('mat-option')

for c in range(0,len(rgs)):
    if regiao == rgs[c].text:
        #rgs[c].click()
        browser.execute_script('arguments[0].click()', rgs[c])
        break

time.sleep(4)
# Consultando os dados
bot = browser.find_element_by_xpath("//button[@class='mat-flat-button mat-primary']//span")
bot.click()


#criando o dataframe
import pandas as pd
dados = pd.DataFrame(columns= ['Código','Nome_da_Estação', 'Estado',' Município',
                               'Responsável_pela_Estação'  ,' Latitude_da_Estação ', ' Longitude_da_Estação'])


# selecionando 100 opções
seli1=browser.find_element_by_class_name('mat-paginator-page-size-select')
seli1.click()
time.sleep(2)
seli = browser.find_elements_by_tag_name('mat-option')
seli[3].click()


# Selecionado o número de paginas
pagnum1 = browser.find_element_by_class_name('mat-paginator-range-label')
pagnum2 = str(pagnum1.text)
pagnum2.split('/')
pagnum3 = int(pagnum2.split('/')[1])
numero_paginas = int(pagnum3/100)



#coletando os dados pagina por pagina

for pag in range(0,numero_paginas+1):

    # clicando nos links dos com os dados
    time.sleep(3)
    link = browser.find_element_by_tag_name('tbody')
    links = link.find_elements_by_tag_name('tr')

    for j in range(0, len(links)):
        lin = links[j].find_elements_by_tag_name('td')
        li = lin[1].find_element_by_tag_name('a')
        li.click()

        # coletando os dados
        test = []
        d = browser.find_element_by_tag_name('app-dados-estacao-convencional-dialogo')
        da = d.find_elements_by_tag_name('div')
        test.append(da[4].text)  # codigo da estação
        test.append(da[7].text)  # nome da estação
        test.append(da[22].text)  # estado
        test.append(da[25].text)  # municipio
        test.append(da[28].text)  # responsável
        test.append(da[34].text)  # latitude
        test.append(da[37].text)  # logitude

        # colocando os dados no df
        dados.loc[len(dados)] = test

        # fechar
        fechar1 = d.find_element_by_tag_name('mat-card-actions')
        fechar2 = fechar1.find_element_by_tag_name('div')
        fechar3 = fechar2.find_element_by_tag_name('button')
        fechar3.click()

    # mudar de páginas
    time.sleep(3)
    trocar_pagina1 = browser.find_element_by_tag_name("mat-paginator")
    trocar_pagina2 = trocar_pagina1.find_elements_by_tag_name('button')
    trocar_pagina2[1].click()



dados.to_csv('Dados_hidroweb.csv')
print(dados)

# fechando
time.sleep(3)
browser.quit()
