import os
import sqlite3 

db_name = "witzeBank.db"
my_db_connection = sqlite3.connect(db_name)

table_name = "witz"
#table_fields = "w_kategory VARCHAR(30), w_text VARCHAR(255), w_like INTEGER"
#my_create_sql = f"CREATE TABLE {table_name} ({table_fields})"

my_db_cursor = my_db_connection.cursor()
# my_db_cursor.execute(my_create_sql)

# Testing:
# my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('Test', 'HAHAHA', 1)"
# my_db_cursor.execute(my_insert_sql)

# my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('Test', 'WITZ WITZ', 1)"
# my_db_cursor.execute(my_insert_sql)

def setup():
    global db_name, my_db_connection, table_name, my_db_cursor
    if os.path.isfile("witzeBank.db"):
        pass
    else:
        table_fields = "w_kategory VARCHAR(30), w_title VARCHAR(50), w_text VARCHAR(255), w_like INTEGER"
        my_create_sql = f"CREATE TABLE {table_name} ({table_fields})"
        my_db_cursor.execute(my_create_sql)

def get_jokes(rank):
    my_db_cursor.execute(f"SELECT w_text, w_kategory, w_like FROM {table_name} ORDER BY w_like DESC")
    jokes = my_db_cursor.fetchall()
    if rank >= len(jokes):
        return ("END OF FAVORITES - Press 'new Joke' to rebegin", "EOF", 0)
    print("ORDER:", jokes)
    return jokes[rank]

def add_joke(joke, category = 'Misc'):
    #print("joke:", joke)
    #print("category:", category)
        my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', 1)"
    #print("insert:", my_insert_sql)
        my_db_cursor.execute(my_insert_sql)
        my_db_cursor.execute(f"SELECT w_text, w_kategory, w_like FROM {table_name} ORDER BY 'w_like'")
        jokes = my_db_cursor.fetchall()
        print("jokes:", jokes)

def like_inkrement(joke, category, likes):
    delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
    my_db_cursor.execute(delete_old_joke)
    insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes + 1})"
    my_db_cursor.execute(insert_new_joke)

def like_dekrement(joke, category, likes):
    if(likes > 1):
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)
        insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes - 1})"
        my_db_cursor.execute(insert_new_joke)
    else:
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)

setup()
