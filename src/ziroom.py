#!/usr/bin/env python3

import time
import config
import random
import pymysql
import telegram
import requests_html

bot = telegram.Bot(token=config.token)

def main():
	with pymysql.connect(host=config.db_host, user=config.db_user, passwd=config.db_passwd, db=config.db_name) as cursor:
		
		keywords = ['世华龙樾', '莱圳家园']
			
		for keyword in keywords:
			print('keyword: ' + keyword)
			
			page = 1
			url = 'http://www.ziroom.com/z/nl/z3.html?qwd=%s' % (keyword)
			
			try:
				while True:
					print('[' + str(page) + ']')
					
					session = requests_html.HTMLSession()
					html = session.get(url).html
					
					if html.text.find('我们找不到任何') >= 0:
						print('')
						break
					
					l = html.find('#houseList', first=True)
					
					for house in l.find('li'):
						t = house.find('.t1', first=True)
						title = t.text
						link = t.absolute_links.pop()
						
						print(title)
						
						sql = 'SELECT * FROM ziroom WHERE link = %s'
						cursor.execute(sql, (link))
						result = cursor.fetchone()
						
						if not result:
							try:
								print('sending to telegram...')
								
								text = '%s\n%s' % (title, link)
								bot.send_message(config.admin_chat_id, text)
								
								sql = 'INSERT INTO ziroom (title, link) VALUES (%s, %s)'
								cursor.execute(sql, (title, link))
							except Exception as error:
								print(error)
																				
					time.sleep(random.uniform(0, 5))
						
					next = html.text.find('下一页')
									
					if next >= 0:
						page += 1
						url += '&p=%d' % (page)
					else:
						print('')
						break
			except Exception as error:
				print(error)
	
if __name__ == '__main__':
	main()
