from sqlalchemy.orm import Declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BIGINT  

class Base(Declarative_base):
    id = Mapped[int] = mapped_column(BIGINT(55), primary_key=True)

