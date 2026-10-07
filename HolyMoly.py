from secondfile import is_odd

numbers = [11, 25, -2, 7, 18]


for num in numbers:
    if is_odd (num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")

    