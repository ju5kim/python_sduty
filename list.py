    
    
"""
    eng 변수, kor 변수, math 변수를 만들고
    각 변수는 과목의 시험 점수이다.
    영어 점수는 80점
    국어 점수는 60
    수학 점수는 50
    3과목의 평균을 구하고
    평균 점수에 따라
    A = 91~100
    B =81~90
    C = 71~80
    D =61~70
    F = 60
    
"""



#eng = input("영어 점수 입력 =");
#kor = input("국어 점수 입력 =");
#math = input("수학 점수 입력 =");

# jumsu= list();
# jumsu.append(int(eng));
# jumsu.append(int(kor));
# jumsu.append(int(math));
# total = 0;
# level = "";

# for i in jumsu : 
#    total+=i
   
# avgjumsu = total/len(jumsu)
# if(avgjumsu >90) :
#     level = "A"    
# elif(avgjumsu >80):
#     level = "B"
# elif(avgjumsu>70):
#     level = "C"
# elif(avgjumsu>60):
#     level = "D"
# else: level="F"

# print("합계 = "+str(total))
# print("평균 = "+str(avgjumsu))
# print("평점 = "+str(level))

# 10진 소수점을 2진수 소수점으로 변환하는 과정에서 소수점이 이상하게 나온다.
# 하드웨어의 부동 소수점 산술을 지원하는 모든 언어에서 같은 에러가 나온다.
print(0.1+1.1 == 1.2)
print(1.1+0.3)
print(0.1+0.1)


#리스트
print("리스트에서 슬라이스와 pop의 리턴값 차이\n")
my = list()
mylist=[1,20,9,4,10]
print(mylist[0:1]) #리턴 값은 리스트
print(mylist[0]) # 리턴 값은 들어있는 값
print("*************************")
print("*************************")
#객체 복사
print("객체복사\n")
print("*************************")
# 얕은 복사 
print("얕은복사 \n")#값 변경시 같이 변경됨
my =mylist 
my.insert(0,10)
print(my)
print(mylist)

print("*************************")
#깊은 복사 방법
import copy
print("깊은복사\n") # import copy 필요 copy.deepcopy()
my = copy.deepcopy(mylist)
my.insert(0,5)
print(my)
print(mylist)

print("*************************")
#기타
print("기타\n")
#리무브, 팝, 인덱스
print(mylist.remove(10)) #매개변수는 리스트 객체 = 리턴 값은 none
print(mylist.pop(0)) # 매개변수는 인덱스값 =  리턴은 객체, 리스트에서 제외됨
print(mylist)

#객체로 인덱스 찾기
print(mylist.index(20)) # 해당 객체가 없으면 에러 있다면 인덱스 번호 리턴
print(mylist.__contains__(10))# 해당 객체가 있으면 True, 없다면 False
print(mylist.count("a")) # 매개변수 객체가 해당 컬렉션에 몇개 있는지 세는 함수

print(mylist.__len__()) #이거 __len__하고 괄호안하면 0 리턴함 

#정렬, 랜덤정렬, 역정렬
mylist.sort()
# mylist.sort(key=len)  이건 문자열만 가능
mylist.sort(reverse=True)

#뒤집기
# 뒤집기와 역정렬은 다르다.
mylist.reverse()


#중복값 제거
print("*************************")
print("**리스트의 중복제거")
data = [1010,2020,3030,1010,2020,3030,4040]

print("*1")
dupleremoved = list(set(data))
print(dupleremoved)
print("*2")
dupleremoved = list(dict.fromkeys(data))
print(dupleremoved)

print("*3")
dupleremoved = sorted(set(data))
print(dupleremoved)

print("*4")
dupleremoved = [('홍길동', 25, 145), ('김시습', 45, 155), ('장보고', 48, 163), ('장길산', 40, 165), ('이순신', 52, 185)]
#2중 구조의 경우 사용가능 
#2중 구조에서 첫번째 인자인 이름으로 정렬
dupleremoved = sorted(set(dupleremoved),key=lambda x : x[0]) 
print(dupleremoved)
#2중 구조에서 두번째 인자인 나이로 정렬
dupleremoved = sorted(set(dupleremoved),key=lambda x : x[1]) 
print(dupleremoved)
# 역순으로 정렬하기  -를 붙이면 된다.
dupleremoved = sorted(set(dupleremoved),key=lambda x : -x[1]) 
print(dupleremoved)

#리스트의 문자열을 합친다.
" ".join(dupleremoved)
print(" 구분자 ".join(dupleremoved))

 #sum()
 #리스트의 요소를 모두 더한다.
numberlist = [1,2,3,3,4]
avg = sum(numberlist)






