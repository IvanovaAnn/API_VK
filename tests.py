import unittest
import api_vk


class Test(unittest.TestCase):
    """
    This is test
    """
    def test_1(self):
        """
        This is test change output user's first_name
        """
        token = '919b9690919b9690919b9690d891e9de319919b919b9690cf4a8ee7082f3c81851ec434'
        version = 5.92
        user_ids = 148629147
        data, data_friends = api_vk.ApiVk.request(token, version, user_ids)
        self.assertTrue(data['first_name'], "Anya")

    def test_2(self):
        """
        This is test change output user's last_name
        """
        token = '919b9690919b9690919b9690d891e9de319919b919b9690cf4a8ee7082f3c81851ec434'
        version = 5.92
        user_ids = 148629147
        data, data_friends = api_vk.ApiVk.request(token, version, user_ids)
        self.assertTrue(data['last_name'], "Ivanova")

    def test_3(self):
        """
        This is test change output user's first friend
        """
        token = '919b9690919b9690919b9690d891e9de319919b919b9690cf4a8ee7082f3c81851ec434'
        version = 5.92
        user_ids = 148629147
        data, data_friends = api_vk.ApiVk.request(token, version, user_ids)
        api_vk.ApiVk.proceccing_request(data_friends)
        one_friend = ""
        with open('id.csv', 'r') as file:
            text = file.readlines()
            one_friend = text[2][:-1]
        self.assertTrue(one_friend, "481541,Ilya,Savinov")
