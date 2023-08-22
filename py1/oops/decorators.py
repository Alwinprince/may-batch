# """
# decoraters
# """
#
# def deco_func(f):
#     def wrapper():
#         print("b'efore")
#         f()
#         print('after')
#     return wrapper()
# @deco_func
# def f():
#     print("inside")


def upper_c(fun):
    def wrap(name):
        r=fun(name)
        return r.upper()
    return wrap

@upper_c
def h (name):
    return "hello"+name

print(h("sui"))

