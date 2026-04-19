id = 0
nome = ""
salario = 0.0
brasileiro = False

id = int(input("Digite seu ID de usuário: "))
nome =(input("Digite seu nome: "))
salario = float(input("Digite seu atual salário: "))
resposta = input("Você é Brasileiro de nascença? (s/n): ")
brasileiro = bool(resposta.lower() == "s")

print()
print("ID de usuário: ", id)
print("Nome: ", nome)
print("Salário: ", salario)
print("Ao ser perguntado sobre ser brasileiro disse: ", brasileiro)
print()
print("Ou")
print()

print(f"O id informado foi {id}. O nome informado pelo usuário foi {nome}. \nO salário que o mesmo disse que recebe é {salario: .0f}. Ao ser perguntado de sua nacionalidade brasileira disse {brasileiro}.")
