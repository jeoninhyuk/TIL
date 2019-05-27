import os

os.chdir(r'C:\Users\Administrator\PycharmProjects\190523\dummy')

for filename in os.listdir('.'):
    os.rename(filename, f'지원자_{filename}')