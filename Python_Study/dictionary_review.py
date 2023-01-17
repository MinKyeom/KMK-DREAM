#딕션너리 선언하기
dict_a={"name": "어밴저스 엔드게임",
        "type": "히어로 무비"
        }

print(dict_a["name"])

#딕션너리에 접근하기
dictionary ={
        "name": "7D 건조망고",
        "type": "당절임",
        "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
        "origin":"필리핀"
}

#출력
print("name",dictionary["name"])
print("ingredient",dictionary["ingredient"])
print()

#값 변경하기
dictionary["name"]="8D 망고"
print("name",dictionary["name"])

#값 추가하기
dictionary["price"]=5000
print(dictionary)

#값 제거하기

del dictionary["ingredient"]

print(dictionary)

#딕션너리에 요소 추가하기
dictionary_1={}
#요소 추가하기 전
print("요소 추가하기 전:",dictionary_1)
#요소 추가하기
dictionary_1["name"]="새로운 이름"

print("요소 추가 이후:",dictionary_1)

#딕션너리 요소 제거하기

dictionary_2={"name":"7D 망고","type":"당절임"}
print("요소 제거이전",dictionary_2)

del dictionary_2["name"]

print("제거 이후:",dictionary_2)