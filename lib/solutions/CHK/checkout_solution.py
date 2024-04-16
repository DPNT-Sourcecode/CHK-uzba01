# noinspection PyUnusedLocal
# skus = unicode string
from typing import Optional, List


def checkout(skus):
    skus_to_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    skus_to_base_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    skus_to_discounts = {
        "A": [
            {"discount_group_size": 5, "discounted_price": 200},
            {"discount_group_size": 3, "discounted_price": 130}
        ],
        "B": [{"discount_group_size": 2, "discounted_price": 45}]
    }
   
    try:
        for sku in skus:
            if sku in skus_to_counts:
                skus_to_counts[sku] += 1
            else:
                return -1
    except TypeError:
        return -1
    
    skus_to_counts["B"] = max(0, skus_to_counts["B"] - skus_to_counts["E"] // 2)

    total_price = 0
    for sku, sku_count in skus_to_counts.items():
        total_price += calculate_total_price(
            sku_count=sku_count,
            price=skus_to_base_prices[sku],
            discounts=skus_to_discounts.get(sku, None)
        )

    return total_price


def calculate_total_price(sku_count: int, price: int, discounts: Optional[List]):
    total = 0
    if discounts:
        for discount in sorted(discounts, key=lambda x: x['discount_group_size'], reverse=True):
            groups, sku_count = divmod(sku_count, discount["discount_group_size"])
            total += groups * discount["discounted_price"]
    total += sku_count * price
    return total



