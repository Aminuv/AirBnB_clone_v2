#!/usr/bin/python3
"""
    generates a .tgz archive
"""
from datetime import datetime
from os import path
from fabric.decorators import runs_once
from fabric.api import local, env, put, run


env.hosts = ['52.90.14.193', '54.90.50.39']

env.user = "ubuntu"

env.key_filename = "~/.ssh/id_rsa"


@runs_once
def do_pack():
    """
      The fabfile to create and distribute an archive to a web server.
    """

    local("mkdir -p versions")
    dformat = "%Y%m%d%H%M%S"
    arch_path = "versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), dformat))
    result = local("tar -cvzf {} web_static".format(arch_path))
    if result.failed:
        return None
    return arch_path


def do_deploy(arch_path):
    """ A distributes of an archive to your web servers """

    try:
        if not path.exists(arch_path):
            return False

        _path = "/data/web_static/releases/"
        filename = path.basename(arch_path)
        file_n_ext, ext = path.splitext(filename)
        put(arch_path, "/tmp/{}".format(filename))
        run("rm -rf {}{}".format(_path, file_n_ext))
        run("mkdir -p {}{}".format(_path, file_without_ext))
        run("tar -xzf /tmp/{} -C {}{}".format(filename, _path, file_n_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(_path, file_n_ext))
        run("rm -rf {}{}/web_static".format(_path, file_n_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(
            _path, file_n_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
