#1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#Примечание: в сумму не включаем пустую строку и строку целиком.
#Пример работы функции:
#
#func("papa")
#6
#func("sova")
#9
#
def num_substr(string):
    """функция получения количества подстрок в строке"""
    string = str(string)
    lenght = len(string)
    substrings = []
    [[substrings.append(string[i:i+n+1]) for i in range(lenght-n) if string[i:i+n+1] not in substrings]
     for n in range(lenght-1)]
    print(substrings)
    return len(substrings)

print(num_substr('knsdfklklsdf'))

def test_func(func):
    print("Тестируем: ", func.__doc__)
    print("testcase #1: ", end="")
    string = 'papa'
    num = 6
    print("Ok" if num_substr(string) == num else "Fail")

    print("Тестируем: ", func.__doc__)
    print("testcase #2: ", end="")
    string = 'sova'
    num = 9
    print("Ok" if num_substr(string) == num else "Fail")

    print("Тестируем: ", func.__doc__)
    print("testcase #3: ", end="")
    string = 'eggs'
    num = 8
    print("Ok" if num_substr(string) == num else "Fail")


if __name__ == "__main__":
    test_func(num_substr)
