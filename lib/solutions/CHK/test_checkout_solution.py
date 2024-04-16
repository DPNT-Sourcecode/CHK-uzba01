from .checkout_solution import checkout

def test_checkout_calculates_correct_total_prices():
    # Test checkout returns expected calculations
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
    # TODO: stop mixing and matching skus at this point and just test the individual base prices and discounts
    # this should be ok because interaction between skus shouldn't differ between cases and above cases already
    # test the interaction. But with more time we would add cases that mix and match as many combinations as possible.
    assert checkout("") == 0
    assert checkout("G") == 20
    assert checkout("H") == 10
    assert checkout("HHHHH") == 45
    assert checkout("HHHHHHHHHH") == 80
    assert checkout("I") == 35
    assert checkout("J") == 60
    assert checkout("K") == 80
    assert checkout("KK") == 120
    assert checkout("L") == 90
    assert checkout("M") == 15
    assert checkout("N") == 40
    assert checkout("NNNM") == 120
    assert checkout("O") == 10
    assert checkout("P") == 50
    assert checkout("PPPPP") == 200
    assert checkout("Q") == 30
    assert checkout("QQQ") == 80
    assert checkout("RRRQ") == 150
    assert checkout("R") == 50
    assert checkout("S") == 30
    assert checkout("T") == 20
    assert checkout("U") == 40
    assert checkout("UUUU") == 120
    assert checkout("V") == 50
    assert checkout("VV") == 90
    assert checkout("VVV") == 130




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




# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+




# Base prices no change
# K 80    | 2K for 150   -> 2K for 120
