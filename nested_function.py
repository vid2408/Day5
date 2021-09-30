def outerfunc(text):
    def innerfunc():
        print(text)
    innerfunc()

outerfunc("hello")