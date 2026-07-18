from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Unit(Base , TimestampMixin):
    
    __tablename__ = "units"

    id : Mapped[int] = mapped_column(primary_key=True)

    name : Mapped[str] = mapped_column(
        String(50),
        index= True,
        nullable = False
    )
    unit_type_id : Mapped[int] = mapped_column(
        ForeignKey(
            "unit_types.id"
        ) # type category of unit 
    )

    parent_unit : Mapped[int | None] = mapped_column(
        ForeignKey("units.id")
        ) # parent unit id for hierarchy self-reference 
    
    nationality_id : Mapped[int | None] = mapped_column(
        Integer,
        nullable = True

    )

    state_id : Mapped[int] = mapped_column(
        ForeignKey("states.id")
    )
    
    district_id : Mapped[int] = mapped_column(
        ForeignKey("districts.id")
    )

    active : Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    state : Mapped["State"] = relationship(
        back_populates="units"
    )

    district : Mapped["District"] = relationship(
        back_populates = "units"
    )

    unit_type : Mapped["UnitType"] = relationship(
        back_populates="units"
    )

    parent : Mapped["Unit | None"] = relationship(
        remote_side = [id],
        
    )