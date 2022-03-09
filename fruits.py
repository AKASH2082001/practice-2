import sqlite3

connection = sqlite3.connect("fruits.db")

table_list = connection.execute("select name from sqlite_master where type='table' and name='market'").fetchall()

if table_list != []:
    print("table already exsist")

else:
    connection.execute(''' create table market(
                       Id integer primary key autoincrement,
                       serialno integer,
                       fruitname text,
                       fruitprice integer,
                       exportplace text,
                       fruitamount integer
    )''')

print("Table created")

while True:
    print("select an option from the given menu")
    print("1. add fruit")
    print("2. search an fruit using price")
    print("3. view all fruits")
    print("4. update an fruit using serialnumber")
    print("5. delete an fruit using amount")
    print("6. exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        getserialno = input("enter the serial number:")
        getfruitname = input("enter the fruit name:")
        getfruitprice = input("enter the fruit price:")
        getexportplace = input("enter the export place:")
        getfruitamount = input("enter the fruit amount:")
        connection.execute("insert into market(serialno,fruitname,fruitprice,exportplace,fruitamount) values("+getserialno+",'"+getfruitname+"',"+getfruitprice+",'"+getexportplace+"',"+getfruitamount+")")

        connection.commit()

        print("data inserted successfully")

    elif choice == 2:
        getfruitprice = input("enter the price to be search:")

        result = connection.execute("select * from market where fruitprice= "+getfruitprice)

        for i in result:
            print("Id =>",i[0])
            print("serialno =>",i[1])
            print("fruitname =>",i[2])
            print("fruitprice =>",i[3])
            print("exportplace =>",i[4])
            print("fruitamount =>",i[5])

    elif choice == 3:
        result = connection.execute("select * from market")

        for i in result:
            print("Id =>",i[0])
            print("serialno =>",i[1])
            print("fruitname =>",i[2])
            print("fruitprice =>",i[3])
            print("exportplace =>",i[4])
            print("fruitamount =>",i[5])


    elif choice == 4:
        getserialno = input("enter the serial number:")
        getfruitname = input("enter the fruit name:")
        getfruitprice = input("enter the fruit price:")
        getexportplace = input("enter the export place:")
        getfruitamount= input("enter the fruit amount:")

        result = connection.execute("update market set fruitname='"+getfruitname+"',fruitprice="+getfruitprice+",exportplace='"+getexportplace+"',fruitamount="+getfruitamount+" where serialno="+getserialno+"")
        connection.commit()

        print("market data updated successfully")

        result = connection.execute("select * from market where serialno="+getserialno+"")

        print("data updated")

        for i in result:
            print("Id =>",i[0])
            print("serialno =>",i[1])
            print("fruitname =>",i[2])
            print("fruitprice =>",i[3])
            print("exportplace =>",i[4])
            print("fruitamount =>",i[5])

    elif choice == 5:
        getfruitamount = input("enter the fruitamount: ")

        connection.execute("delete from market where fruitamount=" +getfruitamount)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from market")

        print("data updated")

        for i in result:
            print("Id =>",i[0])
            print("serialno =>",i[1])
            print("fruitname =>",i[2])
            print("fruitprice =>",i[3])
            print("exportplace =>",i[4])
            print("fruitamount =>",i[5])

    elif choice == 6:
        break

    else:
        print("invalid choice")