#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.person import Person
from hercsis.models.communication import PhoneNumber


def test_phone_number(db_session_factory, example_persons):
    with db_session_factory() as session:

        session.add(PhoneNumber(person=example_persons[0],
                                digits=14145551234,
                                is_mobile=True,
                                can_text=True))

        sought = session.scalars(
            select(PhoneNumber)
            .join(Person)
            .where(Person.full_name.contains("er"))
        ).first()

        assert sought.is_mobile
        assert sought.can_text
        assert sought.digits == 14145551234
        assert sought.person.full_name == "Bert"

        assert str(sought) == "1 (414) 555-1234"
