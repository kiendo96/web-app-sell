import math

from saleapp import app
from flask import render_template, request
from saleapp.admin import *
import utils

@app.route("/")
def home():
    cat = utils.load_categories()
    cat_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    page = request.args.get('page', 1)
    prod = utils.load_products(cat_id=cat_id, kw=kw, page=int(page))
    counter = utils.count_product()
    return render_template('index.html',
                           categories=cat,
                           products=prod,
                           pages=math.ceil(counter/app.config['PAGE_SIZE']))
@app.route("/register", methods=['GET', 'POST'])
def user_register():
    return render_template('register.html')


@app.route("/products")
def product_list():
    cat_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    prod = utils.load_products(cat_id=cat_id, kw=kw, from_price=from_price, to_price=to_price)
    return render_template('products.html', products=prod)

@app.route("/products/<int:product_id>")
def get_product_id(product_id):
    prod = utils.get_product_by_id(product_id)
    return render_template('product_detail.html', product=prod)

if __name__ == '__main__':
    app.run(debug=True)