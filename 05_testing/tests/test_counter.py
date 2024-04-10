import unittest
import src.counter as cnt


class TestConstructor(unittest.TestCase):

    def test_constructor_default(self):
        c = cnt.Counter()
        self.assertEqual(c.get_count(), 0)
        self.assertEqual(c.get_step(), 1)

    def test_constructor_params(self):
        c = cnt.Counter(start_count=10, step=3)
        self.assertEqual(c.get_count(), 10)
        self.assertEqual(c.get_step(), 3)


class TestIncrement(unittest.TestCase):

    def setUp(self):
        self._counter = cnt.Counter(start_count=11, step=3)

    def test_increment(self):
        self._counter.increment()
        self.assertTrue(self._counter.get_count(), 14)

    def test_multiple_increment(self):
        self._counter.increment()
        self._counter.increment()
        self.assertTrue(self._counter.get_count(), 17)


class TestRepresentation(unittest.TestCase):

    def setUp(self):
        self._counter = cnt.Counter(start_count=1, step=3)

    def test_set_step(self):
        self._counter.set_step(2)
        self.assertEqual(self._counter.get_step(), 2)

    def test_set_increment(self):
        self._counter.set_step(2)
        self._counter.increment()
        self.assertEqual(self._counter.get_count(), 3)

    def test_reset_default(self):
        self._counter.reset()
        self.assertEqual(self._counter.get_count(), 0)
        self.assertEqual(self._counter.get_step(), 1)

    def test_reset_default(self):
        self._counter.reset(start_count=45, step=32)
        self.assertEqual(self._counter.get_count(), 45)
        self.assertEqual(self._counter.get_step(), 32)


class TestSetters(unittest.TestCase):

    def setUp(self):
        self._counter1 = cnt.Counter(start_count=23, step=14)
        self._counter2 = cnt.Counter(start_count=17, step=13)

    def test_str(self):
        self.assertEqual(str(self._counter1), "23")

    def test_lt_true(self):
        self.assertTrue(self._counter2 < self._counter1)

    def test_lt_true(self):
        self.assertFalse(self._counter1 < self._counter2)


class TestEdgeCases(unittest.TestCase):

    def test_negative_count(self):
        c1 = cnt.Counter(start_count=-1, step=2)
        c1.increment()
        self.assertEqual(c1.get_count(), 1)

    def test_negative_step(self):
        c1 = cnt.Counter(start_count=1, step=-2)
        c1.increment()
        self.assertEqual(c1.get_count(), -1)

    def test_zero_step(self):
        c1 = cnt.Counter(start_count=1, step= 0)
        c1.increment()
        self.assertEqual(c1.get_count(), 1)

    def test_equal(self):
        c1 = cnt.Counter(start_count=1, step=0)
        c2 = cnt.Counter(start_count=1, step=0)
        self.assertFalse(c1 < c2)







