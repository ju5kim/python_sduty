money = 10000
price = 1000
coffe = 5
while money >= price:
    print("커피를 구매했습니다.")
    money -= price
    coffe -= 1
    print("남은 커피 :",coffe)
    if coffe == 0 :
        break

#1부터 10까지 홀수만 출력
a=1
while (a <= 10 ):
    a+=1
    if(a%2>0) :
        print(a)

#break
#반복문을 빠져나감
#continue
#반복문의 처음으로 돌아감
print("**********************")
b=0
while (b<=10) :
    b+=1
    if(b%2 ==0) :  
        continue
    print(b)

# 구구단     
dan = 2;
number =1;        
limit = 10;
while(dan<limit) :
    while(number<limit):
        print(str(dan)+"x"+str(number)+ "="+str(dan*number))
        number+=1
    dan+=1
    number=1

# 레인지 함수
#  range()
# 리턴값은?? range 객체
# 이더 숫자만 사용하는 컬랙션 리스트 같은 
print("==레인지 테스트")
v = range(10)
print(v)
print(type(v))


# 0~9까지
for i in range(10) : 
    print(i)
    
# 0~9까지
# 매개변수 시작 값 ,끝 값
for i in range(0,10) : 
    print(i)

# 0~9까지 2개씩 증가 
# 기본은 1부터
# 매개변수 시작 값, 끝 값, 증가값
for i in range(0,10,2) : 
    print(i)