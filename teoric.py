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
    #msg = ('Paridade: ', info['par'], '\n Horario:', hora, '\n Evento:', info['evento'], '\n Impacto', info['impacto'])
    #economic = pais + eventu + hora + impacto
    economic = hora
    #print(msg)

#calendario





#OPERACIONAIS
absorcao = "Se você está vendo que estão agredindo forte pra um lado, o volume cresce porém o preço não desloca existe uma grande possibilidade de estar acontecendo uma absorção!"
exaustao = "Mercado está perdendo força após um movimento forte de alta ou baixa, com um intervalo maior entre as agressões, existindo lotes para buscar mas não possui força para continuar? Pode estar acontecendo uma exaustão, fique atento! "
liquidez = "Muitas vezes confundido com os lotes de escora, lotes de liquidez ocorrem quando um player comprado/vendido está colocando lotes na contraparte do book chamando o mercado pro lado que seja a favor de sua posição e assim aumente o seu lucro."
escora = "Você percebe que um player está comprado/vendido e continua deixando lote no book de ofertas a favor de sua posição? Ele pode estar querendo defender aquele nível de preço. Lotes de escora são lotes para defender uma região."
renovacao = "A renovação pode ser considerada também como um tipo de absorção. Você pode percebe-la no momento em que o mercado está tentando ganhar um nível de preço. Por exemplo, existem 150 lotes na venda e os compradores agridem esses lotes porém o preço não desloca e você nota que agora passou a ter 180 lotes na venda, se caracterizando assim uma renovação nesse nível de preço."
cancelamento = "Diferente da renovação, o cancelamento seria o 'cair/subir no vazio'. Vamos supor que a média de lotes no book é de 150 contratos, porém você percebe que o mercado subiu 3 níveis de preço com cerca de 50 por nivel. Isso pode ter acontecido pelos players terem cancelado os lotes que estavam no book. "

vwap = "A VWAP ou Preço Médio Ponderado Por Volume é um dos indicador técnicos mais famosos do mercado. Por ele marcar uma região de muito volume financeiro, é comum institucionais estarem posicionados na região e dessa forma demonstrar interesse em protege-la. "
ajuste = "Está pensando em ficar posicionado até o próximo pregão? Então é melhor ficar atento ao ajuste, pois é no preço do ajuste que você ficará posicionado. Ele é um ajuste financeiro, podendo ser débito ou crédito, no próximo dia útil na conta dos investidores. "

#FERRAMENTAS
book = "Por ele é possível enxergar as intenções de compra e venda que o ativo está sendo negociado."
times = "Com essa ferramente você conseguirar visualizar todos os negocios que foram efetuados. Nele é informado o comprador, vendedor, o horário e a quantidade negociada."
dom = "Através dele conseguimos enviar nossas ordens de compra e venda. "
vol = "Através dessa ferramenta conseguimos visualizar o volume por contratos ou financeiro em determinado nível de preço."
#INFORMAÇÕES
rules = "É desejável e necessário que todos os participantes estejam cientes e de acordo com:\n \n 📌 REGRAS DO CANAL \n \n ✅ PERMITIDO ✅  \n \n 📌 Dúvidas sobre os replays e seus convidados, dia, horário específico; \n \n 📌 Sugestões sobre os convidados para rodar o replay, no dia de replay: (Profissionais ou amadores que podemos contatar).\n \n 📌 NÃO HÁ distinção de habilidades, qualquer um pode ficar a vontade para pedir e realizar um replay caso queira, será incluído no CRONOGRAMA DE CONVIDADOS.\n \n ❌ NÃO É PERMITIDO ❌\n \n 📌 NÃO é um grupo para troca de informações de operações no dia-a-dia e nem durante o pregão;\n \n 📌 NÃO MANDEM RELATÓRIO DE PERFORMANCE; \n \n 📌 GRUPO EXCLUSIVO PARA TROCA DE EXPERIÊNCIAS E TIRA DÚVIDAS DE REPLAYS;\n \n______________________________\n \n 📌 Todos os estudos, dúvidas, troca de ideias, poderão ser feitas pós-replay e em qualquer dia e horário que tenha dúvida;\n \n 📌 TODOS OS REPLAYS SERÃO GRAVADOS, RENDERIZADOS E ENVIADOS O LINK AQUI PARA ACOMPANHAR POSTERIORMENTE;\n \n 📌 Ao fim de cada Replay teremos espaço para perguntas e questionamentos ao convidado que executou o Replay de mercado e narrou sua análise para os presentes na sala de reunião;\n (Via Zoom ou Google Meets)\n \n 📌 FRISANDO, o intuito deste canal é gerar conteúdo em Replay, estudo em replay, convidar profissionais, amadores e pessoas que estão firmes e ativos no estudo de Fluxo/Tape reading, específicamente no DÓLAR FUTURO.\n \n ______________________________\n \n ‼️‼️As regras é só uma maneira de manter um objetivo claro e único, que é estudo de replays de mercado e análise intraday e macro econômica ‼️‼️"
replay = "Não tem nenhum replay agendado"
lista = "Lista dos replays está vazia, se deseja puxar algum replay basta nos chamar"
vinho = "Você tem que estudar primeiro seu Rubinho, tá pensando que é o Caique??"

