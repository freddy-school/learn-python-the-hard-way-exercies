def test(*args):
    i = -1
    argss = args
    for args in args:
        args = str(args) + "more stuff"   
        print(args)
        argss = str(argss) + str(args)
    print(argss)



# test(1,2,3,4,5,6,7,8,9,0,"we","sadfasdf?k")

i = 1; i = i+1;print(i)
