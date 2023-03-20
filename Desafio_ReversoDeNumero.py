# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado

def reverso(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = (reverso * 10) + digito
        numero = numero // 10
    return reverso