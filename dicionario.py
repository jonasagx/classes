# definicao:
# Dicionario contem palavras e suas definicoes
# e permite buscar essas definicoes a partir da
# palavra em questao

definições = {
    "dia": "1 tempo que transcorre, em determinada região da Terra, entre o instante do nascer do Sol e o do seu ocaso",
    "ocaso": "1 o aparente declínio de um astro no horizonte, do lado oeste; pôr, poente",
    "horizonte": "1 linha circular em que a terra ou o mar parecem unir-se ao céu, e que limita o campo visual de uma pessoa"
}

print("Bem-vinda(o) - Dicionario de Jonas contem", len(definições), "definições")

while True:
	palavra = input("Que palavra voce gostaria de definir? ")

	if palavra in definições:
		print(definições[palavra])
	else:
		print("palavra não encontrada")
		novaDefi = input("qual definição você gostaria de usar")
		definições[palavra] = novaDefi 