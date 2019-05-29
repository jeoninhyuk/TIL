def hello(func):
        print('hihi')
        func()
        print('hihi')

@hello
def bye():
    print('bye bye')

bye()