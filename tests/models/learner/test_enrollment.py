#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select
from hercsis.models.institutions import District
from hercsis.models.learner import Enrollment, Registration


def test_enrollment(db_session_factory,
                    example_persons,
                    example_schools):

    with db_session_factory() as session:
        registration = Registration(student=example_persons[0],
                                    district=example_schools[0].district,
                                    student_number=112358)
        enrollment = Enrollment(registration=registration,
                                school=example_schools[0])
        session.add(enrollment)

        sought = session.scalars(
            select(Enrollment)
            .join(Registration)
            .join(District)
            .where(District.nickname == example_schools[0].district.nickname)
        ).first()

        assert sought.registration.student.full_name == example_persons[0].full_name