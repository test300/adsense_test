import os,shutil

tag = "<!-- anuncio -->"
ads = """
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <ins class="adsbygoogle" style="display:block;background-color:transparent" data-ad-client="ca-pub-0000000000000000" data-ad-slot="0000000000" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""

# Generar lista de ficheros a revisar
lista = []
for base, dirs, files in os.walk('.'):
	print(base,files)
	try:
		if (files[0]=='index.html'):
			lista.append(base +"\index.html")
	except:
		pass
	
print(lista)

for fichero in lista:
	print(fichero+"init")
	lectura=open(fichero, "r", encoding="utf-8")
	temp = open("temp.txt", 'w', encoding="utf-8")

	for linea in lectura:
		if tag in linea:
			temp.write(ads + '\n')
		else:
			if linea != "/n":
				temp.write(linea)
	temp.close()
	lectura.close()
	os.remove(fichero)
	shutil.move("temp.txt", fichero)
	print(fichero+"end")
