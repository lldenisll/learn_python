from datetime import date, time, datetime, timedelta
def trabalhando_datetime():
    data_atual=datetime.now()
    print(data_atual)
    print(type(data_atual))
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(type(data_atual))
    print(data_atual.strftime("%c"))
    print(data_atual.weekday())
    tupla=("Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo")
    print(tupla[data_atual.weekday()])
    nova_data=data_atual - timedelta(days=365)
    print(nova_data.strftime("%c"))

def trabalhando_date():

    dataatual=date.today()
    print(dataatual.strftime('%d/%m/%y'))
    print(dataatual.strftime('%A %B %Y'))

def trabalhando_time():
    horario=time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))



if __name__ == '__main__':
    trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()