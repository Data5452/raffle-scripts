import requests
from random import getrandbits
url = 'http://dtlrlaunch.com/adidas-yeezy-boost-350-v2-white/'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

#fill in the things
def main(limit):
    for i in range(1, limit):
        email = 'youremail+{}@gmail.com'.format(getrandbits(40)) #change youremail to youremail do not change anything after
        payload = {
                        'email' : email,
                        'first_name' : '', #first name
                        'last_name' : '', #last name
                        'birth_month' : '', #birth month in 01 format
                        'birth_date' : '', #birth date in 01 format
                        'shoe_size' : '', # US shoe size like 9 or 9.5
                        'phone_number' : '', # no space like 1234567890
                        'billing_address' : '', #only ship and bill to this address ex: 121 Smith Ave
                        'address_line_2' : '', #if you don't have don't fill
                        'city' : '', #city you live in
                        'state' : '', #fill out full name of state ex: New York do not use NY
                        'postal/zip_code' : '', #zip code
                        'country' : '164', #default USA change 164 if you are in the UK replace 164 with 262
                        'mce-group[149]' : '[1]' #leave it be
                }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
