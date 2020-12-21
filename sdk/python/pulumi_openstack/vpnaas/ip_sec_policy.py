# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['IpSecPolicy']


class IpSecPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_algorithm: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encapsulation_mode: Optional[pulumi.Input[str]] = None,
                 encryption_algorithm: Optional[pulumi.Input[str]] = None,
                 lifetimes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSecPolicyLifetimeArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pfs: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 transform_protocol: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron IPSec policy resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        policy1 = openstack.vpnaas.IpSecPolicy("policy1")
        ```

        ## Import

        Policies can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:vpnaas/ipSecPolicy:IpSecPolicy policy_1 832cb7f3-59fe-40cf-8f64-8350ffc03272
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_algorithm: The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
               Default is sha1. Changing this updates the algorithm of the existing policy.
        :param pulumi.Input[str] description: The human-readable description for the policy.
               Changing this updates the description of the existing policy.
        :param pulumi.Input[str] encapsulation_mode: The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
               Changing this updates the existing policy.
        :param pulumi.Input[str] encryption_algorithm: The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
               The default value is aes-128. Changing this updates the existing policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSecPolicyLifetimeArgs']]]] lifetimes: The lifetime of the security association. Consists of Unit and Value.
        :param pulumi.Input[str] name: The name of the policy. Changing this updates the name of
               the existing policy.
        :param pulumi.Input[str] pfs: The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
               Changing this updates the existing policy.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an IPSec policy. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               policy.
        :param pulumi.Input[str] tenant_id: The owner of the policy. Required if admin wants to
               create a policy for another project. Changing this creates a new policy.
        :param pulumi.Input[str] transform_protocol: The transform protocol. Valid values are ESP, AH and AH-ESP.
               Changing this updates the existing policy. Default is ESP.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
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

            __props__['auth_algorithm'] = auth_algorithm
            __props__['description'] = description
            __props__['encapsulation_mode'] = encapsulation_mode
            __props__['encryption_algorithm'] = encryption_algorithm
            __props__['lifetimes'] = lifetimes
            __props__['name'] = name
            __props__['pfs'] = pfs
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
            __props__['transform_protocol'] = transform_protocol
            __props__['value_specs'] = value_specs
        super(IpSecPolicy, __self__).__init__(
            'openstack:vpnaas/ipSecPolicy:IpSecPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_algorithm: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encapsulation_mode: Optional[pulumi.Input[str]] = None,
            encryption_algorithm: Optional[pulumi.Input[str]] = None,
            lifetimes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSecPolicyLifetimeArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pfs: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            transform_protocol: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'IpSecPolicy':
        """
        Get an existing IpSecPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_algorithm: The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
               Default is sha1. Changing this updates the algorithm of the existing policy.
        :param pulumi.Input[str] description: The human-readable description for the policy.
               Changing this updates the description of the existing policy.
        :param pulumi.Input[str] encapsulation_mode: The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
               Changing this updates the existing policy.
        :param pulumi.Input[str] encryption_algorithm: The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
               The default value is aes-128. Changing this updates the existing policy.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpSecPolicyLifetimeArgs']]]] lifetimes: The lifetime of the security association. Consists of Unit and Value.
        :param pulumi.Input[str] name: The name of the policy. Changing this updates the name of
               the existing policy.
        :param pulumi.Input[str] pfs: The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
               Changing this updates the existing policy.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an IPSec policy. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               policy.
        :param pulumi.Input[str] tenant_id: The owner of the policy. Required if admin wants to
               create a policy for another project. Changing this creates a new policy.
        :param pulumi.Input[str] transform_protocol: The transform protocol. Valid values are ESP, AH and AH-ESP.
               Changing this updates the existing policy. Default is ESP.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth_algorithm"] = auth_algorithm
        __props__["description"] = description
        __props__["encapsulation_mode"] = encapsulation_mode
        __props__["encryption_algorithm"] = encryption_algorithm
        __props__["lifetimes"] = lifetimes
        __props__["name"] = name
        __props__["pfs"] = pfs
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        __props__["transform_protocol"] = transform_protocol
        __props__["value_specs"] = value_specs
        return IpSecPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authAlgorithm")
    def auth_algorithm(self) -> pulumi.Output[str]:
        """
        The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
        Default is sha1. Changing this updates the algorithm of the existing policy.
        """
        return pulumi.get(self, "auth_algorithm")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The human-readable description for the policy.
        Changing this updates the description of the existing policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encapsulationMode")
    def encapsulation_mode(self) -> pulumi.Output[str]:
        """
        The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
        Changing this updates the existing policy.
        """
        return pulumi.get(self, "encapsulation_mode")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> pulumi.Output[str]:
        """
        The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
        The default value is aes-128. Changing this updates the existing policy.
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter
    def lifetimes(self) -> pulumi.Output[Sequence['outputs.IpSecPolicyLifetime']]:
        """
        The lifetime of the security association. Consists of Unit and Value.
        """
        return pulumi.get(self, "lifetimes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy. Changing this updates the name of
        the existing policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pfs(self) -> pulumi.Output[str]:
        """
        The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
        Changing this updates the existing policy.
        """
        return pulumi.get(self, "pfs")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an IPSec policy. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        policy.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the policy. Required if admin wants to
        create a policy for another project. Changing this creates a new policy.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="transformProtocol")
    def transform_protocol(self) -> pulumi.Output[str]:
        """
        The transform protocol. Valid values are ESP, AH and AH-ESP.
        Changing this updates the existing policy. Default is ESP.
        """
        return pulumi.get(self, "transform_protocol")

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

