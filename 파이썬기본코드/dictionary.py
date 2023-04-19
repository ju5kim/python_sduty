#딕셔너리 = map

#딕셔너리의 다양한 선언
dic1 = dict()
{"이름" : "홍길동", "나이":18}
dic2 = {}
newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)

# 딕셔너리로 형변환하기
# 2차원 리스트 => dic
name_and_ages = [['alice', 5], ['Bob', 13]]
# 키 벨류 형태로 되어 있어야 변환가능
# name_and_ages = [['alice', 5], ['Bob', 13],["weqwe",19,20]]
name_and_ages=dict(name_and_ages)
print(name_and_ages)
#리스트 내부 듀플 -> dic
name_and_ages = [('alice', 5), ('Bob', 13)]
name_and_ages=dict(name_and_ages)
print(name_and_ages)
#튜플 내부 듀플 -> dic
name_and_ages = (('alice', 5), ('Bob', 13))
name_and_ages=dict(name_and_ages)
print(name_and_ages)
#튜플 내부 리스트 -> dic
name_and_ages = (['alice', 5], ['Bob', 13])
name_and_ages= dict(name_and_ages)
print()
print("*********************")
#이중 딕셔너리
print("**이중 딕셔너리")
dic2 = {"a":{"ab":10}, "b":{"bc":20}}
print(dic2)
print(dic2["b"])
print(dic2["b"]["bc"])
print("*********************")
#딕셔너리에 값 추가
print("**딕셔너리 값 추가")
dic1 = {1:'a'}
print(dic1)
dic1['b'] = 2
print(dic1)
print("*********************")
#딕셔너리 값 삭제
print("**딕셔너리 값 삭제")
del dic1[1]
print(dic1)
print("*********************")

#딕셔너리 값과 키 추출
print("*딕셔너리 값과 키 추출")
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items()) ##for 문에서 key와 value를 한번에 사용하려면 items() 메서드 사용
dic2.get("키값")
print(dic2.get("키값"))
print(dic2.get("키값","Default 출력 값 (키가 없는 경우 None 값인 경우)"))
print("*********************")



     





