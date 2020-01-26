from __future__ import unicode_literals
from moto.core.exceptions import RESTError


class AccessPointAlreadyExists(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class AccessPointLimitExceeded(RESTError):
    """ """
    code = 403

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class AccessPointNotFound(RESTError):
    """ """
    code = 404

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class BadRequest(RESTError):
    """ Something Bad! """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class DependencyTimeout(RESTError):
    """ """
    code = 504

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class FileSystemAlreadyExists(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class FileSystemInUse(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class FileSystemLimitExceeded(RESTError):
    """ """
    code = 403

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class FileSystemNotFound(RESTError):
    """ """
    code = 404

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class IncorrectFileSystemLifeCycleState(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class IncorrectMountTargetState(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class InsufficientThroughputCapacity(RESTError):
    """ """
    code = 503

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class InternalServerError(RESTError):
    """ """
    code = 500

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class IpAddressInUse(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class MountTargetConflict(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class MountTargetNotFound(RESTError):
    """ """
    code = 404

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class NetworkInterfaceLimitExceeded(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class NoFreeAddressesInSubnet(RESTError):
    """ """
    code = 409

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class PolicyNotFound(RESTError):
    """ """
    code = 404

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class SecurityGroupLimitExceeded(RESTError):
    """ """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class SecurityGroupNotFound(RESTError):
    """ """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class SubnetNotFound(RESTError):
    """ """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class ThroughputLimitExceeded(RESTError):
    """ """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class TooManyRequests(RESTError):
    """ """
    code = 429

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)


class UnsupportedAvailabilityZone(RESTError):
    """ """
    code = 400

    def __init__(self):
        super().__init__(self.__class__.__name__, self.__doc__)
