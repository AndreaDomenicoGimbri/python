import sqlite3
import psycopg2
import os
import shutil
from datetime import datetime, timedelta

# Funzione per convertire il tempo di Chrome in datetime leggibile
def chrome_time_to_datetime(microseconds):
    base_date = datetime(1601, 1, 1)
    return base_date + timedelta(microseconds=microseconds)

#Copia il file di cronologia di Chrome (chiudi Chrome prima!)
chrome_history_path = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/History")
#esegue una copia del file di cronologia di Chrome nella cartella corrente così da evitare dei problemi in lettura nel caso in cui il motore di ricerca è ancora attivo
shutil.copy(chrome_history_path, "./History_copy1")

#Leggi la cronologia dal file SQLite copiato
conn_sqlite = sqlite3.connect('History_copy1')
cur_sqlite = conn_sqlite.cursor()
cur_sqlite.execute("""
    SELECT url, title, last_visit_time FROM urls
    WHERE title NOT LIKE '%Kibana%'
      AND title NOT LIKE '%Grafana%'
      AND title NOT LIKE '%Logstash%'
      AND title NOT LIKE '%Elasticsearch%'
                   AND title NOT LIKE '%Elastic%'
""")
rows = cur_sqlite.fetchall()
conn_sqlite.close()

#Connessione a PostgreSQL
conn_pg = psycopg2.connect(
    dbname="prova_database",
    user="andrea",
    password="andrea2019",
    host="localhost"
)
cur_pg = conn_pg.cursor()

#Crea la tabella se non esiste (con last_visit come TIMESTAMP)
cur_pg.execute("""
    CREATE TABLE IF NOT EXISTS chrome_history_filtered1 (
        url TEXT,
        title TEXT,
        last_visit TIMESTAMP
    );
""")

#Inserisci i dati nella tabella
for url, title, last_visit in rows:
    timestamp = chrome_time_to_datetime(last_visit)
    cur_pg.execute(
        "INSERT INTO chrome_history_filtered1 (url, title, last_visit) VALUES (%s, %s, %s)",
        (url, title, timestamp)
    )

conn_pg.commit()
cur_pg.close()
conn_pg.close()
print("Cronologia Chrome importata con successo.")
