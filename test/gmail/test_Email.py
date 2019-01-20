import os
import unittest

from gmail import ReadEmail
from gmail import SendEmail


class TestEmail(unittest.TestCase):
    def setUp(self):
        self.email_address = os.environ['EMAIL_ADDRESS']
        self.password = os.environ['PASSWORD']
        self.read_server = ReadEmail.login(self.email_address, self.password)
        self.send_server = SendEmail.login(self.email_address, self.password)

    def test_email(self):
        SendEmail.send_email(self.send_server, self.email_address, self.email_address, "SUBJECT", "BODY")
        self.read_server.select('INBOX')
        messages = ReadEmail.get_email_content(self.read_server, "(UNSEEN)")
        self.assertTrue(len(messages) > 0, "No message delivered!")
        self.assertEqual(messages[0].address, self.email_address, "FROM_EMAIL_ADDRESS WRONG")
        self.assertEqual(messages[0].name.strip(), "", "NAME WRONG")
        self.assertEqual(messages[0].subject, "SUBJECT", "SUBJECT WRONG")
        self.assertEqual(messages[0].content, "BODY\r\n", "EMAIL_BODY WRONG")

    def tearDown(self):
        self.read_server.close()
        self.send_server.close()


if __name__ == "__main__":
    unittest.main()
