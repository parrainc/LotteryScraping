# LotteryScraping

LotteryScraping es una aplicacion realizada en python 3 que lee los 
resultados de la lotería nacional dominicana, a través de la web [http://www.loteriasdominicanas.com][web]

[web]: http://www.loteriasdominicanas.com

### Librerias utilizadas
* BeautifulSoup 4
* urllib.request
* re (python's regular expressions library)

### En ejecución

Antes de ejecutar la aplicación, necesitarás tener instalada la librería 'BeautifulSoup 4':

```sh
$ pip install beautifulsoup4==4.4.1
```
Luego, podrás ejecutar la aplicación:
```sh
$ python scraper.py
```
Y verás en tu consola/terminal algo como esto:
```sh
$ python scraper.py
Quiniela Loteka -> {'date': '14-02-2016', 'numbers': ['02', '65', '36']}
Lotería Nacional -> {'date': '14-02-2016', 'numbers': ['13', '95', '27']}
Loto Pool -> {'date': '14-02-2016', 'numbers': ['03', '05', '10', '16', '18']}
Quiniela Real -> {'date': '14-02-2016', 'numbers': ['69', '92', '56']}
Quiniela Leidsa -> {'date': '14-02-2016', 'numbers': ['58', '34', '68']}
Super Kino TV -> {'date': '14-02-2016', 'numbers': ['11', '18', '20', '24', '26', '27', '28', '30', '31', '35', '46', '47', '48', '53', '60', '62', '66', '67', '73', '79']}
Mega Millions -> {'date': '12-02-2016', 'numbers': ['01', '07', '44', '68', '73']}
PowerBall -> {'date': '13-02-2016', 'numbers': ['07', '15', '18', '19', '36']}
Loto - Loto Más -> {'date': '13-02-2016', 'numbers': ['09', '10', '15', '31', '37', '38']}
Gana Más -> {'date': '14-02-2016', 'numbers': ['19', '56', '89']}
Loto Real -> {'date': '12-02-2016', 'numbers': ['04', '06', '09', '21', '23', '33']}
Pega 3 Más -> {'date': '14-02-2016', 'numbers': ['04', '22', '03']}
```
### Quieres colaborar?

Si crees que esta aplicación se puede hacer de una mejor manera **(*estoy seguro que si*)**, o quieres añadirle alguna otra funcionalidad... sientete libre de hacerle fork, modificar el código y hacer el pull request ;).
