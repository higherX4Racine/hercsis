#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""Fixtures for testing the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pytest

from hercsis.models import database_metadata
from hercsis.models.institutions import (
    District,
    School,
)
from hercsis.models.person import Person


@pytest.fixture(scope="session")
def db_url():
    return "sqlite://"


@pytest.fixture(scope="session")
def db_engine(db_url):
    engine = create_engine(db_url)
    database_metadata.create_all(engine)
    return engine


@pytest.fixture(scope="session")
def db_session_factory(db_engine):
    return sessionmaker(db_engine)

@pytest.fixture(scope="package")
def example_persons():
    return [
        Person(pk=i, full_name=n)
        for i, n
        in enumerate([
            "Bert",
            "Ernie",
            "Grover",
            "Oscar"
        ])
    ]

@pytest.fixture(scope="function")
def example_districts():
    return [
        District(
            pk=3060,
            name="Nashua School District",
            nickname="Nashua",
            federal_id=3304980,
            state_id=371
        ),
        District(
            pk=53495,
            name="Racine Unified School District",
            nickname="RUSD",
            federal_id=5512360,
            state_id=4620
        ),
    ]


@pytest.fixture(scope="function")
def example_schools(example_districts):
    return [
        School(
            pk=42,
            name="Charlotte Avenue School",
            nickname="CAS",
            federal_id=315,
            state_id=21930,
            district=example_districts[0]
        ),
        School(
            pk=99,
            name="Jerome I. Case Senior High School",
            nickname="Case",
            federal_id=1621,
            state_id=491,
            district=example_districts[1]
        ),
    ]
