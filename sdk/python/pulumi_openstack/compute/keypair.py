# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Keypair']


class Keypair(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Keypairs can be imported using the `name`, e.g.

        ```sh
         $ pulumi import openstack:compute/keypair:Keypair my-keypair test-keypair
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A unique name for the keypair. Changing this creates a new
               keypair.
        :param pulumi.Input[str] public_key: A pregenerated OpenSSH-formatted public key.
               Changing this creates a new keypair. If a public key is not specified, then
               a public/private key pair will be automatically generated. If a pair is
               created, then destroying this resource means you will lose access to that
               keypair forever.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               Keypairs are associated with accounts, but a Compute client is needed to
               create one. If omitted, the `region` argument of the provider is used.
               Changing this creates a new keypair.
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

            __props__['name'] = name
            __props__['public_key'] = public_key
            __props__['region'] = region
            __props__['value_specs'] = value_specs
            __props__['fingerprint'] = None
            __props__['private_key'] = None
        super(Keypair, __self__).__init__(
            'openstack:compute/keypair:Keypair',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Keypair':
        """
        Get an existing Keypair resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fingerprint: The fingerprint of the public key.
        :param pulumi.Input[str] name: A unique name for the keypair. Changing this creates a new
               keypair.
        :param pulumi.Input[str] private_key: The generated private key when no public key is specified.
        :param pulumi.Input[str] public_key: A pregenerated OpenSSH-formatted public key.
               Changing this creates a new keypair. If a public key is not specified, then
               a public/private key pair will be automatically generated. If a pair is
               created, then destroying this resource means you will lose access to that
               keypair forever.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               Keypairs are associated with accounts, but a Compute client is needed to
               create one. If omitted, the `region` argument of the provider is used.
               Changing this creates a new keypair.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["fingerprint"] = fingerprint
        __props__["name"] = name
        __props__["private_key"] = private_key
        __props__["public_key"] = public_key
        __props__["region"] = region
        __props__["value_specs"] = value_specs
        return Keypair(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The fingerprint of the public key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the keypair. Changing this creates a new
        keypair.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        The generated private key when no public key is specified.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        A pregenerated OpenSSH-formatted public key.
        Changing this creates a new keypair. If a public key is not specified, then
        a public/private key pair will be automatically generated. If a pair is
        created, then destroying this resource means you will lose access to that
        keypair forever.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Compute client.
        Keypairs are associated with accounts, but a Compute client is needed to
        create one. If omitted, the `region` argument of the provider is used.
        Changing this creates a new keypair.
        """
        return pulumi.get(self, "region")

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

