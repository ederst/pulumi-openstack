# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ContainerV1(pulumi.CustomResource):
    consumers: pulumi.Output[list]
    """
    The list of the container consumers. The structure is described below.
    
      * `name` (`str`) - Human-readable name for the Container. Does not have
        to be unique.
      * `url` (`str`) - The consumer URL.
    """
    container_ref: pulumi.Output[str]
    """
    The container reference / where to find the container.
    """
    created_at: pulumi.Output[str]
    """
    The date the container was created.
    """
    creator_id: pulumi.Output[str]
    """
    The creator of the container.
    """
    name: pulumi.Output[str]
    """
    Human-readable name for the Container. Does not have
    to be unique.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V1 KeyManager client.
    A KeyManager client is needed to create a container. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    V1 container.
    """
    secret_refs: pulumi.Output[list]
    """
    A set of dictionaries containing references to secrets. The structure is described
    below.
    
      * `name` (`str`) - Human-readable name for the Container. Does not have
        to be unique.
      * `secret_ref` (`str`)
    """
    status: pulumi.Output[str]
    """
    The status of the container.
    """
    type: pulumi.Output[str]
    """
    Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
    """
    updated_at: pulumi.Output[str]
    """
    The date the container was last updated.
    """
    def __init__(__self__, resource_name, opts=None, name=None, region=None, secret_refs=None, type=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V1 Barbican container resource within OpenStack.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Human-readable name for the Container. Does not have
               to be unique.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a container. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 container.
        :param pulumi.Input[list] secret_refs: A set of dictionaries containing references to secrets. The structure is described
               below.
        :param pulumi.Input[str] type: Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
        
        The **secret_refs** object supports the following:
        
          * `name` (`pulumi.Input[str]`) - Human-readable name for the Container. Does not have
            to be unique.
          * `secret_ref` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown.
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

            __props__['name'] = name
            __props__['region'] = region
            __props__['secret_refs'] = secret_refs
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['consumers'] = None
            __props__['container_ref'] = None
            __props__['created_at'] = None
            __props__['creator_id'] = None
            __props__['status'] = None
            __props__['updated_at'] = None
        super(ContainerV1, __self__).__init__(
            'openstack:keymanager/containerV1:ContainerV1',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, consumers=None, container_ref=None, created_at=None, creator_id=None, name=None, region=None, secret_refs=None, status=None, type=None, updated_at=None):
        """
        Get an existing ContainerV1 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] consumers: The list of the container consumers. The structure is described below.
        :param pulumi.Input[str] container_ref: The container reference / where to find the container.
        :param pulumi.Input[str] created_at: The date the container was created.
        :param pulumi.Input[str] creator_id: The creator of the container.
        :param pulumi.Input[str] name: Human-readable name for the Container. Does not have
               to be unique.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a container. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 container.
        :param pulumi.Input[list] secret_refs: A set of dictionaries containing references to secrets. The structure is described
               below.
        :param pulumi.Input[str] status: The status of the container.
        :param pulumi.Input[str] type: Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
        :param pulumi.Input[str] updated_at: The date the container was last updated.
        
        The **consumers** object supports the following:
        
          * `name` (`pulumi.Input[str]`) - Human-readable name for the Container. Does not have
            to be unique.
          * `url` (`pulumi.Input[str]`) - The consumer URL.
        
        The **secret_refs** object supports the following:
        
          * `name` (`pulumi.Input[str]`) - Human-readable name for the Container. Does not have
            to be unique.
          * `secret_ref` (`pulumi.Input[str]`)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["consumers"] = consumers
        __props__["container_ref"] = container_ref
        __props__["created_at"] = created_at
        __props__["creator_id"] = creator_id
        __props__["name"] = name
        __props__["region"] = region
        __props__["secret_refs"] = secret_refs
        __props__["status"] = status
        __props__["type"] = type
        __props__["updated_at"] = updated_at
        return ContainerV1(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
