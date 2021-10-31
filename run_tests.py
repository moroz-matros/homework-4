# -*- coding: utf-8 -*-

import sys
import unittest

from cases.events_cases import EventsTest
from cases.login_cases import LoginTest
from cases.registration_cases import RegistrationTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
        #unittest.makeSuite(LoginTest),
        #unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(EventsTest)
    )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())