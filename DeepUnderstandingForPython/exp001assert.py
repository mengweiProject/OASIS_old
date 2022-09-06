'''
@Project ：OASIS 
@Author  ：孟威
@Date    ：2022/7/21 9:59 
'''


def get_discounted_price(price, discount):
    """
    获取商品折后价
    :param price:
    :param discount:
    :return:
    """
    discounted_price = price * discount
    assert 0 <= discounted_price <= price
    return discounted_price

if __name__ == '__main__':
    price = 100
    discount = 1.1
    print(get_discounted_price(price, discount))
