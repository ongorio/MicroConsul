from fbdatabase.firebird import db
from products.queries import get_products, get_product_by_id

class ProductsService:
    @staticmethod
    def get_products():
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_products)
                return cursor.fetchall()

    @staticmethod
    def get_product_by_id(id):
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_product_by_id, (id,))
                return cursor.fetchone()