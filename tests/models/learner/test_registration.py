#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.institutions import District
from hercsis.models.learner import Registration


def test_registration(db_session_factory,
                      example_districts,
                      example_persons):
    with db_session_factory() as session:
        original = Registration(student=example_persons[0],
                                district=example_districts[0],
                                student_number=112358)
        session.add(original)

        sought = session.scalars(
            select(Registration)
            .join(District)
            .where(District.pk == example_districts[0].pk)
        ).first()

        assert sought.student.full_name == original.student.full_name
