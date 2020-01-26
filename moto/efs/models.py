from __future__ import unicode_literals
from boto3 import Session
from moto.core import BaseBackend, BaseModel
from .utils import random_file_system_id, aws_date_time, get_name_tag


class BaseObject(BaseModel):
    """ BaseObject for All EFS DataTypes """

    def pascal_case(self, attr):
        """ EFS Datatypes and their attributes are all *PascalCase* """
        return "".join([word.title() for word in attr.split("_")])

    def response(self):
        """ Return instances of this class as a dict with PascalCase'd keys """
        return {self.pascal_case(k): v for k, v in self.__dict__.items()}


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

    def __repr__(self):
        return self.response()

    @property
    def physical_resource_id(self):
        return self.name


class CreationInfo(BaseObject):
    def __init__(self, owner_gid, owner_uid, permissions):
        self.owner_gid = owner_gid
        self.owner_uid = owner_uid
        self.permissions = permissions

    def __repr__(self):
        return self.response()


class FileSystemDescription(BaseObject):
    def __init__(
        self,
        creation_time=None,
        creation_token=None,
        encrypted=None,
        file_system_id=None,
        kms_key_id=None,
        life_cycle_state=None,
        name=None,
        number_of_mount_targets=None,
        owner_id=None,
        performance_mode=None,
        provisioned_throughput_in_mibps=None,
        size_in_bytes=None,
        tags=None,
        throughput_mode=None,
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

    def __repr__(self):
        return self.response()

    @property
    def physical_resource_id(self):
        return self.name


class FileSystemSize(BaseObject):
    def __init__(self, timestamp, value, value_in_I_A, value_in_standard):
        self.timestamp = timestamp
        self.value = value
        self.value_in_I_A = value_in_I_A
        self.value_in_standard = value_in_standard

    def __repr__(self):
        return self.response()


class LifeCyclePolicy(BaseObject):
    def __init__(self, transition_to_IA):
        self.transition_to_IA = transition_to_IA

    def __repr__(self):
        return self.response()


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

    def __repr__(self):
        return self.response()


class PosixUser(BaseObject):
    def __init__(self, gid, secondary_gids, uid):
        self.gid = gid
        self.secondary_gids = secondary_gids
        self.uid = uid

    def __repr__(self):
        return self.response()


class RootDirectory(BaseObject):
    def __init__(self, creation_info, path):
        self.creation_info = creation_info
        self.path = path

    def __repr__(self):
        return self.response()


class Tag(BaseObject):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return self.response()


class EFSBackend(BaseBackend):
    def __init__(self, region_name=None):
        super(EFSBackend, self).__init__()
        self.region_name = region_name
        self.access_points = {}
        self.file_systems = {}
        self.file_system_policies = {}
        self.lifecycle_configurations = {}
        self.mount_targets = {}
        self.mount_target_security_groups = {}
        self.tags = {}

    def reset(self):
        region_name = self.region_name
        self.__dict__ = {}
        self.__init__(region_name)

    def create_access_point(
        self, *, client_token, tags, file_system_id, posix_user, root_directory
    ):
        pass

    def create_file_system(
        self,
        *,
        creation_token,
        encrypted=None,
        kms_key_id=None,
        performance_mode=None,
        provisioned_throughput_in_mibps=None,
        tags=None,
        throughput_mode=None,
    ):

        file_system = FileSystemDescription(
            owner_id="123456789012",
            creation_time=aws_date_time(),
            creation_token=creation_token,
            encrypted=encrypted or False,
            file_system_id=random_file_system_id(),
            number_of_mount_targets=0,
            life_cycle_state="available",
            kms_key_id=kms_key_id,
            size_in_bytes=FileSystemSize(
                timestamp=aws_date_time(),
                value=6144,
                value_in_I_A=0,
                value_in_standard=6144,
            ).response(),
            performance_mode=performance_mode or "generalPurpose",
            provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
            tags=tags,
            throughput_mode=throughput_mode or "bursting",
            name=get_name_tag(tags),
        )

        self.file_systems[file_system.file_system_id] = file_system.response()
        return file_system.response()

    def create_mount_target(
        self, *, file_system_id, subnet_id, ip_address, security_groups
    ):
        pass

    def create_tags(self, *, file_system_id, tags):
        pass

    def delete_access_point(self, *, access_point_id):
        pass

    def delete_file_system(self, *, file_system_id):
        pass

    def delete_file_system_policy(self, *, file_system_id):
        pass

    def delete_mount_target(self, *, mount_target_id):
        pass

    def delete_tags(self, *, file_system_id, tag_keys):
        pass

    def describe_access_points(
        self, *, max_results, next_token, access_point_id, file_system_id
    ):
        pass

    def describe_file_system_policy(self, *, file_system_id):
        pass

    def describe_file_systems(
        self, *, max_items, marker, creation_token, file_system_id
    ):
        pass

    def describe_lifecycle_configuration(self, *, file_system_id):
        pass

    def describe_mount_target_security_groups(self, *, mount_target_id):
        pass

    def describe_mount_targets(
        self, *, max_items, marker, file_system_id, mount_target_id, access_point_id
    ):
        pass

    def describe_tags(self, *, max_items, marker, file_system_id):
        pass

    def list_tags_for_resource(self, *, resourcde_id, max_results, next_token):
        pass

    def modify_mount_target_security_groups(self, *, mount_target_id, security_groups):
        pass

    def put_file_system_policy(
        self, *, file_system_id, policy, bypass_policy_lockout_safety_check
    ):
        pass

    def put_lifecycle_configuration(self, *, file_system_id, lifecycle_policies):
        pass

    def tag_resources(self, *, resource_id, tags):
        pass

    def untag_resource(self, *, resource_id, tag_keys):
        pass

    def update_file_system(
        self, *, file_system_id, throughput_mode, provisioned_throughput_in_mibps
    ):
        pass


efs_backends = {}
for region in Session().get_available_regions("efs"):
    efs_backends[region] = EFSBackend()
for region in Session().get_available_regions("efs", partition_name="aws-us-gov"):
    efs_backends[region] = EFSBackend()
for region in Session().get_available_regions("efs", partition_name="aws-cn"):
    efs_backends[region] = EFSBackend()
