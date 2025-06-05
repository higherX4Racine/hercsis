#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.person import Person
from hercsis.models.communication import EmailAddress


def test_phone_number(db_session_factory, example_persons):
    with db_session_factory() as session:

        session.add(EmailAddress(person=example_persons[1],
                                text="hello@example.com"))

        sought = session.scalars(
            select(EmailAddress)
            .join(Person)
            .where(Person.full_name.contains("er"))
        ).first()

        assert sought.person.full_name == "Ernie"
        assert str(sought) == "hello@example.com"
