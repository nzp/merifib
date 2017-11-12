import types

from merifib.fibonacci import Fibonacci


class TestFibonacci:

    def test_init(self):
        f = Fibonacci()
        assert f.seed == 0
        assert f.length == None

        f = Fibonacci(10, 13)
        assert f.length == 10
        assert f.seed == 13

        f = Fibonacci(seed=8, length=15)
        assert f.length == 15
        assert f.seed == 8

    def test_sequence(self):
        test_seq1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        f = Fibonacci(10)
        assert f.sequence() == test_seq1

        test_seq2 = [55, 89, 144, 233, 377, 610]
        f = Fibonacci(length=6, seed=55)
        assert f.sequence() == test_seq2

        f = Fibonacci()
        tmp = []
        genseq = f.sequence()

        assert type(genseq) == types.GeneratorType

        while len(tmp) < 10:
            tmp.append(next(genseq))
        assert tmp == test_seq1

        f = Fibonacci(seed=55)
        tmp = []
        genseq = f.sequence()

        assert type(genseq) == types.GeneratorType

        while len(tmp) < 6:
            tmp.append(next(genseq))
        assert tmp == test_seq2

    def test_nth(self):
        f = Fibonacci()

        # 499th
        assert f.nth(500) == 86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501

    def test_json(self):
        pass
