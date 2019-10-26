# -*- coding: iso-8859-1 -*-
from cargaDatos import leer, escribir
import alfabeto
LARGO = 0
#==========================================================================================
def arreglo(texto, alfabeto):
	texto = leer(texto)
	global LARGO
	LARGO = len(texto)
	fill = 0
	
	if (LARGO % 4) != 0:
		fill = 4 - (LARGO % 4)
		texto = texto + ('a'*fill)
	
	
	temp_in = []
	bloque = []
	
	for i in range(0, len(texto), 4):
		cadena = texto[i: i + 4]
		for x in cadena:
			temp_in.append(alfabeto.find(x))
			#if alfabeto.find(x) == -1:
			#	print x
		bloque.append(temp_in)
		temp_in = []

	if (len(bloque) % 2) != 0:
		bloque.append([0,0,0,0])
	return bloque
#==========================================================================================
def permuta_cif(lista):
	orden = [2, 1, 3, 0]
	return [lista[i] for i in orden]
	
def permuta_decif(lista):
	orden = [3, 1, 0, 2]
	return [lista[i] for i in orden]
#==========================================================================================
def cifrar_feistel(texto, key, alfabeto, resultado, N):
	mensaje = arreglo(texto, alfabeto)
	guarda_bloque = []
	s = []
	iteracion = 0
	
	while True:
		iteracion = iteracion + 1
		if iteracion <= N:
			#contruir S
			for bloque in range(len(mensaje)):
				if (bloque % 2) == 0:
					for letra in mensaje[bloque]:
						guarda_bloque.append((letra + key) % len(alfabeto))
					s.append(guarda_bloque)
					guarda_bloque = []
				else:
					s.append(mensaje[bloque])
			
			#permutacion
			for bloque in range(len(s)):
				if (bloque % 2) == 0:
					s[bloque] = permuta_cif(s[bloque])
					
			#cambio de posicion
			mensaje = []
			for i in range(0, len(s), 2):
				mensaje.append(s[i+1])
				mensaje.append(s[i])
			s = []
		else:
			break
	cifrado = ''.join(alfabeto[letra] for bloque in mensaje for letra in bloque)
	escribir('len', str(LARGO))
	escribir(resultado, cifrado)
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
def descifrar_feistel(texto, key, alfabeto, resultado, N):
	mensaje = arreglo(texto, alfabeto)
	guarda_bloque = []
	s = []
	global LARGO
	f=open("len", "r")
	LARGO = int(f.read())
	iteracion = 0
	
	while True:
		iteracion = iteracion + 1
		if iteracion <= N:
			#cambio de posicion
			for i in range(0, len(mensaje), 2):
				s.append(mensaje[i+1])
				s.append(mensaje[i])
			
			#permutacion
			for bloque in range(len(s)):
				if (bloque % 2) == 0:
					s[bloque] = permuta_decif(s[bloque])
			
			#contruir mensaje
			mensaje = []
			for bloque in range(len(s)):
				if (bloque % 2) == 0:
					for letra in s[bloque]:
						guarda_bloque.append((letra - key) % len(alfabeto))
					mensaje.append(guarda_bloque)
					guarda_bloque = []
				else:
					mensaje.append(s[bloque])
			s = []
		else:
			break
			
	cifrado = ''.join(alfabeto[letra] for bloque in mensaje for letra in bloque)[:LARGO]
	escribir(resultado, cifrado)
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================


#test1 = 'STARWARSLAMISIONCONTINUA'
#test2 = 'WARSBUSTSIONNBJMINUAÑPUD'
#print cifrar_feistel('quijote.txt', 1, alfabeto.es_letras, 'AAA', 2)
#print descifrar_feistel('AAA', 1, alfabeto.es_letras, 'BBB', 2)
#print "aloha"


