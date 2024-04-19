import os


def is_test() -> bool:
    """Return True if tests are running.

    Returns:
        bool (True/False)
    """
    raw_value = os.getenv('UNIT_TESTS', default='')
    env_value = raw_value.strip().lower()
    return env_value == 'true'
