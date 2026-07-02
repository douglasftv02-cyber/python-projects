import random
import string

print("=" * 35)
print("      GERADOR DE SENHAS")
print("=" * 35)

# Pergunta o tamanho da senha
tamanho = int(input("Digite o tamanho da senha: "))

# Caracteres disponíveis
letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

caracteres = letras + numeros + simbolos

# Gera a senha
senha = ""

for i in range(tamanho):
    senha += random.choice(caracteres)

print("\nSua senha gerada é:")
print(senha)
