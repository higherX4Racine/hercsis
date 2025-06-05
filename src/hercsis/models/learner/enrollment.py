from sqlalchemy import ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel


class Enrollment(BaseModel):
    r"""One student identity for tracking through an academic career.

    Attributes
    ----------
    registration: Registration
        one person moving through an academic career
    school: School
        the authority supervising the person's education
    """

    __tablename__ = "enrollment"

    student_pk: Mapped[int] = mapped_column()
    district_pk: Mapped[int] = mapped_column()
    registration: Mapped["Registration"] = relationship(foreign_keys=[student_pk, district_pk])

    school_pk: Mapped[int] = mapped_column(ForeignKey("school.pk"))
    school: Mapped["School"] = relationship(foreign_keys=[school_pk])

    __table_args__ = (
        PrimaryKeyConstraint("student_pk", "district_pk", "school_pk"),
        ForeignKeyConstraint(["student_pk", "district_pk"],
                             ["registration.student_pk", "registration.district_pk"]),
    )
