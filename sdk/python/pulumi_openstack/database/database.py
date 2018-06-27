# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Database(pulumi.CustomResource):
    """
    Manages a V1 DB database resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, instance_id=None, name=None, region=None):
        """Create a Database resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        elif not isinstance(instance_id, basestring):
            raise TypeError('Expected property instance_id to be a basestring')
        __self__.instance_id = instance_id
        """
        The ID for the database instance.
        """
        __props__['instanceId'] = instance_id

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the resource.
        """
        __props__['name'] = name

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        Openstack region resource is created in.
        """
        __props__['region'] = region

        super(Database, __self__).__init__(
            'openstack:database/database:Database',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'instanceId' in outs:
            self.instance_id = outs['instanceId']
        if 'name' in outs:
            self.name = outs['name']
        if 'region' in outs:
            self.region = outs['region']