# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a_skus = []
    b_skus = []
    c_skus = []
    d_skus = []

    for sku in skus:
        match sku:
            case "A":
                a_skus.append(sku)
            case "B":
                b_skus.append(sku)
            case "C":
                c_skus.append(sku)
            case "D":
                d_skus.append(sku)
            case _:
                raise ValueError(f"Invalid SKU: {sku}")
    
    discount_groups_count, non_discounted_items = divmod(len(a_skus), 3)
    a_total_price = discount_groups_count * 130 + non_discounted_items * 50

    discount_groups_count, non_discounted_items = divmod(len(b_skus), 2)
    b_total_price = discount_groups_count * 45 + non_discounted_items * 30

    c_total_price = len(c_skus) * 20

    d_total_price = len(d_skus) * 15

    return a_total_price + b_total_price + c_total_price + d_total_price


def calculate_total_price_of_discounted_skus(skus)
