import sqlite3
import time
import os

def execute_query(db_path, query, params=()):
    conn = None  
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query, params)

        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            conn.commit()
            return [] 
            
    finally:
        if conn:
            conn.close()

class UserService:
    def __init__(self, db_path='app.db'):
        self.db_path = db_path

    def get_user(self, user_id):
        sql_get_user = "SELECT * FROM users WHERE id = ?"
        return execute_query(self.db_path, sql_get_user, (user_id,))
 
class OrderService:
    def __init__(self, db_path='app.db'):
        self.db_path = db_path

    def get_orders(self, user_id):
        sql_get_orders = "SELECT * FROM orders WHERE user_id = ?"
        return execute_query(self.db_path, sql_get_orders, (user_id,))

def setup_database(db_path='app.db'):
    if os.path.exists(db_path):
        os.remove(db_path)
    execute_query(db_path, "CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, name TEXT)")
    execute_query(db_path, "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id TEXT, item TEXT)")
    execute_query(db_path, "INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)", ('A', 'Alice'))
    execute_query(db_path, "INSERT OR IGNORE INTO orders (user_id, item) VALUES (?, ?)", ('A', 'Laptop'))

class UserService_old:
    def get_user(self, user_id):
        conn = sqlite3.connect('app.db')  # New connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
 
class OrderService_old:
    def get_orders(self, user_id):
        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result
    
if __name__ == "__main__":
    DB_FILE = 'app.db'
    setup_database(DB_FILE)

    user_service = UserService(DB_FILE)
    order_service = OrderService(DB_FILE)
    user_service = UserService(DB_FILE)
    order_service = OrderService(DB_FILE)

    user_service_old = UserService_old()
    order_service_old = OrderService_old()

    print("--- Getting user A ---")

    start_time = time.time()
    user_old = user_service_old.get_user(user_id='A')
    print(f"Result by old way: {user_old}")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    user_list = user_service.get_user(user_id='A')
    # The new service returns a list, so we extract the user
    user = user_list[0] if user_list else None
    print(f"Result by new way: {user}")
    print("--- %s seconds ---" % (time.time() - start_time))

    print("\n--- Getting orders for user A ---")

    start_time = time.time()
    orders_old = order_service_old.get_orders(user_id='A')
    print(f"Result by old way: {orders_old}")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    orders = order_service.get_orders(user_id='A')
    print(f"Result by new way: {orders}")
    print("--- %s seconds ---" % (time.time() - start_time))