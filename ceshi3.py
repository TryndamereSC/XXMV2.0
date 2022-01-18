import pytest

@pytest.fixture(scope="function")
def start():
    print("\n-----开始执行function------")

@pytest.mark.usefixtures("start")
def test_a():
    print("------用例a执行------")

@pytest.mark.usefixtures("start")
class Test_aaa():
    def test_01(self):
        print("------用例01-------")

    def test_02(self):
        print("------用例02-------")

class Test_aaaa():
    def test_001(self):
        a = 1
        b = 2
        assert a == b

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_the_unknown(self):
        print(1)

if __name__ == '__main__':
    pytest.main(["-s","ceshi3.py"])