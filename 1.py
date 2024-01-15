from datetime import datetime 
import random

print('--------------- Olá, seja bem-vindo a nossa empresa -------------')
name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
data_register = datetime.now()
cards = ['R$: 50,00', 'R$: 250,00', "R$: 120,00"]
card = random.choice(cards)
birthday = datetime.strptime(
    input("Digite sua data de aniversário no formato dd/mm/aaaa: "), '%d/%m/%Y')

print(f'Olá {name}, seu registro foi concluído com sucesso no dia {data_register.day}/{data_register.month}/{data_register.year}. \n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {card}')