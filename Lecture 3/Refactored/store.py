# -!- coding: utf-8 -!-
from user import User

class UserStore:
	def __init__(self):
		self.users = []
	
	# 새로운 유저를 추가한다.
	def add(self, user):
		self.users.append(user)
	
	# 해당 이메일과 패스워드를 가진 유저를 찾는다.
	def find(self, email, pw):
		for user in self.users:
			if user.email == email and user.pw == pw:
				return user

		# Not Found
		return None
