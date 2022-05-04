def elevaxcomy(nro1,nro2):
    eleva = nro1**nro2
    return eleva

while True:
    try:
        nro1 = int(input('Digite o primeiro valor:' ))
        nro2 = int(input('Digite o segundo valor:' ))
        if nro1<0 and nro2<0:
            print('Não serão aceitos números negativos!')
        break
    except ValueError:
        print('Digite um número válido!')

print('O primeiro valor elevado ao segundo valor é:', elevaxcomy(nro1,nro2))