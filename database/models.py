from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm  import relationship
import sqlalchemy as sa
import datetime
import sqlalchemy.orm as so
from sqlalchemy.dialects.postgresql import UUID


from sqlalchemy import MetaData


class Base(so.DeclarativeBase):
    pass
class Client(Base):
    __tablename__ = "client",

    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    first_name: so.Mapped[str] = so.mapped_column(sa.String(75), nullable=False)
    last_name: so.Mapped[str] = so.mapped_column(sa.String(75), nullable=False)
    middle_name: so.Mapped[str] = so.mapped_column(sa.String(75), nullable=False)
    phone: so.Mapped[str] = so.mapped_column(sa.String(20), nullable=False)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: so.Mapped[str] = so.mapped_column(
        sa.String(length=1024), nullable=False
    )
    is_active: so.Mapped[bool] = so.mapped_column(nullable=False)
    birth_date: so.Mapped[datetime.date]=so.mapped_column( nullable=False)

##class Tokens(Base):
 ##   __tablename__="tokens"
 ##   id: so.Mapped [int]=so.mapped_column(primary_key=True, autoincrement=True)
##    token: so.Mapped[str]=so.mapped_column( UUID(as_uuid=False),
 ##       server_default=sa.text("uuid_generate_v4()"),
 ##       unique=True,
 ##       nullable=False,
 ##       index=True)
    ##expires: so.Mapped[datetime]=so.mapped_column(nullable=False)
 ##   client_id: so.Mapped[int]=so.mapped_column(sa.ForeignKey(Client.id))
## room_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("room.id"), nullable=False) или примерно так
 ##   room: so.Mapped[Room] = so.relationship()


