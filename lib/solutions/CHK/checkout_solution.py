# noinspection PyUnusedLocal
# skus = unicode string
from typing import Optional, List


def checkout(skus):
    skus_to_counts = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}

    skus_to_base_prices = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35, 
        "J": 60, "K": 70, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50, 
        "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21
    }

    group_discount_for_s_t_x_y_z = [{"discount_group_size": 3, "discounted_price": 45}]

    skus_to_discounts = {
        "A": [
            {"discount_group_size": 5, "discounted_price": 200},
            {"discount_group_size": 3, "discounted_price": 130}
        ],
        "B": [{"discount_group_size": 2, "discounted_price": 45}],
        "H": [
            {"discount_group_size": 5, "discounted_price": 45},
            {"discount_group_size": 10, "discounted_price": 80}
        ],
        "K": [{"discount_group_size": 2, "discounted_price": 120}],
        "P": [{"discount_group_size": 5, "discounted_price": 200}],
        "Q": [{"discount_group_size": 3, "discounted_price": 80}],
        "V": [
            {"discount_group_size": 3, "discounted_price": 130},
            {"discount_group_size": 2, "discounted_price": 90}
        ],
        **{sku: group_discount_for_s_t_x_y_z for sku in "STXYZ"}
    }
   

    try:
        for sku in skus:
            if sku in skus_to_counts:
                skus_to_counts[sku] += 1
            else:
                return -1
    except TypeError:
        return -1

    # Remove free skus from sku counts
    skus_to_counts["B"] = max(0, skus_to_counts["B"] - skus_to_counts["E"] // 2)
    skus_to_counts["F"] = max(0, skus_to_counts["F"] - skus_to_counts["F"] // 3)
    skus_to_counts["M"] = max(0, skus_to_counts["M"] - skus_to_counts["N"] // 3)
    skus_to_counts["Q"] = max(0, skus_to_counts["Q"] - skus_to_counts["R"] // 3)
    skus_to_counts["U"] = max(0, skus_to_counts["U"] - skus_to_counts["U"] // 4)

    total_price = 0

    for sku, sku_count in skus_to_counts.items():
        if sku not in "STXYZ":
            total_price += calculate_total_price(
                sku_count=sku_count,
                price=skus_to_base_prices[sku],
                discounts=skus_to_discounts.get(sku, None)
            )

    # now calculate the price for skus in STXYZ
    s_t_x_y_z_skus = [sku for sku in skus if sku in "STXYZ"]
    num_groups, remainder = divmod(len(s_t_x_y_z_skus), 3)
    if remainder:
        skus_with_base_price = s_t_x_y_z_skus[-remainder:]
        total_price += sum(skus_to_base_prices[sku] for sku in skus_with_base_price)

    total_price += num_groups * 45

    return total_price


def calculate_total_price(sku_count: int, price: int, discounts: Optional[List]):
    total = 0
    if discounts:
        for discount in sorted(discounts, key=lambda x: x['discount_group_size'], reverse=True):
            groups, sku_count = divmod(sku_count, discount["discount_group_size"])
            total += groups * discount["discounted_price"]
    total += sku_count * price
    return total

