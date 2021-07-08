#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from fire import Fire
from smtplib import SMTP
from pathlib import Path
from random import choice
from collections import namedtuple
from email.message import EmailMessage


SMTP_INFO = namedtuple(
    "CREDENTIALS", ["SMTP_SERVER", "SMTP_PORT", "SMTP_LOGIN", "SMTP_PASSWORD"]
)(
    os.getenv("SMTP_SERVER"),
    os.getenv("SMTP_PORT"),
    os.getenv("SMTP_LOGIN"),
    os.getenv("SMTP_PASSWORD"),
)


def random_quote():
    with open(Path('../quotes.txt'), "r") as quotes:
        lines = [line for line in quotes if line != ""]
    return choice(lines)


def create_email(to_mail):
    msg = EmailMessage()
    msg["From"] = SMTP_INFO.SMTP_LOGIN
    msg["To"] = to_mail
    msg["Subject"] = "Inspirational Quote Of The Day!"
    msg.set_content(random_quote())
    return msg


def send_email(to_mail=None):
    if to_mail == None:
        raise TypeError("Usage python email_sender <email address>")
    session = SMTP(SMTP_INFO.SMTP_SERVER, SMTP_INFO.SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(SMTP_INFO.SMTP_LOGIN, SMTP_INFO.SMTP_PASSWORD)
    session.send_message(create_email(to_mail))
    session.quit()


if __name__ == "__main__":
    Fire(send_email)



###############################3
###############################
###############################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import unittest
from unittest import TestCase
from unittest.mock import patch
from collections import namedtuple
from email_sender import (
    send_email,
    create_email,
    EmailMessage,
    SMTP,
)


class TestEmailSender(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.smtp_info_patcher = patch(
            "email_sender.SMTP_INFO",
            namedtuple(
                "CREDENTIALS",
                ["SMTP_SERVER", "SMTP_PORT", "SMTP_LOGIN", "SMTP_PASSWORD"],
            )(
                "test@localhost",
                "1025",
                "test.from@mail.com",
                "xyzJKLmonPqR57",
            ),
        )
        cls.smtp_info_patcher.start()

    @patch('email_sender.SMTP')
    def test_send_email_with_with_email(self, smtplib_mock):
        send_email('test.to@mail.com')
        smtplib_mock.assert_called_once()
        smtplib_mock.called_with("test@localhost", "1025")

    def test_send_mail_with_without_email(self):
        with self.assertRaises(TypeError):
            send_email()

    def test_email_body(self):
        email_message = create_email("test.to@mail.com")
        email_body = email_message.get_content().strip("\n")
        assert re.match(r"^\".+\" \- .+$", email_body)

    def test_email_headers(self):
        email_message = create_email("test.to@mail.com")
        email_headers = dict(email_message.items())
        self.assertEqual(
            email_headers["To"], "test.to@mail.com", "To mail address not correct"
        )
        self.assertEqual(
            email_headers["From"], "test.from@mail.com", "From mail address not correct"
        )
        self.assertEqual(
            email_headers["Subject"],
            "Inspirational Quote Of The Day!",
            "Subject not correct",
        )

    @patch("email_sender.create_email", return_value=EmailMessage())
    @patch("email_sender.SMTP")
    @patch("email_sender.SMTP.send_message")
    def test_send_mail(self, mail_mock, smtplib_mock, send_message_mock):
        send_email("test.to@mail.com")
        send_message_mock.called_with(mail_mock)

    @classmethod
    def tearDownClass(cls):
        cls.smtp_info_patcher.stop()

if __name__ == "__main__":
    unittest.main()
