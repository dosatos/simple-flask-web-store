# ============== #
#  Products App  #
# ============== #

from flask import Blueprint


products_app = Blueprint("products_app", __name__)

@products_app.route("/")
def show_products():
    return "Hello World!"


@products_app.route("/<int:product_id>")
def show_product(product_id):
    return f"This is a product, ID = {product_id}"