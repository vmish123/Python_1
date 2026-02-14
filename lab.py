def main():
    print("Задание №1:")
    first_task()

    print("Задание №2:")
    second_task()

    print("Задание №3:")
    third_task()

    print("Задание №5:")
    fifth_task()

    print("Задание №6:")
    sixth_task()

    print("Задание №7:")
    seventh_task()

    print("Задание №8:")
    eighth_task()

    print("Задание №9:")
    ninth_task()

    print("Задание №10:")
    tenth_task()

    print("Задание №11:")
    eleventh_task()

    print("Задание №12:")
    twelfth_task()

    print("Задание №13")
    thirteenth_task()


# Задание 1
def first_task():
    film_name = input()
    theater_name = input()
    session_time = input()

    print(f"Билет на \" {film_name} \" в \" {theater_name} \" на {session_time} забронирован.")


# Задание 2
def second_task():
    first_string = input("Введите превую строку (да/нет): ").lower()
    second_string = input("Введите вторую строку (да/нет): ").lower()
    allowed_words = ["да", "нет"]

    if (first_string in allowed_words) and (second_string in allowed_words):
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")


# Задание 3
def third_task():
    login_input = input("Введите логин: ")
    reserve_address = input("Введите резервный адрес: ")

    if ("@" not in login_input) and ("@" in reserve_address):
        print("Корректные логин и резервный адрес")
    else:
        print("Некорректный логин или резервный адрес")


# Задание 4
print(input())


# Задание 5
def fifth_task():
    string_length = len(input("Введите строку: "))
    if string_length == 0:
        print("ДА")
    else:
        print("НЕТ")


# Задание 6
def sixth_task():
    entered_numbers = input()

    if len(entered_numbers) == 3 and entered_numbers.isdigit():

        entered_numbers = list(entered_numbers)  # Преобразование строки в список

        half_amount = 0.5 * (int(max(entered_numbers)) + int(min(entered_numbers)))
        entered_numbers.remove(max(entered_numbers))
        entered_numbers.remove(min(entered_numbers))

        if half_amount == float("".join(entered_numbers)):
            print("Вы ввели красивое число")
        else:
            print("Жаль, вы ввели обычное число")

    else:
        print("Некорректное число")


# Задание 7
def seventh_task():
    entered_number = int(input())
    first_num = entered_number % 10
    entered_number //= 10
    second_num = entered_number % 10
    entered_number //= 10
    third_num = entered_number % 10
    fourth_num = entered_number // 10

    # Сортировка
    if first_num > second_num:
        first_num, second_num = second_num, first_num
    if third_num > fourth_num:
        third_num, fourth_num = fourth_num, third_num

    if first_num > third_num:
        first_num, third_num = third_num, first_num
    if second_num > fourth_num:
        second_num, fourth_num = fourth_num, second_num

    if second_num > third_num:
        second_num, third_num = third_num, second_num

    # Обработка нуля в начале
    if first_num == 0 and second_num != 0:
        first_num, second_num = second_num, first_num
    elif first_num == 0 and third_num != 0:
        first_num, third_num = third_num, first_num
    elif first_num == 0 and fourth_num != 0:
        first_num, fourth_num = fourth_num, first_num

    print(first_num * 1000 + second_num * 100 + third_num * 10 + fourth_num)


# Задание 8
def eighth_task():
    allowed_max = 190
    allowed_min = 150
    candidates = []

    while True:
        current_candidate = input()
        if current_candidate != "!":
            if allowed_max >= int(current_candidate) >= allowed_min:
                candidates.append(int(current_candidate))
        else:
            break

    print(len(candidates))
    print(min(candidates), max(candidates))


# Задание 9
def ninth_task():
    while True:
        password = input("Введите пароль: ")
        repeated_password = input("Повторите пароль: ")

        if len(password) < 8:
            print("Короткий!")
            continue
        elif "123" in password:
            print("Простой!")
            continue
        elif password != repeated_password:
            print("Различаются.")
            continue
        else:
            print("OK")
            break


# Задание 10
def tenth_task():

    while True:
        entered_number = int(input())
        entered_operator = input()

        if entered_operator in ["+", "-", "*", "/", "%"]:
            second_number = int(input())

            if second_number == 0 and entered_operator in ["/", "%"]:
                continue

            if entered_operator == "+":
                print(entered_number + second_number)
            elif entered_operator == "-":
                print(entered_number - second_number)
            elif entered_operator == "*":
                print(entered_number * second_number)
            elif entered_operator == "/":
                print(entered_number // second_number)
            elif entered_operator == "%":
                print(entered_number % second_number)

        elif entered_operator == "!":
            if entered_number < 0:
                continue

            result = 1

            for i in range(1, entered_number + 1):
                result *= i
            print(result)

        elif entered_operator == "x":
            print(entered_number)
            break


# Задание 11
def eleventh_task():
    height = int(input())
    if height >= 1:
        for i in range(1, height + 1):
            print(" " * (height - i) + "*" * (i - 1) + "*" + "*" * (i - 1))


# Задание 12
def twelfth_task():
    N = int(input())
    numbers_in_row = 1
    current_number = 1

    while current_number <= N:

        for i in range(numbers_in_row):

            if current_number > N:
                break

            print(current_number, end=" ")
            current_number += 1

        print()
        numbers_in_row += 1


# Задание 13
def thirteenth_task():
    n = int(input())
    m = int(input())
    symb = input()

    if n >= 1 and m >= 1:
        print(symb * m)
        for i in range(n - 2):
            if m > 1:
                print(symb + " " * (m - 2) + symb)
            else:
                print(symb)
        if n > 1:
            print(symb * m)


main()
