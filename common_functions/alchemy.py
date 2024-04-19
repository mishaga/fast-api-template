from typing import Final

from sqlalchemy.exc import IntegrityError

PG_FOREIGN_KEY_VIOLATION_CODE: Final[str] = '23503'
PG_UNIQUE_VIOLATION_CODE: Final[str] = '23505'


def is_fk_violation(exc: IntegrityError) -> bool:
    """Check if an exception was a "violates foreign key constraint"."""
    return getattr(exc.orig, 'pgcode', None) == PG_FOREIGN_KEY_VIOLATION_CODE


def is_unique_violation(exc: IntegrityError) -> bool:
    """Check if an exception was a Unique violation error."""
    return getattr(exc.orig, 'pgcode', None) == PG_UNIQUE_VIOLATION_CODE
