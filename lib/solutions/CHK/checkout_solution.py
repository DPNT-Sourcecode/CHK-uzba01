# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    a_skus = []
    b_skus = []
    c_skus = []
    d_skus = []

    for sku in skus:
        match sku:
            case "A" | "a":
                a_skus.append(sku)
            case "B" | "b":
                b_skus.append(sku)
            case "C" | "c":
                c_skus.append(sku)
            case "D" | "d":
                d_skus.append(sku)
            case _:
                pass
    
    a_total_price = calculate_total_price_of_discounted_skus(
        skus=a_skus,
        discount_group_size=3,
        discounted_group_price=130,
        base_sku_price=50
    )

    b_total_price = calculate_total_price_of_discounted_skus(
        skus=b_skus,
        discount_group_size=2,
        discounted_group_price=45,
        base_sku_price=30
    )

    c_total_price = len(c_skus) * 20

    d_total_price = len(d_skus) * 15

    return sum([a_total_price, b_total_price, c_total_price, d_total_price])


def calculate_total_price_of_discounted_skus(
    skus: list,
    discount_group_size: int,
    discounted_group_price: int,
    base_sku_price,
) -> int:
    discount_groups_count, non_discounted_items = divmod(len(skus), discount_group_size)
    return discount_groups_count * discounted_group_price + non_discounted_items * base_sku_price



