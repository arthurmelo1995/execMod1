def verificar(n):
    if n % 5 == 0 and n % 7 ==0:
        print('fizzbuzz')

    elif n % 7 == 0:
        print('buzz')

    elif n % 5 == 0:
        print('fizz')
    else:
        print('Não é divisivel nem por 5, nem por 7!')