def print_triangle(angle):
    space = angle-1
    star = 1
    for i in range(angle):
        if i == 0:
            print((" "*space)+"*")
        elif i != angle-1:
            print((" "*space)+"*"+(" "*(star-2))+"*"+(" "*space))
        else:
            star= int(star/2)+1
            print(("* "*space)+"* "+("* "*(star-2))+"*"+("* "*space))
        space-=1
        star+=2

print_triangle(10)
