from src.mathop import add,sub

def test_add():
    assert add(2,3)==5
    assert add(3,1)==4

def test_sub():
    assert sub(2,1)==1
    assert sub(5,2)==3