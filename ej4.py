import random
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]
puntaje = 0
answ = str()
listapreg = list(range(len(preguntas)))
random.shuffle(listapreg)
for i in range(0, len(listapreg)):
	ques = preguntas[listapreg[i]][0]
	print('Pregunta: ', ques)
	answ = input('Ingresa tu respuesta: ').lower()
	if answ == (preguntas[listapreg[i]][1]):
		print('Respuesta correcta.')
		puntaje = puntaje + 1
	else:
		print('Respuesta incorrecta.')
print('Tu puntaje total es: ', puntaje)
	
