import sys
import MySQLdb
import config


def get_connection():
    connection = MySQLdb.connect(
        host=config.db_host,
        user=config.db_user,
        passwd=config.db_passwd,
        db=config.db,
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
