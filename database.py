import psycopg2
import os

from datetime import datetime


def create_table(connect):
    commands = ("""
        CREATE TABLE timetable (
            Number INTEGER,
            Day INTEGER,
            Time CHARACTER VARYING(30),
            NameObj CHARACTER VARYING(30),
            Auditorium INTEGER,
            Week CHARACTER VARYING(30)
        );
    """)

    with connect.cursor() as cursor:
        connect.autocommit = True
        cursor.execute(commands)


def get_request(connect, number_of_group):
    try:
        now = datetime.weekday(datetime.now())
        with connect.cursor() as cursor:
            cursor = connect.cursor()
            cursor.execute("""select time, nameobj, auditorium, week from timetable where number=""" + str(number_of_group) + """ and day=""" + str(now))
            info = cursor.fetchall()
        return info
    except:
        return 0


def get_connection(number_of_group):
    connect = psycopg2.connect(
        database="db9ffeo3f1039r",
        user="heetupgqnhaysy",
        password="3c112f195b75854016039d9c9833efe22c279262b9326ac4079e8b1b6a6585c0",
        host="ec2-23-21-148-109.compute-1.amazonaws.com",
        port="5432",
    )
    info = get_request(connect, number_of_group)
    connect.close()
    return info
