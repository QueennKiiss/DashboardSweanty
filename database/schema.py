""" Module containing schema database"""

import logging
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

Base = declarative_base()


class DashboardSessions(Base):
    """Class to create a table with all the dashboard sessions created"""
    __tablename__ = 'dashboard_sessions'

    id = Column(Integer(), primary_key=True)
    session_name = Column(String(50), nullable=False)
    session_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return f"Session {self.session_name} started at {self.session_date}"


def insert_to_dashboard(session: Session, session_name: dict) -> None:
    """ Insert entries to dashboard table"""
    try:
        name = session_name.get('session_name')
        entry = DashboardSessions(session_name=name)
        session.add(entry)
        session.commit()
    except Exception as excp:
        logging.error(excp)


class Athletes(Base):
    """Class to create an athletes table"""
    __tablename__ = 'athletes'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    surnames = Column(String(10))
    age = Column(Integer())
    sport = Column(String(50), nullable=False)
    session_id = Column(
        Integer(),
        ForeignKey("dashboard_sessions.id", ondelete="CASCADE"),
        nullable=False
        )
    # Property for crossed information between related tables. Not real column
    session = relationship("DashboardSessions")

    def __str__(self):
        return f"Athlete: {self.name} {self.surnames} Belongs to sessions: {self.session}"


def insert_to_athletes(session: Session, entry_args: dict) -> None:
    """ Insert entries to Athletes table"""
    try:
        entry = Athletes(
            name=entry_args.get('name'),
            surnames=entry_args.get('surname'),
            age=int(entry_args.get('age')),
            sport=entry_args.get('sport'),
            session_id=entry_args.get('session_id'))
        session.add(entry)
        session.commit()
    except Exception as excp:
        logging.error(excp)
