# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Ec2CredentialV3']


class Ec2CredentialV3(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V3 EC2 Credential resource within OpenStack Keystone.
        EC2 credentials in Openstack are used to access S3 compatible Swift/RadosGW endpoints

        > **Note:** All arguments including the EC2 credential access key and secret
        will be stored in the raw state as plain-text. [Read more about sensitive data
        in state](https://www.terraform.io/docs/state/sensitive-data.html).

        ## Example Usage
        ### EC2 credential in current project scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        ec2_key1 = openstack.identity.Ec2CredentialV3("ec2Key1")
        ```
        ### EC2 credential in pre-defined project scope
        ```python
        import pulumi
        import pulumi_openstack as openstack

        ec2_key1 = openstack.identity.Ec2CredentialV3("ec2Key1", project_id="f7ac731cc11f40efbc03a9f9e1d1d21f")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The ID of the project the EC2 credential is created
               for and that authentication requests using this EC2 credential will
               be scoped to.
        :param pulumi.Input[str] user_id: The ID of the user the EC2 credential is created for.
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

            __props__['project_id'] = project_id
            __props__['region'] = region
            __props__['user_id'] = user_id
            __props__['access'] = None
            __props__['secret'] = None
            __props__['trust_id'] = None
        super(Ec2CredentialV3, __self__).__init__(
            'openstack:identity/ec2CredentialV3:Ec2CredentialV3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            trust_id: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'Ec2CredentialV3':
        """
        Get an existing Ec2CredentialV3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access: contains an EC2 credential access UUID
        :param pulumi.Input[str] project_id: The ID of the project the EC2 credential is created
               for and that authentication requests using this EC2 credential will
               be scoped to.
        :param pulumi.Input[str] secret: contains an EC2 credential secret UUID
        :param pulumi.Input[str] trust_id: contains an EC2 credential trust ID scope
        :param pulumi.Input[str] user_id: The ID of the user the EC2 credential is created for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access"] = access
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["secret"] = secret
        __props__["trust_id"] = trust_id
        __props__["user_id"] = user_id
        return Ec2CredentialV3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def access(self) -> pulumi.Output[str]:
        """
        contains an EC2 credential access UUID
        """
        return pulumi.get(self, "access")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project the EC2 credential is created
        for and that authentication requests using this EC2 credential will
        be scoped to.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        contains an EC2 credential secret UUID
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="trustId")
    def trust_id(self) -> pulumi.Output[str]:
        """
        contains an EC2 credential trust ID scope
        """
        return pulumi.get(self, "trust_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The ID of the user the EC2 credential is created for.
        """
        return pulumi.get(self, "user_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

