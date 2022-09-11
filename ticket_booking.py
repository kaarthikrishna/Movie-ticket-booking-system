import pyfiglet
import mysql.connector
import time
import sys

connection=mysql.connector.connect(host="localhost",user="root",passwd="karthik123",database="movie")
cursor=connection.cursor()


def insert():
    insert = """INSERT INTO booking_rec(NAME,MOVIE,PRICE,PHONE_NUMBER) 
                            VALUES('{}','{}',{},{})""".format(name, movie, price, ph)
    cursor.execute(insert)
    connection.commit()
    print("BOOKED SUCCESSFULLY")
    open()


def details():
    exec = "select * from movie_list"
    cursor.execute(exec)
    data = cursor.fetchall()
    for i in data:

        print(i)
    conf=input("DO YOU WISH TO CONTINUE? y/n" )
    if conf=="y":
        global movie
        movie=input("ENTER THE MOVIE (please enter within double quotes")
        global name
        name=input("ENTER YOUR NAME:"'\t')
        global ph
        ph= int(input("ENTER YOUR PHONE NUMBER"'\t'))
        count=int(input("ENTER NUMBER OF TICKETS"'\t'))
        exec = "select * from movie_list where MOVIE= %s"%(movie,)
        cursor.execute(exec)
        data = cursor.fetchall()
        for i in data:
            # global movieprice
            movieprice = i[1]
        global price
        price= int(count * movieprice)
        print("TOTAL COST IS"'\t',price)
    if conf=="n":
        print("THANK YOU! VISIT AGAIN")
        open()
    print("DO YOU WISH TO BOOK YOUR TICKET?")
    ch=input("y/n"'\t')
    if ch=="y":
        insert()

def open():

    print("Loading:")

    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    details()







a=pyfiglet.figlet_format("PVR", font="doh")
print(a)


print("#### NOW SHOWING ####")
open()
