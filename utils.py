import json
from saleapp import app
from saleapp.models import Category, Product

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    return Category.query.all()
    # return read_json(os.path.join(app.root_path, 'data/categories.json')) //read from jsonfile

def load_products(cat_id=None, kw=None, from_price=None, to_price=None, page=1):
    # prod = Product.query.all()
    prod = Product.query.filter(Product.active.__eq__(True))
    if cat_id:
        prod = prod.filter(Product.category_id.__eq__(cat_id))
    if kw:
        prod = prod.filter(Product.name.contains(kw))
    if from_price:
        prod = prod.filter(Product.price.__ge__(from_price))
    if to_price:
        prod = prod.filter(Product.price.__le__(to_price))
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size
    #select * from product limit 4 offset 0 //Query in sql
    return prod.slice(start, end).all()
    # prod = read_json(os.path.join(app.root_path, 'data/products.json'))
    # if cat_id:
    #     prod = [p for p in prod if p['category_id'] == int(cat_id) ]
    #
    # if kw:
    #     prod = [p for p in prod if p['name'].lower().find(kw.lower()) >= 0]
    #
    # if from_price:
    #     prod = [p for p in prod if p['price'] >= float(from_price)]
    #
    # if to_price:
    #     prod = [p for p in prod if p['price'] <= float(to_price)]
    # return prod

def count_product():
    return Product.query.filter(Product.active.__eq__(True)).count()

def get_product_by_id(product_id):
    return Product.query.get(product_id)
    # prod = read_json(os.path.join(app.root_path, 'data/products.json'))
    # for p in prod:
    #     if p['id'] == product_id:
    #         return p
    # return None