import pysubs2
import pysrt
archivo = 'subtitle.ass'
subs = pysubs2.load(archivo, encoding='utf-8')

for line in subs:
    print(line.text)
    textoplano = line.text
    texto = open('textoplano.txt', 'a')
    texto.write(textoplano)
    texto.close()







