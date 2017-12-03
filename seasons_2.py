 if month in [1, 2, 12] or month in ['January', 'February', 'December']:
        return 'winter'
    elif month in [3, 4, 5] or month in ['March', 'April', 'May']:
        return 'spring'
    elif month in [6, 7, 8] or month in ['June', 'July', 'August']:
        return 'summer'
    elif month in [9, 10, 11] or month in ['September', 'October', 'November']:
        return 'autumn'
    else:
        return 'Go to sleep, Boy!'
