numbers = [11, 25, -2, 7, 18]

def is_odd (numero):
    global odd
    odd = True
    if numero % 2 == 0:
        odd = False
    if numero % 2 != 0:
        odd = True

    return odd

for num in numbers:
    if is_odd (num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")

    