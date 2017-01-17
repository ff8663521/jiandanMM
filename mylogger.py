import logging

#日志系统， 既要把日志输出到控制台， 还要写入日志文件   
class MyLogger():
	def __init__(self,loglevel,logger):
		'''
		指定日志级别，以及调用文件
		日志自动记录与log文件夹下，以年月日为文件名进行记录
		'''
		#输出格式字典
		format_dict = {
			1 : '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
			2 : '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
			3 : '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
			4 : '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s',
			5 : '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s'
		}

		# 创建一个logger
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		# 创建一个handler，用于写入日志文件
		fh = logging.FileHandler('log/access.log')
		fh.setLevel(logging.DEBUG)

		# 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		# 定义handler的输出格式

		formatter =logging.Formatter(format_dict[int(loglevel)]) 
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		# 给logger添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)


	def getlog(self):
		return self.logger
