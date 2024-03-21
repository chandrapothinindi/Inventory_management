from flask import Flask, request, jsonify, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

db_host = 'localhost'
db_user = 'root'
db_password = 'Priyachandra@95'
db_name = 'inventory'

db = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = db.cursor()

def execute_select_query(query):
    cursor.execute(query)
    return cursor.fetchall()

def execute_query(query, data=None):
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    db.commit()

@app.route('/')
def index():
    select_query = "SELECT * FROM inventory_products"
    products = execute_select_query(select_query)

    return render_template('index.html', products=products)

@app.route('/add_product')
def add_product():
    return render_template('add_product.html')

@app.route('/save_product', methods=['POST'])
def save_product():
    name = request.form.get('name')
    desc = request.form.get('desc')
    count = request.form.get('count')

    insert_query = "INSERT INTO inventory_products (product_name, product_desc, product_count) VALUES (%s, %s, %s)"
    execute_query(insert_query, (name, desc, count))

    return redirect(url_for('index'))

@app.route('/update_product/<int:product_id>', methods=['GET'])
def get_update_product(product_id):

    select_query = "SELECT * FROM inventory_products WHERE product_id = %s"
    cursor.execute(select_query, (product_id,))
    product = cursor.fetchone()

    return render_template('update_product.html', product_id=product_id, product=product)

@app.route('/update_product', methods=['POST'])
def update_product():
    product_id = request.form.get('product_id')
    name = request.form.get('name')
    desc = request.form.get('desc')
    count = request.form.get('count')

    update_query = "UPDATE inventory_products SET product_name = %s, product_desc = %s, product_count = %s WHERE product_id = %s"
    execute_query(update_query, (name, desc, count, product_id))

    return redirect(url_for('index'))

@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
        # Delete the product from the database
        delete_query = "DELETE FROM inventory_products WHERE product_id = %s"
        execute_query(delete_query, (product_id,))
        return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
