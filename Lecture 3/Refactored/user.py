# -!- coding: utf-8 -!-
import json

class User:
    def __init__(self, email, pw, name, age):
        self.email = email
        self.pw    = pw
        self.name  = name
        self.age   = age

    # 패스워드를 제외한 회원 정보를 JSON 문자열로 반환한다.        
    def getJson(self):
        data = {
            'email': self.email,
            'name': self.name,
            'age': self.age
        }
        return json.dumps(data)
 