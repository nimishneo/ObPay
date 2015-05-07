__author__ = 'nimish'

import falcon
import json
from datetime import datetime

'''
Example 

{
'iin': '637812',
'bin': '00',
'sponsor': '01',
'account': '7992739'
} 

9 + 3 + 5 + 2 + 9 + 9 + 5 = 42 check = 10-2 = 8

'''

#  ALGORITHM DIRECTLY TAKEN FROM WIKIPEDIA http://en.wikipedia.org/wiki/Luhn_algorithm

class LuhnAlgorithm(object):

    def calculate_luhn(self,partial_card_number):
        def luhn_checksum(card_number):
            def digits_of(n):
                return [int(d) for d in str(n)]  
            digits = digits_of(card_number)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = 0
            checksum += sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d*2))
            return checksum % 10
        check_digit = luhn_checksum(int(partial_card_number) * 10)
        return check_digit if check_digit == 0 else 10 - check_digit

class GenAccNo(object):

    def calculateAccountNumber(self,partial_card_number):
        Luhnobj = LuhnAlgorithm()
        ans = Luhnobj.calculate_luhn(partial_card_number)
        return str(partial_card_number)+str(ans)

class GenResource(object):
    
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = 'Luhn Application'
 
    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Error',
                ex.message)
 
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
            data = {}
            accountNo = result_json["account"]
            iinNo = result_json["iin"]
            binNo = result_json["bin"]
            sponsor = result_json["sponsor"]
            objGenAccNo = GenAccNo()
            newAccountNo = objGenAccNo.calculateAccountNumber(accountNo)
            data["cardnumber"] = str(iinNo)+" "+str(binNo)+str(sponsor)+" "+str(newAccountNo[:4])+" "+str(newAccountNo[4:])
            data["datetime_generated"] = str(datetime.utcnow())
        
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_202
        resp.body = json.dumps(data, encoding='utf-8')
 
wsgi_app = api = falcon.API()
resObject = GenResource()
 
# resObject will handle all requests to the '/v1.0/utilities/luhn' URL path
api.add_route('/v1.0/utilities/luhn', resObject)

