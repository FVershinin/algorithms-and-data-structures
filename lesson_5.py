import collections, functools


def task_1():
    count = int(input("Кол-во предприятий: "))
    companies = collections.defaultdict(int)
    for i in range(count):
        name = input(f'Название #{i + 1} компании:')
        incomes = [int(it) for it in input("Прибыль(перечислите через запятую)").split(',')]
        assert len(incomes) == 4
        companies[name] = sum(incomes)
    average = sum(companies.values()) / count
    print(f'Средняя прибыль всех компаний за год: {average}')
    for company in companies:
        status = 'выше' if companies[company] >= average else 'ниже'
        print(f'Компании с прибылью {status} средней: {company}, {companies[company]}')


def task_2():
    numbers = collections.defaultdict(list)
    number_a = input('Введите первое HEX число: ')
    number_b = input('Введите второе HEX число: ')
    numbers[f'1-{number_a}'] = list(number_a)
    numbers[f'2-{number_b}'] = list(number_b)
    print(numbers)
    hex_sum = sum([int(''.join(i), 16) for i in numbers.values()])
    print("Сумма: ", list('%X' % hex_sum))
    hex_multiplication = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numbers.values()])
    print("Произведение: ", list('%X' % hex_multiplication))

task_2()
