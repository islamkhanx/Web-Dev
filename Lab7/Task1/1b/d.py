# Для данного числа x выведите значение sign(x).

if __name__ == "__main__":
    x = int(input())
    print(1 if x > 0 else -1 if x < 0 else 0)
