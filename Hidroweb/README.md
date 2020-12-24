# **__Coletando dados de Chuva do Site Hidroweb__** 

1. Objetivo desse projeto foi desenvolver de forma altomatizada a coleta de uma grande quantidade de dados da pagina [__hidroweb__](http://www.snirh.gov.br/hidroweb/serieshistoricas). 
---
2. A primeira parte desse projeto foi feito um script em python [Busca de dados]() aonde ele coletou através da biblioteca Selenium os seguintes dados da página :
    
    - Código da estação
    - Nome da estação
    - Estado
    - Município
    - Responsável
    - Latitude
    - Logitude
 
 Para coletar essas informações foram selecionados as seguintes opções : 
  - Tipo de Estação : Pluviometricas 
  - Estado : Acre 
  - Responsavel : Ana 

3. Apos a coleta desses dados ele salva todas as informaçõe em um dataset criado com a biblioteca pandas e baixa no final do script um arquivo no formato Zip com os dados historicos de chuvas relacionados com o código da estação coletada anteriormente.

---
4. Na segunda parte desse projeto foi feito um segundo script, mas agora para tratar os dados coletados e organiza-los, na pasta [dados coletados]() temos o arquivo Medicoes_convencionais.zip que é o arquivo baixado e um segundo dados_tratados e aqui já temos nossos dados tratados. 

5.  Qualquer dúvida ou sugestão para esse projeto fique a vontade para entrar em contato. 


---
Redes Sociais :

- [Linkedin](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)
- [Blog: Data Marte](https://datamarte.com/)



