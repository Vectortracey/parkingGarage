"""
functions for spaceship garage.
"""
import mysql.connector
from datetime import datetime
import time



global connect, cursor
connect = mysql.connector.connect(
    host="localhost", database="space_parking", user="root", password="pappa667")
cursor = connect.cursor()


def clear():
    for _ in range(100):
        print()

def garage_status():
    """
    shows the status in the garage
    """

    clear()
    sql1 = "SELECT * from parking_garage WHERE status ='empty' AND floor='1'"
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    sql2 = "SELECT * from parking_garage WHERE status ='empty' AND floor='2'"
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    sql3 = "SELECT * from parking_garage WHERE status ='empty' AND floor='2'"
    cursor.execute(sql3)
    result3 = cursor.fetchall()

    if len(result1) >=1:
        print("Available spaces at floor1: " + str(len(result1)))
    elif len(result1) == 0:
        print("Floor 1 is full")
    if len(result2) >= 1:
        print("Available spaces at floor2: " + str(len(result2)))
    elif len(result2) == 0:
        print("Floor 2 is full")
    if len(result3) >= 1:
        print("Available spaces at floor3: " + str(len(result3)))
    elif len(result3) == 0:
        print("Floor 3 is full")
    wait = input("press any key to continue.")


def remove_spaceship():
    """
    removes spaceship from garage
    """

    clear()
    print("Sign out your spaceship\n")
    print("Testing spots, id 1,2 and 3 are available to sign out")
    wait = input("Type any key to continue")
    clear()

    spaceship_id = input("Enter your spaceship digit number.")

    exit_date = datetime.now()

    sql_remove = 'SELECT parking_id,price,entry_date from receipt tr,parking_garage pg, parking_type pt \
               where tr.parking_id = pg.id and pg.floor = pt.id and \
               spaceship_id ="' + spaceship_id + '" and exit_date is NULL;'
    cursor.execute(sql_remove)
    record = cursor.fetchone()

    duration = (exit_date - record[2])

    duration_hours = duration.total_seconds() / 3600

    print("You have parked for " + str(duration_hours//24)+" Days and "+(str(round(duration_hours % 24)))+" hours.")

    amount = 0
    if duration_hours >= 24:
        days = (duration_hours / 24)
        amount = round(days * 50)
    elif duration_hours < 24:
        amount = (round(duration_hours) * 15)



    print("total cost " + str(round(amount)))
    wait = input("press any key to continue.")
    clear()

    print("Parking ID: " + str(record[0]))
    print("Vehicle ID: " + str(spaceship_id))
    print("Parking Date: " + str(record[2]))
    print("Current Date: " + str(exit_date.replace(second=0, microsecond=0)))
    print("Amount Payable: " + str(amount))
    wait = input("press any key to continue.")
    sql1 = 'update receipt set exit_date ="{}" , amount ={} where spaceship_id ="{}" \
                and exit_date is NULL;'.format(exit_date, amount, spaceship_id)
    sql2 = 'update parking_garage set status ="empty" where id = {}'.format(record[0])
    cursor.execute(sql1)
    cursor.execute(sql2)
    wait = input("Your spaceship has signed out successfully, press any key to continue.")



def add_spaceship():
    """
    adds spaceship to garage
    """

    clear()
    sql1 = "SELECT * from parking_garage WHERE status ='empty' AND floor='1'"
    cursor.execute(sql1)
    result1 = cursor.fetchall()

    sql2 = "SELECT * from parking_garage WHERE status ='empty' AND floor='2'"
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    sql3 = "SELECT * from parking_garage WHERE status ='empty' AND floor='2'"
    cursor.execute(sql3)
    result3 = cursor.fetchall()

    print("Available floors:\n")
    if len(result1) >= 1:
        print("Available spaces at floor1: " + str(len(result1)))
    elif len(result1) == 0:
        print("Floor 1 is full")
    if len(result2) >= 1:
        print("Available spaces at floor2: " + str(len(result2)))
    elif len(result2) == 0:
        print("Floor 2 is full")
    if len(result3) >= 1:
        print("Available spaces at floor3: " + str(len(result3)))
    elif len(result3) == 0:
        print("Floor 3 is full")

    choose_floor = input("\nChoose floor or type \"q\" to quit.\n")
    while True:
        entry_date = datetime.now()
        if choose_floor == "q":
            break
        if choose_floor == "1" and len(result1) >= 1:
            print("Sign in your spaceship\n")
            floor_sql = "SELECT id from parking_garage WHERE floor='1' AND status='empty'"
            cursor.execute(floor_sql)
            floor_result = cursor.fetchall()
            available_space = []
            for row in floor_result:
                available_space.append(row[0])
            print(available_space)
            floor_space = int(input("Enter space number:\n"))
            if floor_space in available_space:
                #print(type(floor_space))
                try:
                    spaceship_id = int(input("Enter your spaceship digit number.\n"))

                    #print(type(spaceship_id))
                    print("Your ship is signed at floor " + choose_floor + " at space: " + str(floor_space))
                    sql_insert = 'INSERT INTO receipt(spaceship_id,parking_id,entry_date) VALUES \
                               ("{}","{}","{}");'.format(spaceship_id, floor_space, entry_date)
                    cursor.execute(sql_insert)
                    cursor.execute('update parking_garage set status ="taken" where id ={}'.format(floor_space))
                    wait = input("Press any key to continue.")
                    break
                except ValueError:
                    print("Invalid input, must be numbers.")

            elif floor_space not in available_space:
                wait = input("Invalid number, press any key to continue.")
                add_spaceship()

            else:
                print("Invalid input")

        if choose_floor == "2" and len(result2) >= 1:
            print("Sign in your spaceship\n")
            floor_sql = "SELECT id from parking_garage WHERE floor='2' AND status='empty'"
            cursor.execute(floor_sql)
            floor_result = cursor.fetchall()
            available_space = []
            for row in floor_result:
                available_space.append(row[0])
            print(available_space)
            floor_space = int(input("Enter space number:\n"))
            if floor_space in available_space:
                #print(type(floor_space))
                try:
                    spaceship_id = int(input("Enter your spaceship digit number.\n"))

                    #print(type(spaceship_id))
                    print("Your ship is signed at floor "+choose_floor+" at space: "+str(floor_space))
                    sql_insert = 'INSERT INTO receipt(spaceship_id,parking_id,entry_date) VALUES \
                               ("{}","{}","{}");'.format(spaceship_id, floor_space, entry_date)
                    cursor.execute(sql_insert)
                    cursor.execute('update parking_garage set status ="full" where id ={}'.format(floor_space))
                    wait = input("Press any key to continue.")
                    break
                except ValueError:
                    print("Invalid input, must be numbers.")

            elif floor_space not in available_space:
                wait = input("Invalid number, press any key to continue.")
                add_spaceship()

            else:
                print("Invalid input")

        if choose_floor == "3" and len(result3) >= 1:
            print("Sign in your spaceship\n")
            floor_sql = "SELECT id from parking_garage WHERE floor='3' AND status='empty'"
            cursor.execute(floor_sql)
            floor_result = cursor.fetchall()
            available_space = []
            for row in floor_result:
                available_space.append(row[0])
            print(available_space)
            floor_space = int(input("Enter space number:\n"))
            if floor_space in available_space:
                #print(type(floor_space))
                try:
                    spaceship_id = int(input("Enter your spaceship digit number.\n"))

                    #print(type(spaceship_id))
                    print("Your ship is signed at floor "+choose_floor+" at space: "+str(floor_space))
                    sql_insert = 'INSERT INTO receipt(spaceship_id,parking_id,entry_date) VALUES \
                               ("{}","{}","{}");'.format(spaceship_id, floor_space, entry_date)
                    cursor.execute(sql_insert)
                    cursor.execute('update parking_garage set status ="full" where id ={}'.format(floor_space))
                    wait = input(" press any key to continue.")
                    break
                except ValueError:
                    print("Invalid input, must be numbers.")

            elif floor_space not in available_space:
                wait = input("Invalid number, press any key to continue.")
                add_spaceship()
            else:
                print("Invalid input")

        else:
            print("Invalid floor")
            time.sleep(2)
            add_spaceship()
