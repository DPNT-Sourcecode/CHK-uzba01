# noinspection PyUnusedLocal
# skus = unicode string
# def checkout(skus):

#     a_skus = []
#     b_skus = []
#     c_skus = []
#     d_skus = []

#     try:
#         for sku in skus:
#             match sku:
#                 case "A":
#                     a_skus.append(sku)
#                 case "B":
#                     b_skus.append(sku)
#                 case "C":
#                     c_skus.append(sku)
#                 case "D":
#                     d_skus.append(sku)
#                 case _:
#                     return -1
#     except TypeError:
#         return -1
    
#     a_total_price = calculate_total_price_of_discounted_skus(
#         skus=a_skus,
#         discount_group_size=3,
#         discounted_group_price=130,
#         base_sku_price=50
#     )

#     b_total_price = calculate_total_price_of_discounted_skus(
#         skus=b_skus,
#         discount_group_size=2,
#         discounted_group_price=45,
#         base_sku_price=30
#     )

#     c_total_price = len(c_skus) * 20

#     d_total_price = len(d_skus) * 15

#     return sum([a_total_price, b_total_price, c_total_price, d_total_price])


# def calculate_total_price_of_discounted_skus(
#     skus: list,
#     discount_group_size: int,
#     discounted_group_price: int,
#     base_sku_price,
# ) -> int:
#     discount_groups_count, non_discounted_items = divmod(len(skus), discount_group_size)
#     return discount_groups_count * discounted_group_price + non_discounted_items * base_sku_price




def checkout(skus):
    skus_to_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

    skus_to_prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    skus_to_discounts = {"A": (3, 130), "B": (2, 45)}  # (discount_group_size, discounted_group_price)

    try:
        # Count SKUs
        for sku in skus:
            if sku in skus_to_counts:
                skus_to_counts[sku] += 1
            else:
                return -1  # Invalid SKU
    except TypeError:
        return -1

    # Calculate total price
    total_price = 0
    for sku, count in skus_to_counts.items():
        total_price += calculate_total_price(count, skus_to_prices[sku], skus_to_discounts.get(sku))

    return total_price


def calculate_total_price(count, price, discount):
    if discount:
        discount_group_size, discounted_group_price = discount
        discount_groups_count, non_discounted_items = divmod(count, discount_group_size)
        return discount_groups_count * discounted_group_price + non_discounted_items * price
    else:
        return count * price




