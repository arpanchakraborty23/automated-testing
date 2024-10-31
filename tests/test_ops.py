from src.math_op import add,sub

def test_add():
    assert add(2,5)== 7
    assert add(-1,1) ==0

def test_sub():
    assert sub(5,3)==2
    assert sub(30,20)==10