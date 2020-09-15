import json
import urllib.request, urllib.parse, urllib.error
total = 0

url = input('Digite a URL: ')
dados = urllib.request.urlopen(url).read().decode()

info = json.loads(dados)
number = info["Comentários"]
for i in number:
    informacao = i.get('Contagem')
    total = total + int(informacao)
print(total)
