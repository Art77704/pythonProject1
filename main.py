# Fibonacci от Джулфаян Артема Суреновича 20-КИС-1

user_input = int(input('Введите номер элемента: '))
user_input -= 1
count = 0
fibonacci = 0
fibonacci2 = 1

if user_input == 0:
    count -= 1
elif user_input == -1:
    result = 0
    print(f'Ответ: {result}')
    input()
    exit()
elif user_input < 0:
    print('Произошла ошибка. Допустим ввод лишь положительных чисел. Попробуйте снова!')
    input()
    exit()
elif user_input > 999:
    print('Возможно, ваш ПК не выдержит таких расчетов, вы действительно хотите продолжить (1 - Да / 2 - Нет)?')
    Answer = int(input())
    if Answer >= 2 or Answer < 1:
        input()
        exit()

while count != user_input:
    count += 1
    result = fibonacci + fibonacci2
    fibonacci = fibonacci2
    fibonacci2 = result

print(f'Ответ: {result}')

input()