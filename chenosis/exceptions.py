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


class ChenosisAPIError(ChenosisException):
    """
    Raised for client and server side errors
    """

    pass
