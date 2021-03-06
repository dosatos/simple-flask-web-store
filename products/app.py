# ============== #
#  Products App  #
# ============== #

from flask import Blueprint, render_template

from web.database import init_db
from web.database import db_session
from products.models import Product


products_app = Blueprint("products_app", __name__,
                         template_folder="./templates",
                         static_folder="./static",
                         static_url_path='/products/static')
init_db()


@products_app.route("/", methods=["GET"])
def show_products():
    products = Product.query.all()
    tempalte_path = "products/products.html"
    context = {
        "products": products,
        "products_page": True,
    }
    return render_template(tempalte_path, **context)


@products_app.route("/<int:product_id>", methods=["GET", "POST"])
def show_single_product(product_id):
    product = db_session.query(Product).get(product_id)
    tempalte_path = "products/product.html"
    context = {
        "product": product,
        "single_product_page": True,
    }
    return render_template(tempalte_path, **context)


@products_app.route("/add_products", methods=["GET"])
def add_products():
    db_session.add(Product('Computer', 15, 'Mac book pro - a product of Apple. Nice looking and easy to use', 'computer.jpeg'))
    db_session.add(Product('Smartphone', 10, 'Android OnePlus5 - quite interesting purchase in this month', 'oneplus5.jpg'))
    db_session.add(Product('Watches', 5, 'Golden watches with GPS tracker and calories counter', 'watches.png'))
    db_session.commit()
    return "Items added"
