# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RecordSet(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    A description of the  record set.
    """
    name: pulumi.Output[str]
    """
    The name of the record set. Note the `.` at the end of the name.
    Changing this creates a new DNS  record set.
    """
    records: pulumi.Output[list]
    """
    An array of DNS records.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 DNS client.
    If omitted, the `region` argument of the provider is used.
    Changing this creates a new DNS  record set.
    """
    ttl: pulumi.Output[int]
    """
    The time to live (TTL) of the record set.
    """
    type: pulumi.Output[str]
    """
    The type of record set. Examples: "A", "MX".
    Changing this creates a new DNS  record set.
    """
    value_specs: pulumi.Output[dict]
    """
    Map of additional options. Changing this creates a
    new record set.
    """
    zone_id: pulumi.Output[str]
    """
    The ID of the zone in which to create the record set.
    Changing this creates a new DNS  record set.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, name=None, records=None, region=None, ttl=None, type=None, value_specs=None, zone_id=None):
        """
        Manages a DNS record set in the OpenStack DNS Service.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] description: A description of the  record set.
        :param pulumi.Input[str] name: The name of the record set. Note the `.` at the end of the name.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[list] records: An array of DNS records.
        :param pulumi.Input[str] region: The region in which to obtain the V2 DNS client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[int] ttl: The time to live (TTL) of the record set.
        :param pulumi.Input[str] type: The type of record set. Examples: "A", "MX".
               Changing this creates a new DNS  record set.
        :param pulumi.Input[dict] value_specs: Map of additional options. Changing this creates a
               new record set.
        :param pulumi.Input[str] zone_id: The ID of the zone in which to create the record set.
               Changing this creates a new DNS  record set.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        __props__['name'] = name

        __props__['records'] = records

        __props__['region'] = region

        __props__['ttl'] = ttl

        __props__['type'] = type

        __props__['value_specs'] = value_specs

        if not zone_id:
            raise TypeError('Missing required property zone_id')
        __props__['zone_id'] = zone_id

        super(RecordSet, __self__).__init__(
            'openstack:dns/recordSet:RecordSet',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

