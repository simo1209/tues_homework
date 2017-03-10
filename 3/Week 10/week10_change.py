def split_change(change):
    if change>=0:
        x=change//5
        y=(change-x*5)//2
        z=(change-(x*5+y*2))//1
        print(x, "* 5")
        print(y, "* 2")
        print(z, "* 1")
    else:
        print("Please, input a \"real\" number for change!") 

change=int(input("Input your change here:"))
split_change(change)
