#!/usr/bin/env python

import docker
import subprocess

client = docker.from_env()

info = client.info()

images = client.images.list()

for image in images:
    repostr = image.attrs.get("RepoTags")
    if isinstance(repostr, list) and len(repostr) > 0:
        repostr = repostr[0]
        if repostr != "":
            print("docker pull " + repostr)
            child = subprocess.Popen(["docker", "pull", repostr])
            pass
        pass
