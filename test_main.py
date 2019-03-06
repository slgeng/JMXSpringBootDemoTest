import unittest


class TestMatch(unittest.TestCase):
    def setUp(self):
        print "set up ...."

    def tearDown(self):
        print "tear down ..."

    def test_1(self):
        print "test_1"
        self.assertEqual(1, 1, "not success")

    def test_2(self):
        print "test_2"
        self.assertIs(1, 1, "failed")


if __name__ == '__main__':
    unittest.main()
