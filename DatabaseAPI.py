import sqlite3 

db_name = "witzeBank.db"
my_db_connection = sqlite3.connect(db_name)

table_name = table_name = "witz"

my_db_cursor = my_db_connection.cursor()

# Testing:
# my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('Test', 'HAHAHA', 1)"
# my_db_cursor.execute(my_insert_sql)

# my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('Test', 'WITZ WITZ', 1)"
# my_db_cursor.execute(my_insert_sql)

def get_jokes():
    my_db_cursor.execute(f"SELECT w_text, w_kategory, w_like FROM {table_name} ORDER BY 'w_like'")
    jokes = my_db_cursor.fetchall()
    return jokes

def add_joke(joke, category = 'Misc'):
    my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', 1)"
    my_db_cursor.execute(my_insert_sql)

def like_inkrement(joke, category, likes):
    delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
    my_db_cursor.execute(delete_old_joke)
    insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes + 1})"
    my_db_cursor.execute(insert_new_joke)

def like_dekrement(joke, category, likes):
    if(likes > 1):
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)
        insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes + 1})"
        my_db_cursor.execute(insert_new_joke)
    else:
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)