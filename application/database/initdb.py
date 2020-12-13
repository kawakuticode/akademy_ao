import sqlite3
from sqlite3 import Error as error

"""create a database connection to the SQLite database
 specified by db_file
:param db_file: database file
:return: Connection object or None
"""
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except error as e:
        print(f"error {e}")

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except error as e:
        print(e)
    print("table criada com sucesso!")

def insert_temp(conn, data_content) :

    sql_data_input = """ INSERT INTO item (fname,lname , type_item,reference,province,status,cellphone,email,note) VALUES (?,?,?,?,?,?,?,?,?) ;"""
    try:
        cur = conn.cursor()
        cur.execute(sql_data_input,data_content)
        cur.lastrowid
        conn.commit()


    except error as e:
        print(e)


def main():
    database = "AKDB.db"
    """ CREATE TABLE IF NOT EXISTS item (
                                            id integer PRIMARY KEY AUTOINCREMENT,
                                            fname text NOT NULL,
                                            lname text NOT NULL,
                                            type_item text NOT NULL,
                                            reference text ,
                                            province text NOT NULL,
                                            status text NOT NULL,
                                            cellphone text NOT NULL, 
                                            email text NOT NULL,
                                            note text
                                             );"""

    sql_create_user_table=""""""
    sql_create_university_table=""""""
    sql_create_faculty_table = """"""
    sql_create_course_table = """"""
    sql_create_university_table = """"""
    sql_create_semester_table = """"""
    sql_create_subject_table = """"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_user_table)
        create_table(conn, sql_create_university_table)
        create_table(conn, sql_create_faculty_table)
        create_table(conn, sql_create_course_table)
        create_table(conn, sql_create_semester_table)
        create_table(conn, sql_create_subject_table)

       # print("inserido item {} " .format(insert_temp(conn, item_1)))
       # print("inserido item {} " .format(insert_temp(conn, item_2)))
       # print("inserido item {} " .format(insert_temp(conn, item_3)))
       # print("inserido item {} " .format(insert_temp(conn , item_4)))
       # print("inserido item {} ".format(insert_temp(conn, item_5)))

    else:
        print("Error! cannot create the database connection.")
    conn.close()

if __name__ == '__main__':
            main()