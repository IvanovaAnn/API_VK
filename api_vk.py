import requests
import csv


class ApiVk:
    @staticmethod
    def request(token, version, user_ids):
        response = requests.get('https://api.vk.com/method/users.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'user_ids': user_ids,
                                    'fields': 'photo_id,city,verified, counters'
                                },
                                )
        friends = requests.get('https://api.vk.com/method/friends.get',
                               params={
                                   'access_token': token,
                                   'v': version,
                                   'user_id': user_ids,
                                   'fields': 'verified'
                               },
                               )
        data = response.json()['response'][0]
        data_friends = friends.json()['response']['items']
        return data, data_friends

    @staticmethod
    def proceccing_request(data_friends):
        with open('id.csv', 'w') as file:
            a_pen = csv.writer(file)
            a_pen.writerow(('id', 'first_name', 'last_name'))
            for i in data_friends:
                if i['last_name']:
                    a_pen.writerow((i['id'], i['first_name'],i['last_name']))


if __name__ == '__main__':
    token = '919b9690919b9690919b9690d891e9de319919b919b9690cf4a8ee7082f3c81851ec434'
    version = 5.92
    user_ids = input()
    Api = ApiVk()
    data, data_friends = Api.request(token, version, user_ids)
    Api.proceccing_request(data_friends)
    print(data['id'], data['first_name'], data['last_name'])
