'''
Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
(программа не должна зависеть от регистра вводимых символов).
'''

genome = input().lower()
print((genome.count('c')+genome.count('g'))/len(genome)*100)