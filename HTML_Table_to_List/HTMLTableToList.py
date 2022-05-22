from bs4 import BeautifulSoup

class HTMLTableToList():

	def __init__(self, table_html):
		self.table_html = table_html

	def get_list(self):
		list_of_list = []
		soup = BeautifulSoup(self.table_html,"lxml")
		table = soup.find('table')
		all_tr = table.findAll('tr')
		for tr in all_tr:
			all_th  = tr.findAll('th')
			all_td  = tr.findAll('td')
			current_row = [th.text for th in all_th]
			current_row.extend(td.text for td in all_td)
			list_of_list.append(current_row)
		return list_of_list