#Psicologia 
ansiedade = 'A ansiedade é um estado de apreensão e medo, onde a possibilidade de prejuízo financeiro e dor emocional não são aceitos previamente, causando a sensação de ameaça. Quanto mais os riscos são aceitos, menos se sentirá ameaçado, o que lhe permite se manter disciplinado, concentrado e confiante. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
medo = ' Não adianta tomar um vinho gafonhoto, o medo é frequentemente o desconforto emocional mais presente no Trading. A não aceitação dos riscos de se entrar numa operação, causa a evitação e evitar o inevitável leva à interpretações e atitudes influenciadas pelo medo fazendo com que o Trader deixe de ser objetivo. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
n_erros = 'É uma medida de proteção que ocorre involuntariamente e que tem por objetivo proteger o Trader do sofrimento de ter que admitir que está errado e ainda perder dinheiro por isso. Assim não terá vinhos bons na mesa! Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
sabotagem = ' A auto sabotagem tem origem em um lugar mais profundo da psique. No lugar onde construímos nossas crenças, modelos mentais e visão de mundo. Requer do Trader Autoavaliação psicológica e reprogramação neurolinguística para que o Trader consiga não somente evitar erros de trading como manter o dinheiro já conquistado. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
n_perder = 'Uma atitude ganhadora prepara o trader para desenvolver as Competências de Trader, que  são exigidas quando se quer transformar em um Tader Consistente. Quem não sabe perder se sentirá sempre traído pelo mercado, e estará bem próximo do fracasso e não condiz com a realidade dos mercados financeiros. É a atitude mais amadora que um trader pode adotar. A análise técnica somente identifica oportunidades de Trading, porém não impede a aleatoriedade do mercado. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
n_ganhar = 'Muitos Traders desconhecem o equilíbrio de se arriscar com a dose certa de prudência e a disciplina. São dominados pela euforia e passam a agir como se o mercado pudesse ser dominado. A aceitação dos riscos inerentes ao Trading deve ser individual, completa e consistente. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
p_dinheiro = 'O foco do Trader Comum não deve ser ganhar dinheiro. Qualquer tipo de valor, que seja diferente de “transformar-se num trader consistente”, pode trazer problemas ao Trader, pois poderá causar distrações que podem colocar em cheque a sua consistência. O foco do Trader deve estar em cruzar a linha da consistência para que deixe de ser um Trader comum. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
n_estudar = 'Quem diz não ter paciência para estudar não entendeu de fato os riscos que impõe o mercado financeiro e a importância de estar preparado, existe operador que pensa e se prepara 24/7 como você quer vencer sem estar preparado?. Pode até estar informado sobre os riscos, mas isso não significa que tenha criado uma forte convicção sobre essa realidade. Enquanto isso não fica claro, o aspirante não achará necessário estudar ou se preparar para operar o mercado. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
n_metas = ' Quem não sabe precisa aprender. As metas e objetivos no Trading facilitam a disciplina, bem como um conjunto de regras, fundamentais em um ambiente onde todas as decisões são tomadas pelo próprio Trader. Esse excesso de liberdade, sem uma estrutura mental bem definida, pode trazer consequências drásticas ao Trader. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'
inseguranca = 'Quando todas as principais competências de Trader estiverem em andamento, é natural que o Trader comece a se sentir mais seguro. Insegurança é um julgamento, que revela o quanto nos sentimos vulneráveis e preparados para lidar com as demandas. Conforme nos capacitamos e interagimos com o meio com disciplina e persistência, é comum que deixemos de nos sentir despreparados e consequentemente mais seguros. Precisa de acompanhamento? Solicite um agendamento com 15% de desconto com nosso mentor de Análise Mental @RenanReligare'

