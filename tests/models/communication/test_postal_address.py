#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.person import Person
from hercsis.models.communication import PostalAddress


def test_email_address(db_session_factory, example_persons):
    with db_session_factory() as session:
        session.add(PostalAddress(person=example_persons[2],
                                  street="221B Baker Street",
                                  municipality="London",
                                  state="England",
                                  code="401835"))

        sought = session.scalars(
            select(PostalAddress)
            .join(Person)
            .where(Person.full_name.contains("er"))
        ).first()

        assert sought.person.full_name == "Grover"
        assert str(sought) == "221B Baker Street\nLondon, England 401835"
