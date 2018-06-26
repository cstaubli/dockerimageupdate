#!/usr/bin/env python

import docker
import subprocess

client = docker.from_env()

info = client.info()

images = client.images.list()

for image in images:
    for a in image.attrs.items():
        repostr = ""
        if isinstance(a[1], dict) or isinstance(a[1], list):
            for sub in a[1]:
                if a[0] == "RepoTags":
                    repostr = sub
                pass
            pass
        else:
            pass
        if repostr != "":
            print ("docker pull " + repostr)
            child = subprocess.Popen(["docker", "pull", repostr])
            child.wait()
            pass
