from __future__ import unicode_literals
from boto3 import Session
from moto.core import BaseBackend, BaseModel


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
