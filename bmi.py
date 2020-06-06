# 몸무게와 키를 받아와 계산하는 함수
def bmi_cal(weight, tall):
    tall = float(tall)*0.01
    bmi = float(weight)/tall**2
    print(bmi)
    return bmi

# bim 수치를 받아와서 표준인지 아닌지 판별하는 함수
def is_Standard(bmi):
    if(bmi >= 20.0 and bmi <25.0):
        print("표준입니다.")
    else:
        print("체중관리가 필요합니다.")

# 몸무게와 키를 입력 받는 변수 이때 입력받는 숫자를 공백으로 구분하여 변수에 저장
# int가 아닌 float으로 받는다.
weight, tall = input('몸무게(kg)와 키(cm) 입력: ').split()

is_Standard(bmi_cal(weight, tall))

