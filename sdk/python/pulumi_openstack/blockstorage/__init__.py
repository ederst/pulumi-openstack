# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_availability_zones_v3 import *
from .get_snapshot_v2 import *
from .get_snapshot_v3 import *
from .get_volume_v2 import *
from .get_volume_v3 import *
from .quote_set_v2 import *
from .quote_set_v3 import *
from .volume import *
from .volume_attach import *
from .volume_attach_v2 import *
from .volume_v1 import *
from .volume_v2 import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "openstack:blockstorage/quoteSetV2:QuoteSetV2":
                return QuoteSetV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/quoteSetV3:QuoteSetV3":
                return QuoteSetV3(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/volume:Volume":
                return Volume(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/volumeAttach:VolumeAttach":
                return VolumeAttach(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/volumeAttachV2:VolumeAttachV2":
                return VolumeAttachV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/volumeV1:VolumeV1":
                return VolumeV1(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:blockstorage/volumeV2:VolumeV2":
                return VolumeV2(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("openstack", "blockstorage/quoteSetV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/quoteSetV3", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/volume", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/volumeAttach", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/volumeAttachV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/volumeV1", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "blockstorage/volumeV2", _module_instance)

_register_module()
