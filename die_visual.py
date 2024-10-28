from die import Die

#Создание кубика D6
die = Die()

# Смоделирование серии бросков с сохранением результатов в списке
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequenciy = results.count(value)
    frequencies.append(frequenciy)

print(frequencies)