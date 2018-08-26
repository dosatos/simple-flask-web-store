# ============== #
#  Products App  #
# ============== #

from flask import Blueprint, render_template


products_app = Blueprint("products_app", __name__, template_folder="templates/")


@products_app.route("/", methods=["GET"])
def show_products():
    tempalte_path = "products/products.html"
    context = {
        "products": [1, 2, 3, 4, 5]
    }
    return render_template(tempalte_path, **context)


@products_app.route("/<int:product_id>", methods=["GET", "POST"])
def show_product(product_id):
    tempalte_path = "products/product.html"
    context = {
        "product_id": product_id,
    }
    return render_template(tempalte_path, **context)

