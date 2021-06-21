def fibo(n):
    first,second = 0,1
    for i in range(n):
        print(first)
        first,second = second, first+second


n = int(input('Enter n: '))
fibo(n)