import pymysql
import datetime

    
def users(name,image,username,user_id,languagecode):

    con = pymysql.Connect(
        host ="localhost",user = "userdatabase",
        passwd="password",database="database_name")
    cs = con.cursor()
    try:
        #Search to the database
        com = "SELECT * from users WHERE numerical_id = %s"
        vel = (user_id)
        cs.execute(com,vel)
        r = cs.fetchall()
        # Add user to the database
        if r ==():

            created_at = datetime.date.today()
            com = f"INSERT INTO users (name,image,numerical_id,username,language,created_at) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (name,image,user_id,username,languagecode,created_at)
            cs.execute(com,val)
            con.commit()     
            con.close()
    except:
        print("Error")

def groups_database(name, count_chat, chat_type, numerical_id, chat_username):

    con = pymysql.Connect(
        host ="localhost",user = "userdatabase",
        passwd="password",database="database_name")
    cs = con.cursor()
    #Search to the database
    try:
        com = "SELECT * from groups WHERE numerical_id = %s"
        vel = (numerical_id)
        cs.execute(com,vel)
        r = cs.fetchall()
        # Add user to the database
        if r ==():
            created_at = datetime.date.today()
            com = f"INSERT INTO groups (name,numerical_id,username_chat,members_count,chat_type,created_at) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (name,numerical_id,chat_username,count_chat,chat_type,created_at)
            cs.execute(com,val)
            con.commit()     
            con.close()
    except:
        print("Error!")
