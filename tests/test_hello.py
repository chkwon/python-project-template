from mypypackage import hello

def test_hello():
    assert hello(3) == 4
    assert hello(10) == 11
    
def test_hello_loop():
    for i in range(100):
        assert hello(i) == i + 1