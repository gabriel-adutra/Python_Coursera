import re

arquivo = open('regex_sum_915661.txt')
numeros = list()
soma = 0

for linha in arquivo:
	linha = linha.strip()
	objetoAPesquisar = re.findall('([0-9]+)',linha)
	if len(objetoAPesquisar) < 1:
		continue
#	print(objetoAPesquisar)
	for elemento in objetoAPesquisar:
		numeros.append(int(elemento))

for numero in numeros:
	soma += numero

print(soma)
