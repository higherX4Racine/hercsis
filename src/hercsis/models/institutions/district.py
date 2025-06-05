#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""A school district contains one or more individual school buildings."""

from sqlalchemy.orm import Mapped, mapped_column

from ..base import BaseModel
from .institution import Institution


class District(Institution, BaseModel):
    r"""A school district or consortium of private schools."""
    __tablename__ = "district"

    pk: Mapped[int] = mapped_column(primary_key=True)
