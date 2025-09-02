from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.shared.data_source.postgres_con import Base    

class Story (Base):

    __tablename__ = "stories"
    
    id = Column(Integer, primary_key=True, index=True )
    title  = Column(String, index=True)
    theme = Column(String, index=True)
    session_id= Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now() )
    world_des = Column(String, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # nullable para guests
    player_id = Column(Integer, ForeignKey("players.id"), nullable=True)

    player = relationship("Player", back_populates="story")
    user= relationship("User", back_populates="stories")
    chapters = relationship("Chapter", back_populates="story")
