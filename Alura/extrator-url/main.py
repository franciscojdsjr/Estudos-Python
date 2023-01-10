url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_interrogação = url.find('?')

print(indice_interrogação)

url_base = url[:(indice_interrogação + 1)]
print(url_base)

url_parametros = url[(indice_interrogação + 1):]
print(url_parametros)

len('moedaorigem')

print()