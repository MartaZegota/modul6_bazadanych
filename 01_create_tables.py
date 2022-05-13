# 01_create_tables.py

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///dbase.db')

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

stations = Table(
   'measure', meta,
   Column('id', Integer, primary_key=True),
   Column('station_id', String),
   Column('date', String),
   Column('precip', String),
   Column('tobs', String),
)

meta.create_all(engine)
print(engine.table_names())