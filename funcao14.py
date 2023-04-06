#PALIDROMO - PALAVRA OU FRASE QUE PODE SE LER
#INDIFERENTEMENTE, DA ESQUERDA PARA A DIREITA E VICE-VERSA
def verificar_palidromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto[::-1]
    
    # texto [::-1]inverte o texto
    
texto = "socorram~me, subi no onibus em marrocos"
if verificar_palidromo(texto):
    print(texto, "é um palidromo.")
else:
    print(texto, "n~so é um palidromo.")