import pysubs2
archivo = 'subtitle.ass'
subs = pysubs2.load(archivo, encoding='utf-8')
for line in subs:
    print(line.text)
