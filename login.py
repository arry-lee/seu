# -*- code:utf-8 -*-
from bs4 import BeautifulSoup
from requests import get,post,Session
from base64 import b64encode

"""
用于解析东南大学登录网页的加密算法，以及登录web服务
经http://tool.oschina.net/encrypt?type=3分析，密码采用的是BASE64加密
"""

def seu_login(username,password):
	"""
	登录东南大学网络接入认证系统
	return True 登录成功 False 登录失败
	"""
	username = str(username)
	password = base64_encode(password)
	
	url = "https://w.seu.edu.cn/index.php/index/login"
	headers = {"User-Agent": "Mozilla/5.0 (compatible, MSIE 9.0, Windows NT 6.1, Trident/5.0)"}
	data = {
		'username': username,
		'password': password,
		'enablemacauth': 0
	}

	resp = post(url, headers=headers, data=data)
	# print(resp)
	# print(resp.text)

	return '"status":1' in resp.text


def base64_encode(password):
	p = b64encode(bytes(password, "utf-8"))
	p = str(p)[2:-1]
	return p




def try_login(fresh_file):
	# from random import choice
	with open(fresh_file) as f:
		for line in f:
			# line = choice(f.readlines())
			username,password = line.strip().split(',')
			login = seu_login(username,password)
			if not login:
				continue
			if login:
				break


if __name__ == '__main__':
	a = seu_login('yourid','password')
	print(a)

