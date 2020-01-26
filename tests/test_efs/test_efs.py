from __future__ import unicode_literals

import boto3
import sure  # noqa
from nose.tools import raises
from moto import mock_efs
from datetime import datetime


@mock_efs
def test_create_file_system_type_bursting():
    client = boto3.client("efs", region_name="us-east-1")
    file_system = client.create_file_system(
        CreationToken="testing-e72ab305-4828-45e7-8d06-0318d54ffdd7",
        Encrypted=True,
        KmsKeyId="1234abcd-12ab-34cd-56ef-1234567890ab",
        PerformanceMode="maxIO",
        Tags=[{"Key":"Name", "Value": "BurstFS"}],
        ThroughputMode="bursting"
    )
    file_system["OwnerId"].should.be.equal("123456789012")
    file_system["CreationToken"].should.equal("testing-e72ab305-4828-45e7-8d06-0318d54ffdd7")
    file_system["FileSystemId"].should.contain("fs-")
    file_system["FileSystemId"].should.have.length_of(11)
    file_system["CreationTime"].should.be.a(datetime)
    file_system["LifeCycleState"].should.equal("available")
    file_system["Name"].should.equal("BurstFS")
    file_system["NumberOfMountTargets"].should.equal(0)
    file_system["SizeInBytes"]["Value"].should.equal(6144)
    file_system["SizeInBytes"]["Timestamp"].should.be.a(datetime)
    file_system["SizeInBytes"]["ValueInIA"].should.equal(0)
    file_system["SizeInBytes"]["ValueInStandard"].should.equal(6144)
    file_system["PerformanceMode"].should.equal("maxIO")
    file_system["Encrypted"].should.equal(True)
    file_system["KmsKeyId"].should.equal("1234abcd-12ab-34cd-56ef-1234567890ab")
    file_system["ThroughputMode"].should.equal("bursting")
    file_system["Tags"].should.equal([{"Key":"Name","Value":"BurstFS"}])

@mock_efs
def test_create_file_system_type_provisioned():
    client = boto3.client("efs", region_name="us-east-1")
    file_system = client.create_file_system(
        CreationToken="testing-f72ab305-4828-45e7-8d06-0318d54ffdd7",
        Encrypted=False,
        KmsKeyId="1234abcd-22ab-34cd-56ef-1234567890ab",
        PerformanceMode="generalPurpose",
        Tags=[{"Key":"Name", "Value": "ProvisionedFS"}],
        ThroughputMode="provisioned",
        ProvisionedThroughputInMibps=123,
    )
    file_system["OwnerId"].should.be.equal("123456789012")
    file_system["CreationToken"].should.equal("testing-f72ab305-4828-45e7-8d06-0318d54ffdd7")
    file_system["FileSystemId"].should.contain("fs-")
    file_system["FileSystemId"].should.have.length_of(11)
    file_system["CreationTime"].should.be.a(datetime)
    file_system["LifeCycleState"].should.equal("available")
    file_system["Name"].should.equal("ProvisionedFS")
    file_system["NumberOfMountTargets"].should.equal(0)
    file_system["SizeInBytes"]["Value"].should.equal(6144)
    file_system["SizeInBytes"]["Timestamp"].should.be.a(datetime)
    file_system["SizeInBytes"]["ValueInIA"].should.equal(0)
    file_system["SizeInBytes"]["ValueInStandard"].should.equal(6144)
    file_system["PerformanceMode"].should.equal("generalPurpose")
    file_system["Encrypted"].should.equal(False)
    file_system["KmsKeyId"].should.equal("1234abcd-22ab-34cd-56ef-1234567890ab")
    file_system["ThroughputMode"].should.equal("provisioned")
    file_system["Tags"].should.equal([{"Key":"Name","Value":"ProvisionedFS"}])
    file_system["ProvisionedThroughputInMibps"].should.equal(123)

@raises(Exception)
@mock_efs
def test_create_file_system_type_provisioned_failure():
    client = boto3.client("efs", region_name="us-east-1")
    client.create_file_system(
        CreationToken="testing-f72ab305-4828-45e7-8d06-0318d54ffdd7",
        Encrypted=False,
        KmsKeyId="1234abcd-22ab-34cd-56ef-1234567890ab",
        PerformanceMode="generalPurpose",
        Tags=[{"Key":"Name", "Value": "ProvisionedFS"}],
        ThroughputMode="provisioned",
    )