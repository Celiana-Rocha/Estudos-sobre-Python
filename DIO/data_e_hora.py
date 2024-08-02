# from datetime import datetime, timedelta

# tipo_carro = 'M' # P, M, G
# tempo_pequeno = 30
# tempo_medio = 45
# tempo_grande = 60
# data_atual = datetime.now()

# if tipo_carro == 'M':
#     data_estimada = data_atual + timedelta(minutes=tempo_medio)
#     print(f'O carro chegou: {data_atual} e saira {data_estimada}')
# elif tipo_carro == 'P':
#     data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
#     print(f'O carro chegou: {data_atual} e saira {data_estimada}')
# else:
#     data_estimada = data_atual + timedelta(minutes=tempo_grande)
#     print(f'O carro chegou: {data_atual} e saira {data_estimada}')

# print(datetime.today() - timedelta(days=1)) #aqui vc remoce um dia

# resultado = datetime(2023, 7, 25, 19, 10) - timedelta(hours=1)
# print(resultado.time()) #este printa apenas a hora
# print(datetime.now().date())

# #strftime e strptime
# #usado oara fromatar hora e data da forma que queremos e no idioma tbm

# from datetime import datetime

# data_hora_atual = datetime.now()
# data_hora_str = "2023-10-20 10:20"
# mascara_ptbr = "%d/%m/%Y %a"
# mascara_en = "%Y-%m-%d %H:%M"

# print(data_hora_atual.strftime(mascara_ptbr))

# data_convertida = datetime.strptime(data_hora_str, mascara_en)
# print(data_convertida)
# print(type(data_convertida))

#timezone
#fuzohorario

from datetime import datetime
import pytz 

data = datetime.now(pytz.timezone('US/Eastern')) #escolja de qual pais e local quer exibir o horario

print(data)