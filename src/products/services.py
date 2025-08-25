from fbdatabase.firebird import db
from products.queries import get_products, get_product_by_id

class ProductsService:
    @staticmethod
    def _tuple_to_dict(tuple_data, fields_names):
        return dict(zip(fields_names, tuple_data))

    @staticmethod
    def get_products():
        fields = ['id', 'name']
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_products)
                tuples_data = cursor.fetchall()
                return [ProductsService._tuple_to_dict(tuple, fields) for tuple in tuples_data]

    @staticmethod
    def get_product_by_id(id):
        fields = ['id', 'name']
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_product_by_id, (id,))
                tuple_data = cursor.fetchone()
                return ProductsService._tuple_to_dict(tuple_data, fields) if tuple_data else None