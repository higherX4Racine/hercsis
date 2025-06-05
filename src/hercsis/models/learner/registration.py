from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel


class Registration(BaseModel):
    r"""One student identity for tracking through an academic career.

    Attributes
    ----------
    student: Person
        one person moving through an academic career
    district: District
        the authority supervising the person's education
    student_number: int
        a unique identifier for anonymously reporting about the student 
    """

    __tablename__ = "registration"

    student_pk: Mapped[int] = mapped_column(ForeignKey("person.pk"),
                                            primary_key=True)
    student: Mapped["Person"] = relationship()

    district_pk: Mapped[int] = mapped_column(ForeignKey("district.pk"),
                                             primary_key=True)
    district: Mapped["District"] = relationship()

    student_number: Mapped[int]
