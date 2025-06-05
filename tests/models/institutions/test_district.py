#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.institutions import District


def test_district(db_session_factory, example_districts):

    with db_session_factory() as session:
        session.add_all(example_districts)

        districts = session.scalars(select(District).order_by(District.pk)).all()

        assert districts[0].nickname == "Nashua"
        assert districts[1].nickname == "RUSD"
