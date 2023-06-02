def solution(price, money, count):
    for i in range(1,count+1):
        money -= price * i
        # 17 # 11 # 2 # -10
    if money > 0 : 
        return 0
    return -money