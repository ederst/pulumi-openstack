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

__all__ = ['VolumeV1']


class VolumeV1(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 source_vol_id: Optional[pulumi.Input[str]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V1 volume resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.VolumeV1("volume1",
            description="first test volume",
            region="RegionOne",
            size=3)
        ```

        ## Import

        Volumes can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:blockstorage/volumeV1:VolumeV1 volume_1 ea257959-eeb1-4c10-8d33-26f0409a755d
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: The availability zone for the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] description: A description of the volume. Changing this updates
               the volume's description.
        :param pulumi.Input[str] image_id: The image ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[Mapping[str, Any]] metadata: Metadata key/value pairs to associate with the volume.
               Changing this updates the existing volume metadata.
        :param pulumi.Input[str] name: A unique name for the volume. Changing this updates the
               volume's name.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new volume.
        :param pulumi.Input[int] size: The size of the volume to create (in gigabytes). Changing
               this creates a new volume.
        :param pulumi.Input[str] snapshot_id: The snapshot ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] source_vol_id: The volume ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] volume_type: The type of volume to create.
               Changing this creates a new volume.
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

            __props__['availability_zone'] = availability_zone
            __props__['description'] = description
            __props__['image_id'] = image_id
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['region'] = region
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['snapshot_id'] = snapshot_id
            __props__['source_vol_id'] = source_vol_id
            __props__['volume_type'] = volume_type
            __props__['attachments'] = None
        super(VolumeV1, __self__).__init__(
            'openstack:blockstorage/volumeV1:VolumeV1',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attachments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeV1AttachmentArgs']]]]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            image_id: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            snapshot_id: Optional[pulumi.Input[str]] = None,
            source_vol_id: Optional[pulumi.Input[str]] = None,
            volume_type: Optional[pulumi.Input[str]] = None) -> 'VolumeV1':
        """
        Get an existing VolumeV1 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VolumeV1AttachmentArgs']]]] attachments: If a volume is attached to an instance, this attribute will
               display the Attachment ID, Instance ID, and the Device as the Instance
               sees it.
        :param pulumi.Input[str] availability_zone: The availability zone for the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] description: A description of the volume. Changing this updates
               the volume's description.
        :param pulumi.Input[str] image_id: The image ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[Mapping[str, Any]] metadata: Metadata key/value pairs to associate with the volume.
               Changing this updates the existing volume metadata.
        :param pulumi.Input[str] name: A unique name for the volume. Changing this updates the
               volume's name.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new volume.
        :param pulumi.Input[int] size: The size of the volume to create (in gigabytes). Changing
               this creates a new volume.
        :param pulumi.Input[str] snapshot_id: The snapshot ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] source_vol_id: The volume ID from which to create the volume.
               Changing this creates a new volume.
        :param pulumi.Input[str] volume_type: The type of volume to create.
               Changing this creates a new volume.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attachments"] = attachments
        __props__["availability_zone"] = availability_zone
        __props__["description"] = description
        __props__["image_id"] = image_id
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["region"] = region
        __props__["size"] = size
        __props__["snapshot_id"] = snapshot_id
        __props__["source_vol_id"] = source_vol_id
        __props__["volume_type"] = volume_type
        return VolumeV1(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attachments(self) -> pulumi.Output[Sequence['outputs.VolumeV1Attachment']]:
        """
        If a volume is attached to an instance, this attribute will
        display the Attachment ID, Instance ID, and the Device as the Instance
        sees it.
        """
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        The availability zone for the volume.
        Changing this creates a new volume.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the volume. Changing this updates
        the volume's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[str]]:
        """
        The image ID from which to create the volume.
        Changing this creates a new volume.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Metadata key/value pairs to associate with the volume.
        Changing this updates the existing volume metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the volume. Changing this updates the
        volume's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to create the volume. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new volume.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the volume to create (in gigabytes). Changing
        this creates a new volume.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[Optional[str]]:
        """
        The snapshot ID from which to create the volume.
        Changing this creates a new volume.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="sourceVolId")
    def source_vol_id(self) -> pulumi.Output[Optional[str]]:
        """
        The volume ID from which to create the volume.
        Changing this creates a new volume.
        """
        return pulumi.get(self, "source_vol_id")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[str]:
        """
        The type of volume to create.
        Changing this creates a new volume.
        """
        return pulumi.get(self, "volume_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

