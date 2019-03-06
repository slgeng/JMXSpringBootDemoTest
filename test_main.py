# coding=utf-8
import unittest
import HtmlTestRunner
import os

# 用例路径
case_path = os.path.join(os.getcwd(), "cases")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*.py", top_level_dir=None)
    return discover


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(all_case())
    runner = HtmlTestRunner.HTMLTestRunner(output='')
    runner.run(suite)
