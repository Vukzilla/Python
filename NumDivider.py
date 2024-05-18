n = int(input("Input N: "))
br = 2

lenBr = str(len(str(n)))

while n % br != 0:
    br += 1

while n > 1:
    print(format(n, lenBr), end = (" | "))
    while n % br != 0:
        br += 1
    n = n / br
    n = int(n)
    print(br)

if n == 1:
    n = int(n)
    print(format(n, lenBr), end = (" | "))