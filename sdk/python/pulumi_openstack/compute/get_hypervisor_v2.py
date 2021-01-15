# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetHypervisorV2Result',
    'AwaitableGetHypervisorV2Result',
    'get_hypervisor_v2',
]

@pulumi.output_type
class GetHypervisorV2Result:
    """
    A collection of values returned by getHypervisorV2.
    """
    def __init__(__self__, disk=None, host_ip=None, hostname=None, id=None, memory=None, state=None, status=None, type=None, vcpus=None):
        if disk and not isinstance(disk, int):
            raise TypeError("Expected argument 'disk' to be a int")
        pulumi.set(__self__, "disk", disk)
        if host_ip and not isinstance(host_ip, str):
            raise TypeError("Expected argument 'host_ip' to be a str")
        pulumi.set(__self__, "host_ip", host_ip)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if memory and not isinstance(memory, int):
            raise TypeError("Expected argument 'memory' to be a int")
        pulumi.set(__self__, "memory", memory)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vcpus and not isinstance(vcpus, int):
            raise TypeError("Expected argument 'vcpus' to be a int")
        pulumi.set(__self__, "vcpus", vcpus)

    @property
    @pulumi.getter
    def disk(self) -> int:
        """
        The amount in GigaBytes of local storage the hypervisor can provide
        """
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter(name="hostIp")
    def host_ip(self) -> str:
        """
        The IP address of the Hypervisor
        """
        return pulumi.get(self, "host_ip")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        """
        The number in MegaBytes of memory the hypervisor can provide
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the hypervisor (`up` or `down`)
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the hypervisor (`enabled` or `disabled`)
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the hypervisor (example: `QEMU`)
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vcpus(self) -> int:
        """
        The number of virtual CPUs the hypervisor can provide
        """
        return pulumi.get(self, "vcpus")


class AwaitableGetHypervisorV2Result(GetHypervisorV2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHypervisorV2Result(
            disk=self.disk,
            host_ip=self.host_ip,
            hostname=self.hostname,
            id=self.id,
            memory=self.memory,
            state=self.state,
            status=self.status,
            type=self.type,
            vcpus=self.vcpus)


def get_hypervisor_v2(hostname: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHypervisorV2Result:
    """
    Use this data source to get information about hypervisors
    by hostname.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    host01 = openstack.compute.get_hypervisor_v2(hostname="host01")
    ```


    :param str hostname: The hostname of the hypervisor
    """
    __args__ = dict()
    __args__['hostname'] = hostname
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:compute/getHypervisorV2:getHypervisorV2', __args__, opts=opts, typ=GetHypervisorV2Result).value

    return AwaitableGetHypervisorV2Result(
        disk=__ret__.disk,
        host_ip=__ret__.host_ip,
        hostname=__ret__.hostname,
        id=__ret__.id,
        memory=__ret__.memory,
        state=__ret__.state,
        status=__ret__.status,
        type=__ret__.type,
        vcpus=__ret__.vcpus)
