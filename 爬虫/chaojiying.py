from yzmfengzhuang import Chaojiying_Client


if __name__ == '__main__':
	chaojiying = Chaojiying_Client('nnothingp', '12345678', '914767')	#用户中心>>软件ID 生成一个替换 96001
	im = open('C://Users//18230//Desktop//captcha.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
	print(chaojiying.PostPic(im, 3004))											#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

