from __future__ import unicode_literals
from moto.core.responses import BaseResponse
from .models import efs_backends
import json


class EFSResponse(BaseResponse):
    SERVICE_NAME = 'efs'
    @property
    def efs_backend(self):
        return efs_backends[self.region]

    
    def create_file_system(self):
        creation_token = self._get_param("CreationToken")
        performance_mode = self._get_param("PerformanceMode")
        encrypted = self._get_param("Encrypted")
        kms_key_id = self._get_param("KmsKeyId")
        throughput_mode = self._get_param("ThroughputMode")
        provisioned_throughput_in_mibps = self._get_param("ProvisionedThroughputInMibps")
        tags = self._get_list_prefix("Tags.member")
        owner_id, creation_token, file_system_id, creation_time, life_cycle_state, name, number_of_mount_targets, size_in_bytes, performance_mode, encrypted, kms_key_id, throughput_mode, provisioned_throughput_in_mibps, tags = self.efs_backend.create_file_system(
            creation_token=creation_token,
            performance_mode=performance_mode,
            encrypted=encrypted,
            kms_key_id=kms_key_id,
            throughput_mode=throughput_mode,
            provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
            tags=tags,
        )
        # TODO: adjust response
        return json.dumps(dict(ownerId=owner_id, creationToken=creation_token, fileSystemId=file_system_id, creationTime=creation_time, lifeCycleState=life_cycle_state, name=name, numberOfMountTargets=number_of_mount_targets, sizeInBytes=size_in_bytes, performanceMode=performance_mode, encrypted=encrypted, kmsKeyId=kms_key_id, throughputMode=throughput_mode, provisionedThroughputInMibps=provisioned_throughput_in_mibps, tags=tags))
    # add methods from here


# add templates from here
