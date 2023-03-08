ano =int(input(" informe o ano: "))


def bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return 'O ano digitado é Bissexto'
    else:
        return 'O ano digitado não é Bissexto'
print(bissexto(ano))