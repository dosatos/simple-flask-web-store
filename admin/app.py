# ============== #
#  Store Admin App  #
# ============== #

from flask import Blueprint, render_template


admin_app = Blueprint("admin_app", __name__, template_folder="templates/")


@admin_app.route("/", methods=["GET", "POST"])
def show_products():
    tempalte_path = "admin/products.html"
    context = {
        "products": [1, 2, 3]
    }
    return render_template(tempalte_path, **context)