from flask import Flask
import sqlite3
from flask import json,jsonify
from flask import request
from flask import make_response,abort




app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': 'order_id not found'}), 404)


@app.route('/insertmany', methods=['POST'])
def insert_row():
	inp=request.data
	tup=tuple(inp.split('&'))
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	cur.execute('''DROP TABLE IF EXISTS test123''')
	cur.execute('''CREATE TABLE test123(order_id TEXT,awb TEXT,breadth TEXT,buyer_city TEXT,buyer_pin TEXT,cancelled_date TEXT,current_status TEXT,delivered_date	TEXT,delivery_attempt_count TEXT,dispatch_date TEXT,heavy TEXT,height TEXT,last_mile_arrival_date TEXT,last_modified TEXT,length TEXT,order_created_date TEXT,price TEXT,product_category TEXT,product_id TEXT,product_name TEXT,product_price TEXT,product_qty TEXT,promised_date TEXT,return_cause TEXT,reverse_logistics_booked_date TEXT,reverse_logistics_date TEXT,reverse_logistics_delivered_date TEXT,rto_date TEXT,rto_delivered_date TEXT,seller_city TEXT,seller_pin TEXT,shipper_confirmation_date TEXT,shipper_name TEXT,shipping_cost TEXT,weight TEXT)''')
	cur.execute('''INSERT INTO test123 (order_id,awb,breadth,buyer_city,buyer_pin,cancelled_date,current_status,delivered_date,delivery_attempt_count,dispatch_date,heavy,height,last_mile_arrival_date,last_modified,length,order_created_date,price,product_category,product_id,product_name,product_price,product_qty,promised_date,return_cause,reverse_logistics_booked_date,reverse_logistics_date,reverse_logistics_delivered_date,rto_date,rto_delivered_date,seller_city,seller_pin,shipper_confirmation_date,shipper_name,shipping_cost,weight
	) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(tup))
	conn.commit()
	return ('DONE'), 201

@app.route('/insertall', methods=['POST'])
def insert_all():
	inp=request.data
	tup=tuple(inp.split('&'))
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	# cur.execute('''DROP TABLE IF EXISTS test123''')
	# cur.execute('''CREATE TABLE test123(order_id TEXT,awb TEXT,breadth TEXT,buyer_city TEXT,buyer_pin TEXT,cancelled_date TEXT,current_status TEXT,delivered_date	TEXT,delivery_attempt_count TEXT,dispatch_date TEXT,heavy TEXT,height TEXT,last_mile_arrival_date TEXT,last_modified TEXT,length TEXT,order_created_date TEXT,price TEXT,product_category TEXT,product_id TEXT,product_name TEXT,product_price TEXT,product_qty TEXT,promised_date TEXT,return_cause TEXT,reverse_logistics_booked_date TEXT,reverse_logistics_date TEXT,reverse_logistics_delivered_date TEXT,rto_date TEXT,rto_delivered_date TEXT,seller_city TEXT,seller_pin TEXT,shipper_confirmation_date TEXT,shipper_name TEXT,shipping_cost TEXT,weight TEXT)''')
	cur.execute('''INSERT INTO Data (order_id,awb,breadth,buyer_city,buyer_pin,cancelled_date,current_status,delivered_date,delivery_attempt_count,dispatch_date,heavy,height,last_mile_arrival_date,last_modified,length,order_created_date,price,product_category,product_id,product_name,product_price,product_qty,promised_date,return_cause,reverse_logistics_booked_date,reverse_logistics_date,reverse_logistics_delivered_date,rto_date,rto_delivered_date,seller_city,seller_pin,shipper_confirmation_date,shipper_name,shipping_cost,weight
	) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(tup))
	conn.commit()
	return ('DONE'), 201

@app.route('/extract_using/order_id/<string:order_id>', methods=['GET'])
def extract_row(order_id):
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	cur.execute('SELECT * FROM Data WHERE order_id=?', (order_id,))
	shipper_name=cur.fetchall()
	sh=[]
	for row in shipper_name:
		sh.append(row[32])
	conn.commit()	
	return jsonify({'shipper_name':sh}), 201

@app.route('/extract_using/seller_location/buyer_location/<string:seller_location>/<string:buyer_location>', methods=['GET'])
def extract_row1(seller_location, buyer_location):
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	cur.execute('SELECT * FROM Data WHERE seller_city= ? AND buyer_city= ?', (seller_location,buyer_location))
	shipper_name=cur.fetchall()
	sh=[]
	for row in shipper_name:
		sh.append(row[32])
	conn.commit()	
	return jsonify({'shipper_name':sh}), 201

@app.route('/extract_using/seller_location/buyer_location/product_category/<string:seller_location>/<string:buyer_location>/<string:product_category>', methods=['GET'])
def extract_row2(seller_location, buyer_location,product_category):
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	cur.execute('SELECT * FROM Data WHERE seller_city= ? AND buyer_city= ? AND product_category= ?', (seller_location,buyer_location, product_category))
	shipper_name=cur.fetchall()
	sh=[]
	for row in shipper_name:
		sh.append(row[32])
	conn.commit()	
	return jsonify({'shipper_name':sh}), 201

@app.route('/list_extract_using/order_id', methods=['GET'])
def list_extract_row():
	inp=request.data
	lst=(inp.split('&'))
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	sh=[]
	for order_id in lst:
		cur.execute('SELECT * FROM Data WHERE order_id=?', (order_id,))
		shipper_name=cur.fetchall()
		for row in shipper_name:
			sh.append(row[32])
	conn.commit()	
	print sh
	return jsonify({'shipper_name':sh}), 201

@app.route('/list_extract_using/seller_location/buyer_location', methods=['GET'])
def list_extract_row1():
	inp=request.data
	pre_lst=(inp.split('~'))
	seller_lst=(pre_lst[0].split('&'))
	buyer_lst=(pre_lst[1].split('&'))
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	sh=[]
	for seller_location in seller_lst:
		for buyer_location in buyer_lst:
			cur.execute('SELECT * FROM Data WHERE seller_city= ? AND buyer_city= ?', (seller_location,buyer_location))
			shipper_name=cur.fetchall()
			for row in shipper_name:
				sh.append(row[32])
	conn.commit()	
	print sh
	return jsonify({'shipper_name':sh}), 201

@app.route('/list_extract_using/seller_location/buyer_location/product_category', methods=['GET'])
def list_extract_row2():
	inp=request.data
	pre_lst=(inp.split('~'))
	seller_lst=(pre_lst[0].split('&'))
	buyer_lst=(pre_lst[1].split('&'))
	product_list=(pre_lst[2].split('&'))
	conn=sqlite3.connect('data.sqlite')
	cur=conn.cursor()
	sh=[]
	for seller_location in seller_lst:
		for buyer_location in buyer_lst:
			for product_category in product_list:
				cur.execute('SELECT * FROM Data WHERE seller_city= ? AND buyer_city= ? AND product_category= ?', (seller_location,buyer_location, product_category))
				shipper_name=cur.fetchall()
				for row in shipper_name:
					sh.append(row[32])
	conn.commit()	
	print sh
	return jsonify({'shipper_name':sh}), 201

if __name__=='__main__':
	app.run(debug=True, port=5000)
