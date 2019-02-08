# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.


def task_1(text: str):
    results = set()
    for i in range(len(text)):
        n = len(text) - (1 if (i == 0) else 0)
        for j in range(n, i, - 1):
            results.add(hash(text[i:j]))
    print(f"Кол-во различных подстрок: {len(results)}")
