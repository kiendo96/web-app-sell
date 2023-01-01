from saleapp import app, db
from flask_admin import Admin
from saleapp.models import Category, Product
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='E-commerce Administrator', template_mode='bootstrap4')

class ProductView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    column_exclude_list = ['image', 'created_date']
    column_sortable_list = ['id', 'name', 'price']
    column_labels = {
        'id': 'STT'
    }

admin.add_views(ModelView(Category, db.session))
admin.add_views(ProductView(Product, db.session))