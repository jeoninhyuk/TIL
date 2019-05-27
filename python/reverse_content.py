"""
다음과 같은 내용의 파일 mulcam.txt가있다.
with open('mulcam.txt', 'w') as f:
    f.writelines(['1\n', '2\n', '3\n'])

1
2
3

이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

3
2
1



"""
with open('mulcam.txt', 'w') as f:
    f.writelines(['3\n', '2\n', '1\n'])
# 1, read file
with open('mulcam.txt', 'r') as f:
    lines = f.readlines() # list
# 2. reverse
lines.reverse()
# 3. write file
with open('mulcam.txt', 'w') as f:
    f.writelines(lines)

#for
for i in range(10):
    print(i)

print(i)
