from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URI = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/postgres'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

labels = Table(
    'labels',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    Column('phone', String(20)),
    Column('count_artists', Integer),
    Column('county', String(12))
)

database = Database(DATABASE_URI)