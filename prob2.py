n = 4
for i in range(1, n+1):
    x = ''
    for j in range(1, i+1):
        #print('#', end='')
        x += '#'
    print(x)
print ("#"*(n+1))
for i in range(n, 0, -1):
    print('#' * i)