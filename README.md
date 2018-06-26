# dockerimageupdate
Update local images from registry with same tag. Does not cleanup dangling images. For cleanup, use

```bash
docker rmi $(docker images -f "dangling=true" -q)
```

## Installation
Docker python library is required. See installation instructions [here](https://github.com/docker/docker-py)

## Usage
./dockerupdate.py
