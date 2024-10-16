# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def conta_pares(número):
    if número % 2 == 0:
        return f"O {número} é par"
    else:
        return f"O {número} é impar"
    
resultado = conta_pares(6)
print(resultado)