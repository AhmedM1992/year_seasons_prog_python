season = input("Enter month's name: ")
lst_1 = ['January', 'February', 'December']
lst_2 = ['March', 'April', 'May']
lst_3 = ['June', 'July', 'August']
lst_4 = ['September', 'October', 'November']
if season in lst_1:
    print ("The season is Winter")
elif season in lst_2:
    print ("The season is Spring")
elif season in lst_3:
    print ("The season is Summer")
elif season in lst_4:
    print ("The season is Fall")
else:
    print ("Go to sleep, BOY!")
