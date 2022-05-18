n = int(input())
for i in range(n):
    result = 0
    temp = list(map(int,input().split(' ')))
    Case = temp[0]
    House = sorted(temp[1::])

    if Case % 2 == 0:
        mid = (int(House[Case//2-1])+int(House[Case//2]))/2
    else:
        mid = int(House[Case//2])

    for j in House:
        result += abs(mid - int(j))
    # print(mid)
    print(int(result))