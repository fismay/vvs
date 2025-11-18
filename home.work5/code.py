import pandas as pd
import numpy as np
test = pd.read_csv('tested.csv')
print(test)
print('---------------------------------')
#pandas only: 1
#1.1
#test = open('tested.csv').readlines()
#1.2 - проанализировать датасет:
#a) - наличие пропущенных значнений
#пропуски могут быть записаны как: <...>, NULL, NONE, EMPTY
count_none = test.isnull().sum().sum()
print(count_none)
#б) - признаки и категории
types = test.dtypes
print(types)
#1.3 - вывести первые n строк
n = int(input(f"Введите количество строк: "))
print(test.head(n))
#1.4 - вывести статистику по любому столбцу - главное численному
print(test.describe())
#1.5 - посчитать кол-во столбцов и кол-во строк в обшем
print(test.shape)

print('---------------------------------')

#numpy 
#2.1 - сравнить две группы
#a) - процент выживших 
survived = test['Survived'].value_counts(normalize=True)[1] * 100
print(f"Процент выживших: {survived}%")
#b) - средний возраст общий
average_age = test['Age'].mean()
print(f"Средний возраст общий: {average_age}")
#c) - средний возраст выживших
survived_age = test[test['Survived'] == 1]['Age'].mean()
print(f"Средний возраст выживших: {survived_age}")
die_age = test[test['Survived'] == 0]['Age'].mean()
print(f"Средний возраст умерших: {die_age}")

test = test.dropna() #удаляю пустые 
# 3 - новая таблица.

grouped = test.groupby(['Sex', 'Pclass'])
mean_age = grouped['Age'].mean()
mean_ticket = grouped['Fare'].mean()
survived_p = grouped['Survived'].mean() * 100

new_table = pd.DataFrame({
    'Mean age': mean_age,
    'Mean ticket': mean_ticket,
    'Survived, %': survived_p
}).reset_index()

print(new_table)


