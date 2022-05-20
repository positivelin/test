while 1:
    check = []
    try:
        check = list(map(int,input().split(' ')))
    except:
        break
    print(abs(check[0]-check[1]))
