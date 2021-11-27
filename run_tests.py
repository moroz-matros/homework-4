# -*- coding: utf-8 -*-

import sys
import unittest

from cases.activity.favourite_case import ActivityFavouriteTest
from cases.activity.subscription_case import ActivitySubscriptionTest
from cases.chat_cases import ChatTest
from cases.event_cases import EventTest
from cases.events_cases import EventsTest
from cases.login_cases import LoginTest
from cases.navbar_cases import NavbarTest
from cases.other_profile_cases import OtherProfileTest
from cases.profile.event_card_cases import ProfileEventCardTest
from cases.profile.good_profile_change import ProfileChangeTest
from cases.profile.good_profile_settings_change import ProfilePasswordChangeTest
from cases.profile.profile_cases import ProfileTest
from cases.registration_cases import RegistrationTest
from cases.search_cases import SearchTest
from cases.subscription_cases import SubscriptionTest


if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
             unittest.makeSuite(LoginTest),
             unittest.makeSuite(RegistrationTest),
             unittest.makeSuite(EventsTest),
             unittest.makeSuite(EventTest),
             unittest.makeSuite(SubscriptionTest),
             unittest.makeSuite(NavbarTest),
             unittest.makeSuite(SearchTest),
             unittest.makeSuite(OtherProfileTest),
             unittest.makeSuite(ChatTest),
             unittest.makeSuite(ActivitySubscriptionTest),
             unittest.makeSuite(ActivityFavouriteTest),
             unittest.makeSuite(ProfileTest),
             unittest.makeSuite(ProfileChangeTest),
             unittest.makeSuite(ProfilePasswordChangeTest),
             unittest.makeSuite(ProfileEventCardTest)
    )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())