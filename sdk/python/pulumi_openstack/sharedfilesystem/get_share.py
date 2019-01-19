# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetShareResult(object):
    """
    A collection of values returned by getShare.
    """
    def __init__(__self__, availability_zone=None, description=None, export_locations=None, is_public=None, metadata=None, name=None, project_id=None, region=None, share_network_id=None, share_proto=None, size=None, snapshot_id=None, status=None, id=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError('Expected argument availability_zone to be a str')
        __self__.availability_zone = availability_zone
        """
        The share availability zone.
        """
        if description and not isinstance(description, str):
            raise TypeError('Expected argument description to be a str')
        __self__.description = description
        """
        See Argument Reference above.
        """
        if export_locations and not isinstance(export_locations, list):
            raise TypeError('Expected argument export_locations to be a list')
        __self__.export_locations = export_locations
        """
        A list of export locations. For example, when a share
        server has more than one network interface, it can have multiple export
        locations.
        """
        if is_public and not isinstance(is_public, bool):
            raise TypeError('Expected argument is_public to be a bool')
        __self__.is_public = is_public
        """
        See Argument Reference above.
        """
        if metadata and not isinstance(metadata, dict):
            raise TypeError('Expected argument metadata to be a dict')
        __self__.metadata = metadata
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError('Expected argument name to be a str')
        __self__.name = name
        """
        See Argument Reference above.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError('Expected argument project_id to be a str')
        __self__.project_id = project_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError('Expected argument region to be a str')
        __self__.region = region
        """
        The region in which to obtain the V2 Shared File System client.
        """
        if share_network_id and not isinstance(share_network_id, str):
            raise TypeError('Expected argument share_network_id to be a str')
        __self__.share_network_id = share_network_id
        """
        See Argument Reference above.
        """
        if share_proto and not isinstance(share_proto, str):
            raise TypeError('Expected argument share_proto to be a str')
        __self__.share_proto = share_proto
        """
        The share protocol.
        """
        if size and not isinstance(size, int):
            raise TypeError('Expected argument size to be a int')
        __self__.size = size
        """
        The share size, in GBs.
        """
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError('Expected argument snapshot_id to be a str')
        __self__.snapshot_id = snapshot_id
        """
        See Argument Reference above.
        """
        if status and not isinstance(status, str):
            raise TypeError('Expected argument status to be a str')
        __self__.status = status
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_share(description=None, export_location_path=None, is_public=None, metadata=None, name=None, region=None, share_network_id=None, snapshot_id=None, status=None):
    """
    Use this data source to get the ID of an available Shared File System share.
    """
    __args__ = dict()

    __args__['description'] = description
    __args__['exportLocationPath'] = export_location_path
    __args__['isPublic'] = is_public
    __args__['metadata'] = metadata
    __args__['name'] = name
    __args__['region'] = region
    __args__['shareNetworkId'] = share_network_id
    __args__['snapshotId'] = snapshot_id
    __args__['status'] = status
    __ret__ = await pulumi.runtime.invoke('openstack:sharedfilesystem/getShare:getShare', __args__)

    return GetShareResult(
        availability_zone=__ret__.get('availabilityZone'),
        description=__ret__.get('description'),
        export_locations=__ret__.get('exportLocations'),
        is_public=__ret__.get('isPublic'),
        metadata=__ret__.get('metadata'),
        name=__ret__.get('name'),
        project_id=__ret__.get('projectId'),
        region=__ret__.get('region'),
        share_network_id=__ret__.get('shareNetworkId'),
        share_proto=__ret__.get('shareProto'),
        size=__ret__.get('size'),
        snapshot_id=__ret__.get('snapshotId'),
        status=__ret__.get('status'),
        id=__ret__.get('id'))
