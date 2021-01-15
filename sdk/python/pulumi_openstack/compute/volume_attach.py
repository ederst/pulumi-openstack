# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['VolumeAttach']


class VolumeAttach(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 multiattach: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 vendor_options: Optional[pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches a Block Storage Volume to an Instance using the OpenStack
        Compute (Nova) v2 API.

        ## Example Usage
        ### Basic attachment of a single volume to a single instance

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.VolumeV2("volume1", size=1)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            volume_id=volume1.id)
        ```
        ### Using Multiattach-enabled volumes

        Multiattach Volumes are dependent upon your OpenStack cloud and not all
        clouds support multiattach.

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.Volume("volume1",
            multiattach=True,
            size=1)
        instance1 = openstack.compute.Instance("instance1", security_groups=["default"])
        instance2 = openstack.compute.Instance("instance2", security_groups=["default"])
        va1 = openstack.compute.VolumeAttach("va1",
            instance_id=instance1.id,
            multiattach=True,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"])
        va2 = openstack.compute.VolumeAttach("va2",
            instance_id=instance2.id,
            multiattach=True,
            volume_id=openstack_blockstorage_volume_v2["volume_1"]["id"],
            opts=pulumi.ResourceOptions(depends_on=["openstack_compute_volume_attach_v2.va_1"]))
        ```

        It is recommended to use `depends_on` for the attach resources
        to enforce the volume attachments to happen one at a time.

        ## Import

        Volume Attachments can be imported using the Instance ID and Volume ID separated by a slash, e.g.

        ```sh
         $ pulumi import openstack:compute/volumeAttach:VolumeAttach va_1 89c60255-9bd6-460c-822a-e2b959ede9d2/45670584-225f-46c3-b33e-6707b589b666
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] device: See Argument Reference above. _NOTE_: The correctness of this
               information is dependent upon the hypervisor in use. In some cases, this
               should not be used as an authoritative piece of information.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['device'] = device
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['multiattach'] = multiattach
            __props__['region'] = region
            __props__['vendor_options'] = vendor_options
            if volume_id is None and not opts.urn:
                raise TypeError("Missing required property 'volume_id'")
            __props__['volume_id'] = volume_id
        super(VolumeAttach, __self__).__init__(
            'openstack:compute/volumeAttach:VolumeAttach',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            device: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            multiattach: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            vendor_options: Optional[pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']]] = None,
            volume_id: Optional[pulumi.Input[str]] = None) -> 'VolumeAttach':
        """
        Get an existing VolumeAttach resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] device: See Argument Reference above. _NOTE_: The correctness of this
               information is dependent upon the hypervisor in use. In some cases, this
               should not be used as an authoritative piece of information.
        :param pulumi.Input[str] instance_id: The ID of the Instance to attach the Volume to.
        :param pulumi.Input[bool] multiattach: Enable attachment of multiattach-capable volumes.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a volume attachment. If omitted, the
               `region` argument of the provider is used. Changing this creates a
               new volume attachment.
        :param pulumi.Input[pulumi.InputType['VolumeAttachVendorOptionsArgs']] vendor_options: Map of additional vendor-specific options.
               Supported options are described below.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["device"] = device
        __props__["instance_id"] = instance_id
        __props__["multiattach"] = multiattach
        __props__["region"] = region
        __props__["vendor_options"] = vendor_options
        __props__["volume_id"] = volume_id
        return VolumeAttach(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def device(self) -> pulumi.Output[str]:
        """
        See Argument Reference above. _NOTE_: The correctness of this
        information is dependent upon the hypervisor in use. In some cases, this
        should not be used as an authoritative piece of information.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Instance to attach the Volume to.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def multiattach(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable attachment of multiattach-capable volumes.
        """
        return pulumi.get(self, "multiattach")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a volume attachment. If omitted, the
        `region` argument of the provider is used. Changing this creates a
        new volume attachment.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="vendorOptions")
    def vendor_options(self) -> pulumi.Output[Optional['outputs.VolumeAttachVendorOptions']]:
        """
        Map of additional vendor-specific options.
        Supported options are described below.
        """
        return pulumi.get(self, "vendor_options")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[str]:
        """
        The ID of the Volume to attach to an Instance.
        """
        return pulumi.get(self, "volume_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

