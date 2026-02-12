from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class TripPlannerState(Base):
    __tablename__ = "trip_planner_state"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    current_step = Column(String, default="STARTING_CITY")
    source = Column(String, nullable=True)
    destination = Column(String, nullable=True)
    days = Column(String, nullable=True)
    vibe = Column(String, nullable=True)
    budget = Column(String, nullable=True)
    people = Column(String, nullable=True)
    itinerary = Column(String, nullable=True)

    user = relationship("User")
