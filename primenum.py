# 숫자를 받아와서 소수이면 True 아니면 False
def is_prime(n):
    i = 1 
    count = 0
    # n을 n보다 작은 수로 계속 나눠서 나머지가 0이 나오는 숫자를 체크
    while i < n: 
        if n%i==0: 
            count += 1
            i += 1
        else:
            i += 1
    # 소수의 조건은 1과 자기자신 외에 나누어 떨어지는 숫자가 없다 
    # 따라서위의 조건에서 나누어지는 경우가 1 이상이면 소수가 아님
    if count > 1:
        return False
    else:
        return True
            
def prime_number_list(length):
    result = []
    count = 2
    # result의 길이를 기준으로 받아온 length와 비교하여 계속 실행하여 length만큼 result에 조건에 맞는 값을 추가시킴
    while len(result) < length:
        if is_prime(count)==True:
            result.append(count)
            count += 1
        else: 
            count += 1
    return result

length = int(input('Length? '))
print(prime_number_list(length))