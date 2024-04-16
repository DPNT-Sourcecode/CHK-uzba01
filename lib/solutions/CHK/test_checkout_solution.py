from .checkout_solution import checkout

def test_checkout_calculates_correct_total_prices():
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("AA") == 100
    assert checkout("BB") == 45
    assert checkout("CC") == 40
    assert checkout("DD") == 30
    assert checkout("AAA") == 130
    assert checkout("BBB") == 75
    assert checkout("CCC") == 60
    assert checkout("DDD") == 45
    assert checkout("ABCD") == 115
    assert checkout("ABCDABCD") == 230
    assert checkout("AAABBBCCCDDD") == 290
    assert checkout("AAABBBCCCDDDAAABBBCCCDDD") == 580
    assert checkout("AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD") == 870
    assert checkout("AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD") == 1160
    assert checkout("AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD") == 1450
    assert checkout("AAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDDAAABBBCCCDDD") == 1740