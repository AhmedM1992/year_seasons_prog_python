season = input("Enter month's name: ")
winter = ['January', 'February', 'December']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
fall = ['September', 'October', 'November']
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
