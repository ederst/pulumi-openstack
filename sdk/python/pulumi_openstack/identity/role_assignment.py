# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RoleAssignment(pulumi.CustomResource):
    domain_id: pulumi.Output[str]
    """
    The domain to assign the role in.
    """
    group_id: pulumi.Output[str]
    """
    The group to assign the role to.
    """
    project_id: pulumi.Output[str]
    """
    The project to assign the role in.
    """
    role_id: pulumi.Output[str]
    """
    The role to assign.
    """
    user_id: pulumi.Output[str]
    """
    The user to assign the role to.
    """
    def __init__(__self__, __name__, __opts__=None, domain_id=None, group_id=None, project_id=None, role_id=None, user_id=None):
        """
        Manages a V3 Role assignment within OpenStack Keystone.
        
        Note: You _must_ have admin privileges in your OpenStack cloud to use
        this resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] domain_id: The domain to assign the role in.
        :param pulumi.Input[str] group_id: The group to assign the role to.
        :param pulumi.Input[str] project_id: The project to assign the role in.
        :param pulumi.Input[str] role_id: The role to assign.
        :param pulumi.Input[str] user_id: The user to assign the role to.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['domain_id'] = domain_id

        __props__['group_id'] = group_id

        __props__['project_id'] = project_id

        if not role_id:
            raise TypeError('Missing required property role_id')
        __props__['role_id'] = role_id

        __props__['user_id'] = user_id

        super(RoleAssignment, __self__).__init__(
            'openstack:identity/roleAssignment:RoleAssignment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

