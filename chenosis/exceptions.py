class ChenosisException(Exception):
    """
    Base class for Chenosis Library
    """
    pass

class InvalidCredentials(ChenosisException):
    """
    Raised after failing to authenticate with Chenosis API
    """
    pass