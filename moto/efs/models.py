from __future__ import unicode_literals
from boto3 import Session
from moto.core import BaseBackend, BaseModel


class BaseObject(BaseModel):
    """ BaseObject for All EFS DataTypes """

    def pascal_case(self, attr):
        """ EFS Datatypes and their attributes are all PascalCase """
        return "".join([word.title() for word in attr.split("_")])

    def __get__(self, instance, owner):
        """ Return instances of this class as a dict with PascalCase'd keys """
        return {self.pascal_case(k):v for k,v in instance.__dict__.items()}


class AccessPointDescription(BaseObject):

    def __init__(
        self,
        access_point_arn,
        access_point_id,
        client_token,
        file_system_id,
        life_cycle_state,
        name,
        owner_id,
        posix_user,
        root_directory,
        tags,
        ):

        self.access_point_arn = access_point_arn
        self.access_point_id = access_point_id
        self.client_token = client_token
        self.file_system_id = file_system_id
        self.life_cycle_state = life_cycle_state
        self.name = name
        self.owner_id = owner_id
        self.posix_user = posix_user
        self.root_directory = root_directory
        self.tags = tags


class CreationInfo(BaseObject):

    def __init__(self, owner_gid, owner_uid, permissions):
        self.owner_gid = owner_gid
        self.owner_uid = owner_uid
        self.permissions = permissions


class FileSystemDescription(BaseObject):

    def __init__(
        self,
        creation_time,
        creation_token,
        encrypted,
        file_system_id,
        kms_key_id,
        life_cycle_state,
        name,
        number_of_mount_targets,
        owner_id,
        performance_mode,
        provisioned_throughput_in_mibps,
        size_in_bytes,
        tags,
        throughput_mode,
        ):

        self.creation_time = creation_time
        self.creation_token = creation_token
        self.encrypted = encrypted
        self.file_system_id = file_system_id
        self.kms_key_id = kms_key_id
        self.life_cycle_state = life_cycle_state
        self.name = name
        self.number_of_mount_targets = number_of_mount_targets
        self.owner_id = owner_id
        self.performance_mode = performance_mode
        self.provisioned_throughput_in_mibps = provisioned_throughput_in_mibps
        self.size_in_bytes = size_in_bytes
        self.tags = tags
        self.throughput_mode = throughput_mode


class FileSystemSize(BaseObject):

    def __init__(self, timestamp, value, value_in_IA, value_in_standard):
        self.timestamp = timestamp
        self.value = value
        self.value_in_IA = value_in_IA
        self.value_in_standard = value_


class LifeCyclePolicy(BaseObject):

    def __init__(self, transition_to_IA):
        self.transition_to_IA = transition_to_IA


class MountTargetDescription(BaseObject):

    def __init__(
        self,
        availability_zone_id,
        availability_zone_name,
        file_system_id,
        ip_address,
        life_cycle_state,
        mount_target_id,
        network_interface_id,
        owner_id,
        subnet_id,
        ):
    
        self.availability_zone_id = availability_zone_id
        self.availability_zone_name = availability_zone_name
        self.file_system_id = file_system_id
        self.ip_address = ip_address
        self.life_cycle_state = life_cycle_state
        self.mount_target_id = mount_target_id
        self.network_interface_id = network_interface_id
        self.owner_id = owner_id
        self.subnet_id = subnet_id


class PosixUser(BaseObject):

    def __init__(self, gid, secondary_gids, uid):
        self.gid = gid
        self.secondary_gids = secondary_gids
        self.uid = uid


class RootDirectory(BaseObject):

    def __init__(self, creation_info, path):
        self.creation_info = creation_info
        self.path = path


class Tag(BaseObject):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class EFSBackend(BaseBackend):
    def __init__(self, region_name=None):
        super(EFSBackend, self).__init__()
        self.region_name = region_name

    def reset(self):
        region_name = self.region_name
        self.__dict__ = {}
        self.__init__(region_name)

    def create_file_system(self, creation_token, performance_mode, encrypted, kms_key_id, throughput_mode, provisioned_throughput_in_mibps, tags):
        # implement here
        return owner_id, creation_token, file_system_id, creation_time, life_cycle_state, name, number_of_mount_targets, size_in_bytes, performance_mode, encrypted, kms_key_id, throughput_mode, provisioned_throughput_in_mibps, tags
    
    # add methods from here


efs_backends = {}
for region in Session().get_available_regions("efs"):
    efs_backends[region] = EFSBackend()
for region in Session().get_available_regions("efs", partition_name="aws-us-gov"):
    efs_backends[region] = EFSBackend()
for region in Session().get_available_regions("efs", partition_name="aws-cn"):
    efs_backends[region] = EFSBackend()
