# 02_select_data.py – przykład odwołania

from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column

engine = create_engine('sqlite:///dbase.db', echo=True)

meta = MetaData()

stations = Table(
   'stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', String),
   Column('longitude', String),
   Column('elevation', String),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

conn = engine.connect()
s = ("SELECT * FROM stations LIMIT 5")
result = conn.execute(s)

for row in result:
   print(row)