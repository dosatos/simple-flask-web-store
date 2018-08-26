# ============== #
#    Main App    #
# ============== #

from flask import Flask, redirect, url_for

from web import config
from products.app import products_app
from admin.app import admin_app


app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")
app.register_blueprint(admin_app, url_prefix="/admin")
app.config.from_object(config.DevelopmentConfig)


@app.route("/")
def index():
    return redirect(url_for('products_app.show_products'))