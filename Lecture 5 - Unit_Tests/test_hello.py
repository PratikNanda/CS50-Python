from hello import hello

def test_default():
    assert hello() == "hello, World"

def test_argument():
    assert hello("David") == "hello, David"

# ---------test using loop---------
# def test_inloop():
#     for name in ["Kusal", "Perera", "Shanaka"]:
#         assert hello(name) == f"hello, {name}"
