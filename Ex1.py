
import datetime as dt

nascimento = input('Data de Nascimento: ')

def vida(nascimento):
  hoje = str(dt.date.today())
  ano = int(nascimento[0:4])
  mes = int(nascimento[5:7])
  dia = int(nascimento[8:10])

  dias_vida = (int(hoje[0:4]) - ano)*365 + (int(hoje[5:7]) - mes)*30 + (int(hoje[8:10]) - dia)
  
  print('Dias de vida: ', dias_vida)

vida(nascimento)