from sqlalchemy import String, DateTime , ForeignKey
from app.models.base import Base , TimestampMixin
from sqlalchemy.orm import Mapped , mapped_column , relationship


class PoliceStation(Base , TimestampMixin):

    __tablename__ = "police_stations"

    id : Mapped[int] = mapped_column(primary_key = True)

    name : Mapped[str] = mapped_column(
        String(100),
        unique = True,
        index = True,
        nullable = False
    )

    district_id : Mapped[int] = mapped_column(
        ForeignKey("districts.id"),
        nullable = False
    )

    district : Mapped["District"] = relationship(
        back_populates = "police_stations"
    )


