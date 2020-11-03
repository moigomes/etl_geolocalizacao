##### 20 Jun 2019 - Moisés Gomes – moigomes@gmail.com

# Script desenvolvido em Python 3.6 destinado a execução de uma rotina ETL
##### A sigla ETL vem do inglês Extract-Transform-Load e visa trabalhar com toda a parte de extração de dados de fontes externas, transformação para atender às necessidades de negócios e carga dos dados dentro do Data Warehouse.
### Extract: É a coleta de dados dos sistemas de origem
- A fonte de dados do processo em questão, são arquivos de texto com coordenadas geográficas no
formato exibido abaixo:
```sh
Latitude: 30°02′59″S   -30.04982864
Longitude: 51°12′05″W   -51.20150245
Distance: 2.2959 km  Bearing: 137.352°

```
- A tarefa de extrair as coordenadas do arquivo de texto é feita pela classe Extract:
- O método ‘get_lista_de_coordenadas()’ retorna uma lista com listas de pares de coordenadas.
[[latitude, longitude] ... ]

### Transform: Limpeza, Ajustes e Consolidação dos dados
- A classe Transform é a responsável por ajustar e enriquecer os dados
- O método ‘get_endereco()’ recebe as coordenadas (Latitude e Longitude) e com o auxílio da lib
‘geocoder’ que ultiliza a API do Google de Geocode Reverso, retorna um dicionário com os dados do
endereço do local.

### Load: Consiste em fisicamente estruturar e carregar os dados para dentro da camada de apresentação seguindo o modelo dimensional.
- A classe Load faz esse trabalho.
- O método ‘salvar’ recebe um dicionário com os dados de endereço e persiste as informações na
base de dados Sqlite3.

### Script main.py
- Este script consome as classes mencionadas anteriormente e procura por arquivos de textos
dentro do diretório ‘resources/’. Ao encontrar, realiza o processo ETL e por fim, move o arquivo lido
para a pasta ‘resources/arquivos_extraidos’.
- Após isso, o programa continua procurando por arquivos na pasta e repetindo o processo até
que seja encerrado manualmente (Crtl+c)

### Configurando
- É preciso ter o Python 3.6 e PIP3 instalado.
Caso não possua:
- Para Linux(Ubuntu)
```sh
$ sudo apt install python3
$ sudo apt install python3-pip
```
- Para Windows
Baixar o instalador do Python em https://www.python.org/.
O PIP3 é instalado automaticamente com o Python, ver: https://vgkits.org/blog/pip3-windows-howto/
- A única dependencia que iremos precisar instalar será o geocoder:
```sh
pip3 install geocoder
```
- Além disso, é necessário uma KEY Google para ultilizar as API’s. A mesma poderá ser gerada
gratuitamente em https://console.cloud.google.com/?hl=pt-BR.

- Clonar os sctipts de: https://gitlab.com/moigomes/etl.git
```sh
git clone https://gitlab.com/moigomes/etl.git
```
- O banco de dados não precisa ser configurado pois utilizei o sqlite3. O Python já cria o arquivo .db
e a tabela para a inserção dos resultados é criada automaticamente.

### Executando:
- Acessar a pasta/repositório (etl) clonado anteriormente e rodar o ‘script main.py’
```sh
python main.py
```
