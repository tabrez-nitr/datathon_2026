
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin



class UnitType(Base):
    """
this is for Police station ,
Circle Office ,
District Office ,
State Office 
"""

    __tablename__ = "unit_types"

    id : Mapped[int] = mapped_column(primary_key=True)

    name : Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,

    )
    city_dist_state : Mapped[str] = mapped_column(
        String(30),  # where it operates 
    )

    hierarchy : Mapped[int] = mapped_column(Integer)
    # lower number means higher hierarchy
    # police station = 5
    # circle office = 4
    # district office = 3
    # state office = 1
    
    active : Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    units : Mapped["Unit"] = relationship(
        back_populates = "unit_type"
    )


    

