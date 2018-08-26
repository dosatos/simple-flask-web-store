from flask import Flask, redirect, url_for
from products.app import products_app

# ============== #
#    Main App    #
# ============== #

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")


@app.route("/")
def index():
    return redirect(url_for('products_app.show_products'))