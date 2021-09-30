def outerfunc(text):
    def innerfunc():
        print(text)
    return innerfunc

a = outerfunc("hello")
del outerfunc
a()