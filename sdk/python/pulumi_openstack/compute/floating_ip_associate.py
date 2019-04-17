# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class FloatingIpAssociate(pulumi.CustomResource):
    fixed_ip: pulumi.Output[str]
    """
    The specific IP address to direct traffic to.
    """
    floating_ip: pulumi.Output[str]
    """
    The floating IP to associate.
    """
    instance_id: pulumi.Output[str]
    """
    The instance to associte the floating IP with.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Compute client.
    Keypairs are associated with accounts, but a Compute client is needed to
    create one. If omitted, the `region` argument of the provider is used.
    Changing this creates a new floatingip_associate.
    """
    wait_until_associated: pulumi.Output[bool]
    """
    In cases where the OpenStack environment
    does not automatically wait until the association has finished, set this
    option to have Terraform poll the instance until the floating IP has been
    associated. Defaults to false.
    """
    def __init__(__self__, resource_name, opts=None, fixed_ip=None, floating_ip=None, instance_id=None, region=None, wait_until_associated=None, __name__=None, __opts__=None):
        """
        Associate a floating IP to an instance. This can be used instead of the
        `floating_ip` options in `openstack_compute_instance_v2`.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fixed_ip: The specific IP address to direct traffic to.
        :param pulumi.Input[str] floating_ip: The floating IP to associate.
        :param pulumi.Input[str] instance_id: The instance to associte the floating IP with.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               Keypairs are associated with accounts, but a Compute client is needed to
               create one. If omitted, the `region` argument of the provider is used.
               Changing this creates a new floatingip_associate.
        :param pulumi.Input[bool] wait_until_associated: In cases where the OpenStack environment
               does not automatically wait until the association has finished, set this
               option to have Terraform poll the instance until the floating IP has been
               associated. Defaults to false.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['fixed_ip'] = fixed_ip

        if floating_ip is None:
            raise TypeError("Missing required property 'floating_ip'")
        __props__['floating_ip'] = floating_ip

        if instance_id is None:
            raise TypeError("Missing required property 'instance_id'")
        __props__['instance_id'] = instance_id

        __props__['region'] = region

        __props__['wait_until_associated'] = wait_until_associated

        super(FloatingIpAssociate, __self__).__init__(
            'openstack:compute/floatingIpAssociate:FloatingIpAssociate',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

