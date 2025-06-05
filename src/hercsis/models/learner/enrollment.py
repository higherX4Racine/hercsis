from sqlalchemy import ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel
from .student import Student
from ..institutions import School


class Enrollment(BaseModel):
    r"""One student identity for tracking through an academic career.

    DANGER! Nothing in the ORM code currently constrains the Student's
    District to actually match the School's District.

    Attributes
    ----------
    student: Student
        one person moving through an academic career
    school: School
        the authority supervising the person's education
    """

    __tablename__ = "enrollment"

    person_pk: Mapped[int] = mapped_column()
    district_pk: Mapped[int] = mapped_column()
    student: Mapped["Student"] = relationship(foreign_keys=[person_pk, district_pk])

    school_pk: Mapped[int] = mapped_column(ForeignKey("school.pk"))
    school: Mapped["School"] = relationship(foreign_keys=[school_pk])

    __table_args__ = (
        PrimaryKeyConstraint("person_pk", "district_pk", "school_pk"),
        ForeignKeyConstraint(["person_pk", "district_pk"],
                             ["student.person_pk", "student.district_pk"]),
    )