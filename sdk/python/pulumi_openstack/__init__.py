# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import importlib
# Make subpackages available:
__all__ = ['blockstorage', 'compute', 'config', 'containerinfra', 'database', 'dns', 'firewall', 'identity', 'images', 'keymanager', 'loadbalancer', 'networking', 'objectstorage', 'orchestration', 'sharedfilesystem', 'vpnaas']
for pkg in __all__:
    if pkg != 'config':
        importlib.import_module(f'{__name__}.{pkg}')

# Export this package's modules as members:
from .provider import *
