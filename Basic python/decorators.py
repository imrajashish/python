#dewrating strings
'''def decorfun(fun):
    def inner(n):
        result=fun(n)
        result="How are you"
        return result
    return inner
    @decorfun
    def hello(name):
        return "hello "+name
        print(hello(" as"))'''
#@decorator
def decorfun(fun):
    def inner():
        result=fun()
        return result*2
    return inner
@decor
def num():
    return 5
print(num())