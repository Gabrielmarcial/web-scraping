import zipfile
import calendar
import pandas as pd
import shutil



#abrindo e extraido o arquivo
measurements = zipfile.ZipFile('C:\\Users\\jorgi\\Desktop\\Foursafe\\hidraweb\\dados\\Medicoes_convencionais.zip','r')
measurements.extractall()

# Criando o DataFrame
df = pd.DataFrame(columns=['Code', 'datetime', 'rain'])

for c in range(0,len(measurements.namelist())):

    # Abrindo o arquivo zip

    element = measurements.namelist()[c]  # elemento da posição 'c' na lista
    element_zip = zipfile.ZipFile(element, 'r')  # abrindo o arquivo no formato zip
    element_name = element_zip.namelist()  # Coletando o nome do arquivo em csv
    element_open = element_zip.open(element_name[0], 'r')  # abrindo o arquivo csv
    element_csv = pd.read_csv(element_open, sep=';', skiprows=range(0, 12),
                              index_col=False)  # abrindo o arquivo com um dataframe

    # Tratando os dados

    for c in range(0, len(element_csv)):
        date = element_csv['Data'][c]
        date.split('/')
        month = int(date[3:5])
        year = int(date[6:10])
        days = calendar.monthrange(year, month)

        for i in range(0, (days[1])):
            try:
                code_df = element_csv['EstacaoCodigo'][0]
                date_df = f'{i + 1}/{month}/{year}'
                i = i + 13
                rain_csv = float((element_csv.iloc[c, i]).replace(',', '.'))
                line = [code_df, date_df, rain_csv]
                df.loc[len(df)] = line
            except Exception as e:
                print("ERROR-%s" % e)




#Salvando os dados e transformando em dic 
df.to_csv('rain_all.csv')
df.to_dict('records')
shutil.move('rain_all.csv','dados')

# Transformanando dados_hidroweb em dic
df1 = pd.read_csv('C:\\Users\\jorgi\\Desktop\\Foursafe\\hidraweb\\dados\\Dados_hidroweb.csv')
df1.drop('Unnamed: 0',axis=1,inplace = True)
df1.to_dict('records')

#Visualizando o resultado 
print(df.to_dict('records'))
print(df1.to_dict('records'))


