import os

import logging
logger = logging.getLogger(__name__)


# Return an environment variable (allow "text" booleans)
def getenv(var, default=None):
    result = os.environ.get(var, default)
    logger.debug("[ENV] {}={}".format(var, result))
    if isinstance(result, (bool, int, list, tuple)) or not result:
        return result
    if result.upper() == "TRUE":
        return True
    elif result.upper() == "FALSE":
        return False
    elif result.upper() == "NONE" or result.strip() == "":
        return None
    if ',' in result:
        return list(filter(lambda x: x, (i.strip() for i in result.split(','))))
    try:
        return int(result)
    except ValueError:
        pass
    return result


__all__ = ("getenv", )
