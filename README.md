# torchserve-docker
TorchServe Docker images with specific Python version working out of the box.

TorchServe's official docker image `pytorch/torchserve:latest-(cpu/gpu)` uses Python 3.9 as default.
One can get around that by, for example, using that as a base image and building a virtual environment (eg with conda) with another supported Python version (eg 3.10).  
The goal of this cron job is to save you that work by providing you with an image that works with the desired Python version out of the box, for example `pytorch/torchserve:latest-(cpu/gpu)-python-3.10`.  

This is a daily cron job that simply mirrors the official TorchServe repository using their Dockerfile and scripts to build the images, producing ready to use images with the desired Python version (3.8, 3.9 or 3.10).  
Thus, any issues or requests regarding the content of the images should addressed directly on the [official torchserce github repository](https://github.com/pytorch/serve)


## Tags
In general, the available tags are the same that you can find on the [official torchserve dockerhub repository](https://hub.docker.com/r/pytorch/torchserve/tags) plus a suffix that signals the python version like so `pytorch/torchserve:<TAG>` --> `fabridamicelli/torchserve:<TAG>-python<VERSION>`, where `TAG` is usually something like `0.6.1-gpu`.
The `rolling` version is built everyday with the very latest state of the code in the [TorchServe repo](https://github.com/pytorch/serve).

The current TorchServe officially released version (0.7.1) has some bugs in the [Dockerfile](https://github.com/pytorch/serve/pull/2202) and the [build script](https://github.com/pytorch/serve/pull/2226) that have been addressed and should be available starting from version 0.7.2.
So for now there are only `rolling` tags available which have `torchserve==0.7.1`, but are not the exact code state that was released.
Starting from TorchServe release 0.7.2, each tag will exactly mirror the code state tagged with the release.


Current tags examples:

| official                      |               `python3.8`                    |                `python3.9`                   |                    `python3.10`                |
| ---- | ---- | ---- | ---- |
|`pytorch/torchserve:0.7.1-cpu` |`fabridamicelli/torchserve:rolling-python3.8` |`fabridamicelli/torchserve:rolling-python3.9` | `fabridamicelli/torchserve:rolling-python3.10` |
| ---- | ---- | ---- | ---- |
|`pytorch/torchserve:0.7.1-gpu` |`fabridamicelli/torchserve:rolling-python3.8` |`fabridamicelli/torchserve:rolling-python3.9` | `fabridamicelli/torchserve:rolling-python3.10` |


## TODO
- Update tags logic after official release 0.7.2
