import mysql.connector


def creat_database():
    try:
        conn = mysql.connector.connect(
            host="host",
            user="username",
            passwd="pass"
        )
        # preparing a cursor object
        cursorObject = conn.cursor()
        # creating database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS kavim_bot")
        print("kavim_bot Data base is created")
        return "kavim_bot"
    except:
        print("Error!")
        return None


def creat_table():
    # Connecting To the Database in Localhost
    DataBase = mysql.connector.connect(
        host="localhost",
        user="userdatabas",
        password="pass",
        database="database_name"
    )
    # Cursor to the database
    Cursor = DataBase.cursor()

    # creat app Table
    APP_TABLE = """CREATE TABLE app (
        running    int,
        private    int,
        groups     int,
        inline     int);"""

    # Creat users Table
    USERS_TABLE = """CREATE TABLE users (

        name      varchar (70),
        image     varchar (190),
        id        bigint(20)  NOT NULL AUTO_INCREMENT,
        numerical_id    varchar (20),
        username    varchar(30),
        phone           varchar (15) Null,
        language        varchar (15),
        created_at      timestamp,
        login_email     varchar (50) Null,
        login_time      timestamp Null,
        PRIMARY KEY (id));"""

    # Creat groups Table
    GROUPS_TABLE = """CREATE TABLE groups (
        name     varchar (30),
        image    varchar (190),
        id        bigint(20)  NOT NULL AUTO_INCREMENT,
        numerical_id   varchar (20),
        username_chat  varchar (30) Null,
        language       varchar (15),
        chat_type   varchar(20),
        members_count int,
        blocked       int,
        created_at    timestamp,
        PRIMARY KEY (id));"""

    Cursor.execute(APP_TABLE)
    Cursor.execute(USERS_TABLE)
    Cursor.execute(GROUPS_TABLE)
    return


def start_database():
    # database = creat_database()
    creat_table()
