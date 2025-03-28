#연습문제 2-1
print( 100,'+', 200 ,'=', 100 + 200 )
100 + 200 = 300
print( 200,'+', 300,'+', 400 ,'=', 200 + 300 + 400 )
200 + 300 + 400 = 900

#연습문제 2-3
width = 30
height = 60
width * height
1800

#연습문제 2-5
side = int(input('정사각형의 밑변을 입력하십시오 : '))
정사각형의 밑변을 입력하십시오 : 40
area = side ** 2
print('정사각형의 면적 :', area)
정사각형의 면적 : 1600

#연습문제 2-7
print(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)
3628800

#연습문제 2-9
print('섭씨\t화씨')
섭씨	화씨
for celsius in range(0, 51, 10): #range 끝값을 51로 해야 끝값인 50이 포함됨
    fahrenheit = (9 / 5) * celsius + 32
    print(f'{celsius}\t{fahrenheit:.1f}')

    
0	32.0
10	50.0
20	68.0
30	86.0
40	104.0
50	122.0

#연습문제 2-11
fahrenheit = float(input("화씨 온도를 입력하세요: ")) #소수점까지 알기위해 floa사용
화씨 온도를 입력하세요: 86
celsius = (5 / 9) * (fahrenheit - 32)
print(f"화씨 {fahrenheit} 도는 섭씨 {celsius:.1f} 도 입니다.")
화씨 86.0 도는 섭씨 30.0 도 입니다.

#연습문제 2-13
PI = 3.141592
radius = float(input('원의 반지름을 입력하세요: '))
원의 반지름을 입력하세요: 11
circumference = 2 * PI * radius
area = PI * radius ** 2
print(f"원의 둘레 = {circumference:.6f}, 원의 면적 = {area:.6f}")
원의 둘레 = 69.115024, 원의 면적 = 380.132632

#연습문제 2-15
a = float(input('밑변을 입력하세요: '))
밑변을 입력하세요: 5
b = float(input('높이를 입력하세요: '))
높이를 입력하세요: 12
c = (a**2 + b**2) ** 0.5

print(f"빗변: {c:.1f}")
빗변: 13.0

#연습문제 2-17
for i in range(10):
    print(2 << i, end=" ") #비트 이동 연산자 사용

    
2 4 8 16 32 64 128 256 512 1024 

#연습문제 2-19
n = int(input('정수를 입력하세요: '))
정수를 입력하세요: 120
result = (0 <= n <= 100) and (n % 2 == 0) #0~100사이, 짝수인지 확인
print(f"입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? {result}")
입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False

#연습문제 2-21
n = int(input('정수를 입력하세요: '))
정수를 입력하세요: 9
print(f"{n}의 이진수는 {bin(n)}입니다.")
9의 이진수는 0b1001입니다.
print(f"{n}의 비트단위 부정 값은 {bin(~n)}입니다.")
9의 비트단위 부정 값은 -0b1010입니다.

#연습문제 2-23
n = int(input('세 자리 정수를 입력하세요: '))
세 자리 정수를 입력하세요: 349
a = n // 100 #백의 자리 계산
b = (n % 100) // 10 #십의 자리 계산
c = n % 10 #일의 자리 계산
print(f"백의 자리: {a}, 십의 자리: {b}, 일의 자리: {c}")
백의 자리: 3, 십의 자리: 4, 일의 자리: 9


    
