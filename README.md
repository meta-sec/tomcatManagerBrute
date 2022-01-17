tomcat manager 后台爆破  自带默认字典  如有需求可自己加字典  

				produced by taamr

安装依赖模块

	pip install -r requirements.txt

使用

	username.txt - 用户名字典
	password.txt - 密码字典
	url.txt	- url （tomcat默认页面的url即可，不用加manager目录，url后面也不要带/，多个换行输入）

	爆破成功的账号密码会在good.txt里
	
	txt准备好后

	python3 tomcatManagerBrute.py

使用截图

	example目录截图

	