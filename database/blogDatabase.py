import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    passwd="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE BLOG;")
mycursor.execute("USE BLOG;")

tables = {}

tables['Users'] = """CREATE TABLE Users (
  UserID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Username VARCHAR(255),
  Password VARCHAR(255),
  Email VARCHAR(255),
  CreatedDate DATETIME
);"""

tables['Posts'] = """CREATE TABLE Post (
  PostID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  PostTitle VARCHAR(255),
  PostBody TEXT,
  CreatedDate DATETIME,
  UserID INT, FOREIGN KEY (UserID) REFERENCES Users(UserID)
);"""

tables['Comments'] = """CREATE TABLE Comments (
  CommentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  CommentText TEXT,
  CommentDate DATETIME,
  UserID INT, FOREIGN KEY (UserID) REFERENCES Users(UserID),
  PostID INT, FOREIGN KEY (PostID) REFERENCES Post(PostID)
);"""


for table_name in tables:
    table_script = tables[table_name]
    mycursor.execute(table_script)

mycursor.close()
mydb.close()