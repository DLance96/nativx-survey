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


def add_record(personailty, eat_activities, play_activities):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO activity_personailty (personallity, activities_eat, activities_play) VALUES (%s, %s, %s)" \
            % (personailty, eat_activities, play_activities)
    try:
        cursor.execute(query)
        db.commit()
    except:
        db.rollback()
    db.close()