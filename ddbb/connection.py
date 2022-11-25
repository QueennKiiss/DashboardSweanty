"""
Needed libraries:
       pip install mysql-connector-python
       pip install SQLAlchemy
"""
import logging
from sqlalchemy import create_engine, MetaData, Table, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

import schema

DB_DRIVER = 'mysql+mysqlconnector'
USERNAME = 'mmaestro'
PASSWORD = 'Mmaestro-236'
HOST = 'localhost'
SCHEMA_DB = 'SWEANTY_DB'

# Create communication with mysql db
# arg: dialect+driver://username:password@host:port/database
engine = create_engine(
    f"{DB_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}/{SCHEMA_DB}", echo=False
    )

# Clear all the tables
schema.Base.metadata.drop_all(engine)
# Create tables defined in tables.py as classes
schema.Base.metadata.create_all(engine)

# # Check if schema already exists, if not it will be created
# inspector = inspect(engine)
# all_schemas = inspector.get_schema_names()
# if SCHEMA not in all_schemas:
#     engine.execute(CreateSchema(SCHEMA))
#     logging.info(f'New schema named {SCHEMA} has been created')

# Create an active session within the engine
Session = sessionmaker(engine)
session = Session()

# Insert an entry to dashboard sessions table
schema.insert_to_dashboard(session, 'bewolfish')

# Get the session id for ForeignKey
query_result = session.query(schema.DashboardSessions).filter(
    schema.DashboardSessions.session_name == 'bewolfish'
    )
for item in query_result:
    current_session_id = item.id
    print(current_session_id)

# Insert entries to athletes table
schema.insert_to_athletes(session, ('Mario', 'Perez', current_session_id))
schema.insert_to_athletes(session, ('Mario', 'Lopez', current_session_id))
schema.insert_to_athletes(session, ('Mario', 'Gerardez', current_session_id))
schema.insert_to_athletes(session, ('Gerardo', 'Mariez', 1))

query_result = session.query(schema.Athletes).filter(
    schema.Athletes.id == 4
    )
for item in query_result:
    print(item)
