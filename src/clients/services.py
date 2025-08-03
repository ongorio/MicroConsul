from fbdatabase.firebird import db
from firebird.driver import DatabaseError
from clients.queries import get_clients, get_client_by_id, create_client, get_next_client_id
import time

class ClientsService:

    @staticmethod
    def _tuple_to_dict(tuple_data, fields_names):
        return dict(zip(fields_names, tuple_data))

    @staticmethod
    def get_next_client_id():
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_next_client_id)
                return cursor.fetchone()[0]

    @staticmethod
    def get_clients():
        fields = ['id', 'name', 'status', 'moneda', 'f_id']
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_clients)
                tuples_data = cursor.fetchall()
                return [ClientsService._tuple_to_dict(tuple, fields) for tuple in tuples_data]

    @staticmethod
    def get_client_by_id(id):
        fields = ['id', 'name', 'status', 'moneda', 'f_id']
        with db.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(get_client_by_id, (id,))
                tuple_data = cursor.fetchone()
                return ClientsService._tuple_to_dict(tuple_data, fields) if tuple_data else None

    @staticmethod
    def create_client(client_data={}, max_retries=3, retry_delay=1):
        last_exception = None

        for attempt in range(max_retries):
            try:
                with db.connect() as conn:
                    with conn.cursor() as cursor:
                        next_client_id = ClientsService.get_next_client_id()
                        
                        params = (
                            next_client_id,
                            client_data['name'],
                            client_data['sujeto_ieps'],
                            client_data['diferir_cfdi_cobros'],
                            client_data['limite_credito'],
                            client_data['moneda_id'],
                            client_data['cond_pago_id']
                        )
                        cursor.execute(create_client, params)
                        conn.commit()

                        return ClientsService.get_client_by_id(next_client_id)
            except DatabaseError as e:
                last_exception = e
                error_message = str(e).lower()

                if any(keyword in error_message for keyword in ['unique constraint', 'duplicate key', 'violation', 'primary key']):
                    if attempt < max_retries - 1:
                        time.sleep(retry_delay)
                        retry_delay *= 1.5
                    else:
                        break
                else:
                    raise e
            except Exception as e:
                raise e

            raise Exception(f"Failed to create client after {max_retries} attempts. Last error: {last_exception}")