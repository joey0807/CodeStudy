n = input() #숫자 입력

octal = '0o'+n #입력받은 숫자 앞에 0o를 붙이면 8진수 형태가 됨
ten = int(octal,8) #8진수를 10진수로 변경
binary = bin(ten) #변경한 10진수를 2진수로 변경

print(binary[2:]) #2진수를 나타내는 0b 제거 후 출력