from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class State(Base):

    __tablename__ = "states"

    id : Mapped[int] = mapped_column(primary_key=True)

    name : Mapped[str] = mapped_column(
        String(50),
        unique = True,
        nullable = False,
        index=True
    )

    nationality_id : Mapped[int | None] = mapped_column(Integer, nullable=True)
    active : Mapped[bool] = mapped_column(
        Boolean,
        default = True
    )
    
    districts : Mapped[list["District"]]=relationship(
        back_populates="state"
    )

    units : Mapped[list["Unit"]] = relationship(
        back_populates = "state"
    )
    