# -*- coding: iso-8859-1 -*-
from cargaDatos import leer, escribir
#importar la lib que nos permite cargar los archivos o escribirlos

#ajusta el largo de la llave al largo del mensaje a cifrar
def largo_de_llave(key, largo):
   return (key * ((largo/len(key))+1))[:largo]

#metodo para cifrar
def cifrar_vigenere(texto, key, alfabeto, resultado):
	#las cadenas entran codificadas
	texto = leer(texto)
	key = leer(key)
	# en caso de que la llave sea mas larga que el mensaje
	if len(key)>len(texto):
		key = key[:len(texto)]
	#en caso de que el mensaje sea mas largo que la llave
	else:
		key = largo_de_llave(key, len(texto))
	
	cifrado = ''
	c = []
	index = 0
	#c = m + k % 27
	while index < len(texto):
		if alfabeto.find(texto[index]) == -1:
			print texto[index]
		c.append(alfabeto[(alfabeto.find(texto[index]) + alfabeto.find(key[index])) % len(alfabeto)])
		index = index + 1
	
	cifrado = ''.join(c)
	escribir(resultado, cifrado)

#metodo para descifrar
def descifrar_vigenere(texto, key, alfabeto, resultado):
	#las cadenas entran codificadas
	texto = leer(texto)
	key = leer(key)

	# en caso de que la llave sea mas larga que el mensaje
	if len(key)>len(texto):
		key = key[:len(texto)]
	#en caso de que el mensaje sea mas largo que la llave
	else:
		key = largo_de_llave(key, len(texto))
	
	cifrado = ''
	c = []
	index = 0
	#m = c - k % 27
	while index < len(texto):
		c.append(alfabeto[(alfabeto.find(texto[index]) - alfabeto.find(key[index])) % len(alfabeto)])
		index = index + 1
	
	cifrado = ''.join(c)
	escribir(resultado, cifrado)
	