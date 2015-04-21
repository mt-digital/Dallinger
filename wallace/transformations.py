from models import Transformation

"""
See class Transmission in models.py for the base class Transmission.
This file stores a list of all the subclasses of Transformation made available by default.
Note that they don't necessarily tell you anything about the nature in which two Info's
relate to each other, but if used sensibly they will do so.
"""


class Replication(Transformation):

    """The identity transformation."""

    __mapper_args__ = {"polymorphic_identity": "replication"}


class Mutation(Transformation):

    """The mutation transformation."""

    __mapper_args__ = {"polymorphic_identity": "mutation"}


class Observation(Transformation):

    """The observation transformation."""

    __mapper_args__ = {"polymorphic_identity": "observation"}
