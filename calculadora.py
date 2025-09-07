# calculadora.py

def adicionar(x, y):
    """Soma dois números"""
    return x + y

def subtrair(x, y):
    """Subtrai dois números"""
    return x - y

def multiplicar(x, y):
    """Multiplica dois números"""
    return x * y

def dividir(x, y):
    """Divide dois números"""
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

print("Selecione a operação:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    escolha = input("Digite sua escolha (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        
        proxima_operacao = input("Deseja realizar outra operação? (sim/não): ")
        if proxima_operacao.lower() != 'sim':
            break
    else:
        print("Escolha inválida. Por favor, selecione uma das opções (1/2/3/4).")
