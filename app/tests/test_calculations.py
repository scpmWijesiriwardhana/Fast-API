from app.calculations import add

def test_add():
    sum = add(5, 8)
    assert sum == 13