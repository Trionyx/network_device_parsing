from typing import List, Dict
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from misc.config import Config


class Base(DeclarativeBase):
    pass


class Itemtypes(Base):
    __tablename__ = "itemtypes"
    itemtype_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    partnumber: Mapped[str] = mapped_column(String(50))  # Артикул
    description: Mapped[str] = mapped_column(String(200))
    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.vendor_id"))

    def __repr__(self) -> str:
        return f"Item(id={self.itemtype_id!r}, name={self.name!r}, description={self.description!r})"


class Ditemtypes(Base):
    __tablename__ = "ditemtypes"
    itemtype_id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(2000))

    def __repr__(self) -> str:
        return f"itemtype_id(itemtype_id={self.itemtype_id!r})"


# example = create_engine('mysql://username:password@localhost/mydatabase')
# engine = create_engine('mysql://p521889_alex568:dI5yO7oG1m@185.105.110.5/p521889_alex568')

# connect to local database file
engine = create_engine(Config.FTP_HOST)

# example
# def write_to_db(data: Dict[Itemtypes]) -> None:
#     """
#     Write data to database
#     :param data: dictionary with data
#     :return:
#     """
#     with Session(engine) as session:
#         spongebob = User(
#             name="spongebob",
#             fullname="Spongebob Squarepants",
#             addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#         )
#         sandy = User(
#             name="sandy",
#             fullname="Sandy Cheeks",
#             addresses=[
#                 Address(email_address="sandy@sqlalchemy.org"),
#                 Address(email_address="sandy@squirrelpower.org"),
#             ],
#         )
#         patrick = User(name="patrick", fullname="Patrick Star")
#         session.add_all([spongebob, sandy, patrick])
#         session.commit()

