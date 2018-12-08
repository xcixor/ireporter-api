"""Set up database."""

import psycopg2


def connect(db_config):
    """Connect to the database.
    args:
        db_config(dict): a dictionary containing db configurations

    returns:
        conn(object): Connection object
    """
    conn = None
    try:
        print('Connecting to db...')
        url = "dbname={} user={} password={} host={} port={}".\
              format(db_config['dbname'], db_config['user'],
                     db_config['password'], db_config['host'],
                     db_config['port'])
        conn = psycopg2.connect(url)
    except(Exception, psycopg2.DatabaseError) as error:
        print("Warning: Connection Error", error)
    finally:
        if conn is not None:
            print("Connected to db")
            db_connection['connection'] = conn
            return conn


def return_conn(connection):
    """Return db connection."""
    return connection


def init_db(db_config):
    """Initialize db."""
    create_tables(db_config)


def create_tables(db_config):
    """Create tables."""
    tables = table_queries()
    try:
        conn = connect(db_config)
        cursor = conn.cursor()
        for table in tables:
            cursor.execute(table)
            conn.commit()
        print('***** db init complete *****')
    except(Exception, psycopg2.DatabaseError) as error:
        print("Warning: Table Creation Error", error)


def drop_tables(db_config):
    """Delete all tables from database."""
    tables = ["users", "incidents", "images", "videos",
              "images", "location" "login"]
    try:
        conn = connect(db_config)
        cursor = conn.cursor()
        for table in tables:
            query = "DROP TABLE IF EXISTS {} CASCADE;".format(table)
            cursor.execute(query)
            conn.commit()
        # print('Table {} deleted'.format(tables), '\n')
    except(Exception, psycopg2.DatabaseError) as error:
        print("Warning: Table Deletion Error", error)


def table_queries():
    """Table queries."""
    tables = []
    user = "CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY,\
    email VARCHAR(60), \
    user_Password TEXT, \
    date_created DATE,\
    is_admin Boolean);"
    tables.append(user)

    incident = "CREATE TABLE IF NOT EXISTS incidents (\
    id serial PRIMARY KEY,\
    creator TEXT,\
    location TEXT,\
    status TEXT,\
    comment TEXT,\
    user_id INTEGER REFERENCES users(id),\
    title TEXT);"
    tables.append(incident)

    images = "CREATE TABLE IF NOT EXISTS images (id serial PRIMARY KEY,\
    url TEXT,\
    incident_id INTEGER REFERENCES incidents(id));"
    tables.append(images)

    videos = "CREATE TABLE IF NOT EXISTS videos (id serial PRIMARY KEY, \
    url TEXT,\
    incident_id INTEGER REFERENCES incidents(id));"
    tables.append(videos)

    location = "CREATE TABLE IF NOT EXISTS location (\
    id serial PRIMARY KEY,\
    longitude FLOAT,\
    latitude FLOAT,\
    incident_id INTEGER REFERENCES incidents(id)\
    );"
    tables.append(location)

    login = "CREATE TABLE IF NOT EXISTS login (\
    id serial PRIMARY KEY,\
    user_id INTEGER REFERENCES users(id),\
    last_login TIMESTAMP,\
    token VARCHAR\
    );"
    tables.append(login)

    return tables

db_connection = {'connect': None}
