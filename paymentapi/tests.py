#from django.test import TestCase
from rest_framework.test import APIClient
import json

# Create your tests here.
client = APIClient()

#Here first we create several users:
client.post('/register/',
            {'username': 'Alex', 'email': 'Alex@example.com', 'password': 'alex1234'},
            format='json')
client.post('/register/',
            json.dumps({'username': 'Sarah', 'email': 'Sarah@example.com', 'password': 'sarah_652'}),
            content_type='application/json')
client.post('/register/',
            {'username': 'Tom', 'email': 'Tom@example.com', 'password': 'robot$007'},
            format='json')


#Now time to login with available users and post some data
client.login(username='Alex', password='alex1234')

client.post('/address/',
            {'coin': 'eth', 'address': '0x0681d8db095565fe8a346fa0277bffde9c0edbbf'},
            format='json')
client.post('/address/',
            {'coin': 'eth', 'address': '0xd67723370420d8120e5f8fab19eb4d8ae473107a'},
            format='json')
client.post('/address/',
            {'coin': 'eth', 'address': '0xd67723370420d81ffe5f8fab19eb4d8ae473107a'},
            format='json')
client.post('/address/',
            {'coin': 'btc', 'address': 'bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh'},
            format='json')
client.post('/address/',
            {'coin': 'bch', 'address': '32uLhn19ZasD5bsVhLdDthhM37JhJHiEE2'},
            format='json')


client.post('/transaction/',
            {'coin': 'eth', 'hash': '0xc847f99ece4306ab665ad38bc8704241819e450c97ac89ba12b2c2fbe1f34e95'},
            format='json')
client.post('/transaction/',
            {'coin': 'eth', 'hash': '0xc847f99ece4306ab661ad38bc8704241819e450c97ac89ba12b2c2fbe1f34e95'},
            format='json')
client.post('/transaction/',
            {'coin': 'btc', 'hash': 'd41fdde6daa18204206de6afde02af18c1fa45c58470207faf3e1f6f8d7bb6a5'},
            format='json')
client.post('/transaction/',
            {'coin': 'bch', 'hash': 'a8a7fe361b7029bf036aed8950a76334db28da748b7e1be66433fd4247f834a7'},
            format='json')

client.logout()




client.login(username='Sarah', password='sarah_652')

client.post('/address/',
            {'coin': 'btc', 'address': 'bc1qn988qqrfdgmrsl2et96xx0gnrpakf2ns9w2v9s'},
            format='json')
client.post('/address/',
            {'coin': 'bch', 'address': '32uLhn19ZasD5bswdgdDthhM37JhJHiEE2'},
            format='json')


client.post('/transaction/',
            {'coin': 'eth', 'hash': '0x2847965644f82595f03f7a218c9ebd9222f80671018217aab89037ad5bcf73df'},
            format='json')
client.post('/transaction/',
            {'coin': 'eth', 'hash': '0x2847965644f82595f03f7a218c9ebd922ff80671018217aab89037ad5bcf73df'},
            format='json')

client.logout()



client.login(username='Tom', password='robot$007')

client.post('/address/',
            {'coin': 'btc', 'address': 'bc1qn988qqrfdgmrsl2et96xx0gnrpakf2ns9w2v9s'},
            format='json')


client.post('/transaction/',
            {'coin': 'eth', 'hash': '0x2847965644f82595f03f7a218c9ebd9222f80671018217aab89037ad5bcf73df'},
            format='json')

client.logout()


#Now it is time to retrieve the histroy of transactions
client.login(username='Tom', password='robot$007')

response = client.get('http://127.0.0.1:8000/address/history/')
assert response.status_code == 200
response = client.get('http://127.0.0.1:8000/transaction/history/')
assert response.status_code == 200

client.logout()
