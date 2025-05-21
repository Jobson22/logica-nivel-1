# Solicita o primeiro número ao usuário
num1_str = input("Digite o primeiro número: ")

# Solicita o segundo número ao usuário
num2_str = input("Digite o segundo número: ")

# Converte as entradas para números (inteiros ou decimais)
# Usamos float() para permitir tanto números inteiros quanto decimais
num1 = float(num1_str)
num2 = float(num2_str)

# Realiza a soma
soma = num1 + num2

# Exibe o resultado
print(f"A soma de {num1} e {num2} é: {soma}")
