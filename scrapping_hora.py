from bs4 import BeautifulSoup
import requests 
import emoji
from datetime import datetime

headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})

data = requests.get('http://br.investing.com/economic-calendar/', headers = headers)

resultados = []

if data.status_code == requests.codes.ok:
    info = BeautifulSoup(data.text, 'html.parser')
    blocos = ((info.find('table', {'id': 'economicCalendarData'})).find('tbody')).findAll('tr', {'class': 'js-event-item'})
    
    for blocos2 in blocos:
        impacto = str((blocos2.find('td', {'class': 'sentiment'})).get('data-img_key')).replace('bull', '')
        horario = str(blocos2.get('data-event-datetime'))
        


        evento = (blocos2.find('td', {'class': 'left event'})).text.strip()
        moeda = (blocos2.find('td', {'class': 'left flagCur noWrap'})).text.strip()
        impacto = int(impacto)
        if impacto > 1:
            resultados.append({'par': moeda, 'horario': horario, 'evento': evento, 'impacto': impacto})
        

for info in resultados:

    if info['par'] == 'USD':
        info['par'] = 'Estados Unidos'
    if info['par'] == 'EUR':
        info['par'] = 'Europa'
    if info['impacto'] == 2:
        info['impacto'] = emoji.emojize(':cow_face: :cow_face:')
    elif info['impacto'] == 3:
        info['impacto'] = emoji.emojize(':cow_face: :cow_face: :cow_face:')
    pais = info['par']
    eventu = info['evento']
    hora = info['horario']
    data_e_hora = datetime.strptime(hora,'%Y/%m/%d %H:%M:%S')
    hora  = data_e_hora.strftime('%H:%M')
    impacto = info['impacto']
    
    msg = ('Paridade: ', info['par'], '\n Horario:', hora, '\n Evento:', info['evento'], '\n Impacto', info['impacto'])
    economic = pais + eventu + hora + impacto
    print(msg)
