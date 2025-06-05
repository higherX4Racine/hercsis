#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

from hercsis.models.institutions import District
from hercsis.models.learner import Student


def test_student(db_session_factory,
                 example_districts,
                 example_persons):
    with db_session_factory() as session:
        original = Student(person=example_persons[0],
                           district=example_districts[0],
                           student_number=112358)
        session.add(original)

        sought = session.scalars(
            select(Student)
            .join(District)
            .where(District.pk == example_districts[0].pk)
        ).first()

        assert sought.person.full_name == original.person.full_name
