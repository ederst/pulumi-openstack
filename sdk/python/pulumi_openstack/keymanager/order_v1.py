# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['OrderV1']


class OrderV1(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 meta: Optional[pulumi.Input[pulumi.InputType['OrderV1MetaArgs']]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V1 Barbican order resource within OpenStack.

        ## Example Usage
        ### Symmetric key order

        ```python
        import pulumi
        import pulumi_openstack as openstack

        order1 = openstack.keymanager.OrderV1("order1",
            meta=openstack.keymanager.OrderV1MetaArgs(
                algorithm="aes",
                bit_length=256,
                mode="cbc",
                name="mysecret",
            ),
            type="key")
        ```
        ### Asymmetric key pair order

        ```python
        import pulumi
        import pulumi_openstack as openstack

        order1 = openstack.keymanager.OrderV1("order1",
            meta=openstack.keymanager.OrderV1MetaArgs(
                algorithm="rsa",
                bit_length=4096,
                name="mysecret",
            ),
            type="asymmetric")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['OrderV1MetaArgs']] meta: Dictionary containing the order metadata used to generate the order. The structure is described below.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a order. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 order.
        :param pulumi.Input[str] type: The type of key to be generated. Must be one of `asymmetric`, `key`.
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

            if meta is None:
                raise TypeError("Missing required property 'meta'")
            __props__['meta'] = meta
            __props__['region'] = region
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['container_ref'] = None
            __props__['created'] = None
            __props__['creator_id'] = None
            __props__['order_ref'] = None
            __props__['secret_ref'] = None
            __props__['status'] = None
            __props__['sub_status'] = None
            __props__['sub_status_message'] = None
            __props__['updated'] = None
        super(OrderV1, __self__).__init__(
            'openstack:keymanager/orderV1:OrderV1',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_ref: Optional[pulumi.Input[str]] = None,
            created: Optional[pulumi.Input[str]] = None,
            creator_id: Optional[pulumi.Input[str]] = None,
            meta: Optional[pulumi.Input[pulumi.InputType['OrderV1MetaArgs']]] = None,
            order_ref: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret_ref: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            sub_status: Optional[pulumi.Input[str]] = None,
            sub_status_message: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            updated: Optional[pulumi.Input[str]] = None) -> 'OrderV1':
        """
        Get an existing OrderV1 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_ref: The container reference / where to find the container.
        :param pulumi.Input[str] created: The date the order was created.
        :param pulumi.Input[str] creator_id: The creator of the order.
        :param pulumi.Input[pulumi.InputType['OrderV1MetaArgs']] meta: Dictionary containing the order metadata used to generate the order. The structure is described below.
        :param pulumi.Input[str] order_ref: The order reference / where to find the order.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a order. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 order.
        :param pulumi.Input[str] secret_ref: The secret reference / where to find the secret.
        :param pulumi.Input[str] status: The status of the order.
        :param pulumi.Input[str] sub_status: The sub status of the order.
        :param pulumi.Input[str] sub_status_message: The sub status message of the order.
        :param pulumi.Input[str] type: The type of key to be generated. Must be one of `asymmetric`, `key`.
        :param pulumi.Input[str] updated: The date the order was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["container_ref"] = container_ref
        __props__["created"] = created
        __props__["creator_id"] = creator_id
        __props__["meta"] = meta
        __props__["order_ref"] = order_ref
        __props__["region"] = region
        __props__["secret_ref"] = secret_ref
        __props__["status"] = status
        __props__["sub_status"] = sub_status
        __props__["sub_status_message"] = sub_status_message
        __props__["type"] = type
        __props__["updated"] = updated
        return OrderV1(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerRef")
    def container_ref(self) -> pulumi.Output[str]:
        """
        The container reference / where to find the container.
        """
        return pulumi.get(self, "container_ref")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The date the order was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> pulumi.Output[str]:
        """
        The creator of the order.
        """
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def meta(self) -> pulumi.Output['outputs.OrderV1Meta']:
        """
        Dictionary containing the order metadata used to generate the order. The structure is described below.
        """
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter(name="orderRef")
    def order_ref(self) -> pulumi.Output[str]:
        """
        The order reference / where to find the order.
        """
        return pulumi.get(self, "order_ref")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V1 KeyManager client.
        A KeyManager client is needed to create a order. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        V1 order.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretRef")
    def secret_ref(self) -> pulumi.Output[str]:
        """
        The secret reference / where to find the secret.
        """
        return pulumi.get(self, "secret_ref")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the order.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subStatus")
    def sub_status(self) -> pulumi.Output[str]:
        """
        The sub status of the order.
        """
        return pulumi.get(self, "sub_status")

    @property
    @pulumi.getter(name="subStatusMessage")
    def sub_status_message(self) -> pulumi.Output[str]:
        """
        The sub status message of the order.
        """
        return pulumi.get(self, "sub_status_message")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of key to be generated. Must be one of `asymmetric`, `key`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[str]:
        """
        The date the order was last updated.
        """
        return pulumi.get(self, "updated")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

