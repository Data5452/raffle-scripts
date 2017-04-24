import requests
from random import getrandbits
url = 'https://www.boutique1.com/competition/yeezy'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

#CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit):
        email = 'youremail+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
                        'First_name' : '', #first name here 
                        'Surname' : '', #last name here
                        'Email' : email,
                        'Moblie' : '', #phone number like this 1234567890 no spaces
                        'Shoe_Size' : '' #not sure if its US or UK sizing find out and fill like this 9 or 9.5
                   }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)

                        
