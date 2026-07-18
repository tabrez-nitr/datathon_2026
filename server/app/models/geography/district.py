from sqlalchemy import String , ForeignKey , Boolean
from sqlalchemy.orm import Mapped , mapped_column , relationship

from app.models.base import Base
from app.models.base import TimestampMixin

class District(Base , TimestampMixin):

    __tablename__ = "districts"

    id : Mapped[int] = mapped_column(primary_key = True)

    # name of the district 
    name : Mapped[str] = mapped_column(
        String(100) ,#max length of the string
        unique=True,
        index= True
    )

    state_id : Mapped[int] = mapped_column(
        ForeignKey("states.id")
    )

    active : Mapped[bool] = mapped_column(
        Boolean,
        nullable = False
    )

    state : Mapped["State"] = relationship(
        back_populates="districts"
    )

    units : Mapped[list["Unit"]] =relationship(
       back_populates = "district"
    )


   

    