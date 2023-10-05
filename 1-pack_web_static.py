#!/usr/bin/python3
"""
    generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """
        method doc.
    """

    local("mkdir -p versions")
    dformat = "%Y%m%d%H%M%S"
    arch_path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), dformat))
    result = local("tar -cvzf {} web_static".format(arch_path))
    if result.failed:
        return None
    return arch_path
