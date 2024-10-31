def fibonachi(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        print(n1)
        n1, n2 = n2, n1 + n2
    print()  


n = int(input("Sheiyvane ricxvi: "))
fibonachi(n)
