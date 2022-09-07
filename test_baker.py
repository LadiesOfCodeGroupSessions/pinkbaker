from baker import cakes

def test_cakes():
    #output = cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    output = cakes ( 500, 1200)
    assert output == 'You can make a cake'