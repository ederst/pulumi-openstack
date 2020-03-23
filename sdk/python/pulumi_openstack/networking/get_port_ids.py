# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetPortIdsResult:
    """
    A collection of values returned by getPortIds.
    """
    def __init__(__self__, admin_state_up=None, description=None, device_id=None, device_owner=None, dns_name=None, fixed_ip=None, id=None, ids=None, mac_address=None, name=None, network_id=None, project_id=None, region=None, security_group_ids=None, sort_direction=None, sort_key=None, status=None, tags=None, tenant_id=None):
        if admin_state_up and not isinstance(admin_state_up, bool):
            raise TypeError("Expected argument 'admin_state_up' to be a bool")
        __self__.admin_state_up = admin_state_up
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if device_id and not isinstance(device_id, str):
            raise TypeError("Expected argument 'device_id' to be a str")
        __self__.device_id = device_id
        if device_owner and not isinstance(device_owner, str):
            raise TypeError("Expected argument 'device_owner' to be a str")
        __self__.device_owner = device_owner
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        __self__.dns_name = dns_name
        if fixed_ip and not isinstance(fixed_ip, str):
            raise TypeError("Expected argument 'fixed_ip' to be a str")
        __self__.fixed_ip = fixed_ip
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        if mac_address and not isinstance(mac_address, str):
            raise TypeError("Expected argument 'mac_address' to be a str")
        __self__.mac_address = mac_address
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        __self__.network_id = network_id
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        __self__.security_group_ids = security_group_ids
        if sort_direction and not isinstance(sort_direction, str):
            raise TypeError("Expected argument 'sort_direction' to be a str")
        __self__.sort_direction = sort_direction
        if sort_key and not isinstance(sort_key, str):
            raise TypeError("Expected argument 'sort_key' to be a str")
        __self__.sort_key = sort_key
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        __self__.tags = tags
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        __self__.tenant_id = tenant_id
class AwaitableGetPortIdsResult(GetPortIdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPortIdsResult(
            admin_state_up=self.admin_state_up,
            description=self.description,
            device_id=self.device_id,
            device_owner=self.device_owner,
            dns_name=self.dns_name,
            fixed_ip=self.fixed_ip,
            id=self.id,
            ids=self.ids,
            mac_address=self.mac_address,
            name=self.name,
            network_id=self.network_id,
            project_id=self.project_id,
            region=self.region,
            security_group_ids=self.security_group_ids,
            sort_direction=self.sort_direction,
            sort_key=self.sort_key,
            status=self.status,
            tags=self.tags,
            tenant_id=self.tenant_id)

def get_port_ids(admin_state_up=None,description=None,device_id=None,device_owner=None,dns_name=None,fixed_ip=None,mac_address=None,name=None,network_id=None,project_id=None,region=None,security_group_ids=None,sort_direction=None,sort_key=None,status=None,tags=None,tenant_id=None,opts=None):
    """
    Use this data source to get a list of Openstack Port IDs matching the
    specified criteria.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_port_ids_v2.html.markdown.


    :param bool admin_state_up: The administrative state of the port.
    :param str description: Human-readable description of the port.
    :param str device_id: The ID of the device the port belongs to.
    :param str device_owner: The device owner of the port.
    :param str fixed_ip: The port IP address filter.
    :param str mac_address: The MAC address of the port.
    :param str name: The name of the port.
    :param str network_id: The ID of the network the port belongs to.
    :param str project_id: The owner of the port.
    :param str region: The region in which to obtain the V2 Neutron client.
           A Neutron client is needed to retrieve port ids. If omitted, the
           `region` argument of the provider is used.
    :param list security_group_ids: The list of port security group IDs to filter.
    :param str sort_direction: Order the results in either `asc` or `desc`.
           Defaults to none.
    :param str sort_key: Sort ports based on a certain key. Defaults to none.
    :param str status: The status of the port.
    :param list tags: The list of port tags to filter.
    """
    __args__ = dict()


    __args__['adminStateUp'] = admin_state_up
    __args__['description'] = description
    __args__['deviceId'] = device_id
    __args__['deviceOwner'] = device_owner
    __args__['dnsName'] = dns_name
    __args__['fixedIp'] = fixed_ip
    __args__['macAddress'] = mac_address
    __args__['name'] = name
    __args__['networkId'] = network_id
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['securityGroupIds'] = security_group_ids
    __args__['sortDirection'] = sort_direction
    __args__['sortKey'] = sort_key
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['tenantId'] = tenant_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:networking/getPortIds:getPortIds', __args__, opts=opts).value

    return AwaitableGetPortIdsResult(
        admin_state_up=__ret__.get('adminStateUp'),
        description=__ret__.get('description'),
        device_id=__ret__.get('deviceId'),
        device_owner=__ret__.get('deviceOwner'),
        dns_name=__ret__.get('dnsName'),
        fixed_ip=__ret__.get('fixedIp'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        mac_address=__ret__.get('macAddress'),
        name=__ret__.get('name'),
        network_id=__ret__.get('networkId'),
        project_id=__ret__.get('projectId'),
        region=__ret__.get('region'),
        security_group_ids=__ret__.get('securityGroupIds'),
        sort_direction=__ret__.get('sortDirection'),
        sort_key=__ret__.get('sortKey'),
        status=__ret__.get('status'),
        tags=__ret__.get('tags'),
        tenant_id=__ret__.get('tenantId'))
