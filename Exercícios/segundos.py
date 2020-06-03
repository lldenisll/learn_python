segundos_str=input("Por favor preencha o numero de segundos que deseja converter: ")
segundos_int=int(segundos_str)

dias=segundos_int//86400
segundosrestantesd=segundos_int%86400
horas_restantes=segundosrestantesd//3600
segundos_restantesh=segundosrestantesd%3600
minutos=segundos_restantesh//60
segundos_restantesf=segundos_restantesh%60

print(dias,"dias,",horas_restantes,"horas,", minutos, "minutos e", segundos_restantesf, "segundos.")

    