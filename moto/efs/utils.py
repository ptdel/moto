from __future__ import unicode_literals
import random
import string
# import six
from datetime import datetime
from dateutil.tz import tzlocal



def random_file_system_id(length=8):
    chars = string.ascii_lowercase + string.digits
    plug = "".join([random.choice(chars) for _ in range(length)])
    return "fs-" + plug

def aws_date_time():
    return datetime.now(tzlocal()).replace(microsecond=0)