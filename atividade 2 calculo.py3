peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
Cálculo do IMC
imc = peso / (altura ** 2)
Exibe o valor do IMC com duas casas decimais
print(f"\nSeu IMC é: {imc:.2f}")
Avaliação do IMC
if imc > 25:
    print("Acima do peso ideal")
elif imc < 18:
    print("Abaixo do peso ideal")
else:
    print("O seu peso está OK