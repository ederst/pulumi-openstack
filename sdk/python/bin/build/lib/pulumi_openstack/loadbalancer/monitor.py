# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Monitor(pulumi.CustomResource):
    """
    Manages a V2 monitor resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, delay=None, expected_codes=None, http_method=None, max_retries=None, name=None, pool_id=None, region=None, tenant_id=None, timeout=None, type=None, url_path=None):
        """Create a Monitor resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if admin_state_up and not isinstance(admin_state_up, bool):
            raise TypeError('Expected property admin_state_up to be a bool')
        __self__.admin_state_up = admin_state_up
        """
        The administrative state of the monitor.
        A valid value is true (UP) or false (DOWN).
        """
        __props__['adminStateUp'] = admin_state_up

        if not delay:
            raise TypeError('Missing required property delay')
        elif not isinstance(delay, int):
            raise TypeError('Expected property delay to be a int')
        __self__.delay = delay
        """
        The time, in seconds, between sending probes to members.
        """
        __props__['delay'] = delay

        if expected_codes and not isinstance(expected_codes, basestring):
            raise TypeError('Expected property expected_codes to be a basestring')
        __self__.expected_codes = expected_codes
        """
        Required for HTTP(S) types. Expected HTTP codes
        for a passing HTTP(S) monitor. You can either specify a single status like
        "200", or a range like "200-202".
        """
        __props__['expectedCodes'] = expected_codes

        if http_method and not isinstance(http_method, basestring):
            raise TypeError('Expected property http_method to be a basestring')
        __self__.http_method = http_method
        """
        Required for HTTP(S) types. The HTTP method used
        for requests by the monitor. If this attribute is not specified, it
        defaults to "GET".
        """
        __props__['httpMethod'] = http_method

        if not max_retries:
            raise TypeError('Missing required property max_retries')
        elif not isinstance(max_retries, int):
            raise TypeError('Expected property max_retries to be a int')
        __self__.max_retries = max_retries
        """
        Number of permissible ping failures before
        changing the member's status to INACTIVE. Must be a number between 1
        and 10..
        """
        __props__['maxRetries'] = max_retries

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The Name of the Monitor.
        """
        __props__['name'] = name

        if not pool_id:
            raise TypeError('Missing required property pool_id')
        elif not isinstance(pool_id, basestring):
            raise TypeError('Expected property pool_id to be a basestring')
        __self__.pool_id = pool_id
        """
        The id of the pool that this monitor will be assigned to.
        """
        __props__['poolId'] = pool_id

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an . If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        monitor.
        """
        __props__['region'] = region

        if tenant_id and not isinstance(tenant_id, basestring):
            raise TypeError('Expected property tenant_id to be a basestring')
        __self__.tenant_id = tenant_id
        """
        Required for admins. The UUID of the tenant who owns
        the monitor.  Only administrative users can specify a tenant UUID
        other than their own. Changing this creates a new monitor.
        """
        __props__['tenantId'] = tenant_id

        if not timeout:
            raise TypeError('Missing required property timeout')
        elif not isinstance(timeout, int):
            raise TypeError('Expected property timeout to be a int')
        __self__.timeout = timeout
        """
        Maximum number of seconds for a monitor to wait for a
        ping reply before it times out. The value must be less than the delay
        value.
        """
        __props__['timeout'] = timeout

        if not type:
            raise TypeError('Missing required property type')
        elif not isinstance(type, basestring):
            raise TypeError('Expected property type to be a basestring')
        __self__.type = type
        """
        The type of probe, which is PING, TCP, HTTP, or HTTPS,
        that is sent by the load balancer to verify the member state. Changing this
        creates a new monitor.
        """
        __props__['type'] = type

        if url_path and not isinstance(url_path, basestring):
            raise TypeError('Expected property url_path to be a basestring')
        __self__.url_path = url_path
        """
        Required for HTTP(S) types. URI path that will be
        accessed if monitor type is HTTP or HTTPS.
        """
        __props__['urlPath'] = url_path

        super(Monitor, __self__).__init__(
            'openstack:loadbalancer/monitor:Monitor',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'adminStateUp' in outs:
            self.admin_state_up = outs['adminStateUp']
        if 'delay' in outs:
            self.delay = outs['delay']
        if 'expectedCodes' in outs:
            self.expected_codes = outs['expectedCodes']
        if 'httpMethod' in outs:
            self.http_method = outs['httpMethod']
        if 'maxRetries' in outs:
            self.max_retries = outs['maxRetries']
        if 'name' in outs:
            self.name = outs['name']
        if 'poolId' in outs:
            self.pool_id = outs['poolId']
        if 'region' in outs:
            self.region = outs['region']
        if 'tenantId' in outs:
            self.tenant_id = outs['tenantId']
        if 'timeout' in outs:
            self.timeout = outs['timeout']
        if 'type' in outs:
            self.type = outs['type']
        if 'urlPath' in outs:
            self.url_path = outs['urlPath']