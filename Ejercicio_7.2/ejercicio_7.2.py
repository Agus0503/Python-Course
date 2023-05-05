import time

hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print("¡Hora de ir a casa!")
else:
    tiempo_restante = (19 - hora_actual)
    print("Todavía quedan {} horas para ir a casa".format(tiempo_restante))
