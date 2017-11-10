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
