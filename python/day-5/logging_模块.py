'''
昨日志用的



'''


import logging

logging.basicConfig(filename='test-logger2' , level=logging.INFO , format='%(asctime)s - %(message)s - %(levelname)s')




logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')




'''
import logging

logger = logging.getLogger('sam-test')
logger.setLevel(logging.DEBUG)


ch = logging.StreamHandler()         #创建一个屏幕输出对象
ch.setLevel(logging.DEBUG)


fh = logging.FileHandler('test-logger')        #创建一个文件输出对象
fh.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')        #创建一个格式

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)




logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
'''