# -!- coding: utf-8 -!-

from store import UserStore
from user import User

class UserManager:
	def __init__(self):
		self.users = UserStore()
		self.currentUser = None

	# 로그인
	def login(self, email, pw):
		user = self.users.find(email, pw)
		if user:
			self.currentUser = user
		return user

	
	# 회원가입
	def register(self, email, pw, name, age):
		newUser = User(email, pw, name, age)
		self.users.add(newUser)
		self.currentUser = newUser

	# 로그아웃	
	def logout(self):
		self.currentUser = None
