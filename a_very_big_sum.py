n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

suma = 0

for i in range(0, n):
    suma += arr[i]

print suma