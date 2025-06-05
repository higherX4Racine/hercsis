#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.institutions import District, School


def test_school(db_session_factory, example_schools):
    with db_session_factory() as session:
        session.add_all(example_schools)
        districts = session.scalars(
            select(District).order_by(District.pk)
        ).all()

        assert len(districts) == 2

        charlotte_ave = session.scalars(
            select(School)
            .join(District)
            .where(District.name.contains("Nashua"))
        ).first()

        assert charlotte_ave.state_id == 21930

        case = session.scalars(
            select(School)
            .join(District)
            .where(District.state_id == 4620)
        ).first()

        assert case.nickname == "Case"
