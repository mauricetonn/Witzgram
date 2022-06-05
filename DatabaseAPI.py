"""
Used to setup and interact with Database

    author: Maurice Tonn / Simon Klingler
    date: 28.05.2022
    version: 0.0.1
    license: free
"""

import os
import sqlite3 

db_name = "witzeBank.db"
my_db_connection = sqlite3.connect(db_name)

table_name = "witz"

my_db_cursor = my_db_connection.cursor()

def __setup():
    """
    Used to setup the database when starting Witzgram

    Test:
        1) run setup() -> witzeBank.db should be created
    """
    global db_name, my_db_connection, table_name, my_db_cursor
    table_fields = "w_kategory VARCHAR(30), w_title VARCHAR(50), w_text VARCHAR(255), w_like INTEGER"
    my_create_sql = f"CREATE TABLE {table_name} ({table_fields})"
    my_db_cursor.execute(my_create_sql)

def get_jokes(rank):
    """
    Returns Jokes depending on given Rank

    Args:
        rank (int): Rank of the Joke in the Database (Based on likes)

    Returns:
        tupel: returns tupel with (joke, category, likes)
    Test:
        1) get_jokes(0) -> should return Joke with most likes
        2) get_jokes(1) -> should return Joke with scond most likes
    """
    my_db_cursor.execute(f"SELECT w_text, w_kategory, w_like FROM {table_name} ORDER BY w_like DESC")
    jokes = my_db_cursor.fetchall()
    if rank >= len(jokes):
        return ("END OF FAVORITES - Press 'new Joke' to rebegin", "EOF", 0)
    print("ORDER:", jokes)
    return jokes[rank]

def add_joke(joke, category = 'Misc'):
    """
    Adds a new Joke to Database, doesnt check if its already in the Database
    # may be TODO for future programming
    Args:
        joke (str): Joke Text
        category (str, optional): sets the Category of the Joke. Defaults to 'Misc'.
    Test:
        1) add_joke("joke") -> Code under "Testing" should show the new Joke in the DB
        2) add_joke(joke="joke", category="Programming") -> Code under Testing should show joke with given Category
    """
    my_insert_sql = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', 1)"
    try:
        my_db_cursor.execute(my_insert_sql)
    except:
        table_fields = "w_kategory VARCHAR(30), w_title VARCHAR(50), w_text VARCHAR(255), w_like INTEGER"
        my_create_sql = f"CREATE TABLE {table_name} ({table_fields})"
        my_db_cursor.execute(my_create_sql)
        my_db_cursor.execute(my_insert_sql)
    # Testing:
    #my_db_cursor.execute(f"SELECT w_text, w_kategory, w_like FROM {table_name} ORDER BY 'w_like'")
    #jokes = my_db_cursor.fetchall()
    #print("jokes:", jokes)

def like_inkrement(joke, category, likes):
    """
    Deletes Joke with old Version of likes. Then saves new Version to DB.

    Args:
        joke (str): Joke Text
        category (str): Joke Category
        likes (int): Like-Amount
    Test:
        1) Use GUI to get joke. like it. and like it again in favorites. Like amount should increase.
    """
    delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
    my_db_cursor.execute(delete_old_joke)
    insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes + 1})"
    my_db_cursor.execute(insert_new_joke)

def like_dekrement(joke, category, likes):
    """
    Deletes old Joke Version and adds new Version with dekremented Like Amount. 
    Deletes Joke completely, when like amount = 0

    Args:
        joke (str): Joke Text
        category (str): Joke Category
        likes (int): Like-Amount
    Test:
        1) Use GUI. Like random Joke. Go to Favorites and dislike it. It should be removed from Database
    """
    if(likes > 1):
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)
        insert_new_joke = f"INSERT INTO {table_name} ('w_kategory', 'w_text', 'w_like') VALUES ('{category}', '{joke}', {likes - 1})"
        my_db_cursor.execute(insert_new_joke)
    else:
        delete_old_joke = f"DELETE FROM {table_name} WHERE w_text = '{joke}'"
        my_db_cursor.execute(delete_old_joke)

def db_commit():
    """
    Commits Data from Journal to DB

    Test:
        1) Data in DB after restart of Gui
    """
    my_db_connection.commit()

# Set up DB
if os.path.isfile("witzeBank.db"):
    pass
else:
    __setup()