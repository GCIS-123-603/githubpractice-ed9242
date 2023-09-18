def add (x,y):
    return x+y

def test():
    result = add(2,3)
    assert result == 7

def square_area(x):
    return x**2



 
def test_square_area_8():
    area = square_area(8)
    assert (area == 64)
    

test_square_area_8()


