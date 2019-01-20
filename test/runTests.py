import unittest

from test.commands import test_WuxiaScraper
from test.gmail import test_Email


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_WuxiaScraper.TestWuxia('test_wuxia_title'))
    test_suite.addTest(test_WuxiaScraper.TestWuxia('test_wuxia_body'))
    test_suite.addTest(test_Email.TestEmail('test_email'))
    return test_suite


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
