# -!- coding: utf-8 -!-
# Main Script.

from manager import UserManager

userManager = UserManager()

# 입력받기
while True:
    print("\n1. 로그인")
    print("2. 회원 가입")
    print("3. 현재 회원 정보 출력")
    print("4. 종료")
    choice = input("동작 선택 >> ")
    
	# 로그인
    if choice == 1:
		email = raw_input("이메일 : ")
		pw = raw_input("패스워드 : ")
		loginUser = userManager.login(email, pw)
		
		if loginUser is None:
			print("로그인에 실패했습니다. 아이디 혹은 패스워드를 확인해주세요.")
		else: print("로그인 성공!")

	# 회원가입
    elif choice == 2:
		email = raw_input("이메일 : ")
		pw = raw_input("패스워드 : ")
		name = raw_input("이름 : ")
		age = input("나이 : ")
		
		userManager.register(email, pw, name, age)
		print("회원가입에 성공했습니다.")

	# 현재 회원 정보 출력
    elif choice == 3:
		if userManager.currentUser is None:
			print("로그인되어있지 않습니다. 로그인해주세요!")
		else:
			print(userManager.currentUser.getJson())

    elif choice == 4:
		userManager.logout()
		print("로그아웃 되었습니다.")

    elif choice == 5: break
