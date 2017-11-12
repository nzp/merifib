import json
import types

import pytest

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

        with pytest.raises(ValueError):
            # F(281) with a couple of randomly changed digits.
            f = Fibonacci(seed=23770696554372451866815101394984845481039225387896643963981)

        with pytest.raises(ValueError):
            # For negative numbers.
            f = Fibonacci(seed=-8)

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
        test_json = {
            "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            "sum": 88,
            "evens": 4,
            "odds": 6
        }

        f = Fibonacci(10)
        try:
            decoded_result_json = json.loads(f.json())
        except json.JSONDecodeError:
            assert False

        assert decoded_result_json == test_json

        f = Fibonacci()
        with pytest.raises(ValueError):
            f.json()
