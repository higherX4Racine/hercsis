#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""this doesn't actually need testing I'm just practicing."""

from sqlalchemy import MetaData

from hercsis.models.base import database_metadata


def test_base_model_metadata():
    r"""Verify that the shortcut to the database's metadata exists."""

    assert type(database_metadata) == MetaData
