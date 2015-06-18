#-!- coding: utf-8 -!-

import json
from user import User

users = []
currentUser = None

def login():
    email = raw_input("이메일 입력 : ")
    pw = raw_input("패스워드 입력 : ")

    # 일치하는 회원 찾기
    for user in users:
        if user.email == email and user.pw == pw:
            # 현재 유저에 저장
            global currentUser
            currentUser = user

            print ("로그인 되었습니다!")            
            return
    
    # 못찾음 ㅜㅜ
    print ("로그인에 실패했습니다! 아이디 혹은 패스워드를 확인해주세요.")
    return

def register():
    email = raw_input("이메일 입력 : ")
    pw = raw_input("패스워드 입력 : ")
    name = raw_input("이름 입력 : ")
    age = raw_input("나이 입력 : ")
    
    # 새로운 유저 만들어서 users 배열에 추가
    newUser = User(email, pw, name, age)
    users.append(newUser)

    # 현재 유저에 저장
    global currentUser
    currentUser = newUser
    
    print ("회원가입이 완료되었습니다!")
    

def printUserJson(user):
    data = {
        "email": user.email,
        "name": user.name,
        "age": user.age
    }
    print(json.dumps(data))

def logout():
    global currentUser
    currentUser = None
    print("정상적으로 로그아웃 되었습니다.")

# 입력받기
while True:
    print("\n1. 로그인")
    print("2. 회원 가입")
    print("3. 현재 회원 정보 출력")
    print("4. 로그아웃")
    print("5. 종료")
    choice = input("동작 선택 >> ")
    
    if choice == 1: login()
    elif choice == 2: register()
    elif choice == 3:
        if currentUser == None:
            print("로그인되어있지 않습니다.")
        else:
            printUserJson(currentUser)

    elif choice == 4: logout()
    elif choice == 5: break