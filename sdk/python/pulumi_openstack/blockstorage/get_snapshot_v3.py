# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetSnapshotV3Result:
    """
    A collection of values returned by getSnapshotV3.
    """
    def __init__(__self__, description=None, id=None, metadata=None, most_recent=None, name=None, region=None, size=None, status=None, volume_id=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The snapshot's description.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        __self__.metadata = metadata
        """
        The snapshot's metadata.
        """
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        __self__.most_recent = most_recent
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        See Argument Reference above.
        """
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        __self__.size = size
        """
        The size of the snapshot.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        See Argument Reference above.
        """
        if volume_id and not isinstance(volume_id, str):
            raise TypeError("Expected argument 'volume_id' to be a str")
        __self__.volume_id = volume_id
        """
        See Argument Reference above.
        """
class AwaitableGetSnapshotV3Result(GetSnapshotV3Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotV3Result(
            description=self.description,
            id=self.id,
            metadata=self.metadata,
            most_recent=self.most_recent,
            name=self.name,
            region=self.region,
            size=self.size,
            status=self.status,
            volume_id=self.volume_id)

def get_snapshot_v3(most_recent=None,name=None,region=None,status=None,volume_id=None,opts=None):
    """
    Use this data source to get information about an existing snapshot.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    snapshot1 = openstack.blockstorage.get_snapshot_v3(most_recent=True,
        name="snapshot_1")
    ```


    :param bool most_recent: Pick the most recently created snapshot if there
           are multiple results.
    :param str name: The name of the snapshot.
    :param str region: The region in which to obtain the V3 Block Storage
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
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:blockstorage/getSnapshotV3:getSnapshotV3', __args__, opts=opts).value

    return AwaitableGetSnapshotV3Result(
        description=__ret__.get('description'),
        id=__ret__.get('id'),
        metadata=__ret__.get('metadata'),
        most_recent=__ret__.get('mostRecent'),
        name=__ret__.get('name'),
        region=__ret__.get('region'),
        size=__ret__.get('size'),
        status=__ret__.get('status'),
        volume_id=__ret__.get('volumeId'))
