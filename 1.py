from flask import Flask, request, jsonify

app=Flask(__name__)

orders = []
searchedorder = []

@app.route('/')
def index():
	return 'hello, kajju'

@app.route('/addorder',methods=['POST'])
def addorder():
	name = request.json['name']
	qty = request.json['qty']
	cost = request.json['cost']

	order={'name':name, 'quantity':qty, 'cost':cost}
	orders.append(order)

	return jsonify({'order':'placed'})

@app.route('/showorders' ,methods=['GET'])
def showdb():
	return jsonify({'totalorders': orders})

@app.route('/searchorder', methods=['GET'])
def search():
	ordername = request.args['name']
	searchedorder= []
	for i in orders:
		if(i['name']==ordername and i['quantity']>=50 and i['cost']==100):
			searchedorder.append(i)
	return jsonify({'searchedorders': searchedorder}),201

@app.route('/deleteorder', methods=['DELETE'])
def deleteorders():
	#ordername = request.json['name']  how???????
	for i in orders:
		if(i['quantity']>=50 and i['cost']==100):
			orders.remove(i)
	return jsonify({'leftorders': orders}),201

if __name__ == '__main__':
	app.run(port=5000, debug=True, use_reloader=True)