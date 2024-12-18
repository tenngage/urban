num = int(input())
result = ''

for i in range(3, num+1):
    if num % i == 0:
        print(i)
        arr = []
        for j in range(1, i):
            n = i - j
            if n == j:
                break
            if n not in arr:
                result += str(j)
                result += str(n)
                arr.extend([j, n])
print(result)
            
            

            

