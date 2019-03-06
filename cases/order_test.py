import unittest


class TestOrder(unittest.TestCase):
    def setUp(self):
        print "set up ...."

    def tearDown(self):
        print "tear down ..."

    def test_1(self):
        print "test_1"
        self.assertEqual(1, 1, "not success")

    def test_2(self):
        print "test_2"
        self.assertIs(1, 2, "failed")