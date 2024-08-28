import requests

class Github:
    def __init__(self):
        self.url = 'https://api.github.com'
    def findUser(self,username):
        response = requests.get(self.url+'/users/'+username)
        return response.json()
    def getRepos(self,username):
        response = requests.get(self.url+'/users/'+username+'/repos')
        return response.json()

github = Github()

while True:
    secim = input('1- Find user\n2- Get repos\n3- Exit\nSecimin: ')
    if secim == '3':
        break
    elif secim == '1':
        secim = input(f'{20*'-'}\n1- Standart secenek\n2- Gelismis secenek\n\nSecimin: ')
        if secim == '1':
            username = input('\nUsername: ')
            result = github.findUser(username)
            print(f'{55*'-'}\nName: {result['name']} - Public repos: {result['public_repos']} - Followers: {result['followers']}\n{55*'-'}')
        elif secim == '2':
            username = input('\nUsername: ')
            result = github.findUser(username)
            print(f'{55*'-'}\nName: {result['name']} - Public repos: {result['public_repos']} - Followers: {result['followers']}')
            print(f'Id: {result['id']} - Type: {result['type']} - Following: {result['following']}')
            print(f'Url address: {result['url']} - Created: {result['created_at']} - NodeId: {result['node_id']}\n{55*'-'}')
        else:
             print('------------\nHatali secim\n------------')
    elif secim == '2':
        username = input('\nUsername: ')
        result = github.getRepos(username)
        for repo in result:
            print(f'{35*'-'}\n{repo['name']}')
        print(f'{35*'-'}\n')
    else:
        print('------------\nHatali secim\n------------')