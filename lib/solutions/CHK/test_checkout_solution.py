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
    assert checkout("ABCDABCD") == 215
    assert checkout("AAABCCBBDAA") == 330
    assert checkout("E") == 40
    assert checkout("EE") == 80
    assert checkout("AAEABCCEBBDAA") == 380
    assert checkout("AAEABCCEBBDAAAA") == 480
    assert checkout("AAEABCCEBBDAAAAA") == 510
    assert checkout("EEB") == 80
    assert checkout("EEEB") == 120
    assert checkout("EEEEBB") == 160
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("AAABCCBBDAAFF") == 350
    assert checkout("AAABCCBBDAAFFF") == 350



    ### Test illegal inputs return -1
    assert checkout("a") == -1
    assert checkout("b") == -1
    assert checkout("c") == -1
    assert checkout("d") == -1
    assert checkout("Aa") == -1
    assert checkout("Bb") == -1
    assert checkout("Cc") == -1
    assert checkout("dD") == -1
    assert checkout("aAa") == -1
    assert checkout("qwertyuiop") == -1
    assert checkout(1) == -1
    assert checkout(None) == -1
    assert checkout([]) == -1


