"""
This module provides classes for testing User object
"""

import unittest

from codeforces import User


class UserTests(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_load_from_dict(self):
        d = {
            "handle": "DmitriyH",
            "email": "secret@email.com",
            "vkId": "12345",
            "openId": "wow, open id!",
            "firstName": "Dmitriy",
            "lastName": "Khodyrev",
            "country": "Russia",
            "city": "Moscow",
            "organization": "KL",
            "contribution": 144,
            "rank": "candidate master",
            "rating": 1799,
            "maxRank": "master",
            "maxRating": 1947,
            "lastOnlineTimeSeconds": 1408612436,
            "registrationTimeSeconds": 1268570311,
            "friendOfCount": 85,
            "titlePhoto":"//userpic.codeforces.com/1592/title/27e43714e4bea090.jpg",
            "avatar":"//userpic.codeforces.com/1592/avatar/7cef566902732053.jpg"
        }

        self.user.load_from_dict(d)

        self.assertEqual("DmitriyH", self.user.handle)
        self.assertEqual("secret@email.com", self.user.email)
        self.assertEqual("12345", self.user.vk_id)
        self.assertEqual("wow, open id!", self.user.open_id)
        self.assertEqual("Dmitriy", self.user.first_name)
        self.assertEqual("Khodyrev", self.user.last_name)
        self.assertEqual("Russia", self.user.country)
        self.assertEqual("Moscow", self.user.city)
        self.assertEqual("KL", self.user.organization)
        self.assertEqual(144, self.user.contribution)
        self.assertEqual("candidate master", self.user.rank)
        self.assertEqual(1799, self.user.rating)
        self.assertEqual("master", self.user.max_rank)
        self.assertEqual(1947, self.user.max_rating)
        self.assertEqual(1408612436, self.user.last_online_time)
        self.assertEqual(1268570311, self.user.registration_time)
        self.assertEqual(85, self.user.friend_of_count)
        self.assertEqual("//userpic.codeforces.com/1592/title/27e43714e4bea090.jpg", self.user.title_photo)
        self.assertEqual("//userpic.codeforces.com/1592/avatar/7cef566902732053.jpg", self.user.avatar)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:

            handle
            contribution
            lastOnlineTimeSeconds
            registrationTimeSeconds
        """
        d = {
            "handle": "DmitriyH",
            "contribution": 144,
            "lastOnlineTimeSeconds": 1408612436,
            "registrationTimeSeconds": 1268570311
        }

        self.user.load_from_dict(d)

        self.assertEqual("DmitriyH", self.user.handle)
        self.assertEqual(144, self.user.contribution)
        self.assertEqual(1408612436, self.user.last_online_time)
        self.assertEqual(1268570311, self.user.registration_time)

        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.vk_id)
        self.assertIsNone(self.user.open_id)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)
        self.assertIsNone(self.user.country)
        self.assertIsNone(self.user.city)
        self.assertIsNone(self.user.organization)
        self.assertIsNone(self.user.rank)
        self.assertIsNone(self.user.max_rank)
        self.assertIsNone(self.user.friend_of_count)
        self.assertIsNone(self.user.title_photo)
        self.assertIsNone(self.user.avatar)

        self.assertEqual(0, self.user.rating)
        self.assertEqual(0, self.user.max_rating)

    def test_load_from_json(self):
        json = '''{
            "handle": "DmitriyH",
            "email": "secret@email.com",
            "vkId": "12345",
            "openId": "wow, open id!",
            "firstName": "Dmitriy",
            "lastName": "Khodyrev",
            "country": "Russia",
            "city": "Moscow",
            "organization": "KL",
            "contribution": 144,
            "rank": "candidate master",
            "rating": 1799,
            "maxRank": "master",
            "maxRating": 1947,
            "lastOnlineTimeSeconds": 1408612436,
            "registrationTimeSeconds": 1268570311,
            "friendOfCount": 85,
            "titlePhoto":"//userpic.codeforces.com/1592/title/27e43714e4bea090.jpg",
            "avatar":"//userpic.codeforces.com/1592/avatar/7cef566902732053.jpg"
        }'''

        self.user.load_from_json(json)

        self.assertEqual("DmitriyH", self.user.handle)
        self.assertEqual("secret@email.com", self.user.email)
        self.assertEqual("12345", self.user.vk_id)
        self.assertEqual("wow, open id!", self.user.open_id)
        self.assertEqual("Dmitriy", self.user.first_name)
        self.assertEqual("Khodyrev", self.user.last_name)
        self.assertEqual("Russia", self.user.country)
        self.assertEqual("Moscow", self.user.city)
        self.assertEqual("KL", self.user.organization)
        self.assertEqual(144, self.user.contribution)
        self.assertEqual("candidate master", self.user.rank)
        self.assertEqual(1799, self.user.rating)
        self.assertEqual("master", self.user.max_rank)
        self.assertEqual(1947, self.user.max_rating)
        self.assertEqual(1408612436, self.user.last_online_time)
        self.assertEqual(1268570311, self.user.registration_time)
        self.assertEqual(85, self.user.friend_of_count)
        self.assertEqual("//userpic.codeforces.com/1592/title/27e43714e4bea090.jpg", self.user.title_photo)
        self.assertEqual("//userpic.codeforces.com/1592/avatar/7cef566902732053.jpg", self.user.avatar)

    def test_load_only_required_from_json(self):
        """
        Required fields are:

            handle
            contribution
            lastOnlineTimeSeconds
            registrationTimeSeconds
        """
        json = '''{
            "handle": "DmitriyH",
            "contribution": 144,
            "lastOnlineTimeSeconds": 1408612436,
            "registrationTimeSeconds": 1268570311
        }'''

        self.user.load_from_json(json)

        self.assertEqual("DmitriyH", self.user.handle)
        self.assertEqual(144, self.user.contribution)
        self.assertEqual(1408612436, self.user.last_online_time)
        self.assertEqual(1268570311, self.user.registration_time)

        self.assertIsNone(self.user.email)
        self.assertIsNone(self.user.vk_id)
        self.assertIsNone(self.user.open_id)
        self.assertIsNone(self.user.first_name)
        self.assertIsNone(self.user.last_name)
        self.assertIsNone(self.user.country)
        self.assertIsNone(self.user.city)
        self.assertIsNone(self.user.organization)
        self.assertIsNone(self.user.rank)
        self.assertIsNone(self.user.max_rank)
        self.assertIsNone(self.user.friend_of_count)
        self.assertIsNone(self.user.title_photo)
        self.assertIsNone(self.user.avatar)

        self.assertEqual(0, self.user.rating)
        self.assertEqual(0, self.user.max_rating)


if __name__ == '__main__':
    unittest.main()
