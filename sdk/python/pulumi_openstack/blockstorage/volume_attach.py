# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['VolumeAttach']


class VolumeAttach(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attach_mode: Optional[pulumi.Input[str]] = None,
                 device: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 initiator: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 multipath: Optional[pulumi.Input[bool]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 wwnn: Optional[pulumi.Input[str]] = None,
                 wwpns: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource is experimental and may be removed in the future! Feedback
        is requested if you find this resource useful or if you find any problems
        with it.

        Creates a general purpose attachment connection to a Block
        Storage volume using the OpenStack Block Storage (Cinder) v3 API.
        Depending on your Block Storage service configuration, this
        resource can assist in attaching a volume to a non-OpenStack resource
        such as a bare-metal server or a remote virtual machine in a
        different cloud provider.

        This does not actually attach a volume to an instance. Please use
        the `compute.VolumeAttach` resource for that.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        volume1 = openstack.blockstorage.Volume("volume1", size=1)
        va1 = openstack.blockstorage.VolumeAttach("va1",
            device="auto",
            host_name="devstack",
            initiator="iqn.1993-08.org.debian:01:e9861fb1859",
            ip_address="192.168.255.10",
            os_type="linux2",
            platform="x86_64",
            volume_id=volume1.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attach_mode: Specify whether to attach the volume as Read-Only
               (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
               If left unspecified, the Block Storage API will apply a default of `rw`.
        :param pulumi.Input[str] device: The device to tell the Block Storage service this
               volume will be attached as. This is purely for informational purposes.
               You can specify `auto` or a device such as `/dev/vdc`.
        :param pulumi.Input[str] host_name: The host to attach the volume to.
        :param pulumi.Input[str] initiator: The iSCSI initiator string to make the connection.
        :param pulumi.Input[str] ip_address: The IP address of the `host_name` above.
        :param pulumi.Input[bool] multipath: Whether to connect to this volume via multipath.
        :param pulumi.Input[str] os_type: The iSCSI initiator OS type.
        :param pulumi.Input[str] platform: The iSCSI initiator platform.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Block Storage
               client. A Block Storage client is needed to create a volume attachment.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new volume attachment.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        :param pulumi.Input[str] wwnn: A wwnn name. Used for Fibre Channel connections.
        :param pulumi.Input[List[pulumi.Input[str]]] wwpns: An array of wwpn strings. Used for Fibre Channel
               connections.
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

            __props__['attach_mode'] = attach_mode
            __props__['device'] = device
            if host_name is None:
                raise TypeError("Missing required property 'host_name'")
            __props__['host_name'] = host_name
            __props__['initiator'] = initiator
            __props__['ip_address'] = ip_address
            __props__['multipath'] = multipath
            __props__['os_type'] = os_type
            __props__['platform'] = platform
            __props__['region'] = region
            if volume_id is None:
                raise TypeError("Missing required property 'volume_id'")
            __props__['volume_id'] = volume_id
            __props__['wwnn'] = wwnn
            __props__['wwpns'] = wwpns
            __props__['data'] = None
            __props__['driver_volume_type'] = None
            __props__['mount_point_base'] = None
        super(VolumeAttach, __self__).__init__(
            'openstack:blockstorage/volumeAttach:VolumeAttach',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attach_mode: Optional[pulumi.Input[str]] = None,
            data: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            device: Optional[pulumi.Input[str]] = None,
            driver_volume_type: Optional[pulumi.Input[str]] = None,
            host_name: Optional[pulumi.Input[str]] = None,
            initiator: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            mount_point_base: Optional[pulumi.Input[str]] = None,
            multipath: Optional[pulumi.Input[bool]] = None,
            os_type: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            volume_id: Optional[pulumi.Input[str]] = None,
            wwnn: Optional[pulumi.Input[str]] = None,
            wwpns: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> 'VolumeAttach':
        """
        Get an existing VolumeAttach resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attach_mode: Specify whether to attach the volume as Read-Only
               (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
               If left unspecified, the Block Storage API will apply a default of `rw`.
        :param pulumi.Input[Mapping[str, Any]] data: This is a map of key/value pairs that contain the connection
               information. You will want to pass this information to a provisioner
               script to finalize the connection. See below for more information.
        :param pulumi.Input[str] device: The device to tell the Block Storage service this
               volume will be attached as. This is purely for informational purposes.
               You can specify `auto` or a device such as `/dev/vdc`.
        :param pulumi.Input[str] driver_volume_type: The storage driver that the volume is based on.
        :param pulumi.Input[str] host_name: The host to attach the volume to.
        :param pulumi.Input[str] initiator: The iSCSI initiator string to make the connection.
        :param pulumi.Input[str] ip_address: The IP address of the `host_name` above.
        :param pulumi.Input[str] mount_point_base: A mount point base name for shared storage.
        :param pulumi.Input[bool] multipath: Whether to connect to this volume via multipath.
        :param pulumi.Input[str] os_type: The iSCSI initiator OS type.
        :param pulumi.Input[str] platform: The iSCSI initiator platform.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Block Storage
               client. A Block Storage client is needed to create a volume attachment.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new volume attachment.
        :param pulumi.Input[str] volume_id: The ID of the Volume to attach to an Instance.
        :param pulumi.Input[str] wwnn: A wwnn name. Used for Fibre Channel connections.
        :param pulumi.Input[List[pulumi.Input[str]]] wwpns: An array of wwpn strings. Used for Fibre Channel
               connections.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["attach_mode"] = attach_mode
        __props__["data"] = data
        __props__["device"] = device
        __props__["driver_volume_type"] = driver_volume_type
        __props__["host_name"] = host_name
        __props__["initiator"] = initiator
        __props__["ip_address"] = ip_address
        __props__["mount_point_base"] = mount_point_base
        __props__["multipath"] = multipath
        __props__["os_type"] = os_type
        __props__["platform"] = platform
        __props__["region"] = region
        __props__["volume_id"] = volume_id
        __props__["wwnn"] = wwnn
        __props__["wwpns"] = wwpns
        return VolumeAttach(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachMode")
    def attach_mode(self) -> Optional[str]:
        """
        Specify whether to attach the volume as Read-Only
        (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
        If left unspecified, the Block Storage API will apply a default of `rw`.
        """
        return pulumi.get(self, "attach_mode")

    @property
    @pulumi.getter
    def data(self) -> Mapping[str, Any]:
        """
        This is a map of key/value pairs that contain the connection
        information. You will want to pass this information to a provisioner
        script to finalize the connection. See below for more information.
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def device(self) -> Optional[str]:
        """
        The device to tell the Block Storage service this
        volume will be attached as. This is purely for informational purposes.
        You can specify `auto` or a device such as `/dev/vdc`.
        """
        return pulumi.get(self, "device")

    @property
    @pulumi.getter(name="driverVolumeType")
    def driver_volume_type(self) -> str:
        """
        The storage driver that the volume is based on.
        """
        return pulumi.get(self, "driver_volume_type")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The host to attach the volume to.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def initiator(self) -> Optional[str]:
        """
        The iSCSI initiator string to make the connection.
        """
        return pulumi.get(self, "initiator")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[str]:
        """
        The IP address of the `host_name` above.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="mountPointBase")
    def mount_point_base(self) -> str:
        """
        A mount point base name for shared storage.
        """
        return pulumi.get(self, "mount_point_base")

    @property
    @pulumi.getter
    def multipath(self) -> Optional[bool]:
        """
        Whether to connect to this volume via multipath.
        """
        return pulumi.get(self, "multipath")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The iSCSI initiator OS type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def platform(self) -> Optional[str]:
        """
        The iSCSI initiator platform.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region in which to obtain the V3 Block Storage
        client. A Block Storage client is needed to create a volume attachment.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new volume attachment.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> str:
        """
        The ID of the Volume to attach to an Instance.
        """
        return pulumi.get(self, "volume_id")

    @property
    @pulumi.getter
    def wwnn(self) -> Optional[str]:
        """
        A wwnn name. Used for Fibre Channel connections.
        """
        return pulumi.get(self, "wwnn")

    @property
    @pulumi.getter
    def wwpns(self) -> Optional[List[str]]:
        """
        An array of wwpn strings. Used for Fibre Channel
        connections.
        """
        return pulumi.get(self, "wwpns")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

