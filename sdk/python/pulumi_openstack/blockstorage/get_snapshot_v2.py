# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'GetSnapshotV2Result',
    'AwaitableGetSnapshotV2Result',
    'get_snapshot_v2',
]

@pulumi.output_type
class GetSnapshotV2Result:
    """
    A collection of values returned by getSnapshotV2.
    """
    def __init__(__self__, description=None, id=None, metadata=None, most_recent=None, name=None, region=None, size=None, status=None, volume_id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if volume_id and not isinstance(volume_id, str):
            raise TypeError("Expected argument 'volume_id' to be a str")
        pulumi.set(__self__, "volume_id", volume_id)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The snapshot's description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, Any]:
        """
        The snapshot's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> float:
        """
        The size of the snapshot.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "volume_id")


class AwaitableGetSnapshotV2Result(GetSnapshotV2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotV2Result(
            description=self.description,
            id=self.id,
            metadata=self.metadata,
            most_recent=self.most_recent,
            name=self.name,
            region=self.region,
            size=self.size,
            status=self.status,
            volume_id=self.volume_id)


def get_snapshot_v2(most_recent: Optional[bool] = None,
                    name: Optional[str] = None,
                    region: Optional[str] = None,
                    status: Optional[str] = None,
                    volume_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotV2Result:
    """
    Use this data source to get information about an existing snapshot.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    snapshot1 = openstack.blockstorage.get_snapshot_v2(most_recent=True,
        name="snapshot_1")
    ```


    :param bool most_recent: Pick the most recently created snapshot if there
           are multiple results.
    :param str name: The name of the snapshot.
    :param str region: The region in which to obtain the V2 Block Storage
           client. If omitted, the `region` argument of the provider is used.
    :param str status: The status of the snapshot.
    :param str volume_id: The ID of the snapshot's volume.
    """
    __args__ = dict()
    __args__['mostRecent'] = most_recent
    __args__['name'] = name
    __args__['region'] = region
    __args__['status'] = status
    __args__['volumeId'] = volume_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:blockstorage/getSnapshotV2:getSnapshotV2', __args__, opts=opts, typ=GetSnapshotV2Result).value

    return AwaitableGetSnapshotV2Result(
        description=__ret__.description,
        id=__ret__.id,
        metadata=__ret__.metadata,
        most_recent=__ret__.most_recent,
        name=__ret__.name,
        region=__ret__.region,
        size=__ret__.size,
        status=__ret__.status,
        volume_id=__ret__.volume_id)
