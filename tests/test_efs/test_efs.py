from __future__ import unicode_literals

import boto3
import sure  # noqa
from moto import mock_efs


@mock_efs
def test_create_file_system_type_bursting():
    client = boto3.client("efs", region_name="us-east-1")
    file_system = client.create_file_system(
        creation_token="testing-e72ab305-4828-45e7-8d06-0318d54ffdd7",
        encrypted=True,
        kms_key_id="1234abcd-12ab-34cd-56ef-1234567890ab",
        performance_mode="maxIO",
        tags=[{"Key":"Name", "Value": "BurstFS"}],
        throughput_mode="bursting"
    )
    file_system.should.be(True)