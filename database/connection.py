"""
Needed libraries:
       pip install mysql-connector-python
       pip install SQLAlchemy
"""
import logging
from time import sleep
from sqlalchemy import create_engine, MetaData, Table, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

from database import schema

DB_DRIVER = 'mysql+mysqlconnector'
USERNAME = 'mmaestro'
PASSWORD = 'Mmaestro-236'
HOST = 'localhost'
SCHEMA_DB = 'QUEENKISS_DB'


class DBConnector:
    """ " """
    def __init__(self):
        self.engine = create_engine(
            f"{DB_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}", echo=False
            )
    # Create communication with mysql db
    # arg: dialect+driver://username:password@host:port/database

    def _check_if_schema_exists(self) -> bool:
        # Check if schema already exists, if not it will be created
        inspector = inspect(self.engine)
        all_schemas = inspector.get_schema_names()
        if SCHEMA_DB not in all_schemas:
            logging.warning(f"Schema {SCHEMA_DB} does not exists")
            return False
        logging.warning(f"Schema {SCHEMA_DB} already exists")
        return True

    def _create_schema(self) -> None:
        self.engine.execute(CreateSchema(SCHEMA_DB))
        logging.warning(f"Schema {SCHEMA_DB} created")

    def engine_connection(self) -> create_engine:
        """ Set the engine related to the DB """
        if not self._check_if_schema_exists():
            self._create_schema()
        engine = create_engine(
            f"{DB_DRIVER}://{USERNAME}:{PASSWORD}@{HOST}/{SCHEMA_DB}", echo=False
            )
        logging.warning("DB engine connection")
        return engine

    def create_db_session(self, engine: create_engine):
        """ Create a session for DB communcation"""
        session_maker = sessionmaker(engine)
        session = session_maker()
        logging.warning("Session created")
        return session

    def insert_to_table(self, table: str, session, **entry_fields):
        """" """
        tables = {
            "DashboardSession": schema.insert_to_dashboard,
            "Athletes": schema.insert_to_athletes,
            }
        insert_function = tables.get(table)
        logging.warning(f"Table: {table}, Entry: {entry_fields}")
        try:
            insert_function(session, entry_fields)
        except Exception as excp:
            logging.error(excp)


def main():
    db_connector = DBConnector()
    engine = db_connector.engine_connection()

    # Create an active session within the engine
    session = db_connector.create_db_session(engine)

    # Clear all the tables
    schema.Base.metadata.drop_all(engine)
    # Create tables defined in tables.py as classes
    schema.Base.metadata.create_all(engine)

    # Insert an entry to dashboard sessions table
    # schema.insert_to_dashboard(session, 'bewolfish')
    db_connector.insert_to_table(
        'DashboardSession', session, session_name='bewolfish'
        )

    # Get the session id for ForeignKey
    query_result = session.query(schema.DashboardSessions).filter(
        schema.DashboardSessions.session_name == 'bewolfish'
        )
    for item in query_result:
        current_session_id = item.id
        print(current_session_id)

    # Insert entries to athletes table
    db_connector.insert_to_table(
        'Athletes',
        session,
        name='Mario',
        surname='Perez',
        age=22,
        sport='Run',
        session_id=current_session_id
        )
    db_connector.insert_to_table(
        'Athletes',
        session,
        name='Pep',
        surname='Lopez',
        sport='Bike',
        session_id=current_session_id
        )
    db_connector.insert_to_table(
        'Athletes',
        session,
        name='Reynaldo',
        surname='Gerardez',
        age=50,
        sport='Marathon',
        session_id=current_session_id
        )

    query_result = session.query(schema.Athletes)
    result = query_result.filter(
        schema.Athletes.session_id == current_session_id
        )
    for item in result:
        print(item.sport)


if __name__ == '__main__':
    main()
