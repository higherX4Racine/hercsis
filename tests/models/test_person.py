#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.person import Person


def test_person_naming(db_session_factory):

    with db_session_factory() as session:
        bert = Person(pk=42, full_name="Albert")
        ernie = Person(pk=41, full_name="Ernest")

        session.add_all([bert, ernie])

        some_guy = session.scalars(
            select(Person).where(Person.full_name.contains("nest"))
        ).first()

        assert some_guy.full_name == ernie.full_name
