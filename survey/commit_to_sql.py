import os
import sys
import MySQLdb


def get_connection():
    connection = MySQLdb.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWD'),
        db=os.environ.get('DB'),
    )
    return connection


def add_record(personality, eat_activities, play_activities):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO activity_personality (personality, activities_eat, activities_play) VALUES ('%s', '%s', '%s')" \
            % (personality, eat_activities, play_activities)
    try:
        cursor.execute(query)
        db.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        db.rollback()
    db.close()
