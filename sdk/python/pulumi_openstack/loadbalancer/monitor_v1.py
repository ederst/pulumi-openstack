# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['MonitorV1']


class MonitorV1(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[str]] = None,
                 delay: Optional[pulumi.Input[int]] = None,
                 expected_codes: Optional[pulumi.Input[str]] = None,
                 http_method: Optional[pulumi.Input[str]] = None,
                 max_retries: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url_path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V1 load balancer monitor resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        monitor1 = openstack.loadbalancer.MonitorV1("monitor1",
            admin_state_up="true",
            delay=30,
            max_retries=3,
            timeout=5,
            type="PING")
        ```

        ## Import

        Load Balancer Members can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:loadbalancer/monitorV1:MonitorV1 monitor_1 119d7530-72e9-449a-aa97-124a5ef1992c
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_state_up: The administrative state of the monitor.
               Acceptable values are "true" and "false". Changing this value updates the
               state of the existing monitor.
        :param pulumi.Input[int] delay: The time, in seconds, between sending probes to members.
               Changing this creates a new monitor.
        :param pulumi.Input[str] expected_codes: Required for HTTP(S) types. Expected HTTP codes
               for a passing HTTP(S) monitor. You can either specify a single status like
               "200", or a range like "200-202". Changing this updates the expected_codes
               of the existing monitor.
        :param pulumi.Input[str] http_method: Required for HTTP(S) types. The HTTP method used
               for requests by the monitor. If this attribute is not specified, it defaults
               to "GET". Changing this updates the http_method of the existing monitor.
        :param pulumi.Input[int] max_retries: Number of permissible ping failures before changing
               the member's status to INACTIVE. Must be a number between 1 and 10. Changing
               this updates the max_retries of the existing monitor.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an LB monitor. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               LB monitor.
        :param pulumi.Input[str] tenant_id: The owner of the monitor. Required if admin wants to
               create a monitor for another tenant. Changing this creates a new monitor.
        :param pulumi.Input[int] timeout: Maximum number of seconds for a monitor to wait for a
               ping reply before it times out. The value must be less than the delay value.
               Changing this updates the timeout of the existing monitor.
        :param pulumi.Input[str] type: The type of probe, which is PING, TCP, HTTP, or HTTPS,
               that is sent by the monitor to verify the member state. Changing this
               creates a new monitor.
        :param pulumi.Input[str] url_path: Required for HTTP(S) types. URI path that will be
               accessed if monitor type is HTTP or HTTPS. Changing this updates the
               url_path of the existing monitor.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['admin_state_up'] = admin_state_up
            if delay is None and not opts.urn:
                raise TypeError("Missing required property 'delay'")
            __props__['delay'] = delay
            __props__['expected_codes'] = expected_codes
            __props__['http_method'] = http_method
            if max_retries is None and not opts.urn:
                raise TypeError("Missing required property 'max_retries'")
            __props__['max_retries'] = max_retries
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
            if timeout is None and not opts.urn:
                raise TypeError("Missing required property 'timeout'")
            __props__['timeout'] = timeout
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['url_path'] = url_path
        super(MonitorV1, __self__).__init__(
            'openstack:loadbalancer/monitorV1:MonitorV1',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[str]] = None,
            delay: Optional[pulumi.Input[int]] = None,
            expected_codes: Optional[pulumi.Input[str]] = None,
            http_method: Optional[pulumi.Input[str]] = None,
            max_retries: Optional[pulumi.Input[int]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            timeout: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url_path: Optional[pulumi.Input[str]] = None) -> 'MonitorV1':
        """
        Get an existing MonitorV1 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] admin_state_up: The administrative state of the monitor.
               Acceptable values are "true" and "false". Changing this value updates the
               state of the existing monitor.
        :param pulumi.Input[int] delay: The time, in seconds, between sending probes to members.
               Changing this creates a new monitor.
        :param pulumi.Input[str] expected_codes: Required for HTTP(S) types. Expected HTTP codes
               for a passing HTTP(S) monitor. You can either specify a single status like
               "200", or a range like "200-202". Changing this updates the expected_codes
               of the existing monitor.
        :param pulumi.Input[str] http_method: Required for HTTP(S) types. The HTTP method used
               for requests by the monitor. If this attribute is not specified, it defaults
               to "GET". Changing this updates the http_method of the existing monitor.
        :param pulumi.Input[int] max_retries: Number of permissible ping failures before changing
               the member's status to INACTIVE. Must be a number between 1 and 10. Changing
               this updates the max_retries of the existing monitor.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an LB monitor. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               LB monitor.
        :param pulumi.Input[str] tenant_id: The owner of the monitor. Required if admin wants to
               create a monitor for another tenant. Changing this creates a new monitor.
        :param pulumi.Input[int] timeout: Maximum number of seconds for a monitor to wait for a
               ping reply before it times out. The value must be less than the delay value.
               Changing this updates the timeout of the existing monitor.
        :param pulumi.Input[str] type: The type of probe, which is PING, TCP, HTTP, or HTTPS,
               that is sent by the monitor to verify the member state. Changing this
               creates a new monitor.
        :param pulumi.Input[str] url_path: Required for HTTP(S) types. URI path that will be
               accessed if monitor type is HTTP or HTTPS. Changing this updates the
               url_path of the existing monitor.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["delay"] = delay
        __props__["expected_codes"] = expected_codes
        __props__["http_method"] = http_method
        __props__["max_retries"] = max_retries
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        __props__["timeout"] = timeout
        __props__["type"] = type
        __props__["url_path"] = url_path
        return MonitorV1(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[str]:
        """
        The administrative state of the monitor.
        Acceptable values are "true" and "false". Changing this value updates the
        state of the existing monitor.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter
    def delay(self) -> pulumi.Output[int]:
        """
        The time, in seconds, between sending probes to members.
        Changing this creates a new monitor.
        """
        return pulumi.get(self, "delay")

    @property
    @pulumi.getter(name="expectedCodes")
    def expected_codes(self) -> pulumi.Output[Optional[str]]:
        """
        Required for HTTP(S) types. Expected HTTP codes
        for a passing HTTP(S) monitor. You can either specify a single status like
        "200", or a range like "200-202". Changing this updates the expected_codes
        of the existing monitor.
        """
        return pulumi.get(self, "expected_codes")

    @property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output[Optional[str]]:
        """
        Required for HTTP(S) types. The HTTP method used
        for requests by the monitor. If this attribute is not specified, it defaults
        to "GET". Changing this updates the http_method of the existing monitor.
        """
        return pulumi.get(self, "http_method")

    @property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> pulumi.Output[int]:
        """
        Number of permissible ping failures before changing
        the member's status to INACTIVE. Must be a number between 1 and 10. Changing
        this updates the max_retries of the existing monitor.
        """
        return pulumi.get(self, "max_retries")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an LB monitor. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        LB monitor.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the monitor. Required if admin wants to
        create a monitor for another tenant. Changing this creates a new monitor.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[int]:
        """
        Maximum number of seconds for a monitor to wait for a
        ping reply before it times out. The value must be less than the delay value.
        Changing this updates the timeout of the existing monitor.
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of probe, which is PING, TCP, HTTP, or HTTPS,
        that is sent by the monitor to verify the member state. Changing this
        creates a new monitor.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="urlPath")
    def url_path(self) -> pulumi.Output[Optional[str]]:
        """
        Required for HTTP(S) types. URI path that will be
        accessed if monitor type is HTTP or HTTPS. Changing this updates the
        url_path of the existing monitor.
        """
        return pulumi.get(self, "url_path")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

