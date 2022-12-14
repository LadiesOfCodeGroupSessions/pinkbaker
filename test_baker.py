from baker import cakes


def test_cakes_1():
    output = cakes({'flour': 500, 'sugar': 200, 'eggs': 1},
                   {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    assert output == 2


def test_cakes_2():
    output = cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
                   {'sugar': 500, 'flour': 2000, 'milk': 2000})
    assert output == 0

def test_cakes_3():
    output = cakes({'flour': 300, 'sugar': 150, 'milk': 100},
                   {'sugar': 500, 'flour': 2000, 'milk': 2000})
    assert output == 3

def test_cakes_4():
    output = cakes({'flour': 300, 'sugar': 150, 'milk': 100},
                   {'sugar': 100, 'flour': 100, 'milk': 50})
    assert output == 0

def test_cakes_5():
    output = cakes({'flour': 300, 'sugar': 150, 'milk': 100},
                   {})
    assert output == 0