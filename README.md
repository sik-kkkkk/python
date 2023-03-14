# python


## 자료형
#### 숫자형
* 정수 : 123, -20, 0  
* 실수 : 123.45, -4321.5, 6.08e9  
* 8진수 : 0o456, 0o123  
* 16진수 : 0xFF, 0x0D0, 0x0A

#### 변수
* 문자 또는 밑줄로 시작(beta, _kim)
* 대소문자를 구분한다.(sum, Sum, SUM)
* 영문자, 숫자, 밑줄(A-z,0-9,_)
* 파이썬 키워드는 사용 불가

```
a = 10
b = 20
c = a + b
d = b - a

print(c,d)
```
```
a = 10
b = 2
# 나눗셈
c = a/b # 나눗셈
d = a//b # 몫을 구하는 나눗셈
e = a%b # 나머지만 구하는 나눗셈
# 곱셈
f = a*b
g = a**b # 제곱 # b는 a의 제곱근

print(c,d,e,f,g)
```

#### 문자열
1. 큰 따옴표 : "Hello World"  
2. 작은 따옴표 : 대한민국'  
3. 큰 따옴표 3 : """Hello!"""
4. 작은 따옴표 3 : '''Life is too short, You need python'''

#### 여러개 변수 할당
```
x,y,z = "포도", "딸기", "수박"
print(x)
print(y)
print(z)
```
```
a= b = c = "오렌지"
print(a)
print(b)
print(c)
```
```
fruits = ["포도", "딸기", "수박"]
x,y,z = fruits
print(x)
print(y)
print(z)
```
```
x = "Life"
y = "is"
z = "Beautiful"
print(x,y,z) # 공백이 생긴다.
print(x+y+z) # 공백 없이 붙어서 생긴다.
```
```
a = 1
b = 2
c = 3
print(a,b,c)
print(a+b+c)
```

#### 데이터 할당
+ 텍스트
+ 숫자
+ 불(bool)
```
a = 10
b = 20
sum = a + b
result = a * b
result2 = a - b
result3 = a/b
result4 = a**b
print(a, '+', b, '=', sum)
print(a, '*', b, '=', result)
print(a, '-', b, '=', result2)
print(a, '/', b, '=', result3)
print(a, '**', b, '=', result4)
```
