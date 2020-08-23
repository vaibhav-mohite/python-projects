import mysql.connector as my


def get_conn():  # Connecting to MySQL through Xampp
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    sql = "CREATE TABLE IF NOT EXISTS books_details (Sr_No INT AUTO_INCREMENT PRIMARY KEY,ID INT, Title VARCHAR(100), Author VARCHAR(100),Publication VARCHAR (100))"
    mycur.execute(sql)
    mydb.commit()
    mydb.close()


get_conn()


def insert(uid, title, author, publication):  # Function to Insert Value
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    sql = "INSERT INTO books_details VALUES (NULL,'{}','{}','{}','{}')".format(uid, title, author, publication)
    mycur.execute(sql)
    mydb.commit()
    mydb.close()


def view():  # Function to View All Records
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM books_details")
    records = mycur.fetchall()  # Fetching all records from database
    mydb.close()
    return records


def search(uid="", title="", author="", publication=""):  # Empty strings
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    sql = "SELECT * FROM books_details WHERE ID = '{}' OR Title = '{}' OR Author='{}' OR Publication = '{}' ".format(
        uid,
        title,
        author,
        publication)
    mycur.execute(sql)
    records = mycur.fetchall()
    mydb.commit()
    mydb.close()
    return records


def delete(uid):  # Function to Delete Function
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    sql = "DELETE FROM books_details WHERE Sr_No= '{}'".format(uid)
    mycur.execute(sql)
    mydb.commit()
    mydb.close()


def update(sr_no, uid, title, author, publication):  # Function to Update Records
    mydb = my.connect(host="localhost", user="root", passwd="", database="book_management")
    mycur = mydb.cursor()
    sql = "UPDATE books_details SET ID = '{}',Title = '{}', Author = '{}',Publication = '{}' WHERE Sr_No = {}".format(
        uid, title,
        author,
        publication,
        sr_no
    )
    mycur.execute(sql)
    mydb.commit()
    mydb.close()
