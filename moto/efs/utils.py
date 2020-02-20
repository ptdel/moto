from __future__ import unicode_literals
import random
import string
from datetime import datetime


def random_id(length=8):
    chars = string.ascii_lowercase + string.digits
    plug = "".join([random.choice(chars) for _ in range(length)])
    return plug

def random_file_system_id(length=8):
    return "fs-" + random_id(length)

def random_mount_target_id(length=8):
    return "fsmt-" + random_id(length)

def random_access_point_id(length=17):
    return "fsap-" + random_id(length)

def aws_date_time():
    return int((datetime.now() - datetime(1970, 1, 1)).total_seconds())

def get_name_tag(tags):
    for tag in tags:
        if tag["Key"] == "Name":
            return tag["Value"]