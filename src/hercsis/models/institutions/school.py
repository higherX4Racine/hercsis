#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""A school is one individual school building/campus."""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel
from .institution import Institution


class School(Institution, BaseModel):
    r"""A school building or other atomic administrative unit."""
    __tablename__ = "school"

    pk: Mapped[int] = mapped_column(primary_key=True)
    district_pk: Mapped[int] = mapped_column(ForeignKey("district.pk"))
    district: Mapped["District"] = relationship()
