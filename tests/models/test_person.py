#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.person import Person


def test_my_understanding_of_select(db_session_factory, example_persons):
    assert len(example_persons) == 4

    with db_session_factory() as session:
        session.add_all(example_persons)
        people = session.scalars(select(Person)).all()
        assert len(people) == 4


def test_person_naming(db_session_factory):
    with db_session_factory() as session:
        bert = Person(pk=42, full_name="Albert")
        ernie = Person(pk=41, full_name="Ernest")

        session.add_all([bert, ernie])

        some_guy = session.scalars(
            select(Person).where(Person.full_name.contains("nest"))
        ).first()

        assert some_guy.full_name == ernie.full_name

        both_guys = session.scalars(
            select(Person)
            .order_by(Person.pk)
        ).all()

        assert len(both_guys) == 2
        assert repr(both_guys[0]) == "Person(pk=41, full_name='Ernest')"
        assert str(both_guys[1]) == "Albert"
