import requests
import sqlite3
import csv

def multiple_rows(start_row, end_row):
	with open('C:\Users\\rishil\Desktop\data.csv') as cs:
		next(cs)
		reader=csv.reader(cs)
		mycsv=list(reader)
		while True:
			if start_row<=end_row:
				query=('&'.join(mycsv[start_row]))
				start_row+=1
				requests.post('http://localhost:5000/insertmany', data=query)
				continue
			else:
				break


def row_by_row():
	with open('C:\Users\\rishil\Desktop\data.csv') as cs:
		next(cs)
		reader=csv.reader(cs)
		for data in reader:
			ordered_data=data[15:16]+data[:15]+data[16:]
			# print len(ordered_data)
			query=('&'.join(ordered_data))
			requests.post('http://localhost:5000/insertall', data=query)


def extract_using_order_id(order_id):
	requests.get('http://localhost:5000/extract_using/order_id/'+order_id)

# extract_using_order_id('32979dfb-b651-4134-8179-615651979998')

def extract_using_seller_buyer(seller_location, buyer_location):
	requests.get('http://localhost:5000/extract_using/seller_location/buyer_location/'+seller_location+'/'+buyer_location)


def extract_using_seller_buyer_product(seller_location, buyer_location,product_category):
	requests.get('http://localhost:5000/extract_using/seller_location/buyer_location/product_category/'+seller_location+'/'+buyer_location+'/'+product_category)


def list_extract_using_order_id(order_id_list):
	query=('&'.join(order_id_list))
	requests.get('http://localhost:5000/list_extract_using/order_id', data=query)

# order_id_list=['3efdcab7-8ff4-45f6-8084-b6c7938e63d3','d37c437c-0e3e-4d8c-9815-f36cfb2ad037']

def list_extract_using_seller_buyer_list(seller_list, buyer_list):
	seller_list.append('~')
	ls=seller_list+buyer_list
	query=('&'.join(ls))
	requests.get('http://localhost:5000/list_extract_using/seller_location/buyer_location',data=query)


def list_extract_using_seller_buyer_product_list(seller_list, buyer_list,product_category):
	seller_list.append('~')
	ls=seller_list+buyer_list
	ls.append('~')
	new_ls=ls+product_category
	query=('&'.join(new_ls))
	requests.get('http://localhost:5000/list_extract_using/seller_location/buyer_location/product_category',data=query)

# buyer_list=['Rohanport','East Tamraville']
# seller_list=['South Arthur','Ivonnestad']
# product_category=['Tablets','Tablets']




# with open('C:\Users\\rishil\Desktop\data.csv') as cs:
# 	reader=csv.DictReader(cs)
# 	for row in reader:
# 		requests.post('http://localhost:5000/insert', json=row)

