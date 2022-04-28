def buy_milk(money=0):
    product = '[milk]'
    price = 25

    if money >= price:
        return product * int(money / price)
    else:
        return None


def buy_bread(money=0):
    product = '[bread]'
    price = 19

    if money / price > 3:
        return product * 3
    elif money / price >= 1:
        return product * int(money / price)
    else:
        return None
