# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a_sku_items = []
    b_sku_items = []
    c_sku_items = []
    d_sku_items = []

    for sku in skus:
        match sku:
            case "A":
                a_sku_items.append(sku)
            case "B":
                b_sku_items.append(sku)
            case "C":
                c_sku_items.append(sku)
            case "D":
                d_sku_items.append(sku)
            case _:
                pass
    
    discount_groups_count, non_discounted_items = divmod(len(a_sku_items), 3)
    a_total_price = discount_groups_count * 130 + non_discounted_items * 50

    discount_groups_count, non_discounted_items = divmod(len(b_sku_items), 2)
    b_total_price = discount_groups_count * 45 + non_discounted_items * 30

    c_total_price = len(c_sku_items) * 20

    d_total_price = len(d_sku_items) * 15

    return a_total_price + b_total_price + c_total_price + d_total_price
