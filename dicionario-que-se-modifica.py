#!/usr/bin/env python
# pickle eh biblioteca do Python que transforma codigo python numa representacao textual mais simples.
import pickle

definições = {
    "dia": "1 tempo que transcorre, em determinada região da Terra, entre o instante do nascer do Sol e o do seu ocaso",
    "ocaso": "1 o aparente declínio de um astro no horizonte, do lado oeste; pôr, poente",
    "horizonte": "1 linha circular em que a terra ou o mar parecem unir-se ao céu, e que limita o campo visual de uma pessoa"
}

# aqui o script le o conteudo do arquivo `dict.p` e manda o conteúdo, que é código python, para a variável `definições`  
definições = pickle.load( open( "dict.p", "rb" ) )
print("Bem-vinda(o) ao Dicionario de Jonas contem", len(definições), "definições")

palavra = input("Que palavra voce gostaria de definir? ")

if palavra in definições:
    print(definições[palavra])
else:
    print("palavra não encontrada")
    novaDefi = input("qual definição você gostaria de usar: ")
    definições[palavra] = novaDefi 

print("Ciao")

# ao final guardamos as novas palavras no arquivo `dict.p` assim na próxima execução podemos usar as novas palavras adicionadas
pickle.dump(definições, open( "dict.p", "wb" ))
