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


def insert_to_dashboard(session: Session, session_name: str) -> None:
    """ Insert entries to dashboard table"""
    entry = DashboardSessions(session_name=session_name)
    session.add(entry)
    session.commit()


class Athletes(Base):
    """Class to create an athletes table"""
    __tablename__ = 'athletes'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    surnames = Column(String(10))
    session_id = Column(
        Integer(),
        ForeignKey("dashboard_sessions.id", ondelete="CASCADE"),
        nullable=False
        )
    # Property for crossed information between related tables. Not real column
    session = relationship("DashboardSessions")

    def __str__(self):
        return f"Athlete: {self.name} {self.surnames} Belongs to sessions: {self.session}"


def insert_to_athletes(session: Session, entry_args: tuple) -> None:
    """ Insert entries to Athletes table"""
    try:
        name, surname, dashboard_session = entry_args
        entry = Athletes(name=name, surnames=surname, session_id=dashboard_session)
        session.add(entry)
        session.commit()
    except Exception as excp:
        logging.error(excp)
