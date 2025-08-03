get_products = """
SELECT a.ARTICULO_ID, a.NOMBRE FROM ARTICULOS a
"""

get_product_by_id = """
SELECT a.ARTICULO_ID, a.NOMBRE FROM ARTICULOS a
WHERE a.ARTICULO_ID = ?
"""