'''Converts numpy to pandas then sends to user specified database'''
import pandas as pd
import sqlite3 as sql


#TODO: sanitize this input using ? or %s instead of {} and .format
def sqlsend(nparr, db, table):
    df = pd.DataFrame(nparr)
    conn = sql.connect("{}.db".format(db))
    

    df.to_sql(table, con=conn, if_exists='fail')

    