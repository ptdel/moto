from __future__ import unicode_literals

import sure  # noqa

import moto.server as server
from moto import mock_efs

"""
Test the different server responses
"""


@mock_efs
def test_efs_list():
    backend = server.create_backend_app("efs")
    test_client = backend.test_client()
    # do test
