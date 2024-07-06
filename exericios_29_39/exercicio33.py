'''
Peça ao usuário para inserir quatro notas. 
Calcule a média e informe se o aluno está aprovado (média >= 7), 
em recuperação (5 <= média < 7) ou reprovado (média < 5).
'''
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")
elif  5 <= media < 7:   
    print("Em recuperação")
else:
    print("Reprovado")

