# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
a=int(input("Digite o primeiro valor da pogreçao aritmetica"))
b=int(input("Digite a razao da pogreçao aritmetica"))
for i in range (10):
    print (i)
    c=a + i * c
    print (f"Termo {i+1}: {c}")