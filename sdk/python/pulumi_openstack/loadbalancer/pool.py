# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Pool(pulumi.CustomResource):
    admin_state_up: pulumi.Output[bool]
    """
    The administrative state of the pool.
    A valid value is true (UP) or false (DOWN).
    """
    description: pulumi.Output[str]
    """
    Human-readable description for the pool.
    """
    lb_method: pulumi.Output[str]
    """
    The load balancing algorithm to
    distribute traffic to the pool's members. Must be one of
    ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
    in Octavia).
    """
    listener_id: pulumi.Output[str]
    """
    The Listener on which the members of the pool
    will be associated with. Changing this creates a new pool.
    Note:  One of LoadbalancerID or ListenerID must be provided.
    """
    loadbalancer_id: pulumi.Output[str]
    """
    The load balancer on which to provision this
    pool. Changing this creates a new pool.
    Note:  One of LoadbalancerID or ListenerID must be provided.
    """
    name: pulumi.Output[str]
    """
    Human-readable name for the pool.
    """
    persistence: pulumi.Output[dict]
    """
    Omit this field to prevent session persistence.  Indicates
    whether connections in the same session will be processed by the same Pool
    member or not. Changing this creates a new pool.

      * `cookieName` (`str`) - The name of the cookie if persistence mode is set
        appropriately. Required if `type = APP_COOKIE`.
      * `type` (`str`) - The type of persistence mode. The current specification
        supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.
    """
    protocol: pulumi.Output[str]
    """
    The protocol - can either be TCP, HTTP, HTTPS, PROXY
    or UDP (supported only in Octavia). Changing this creates a new pool.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create an . If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    pool.
    """
    tenant_id: pulumi.Output[str]
    """
    Required for admins. The UUID of the tenant who owns
    the pool.  Only administrative users can specify a tenant UUID
    other than their own. Changing this creates a new pool.
    """
    def __init__(__self__, resource_name, opts=None, admin_state_up=None, description=None, lb_method=None, listener_id=None, loadbalancer_id=None, name=None, persistence=None, protocol=None, region=None, tenant_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 pool resource within OpenStack.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the pool.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the pool.
        :param pulumi.Input[str] lb_method: The load balancing algorithm to
               distribute traffic to the pool's members. Must be one of
               ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
               in Octavia).
        :param pulumi.Input[str] listener_id: The Listener on which the members of the pool
               will be associated with. Changing this creates a new pool.
               Note:  One of LoadbalancerID or ListenerID must be provided.
        :param pulumi.Input[str] loadbalancer_id: The load balancer on which to provision this
               pool. Changing this creates a new pool.
               Note:  One of LoadbalancerID or ListenerID must be provided.
        :param pulumi.Input[str] name: Human-readable name for the pool.
        :param pulumi.Input[dict] persistence: Omit this field to prevent session persistence.  Indicates
               whether connections in the same session will be processed by the same Pool
               member or not. Changing this creates a new pool.
        :param pulumi.Input[str] protocol: The protocol - can either be TCP, HTTP, HTTPS, PROXY
               or UDP (supported only in Octavia). Changing this creates a new pool.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               pool.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the pool.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new pool.

        The **persistence** object supports the following:

          * `cookieName` (`pulumi.Input[str]`) - The name of the cookie if persistence mode is set
            appropriately. Required if `type = APP_COOKIE`.
          * `type` (`pulumi.Input[str]`) - The type of persistence mode. The current specification
            supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['admin_state_up'] = admin_state_up
            __props__['description'] = description
            if lb_method is None:
                raise TypeError("Missing required property 'lb_method'")
            __props__['lb_method'] = lb_method
            __props__['listener_id'] = listener_id
            __props__['loadbalancer_id'] = loadbalancer_id
            __props__['name'] = name
            __props__['persistence'] = persistence
            if protocol is None:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
        super(Pool, __self__).__init__(
            'openstack:loadbalancer/pool:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, admin_state_up=None, description=None, lb_method=None, listener_id=None, loadbalancer_id=None, name=None, persistence=None, protocol=None, region=None, tenant_id=None):
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the pool.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the pool.
        :param pulumi.Input[str] lb_method: The load balancing algorithm to
               distribute traffic to the pool's members. Must be one of
               ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
               in Octavia).
        :param pulumi.Input[str] listener_id: The Listener on which the members of the pool
               will be associated with. Changing this creates a new pool.
               Note:  One of LoadbalancerID or ListenerID must be provided.
        :param pulumi.Input[str] loadbalancer_id: The load balancer on which to provision this
               pool. Changing this creates a new pool.
               Note:  One of LoadbalancerID or ListenerID must be provided.
        :param pulumi.Input[str] name: Human-readable name for the pool.
        :param pulumi.Input[dict] persistence: Omit this field to prevent session persistence.  Indicates
               whether connections in the same session will be processed by the same Pool
               member or not. Changing this creates a new pool.
        :param pulumi.Input[str] protocol: The protocol - can either be TCP, HTTP, HTTPS, PROXY
               or UDP (supported only in Octavia). Changing this creates a new pool.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               pool.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the pool.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new pool.

        The **persistence** object supports the following:

          * `cookieName` (`pulumi.Input[str]`) - The name of the cookie if persistence mode is set
            appropriately. Required if `type = APP_COOKIE`.
          * `type` (`pulumi.Input[str]`) - The type of persistence mode. The current specification
            supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["description"] = description
        __props__["lb_method"] = lb_method
        __props__["listener_id"] = listener_id
        __props__["loadbalancer_id"] = loadbalancer_id
        __props__["name"] = name
        __props__["persistence"] = persistence
        __props__["protocol"] = protocol
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        return Pool(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

