import codecs

#esta clase solo lee un archivo o lo escribe
#def <nombre del metodo>(variales que entran)   iso-8859-1

def leer(filename):
	with codecs.open(filename, 'r', encoding='cp1252') as f:
		return f.read().encode('cp1252').decode('cp1252')
		

def escribir(filename, text):
	with codecs.open(filename, 'w', encoding='cp1252') as f:
		f.write(text.encode('cp1252').decode('cp1252'))