# noinspection PyUnusedLocal
# skus = unicode string
# def checkout(skus):
#     skus_to_counts = {"A": 0, "B": 0, "C": 0, "D": 0}

#     skus_to_prices = {"A": 50, "B": 30, "C": 20, "D": 15}
#     skus_to_discounts = {"A": (3, 130), "B": (2, 45)}

#     try:
#         for sku in skus:
#             if sku in skus_to_counts:
#                 skus_to_counts[sku] += 1
#             else:
#                 return -1 # We could alternatively raise ValueError(f"Invalid SKU {sku}")
#     except TypeError:
#         return -1

#     total_price = 0
#     for sku, count in skus_to_counts.items():
#         total_price += calculate_total_price(count, skus_to_prices[sku], skus_to_discounts.get(sku))

#     return total_price


# def calculate_total_price(count, price, discount):
#     if discount:
#         discount_group_size, discounted_group_price = discount
#         discount_groups_count, non_discounted_items = divmod(count, discount_group_size)
#         return discount_groups_count * discounted_group_price + non_discounted_items * price
#     else:
#         return count * price

from typing import Optional, List


def checkout(skus):
    skus_to_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    skus_to_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    skus_to_discounts = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}

    try:
        for sku in skus:
            if sku in skus_to_counts:
                skus_to_counts[sku] += 1
            else:
                return -1  # TODO: We could alternatively raise ValueError(f"Invalid SKU {sku}")
    except TypeError:
        return -1

    total_price = 0
    for sku, count in skus_to_counts.items():
        total_price += calculate_total_price(
            count=count,
            price=skus_to_prices[sku],
            discounts=skus_to_discounts.get(sku, None)
        )

    return total_price


def calculate_total_price(count: int, price: int, discounts: Optional[List]):
    total = 0
    if discounts:
        for discount in sorted(discounts, reverse=True):
            discount_group_size, discounted_group_price = discount
            groups, count = divmod(count, discount_group_size)
            total += groups * discounted_group_price
    total += count * price
    return total
