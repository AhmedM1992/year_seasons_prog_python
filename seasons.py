season = input("Enter month's name: ")
winter = ['January', 'February', 'December', 1, 2, 12]
spring = ['March', 'April', 'May', 3, 4, 5]
summer = ['June', 'July', 'August', 6, 7, 8]
fall = ['September', 'October', 'November', 9, 10, 11]


def seasons():
    if season in winter:
        print ("The season is Winter")
    elif season in spring:
        print ("The season is Spring")
    elif season in summer:
        print ("The season is Summer")
    elif season in fall:
        print ("The season is Fall")
    else:
        print ("Go to sleep, BOY!")
