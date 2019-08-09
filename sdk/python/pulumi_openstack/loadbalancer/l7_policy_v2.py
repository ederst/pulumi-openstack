# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class L7PolicyV2(pulumi.CustomResource):
    action: pulumi.Output[str]
    """
    The L7 Policy action - can either be REDIRECT\_TO\_POOL,
    REDIRECT\_TO\_URL or REJECT.
    """
    admin_state_up: pulumi.Output[bool]
    """
    The administrative state of the L7 Policy.
    A valid value is true (UP) or false (DOWN).
    """
    description: pulumi.Output[str]
    """
    Human-readable description for the L7 Policy.
    """
    listener_id: pulumi.Output[str]
    """
    The Listener on which the L7 Policy will be associated with.
    Changing this creates a new L7 Policy.
    """
    name: pulumi.Output[str]
    """
    Human-readable name for the L7 Policy. Does not have
    to be unique.
    """
    position: pulumi.Output[float]
    """
    The position of this policy on the listener. Positions start at 1.
    """
    redirect_pool_id: pulumi.Output[str]
    """
    Requests matching this policy will be redirected to the
    pool with this ID. Only valid if action is REDIRECT\_TO\_POOL.
    """
    redirect_url: pulumi.Output[str]
    """
    Requests matching this policy will be redirected to this URL.
    Only valid if action is REDIRECT\_TO\_URL.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create an . If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    L7 Policy.
    """
    tenant_id: pulumi.Output[str]
    """
    Required for admins. The UUID of the tenant who owns
    the L7 Policy.  Only administrative users can specify a tenant UUID
    other than their own. Changing this creates a new L7 Policy.
    """
    def __init__(__self__, resource_name, opts=None, action=None, admin_state_up=None, description=None, listener_id=None, name=None, position=None, redirect_pool_id=None, redirect_url=None, region=None, tenant_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Load Balancer L7 Policy resource within OpenStack.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\_TO\_POOL,
               REDIRECT\_TO\_URL or REJECT.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[float] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\_TO\_POOL.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\_TO\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_l7policy_v2.html.markdown.
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

            if action is None:
                raise TypeError("Missing required property 'action'")
            __props__['action'] = action
            __props__['admin_state_up'] = admin_state_up
            __props__['description'] = description
            if listener_id is None:
                raise TypeError("Missing required property 'listener_id'")
            __props__['listener_id'] = listener_id
            __props__['name'] = name
            __props__['position'] = position
            __props__['redirect_pool_id'] = redirect_pool_id
            __props__['redirect_url'] = redirect_url
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
        super(L7PolicyV2, __self__).__init__(
            'openstack:loadbalancer/l7PolicyV2:L7PolicyV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, action=None, admin_state_up=None, description=None, listener_id=None, name=None, position=None, redirect_pool_id=None, redirect_url=None, region=None, tenant_id=None):
        """
        Get an existing L7PolicyV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: The L7 Policy action - can either be REDIRECT\_TO\_POOL,
               REDIRECT\_TO\_URL or REJECT.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Policy.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the L7 Policy.
        :param pulumi.Input[str] listener_id: The Listener on which the L7 Policy will be associated with.
               Changing this creates a new L7 Policy.
        :param pulumi.Input[str] name: Human-readable name for the L7 Policy. Does not have
               to be unique.
        :param pulumi.Input[float] position: The position of this policy on the listener. Positions start at 1.
        :param pulumi.Input[str] redirect_pool_id: Requests matching this policy will be redirected to the
               pool with this ID. Only valid if action is REDIRECT\_TO\_POOL.
        :param pulumi.Input[str] redirect_url: Requests matching this policy will be redirected to this URL.
               Only valid if action is REDIRECT\_TO\_URL.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Policy.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Policy.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Policy.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_l7policy_v2.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["action"] = action
        __props__["admin_state_up"] = admin_state_up
        __props__["description"] = description
        __props__["listener_id"] = listener_id
        __props__["name"] = name
        __props__["position"] = position
        __props__["redirect_pool_id"] = redirect_pool_id
        __props__["redirect_url"] = redirect_url
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        return L7PolicyV2(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

