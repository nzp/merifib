from merifib.fibonacci import Fibonacci


class TestFibonacci:

    def test_init(self):
        f = Fibonacci()
        assert f.initial == 0

        f = Fibonacci(13)
        assert f.initial == 13

    def test_sequence(self):
        test_seq1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        f = Fibonacci()

        assert f.sequence(10) == test_seq1

        test_seq2 = [55, 89, 144, 233, 377, 610]
        f = Fibonacci(55)

        assert f.sequence(6) == test_seq2

    def test_nth(self):
        f = Fibonacci()

        # 499th
        assert f.nth(500) == 86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501
