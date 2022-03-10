import sqlite3

from prettytable import PrettyTable

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
    print("6. view the most expensive fruit")
    print("7. view the less expensive fruit")
    print("8. disply sum of fruit prices")
    print("9. display the fruits between the range")
    print("10. display an average of total amount")
    print("11. exit")

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

        table = PrettyTable(["Id","serialno","fruitname","fruitprice","exportplace","fruitamount"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)

    elif choice == 3:
        result = connection.execute("select * from market")

        table = PrettyTable(["Id","serialno","fruitname","fruitprice","exportplace","fruitamount"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)



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

        table = PrettyTable(["Id","serialno","fruitname","fruitprice","exportplace","fruitamount"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)

    elif choice == 5:
        getfruitamount = input("enter the fruitamount: ")

        connection.execute("delete from market where fruitamount=" +getfruitamount)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from market")

        print("data updated")

        table = PrettyTable(["Id","serialno","fruitname","fruitprice","exportplace","fruitamount"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)

    elif choice == 6:
        result = connection.execute("select max(fruitprice) as fruitprice from market")

        table = PrettyTable(["fruitprice"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 7:
        result = connection.execute("select min(fruitprice) as fruitprice from market")

        table = PrettyTable(["fruitprice"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 8:
        result = connection.execute("select sum(fruitprice) as fruitprice from market")

        table = PrettyTable(["fruitprice"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 9:
        lowerrange = input("enter the lower range")
        higherrange = input("enter the higher range")
        result = connection.execute("select * from market where fruitprice between " + lowerrange + " AND " + higherrange + "")

        table = PrettyTable(["Id","serialno","fruitname","fruitprice","exportplace","fruitamount"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)

    elif choice == 10:
        result = connection.execute("select avg(fruitamount) as fruitamount from market")

        table = PrettyTable(["fruitamount"])
        for i in result:
            table.add_row([i[0]])
        print(table)

    elif choice == 11:
        break

    else:
        print("invalid choice")