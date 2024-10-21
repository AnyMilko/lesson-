N = 20
dividers = list()
for div in range(3, N//2+1):
    if N % div == 0:
        dividers.append(div)
dividers.append(N)
