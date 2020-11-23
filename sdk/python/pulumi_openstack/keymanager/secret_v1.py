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

__all__ = ['SecretV1']


class SecretV1(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl: Optional[pulumi.Input[pulumi.InputType['SecretV1AclArgs']]] = None,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 bit_length: Optional[pulumi.Input[int]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 payload: Optional[pulumi.Input[str]] = None,
                 payload_content_encoding: Optional[pulumi.Input[str]] = None,
                 payload_content_type: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Secrets can be imported using the secret id (the last part of the secret reference), e.g.

        ```sh
         $ pulumi import openstack:keymanager/secretV1:SecretV1 secret_1 8a7a79c2-cf17-4e65-b2ae-ddc8bfcf6c74
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecretV1AclArgs']] acl: Allows to control an access to a secret. Currently only the
               `read` operation is supported. If not specified, the secret is accessible
               project wide.
        :param pulumi.Input[str] algorithm: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[int] bit_length: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[str] expiration: The expiration time of the secret in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted, a secret will never expire. Changing this creates a new secret.
        :param pulumi.Input[Mapping[str, Any]] metadata: Additional Metadata for the secret.
        :param pulumi.Input[str] mode: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[str] name: Human-readable name for the Secret. Does not have
               to be unique.
        :param pulumi.Input[str] payload: The secret's data to be stored. **payload\_content\_type** must also be supplied if **payload** is included.
        :param pulumi.Input[str] payload_content_encoding: (required if **payload** is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either `base64` or `binary`.
        :param pulumi.Input[str] payload_content_type: (required if **payload** is included) The media type for the content of the payload. Must be one of `text/plain`, `text/plain;charset=utf-8`, `text/plain; charset=utf-8`, `application/octet-stream`, `application/pkcs8`.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a secret. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 secret.
        :param pulumi.Input[str] secret_type: Used to indicate the type of secret being stored. For more information see [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
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

            __props__['acl'] = acl
            __props__['algorithm'] = algorithm
            __props__['bit_length'] = bit_length
            __props__['expiration'] = expiration
            __props__['metadata'] = metadata
            __props__['mode'] = mode
            __props__['name'] = name
            __props__['payload'] = payload
            __props__['payload_content_encoding'] = payload_content_encoding
            __props__['payload_content_type'] = payload_content_type
            __props__['region'] = region
            __props__['secret_type'] = secret_type
            __props__['all_metadata'] = None
            __props__['content_types'] = None
            __props__['created_at'] = None
            __props__['creator_id'] = None
            __props__['secret_ref'] = None
            __props__['status'] = None
            __props__['updated_at'] = None
        super(SecretV1, __self__).__init__(
            'openstack:keymanager/secretV1:SecretV1',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl: Optional[pulumi.Input[pulumi.InputType['SecretV1AclArgs']]] = None,
            algorithm: Optional[pulumi.Input[str]] = None,
            all_metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            bit_length: Optional[pulumi.Input[int]] = None,
            content_types: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            creator_id: Optional[pulumi.Input[str]] = None,
            expiration: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            payload: Optional[pulumi.Input[str]] = None,
            payload_content_encoding: Optional[pulumi.Input[str]] = None,
            payload_content_type: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret_ref: Optional[pulumi.Input[str]] = None,
            secret_type: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'SecretV1':
        """
        Get an existing SecretV1 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SecretV1AclArgs']] acl: Allows to control an access to a secret. Currently only the
               `read` operation is supported. If not specified, the secret is accessible
               project wide.
        :param pulumi.Input[str] algorithm: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[Mapping[str, Any]] all_metadata: The map of metadata, assigned on the secret, which has been
               explicitly and implicitly added.
        :param pulumi.Input[int] bit_length: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[Mapping[str, Any]] content_types: The map of the content types, assigned on the secret.
        :param pulumi.Input[str] created_at: The date the secret ACL was created.
        :param pulumi.Input[str] creator_id: The creator of the secret.
        :param pulumi.Input[str] expiration: The expiration time of the secret in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted, a secret will never expire. Changing this creates a new secret.
        :param pulumi.Input[Mapping[str, Any]] metadata: Additional Metadata for the secret.
        :param pulumi.Input[str] mode: Metadata provided by a user or system for informational purposes.
        :param pulumi.Input[str] name: Human-readable name for the Secret. Does not have
               to be unique.
        :param pulumi.Input[str] payload: The secret's data to be stored. **payload\_content\_type** must also be supplied if **payload** is included.
        :param pulumi.Input[str] payload_content_encoding: (required if **payload** is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either `base64` or `binary`.
        :param pulumi.Input[str] payload_content_type: (required if **payload** is included) The media type for the content of the payload. Must be one of `text/plain`, `text/plain;charset=utf-8`, `text/plain; charset=utf-8`, `application/octet-stream`, `application/pkcs8`.
        :param pulumi.Input[str] region: The region in which to obtain the V1 KeyManager client.
               A KeyManager client is needed to create a secret. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               V1 secret.
        :param pulumi.Input[str] secret_ref: The secret reference / where to find the secret.
        :param pulumi.Input[str] secret_type: Used to indicate the type of secret being stored. For more information see [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
        :param pulumi.Input[str] status: The status of the secret.
        :param pulumi.Input[str] updated_at: The date the secret ACL was last updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["acl"] = acl
        __props__["algorithm"] = algorithm
        __props__["all_metadata"] = all_metadata
        __props__["bit_length"] = bit_length
        __props__["content_types"] = content_types
        __props__["created_at"] = created_at
        __props__["creator_id"] = creator_id
        __props__["expiration"] = expiration
        __props__["metadata"] = metadata
        __props__["mode"] = mode
        __props__["name"] = name
        __props__["payload"] = payload
        __props__["payload_content_encoding"] = payload_content_encoding
        __props__["payload_content_type"] = payload_content_type
        __props__["region"] = region
        __props__["secret_ref"] = secret_ref
        __props__["secret_type"] = secret_type
        __props__["status"] = status
        __props__["updated_at"] = updated_at
        return SecretV1(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def acl(self) -> pulumi.Output['outputs.SecretV1Acl']:
        """
        Allows to control an access to a secret. Currently only the
        `read` operation is supported. If not specified, the secret is accessible
        project wide.
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Output[str]:
        """
        Metadata provided by a user or system for informational purposes.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="allMetadata")
    def all_metadata(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The map of metadata, assigned on the secret, which has been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "all_metadata")

    @property
    @pulumi.getter(name="bitLength")
    def bit_length(self) -> pulumi.Output[int]:
        """
        Metadata provided by a user or system for informational purposes.
        """
        return pulumi.get(self, "bit_length")

    @property
    @pulumi.getter(name="contentTypes")
    def content_types(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        The map of the content types, assigned on the secret.
        """
        return pulumi.get(self, "content_types")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date the secret ACL was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> pulumi.Output[str]:
        """
        The creator of the secret.
        """
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration time of the secret in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted, a secret will never expire. Changing this creates a new secret.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Additional Metadata for the secret.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        Metadata provided by a user or system for informational purposes.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human-readable name for the Secret. Does not have
        to be unique.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def payload(self) -> pulumi.Output[str]:
        """
        The secret's data to be stored. **payload\_content\_type** must also be supplied if **payload** is included.
        """
        return pulumi.get(self, "payload")

    @property
    @pulumi.getter(name="payloadContentEncoding")
    def payload_content_encoding(self) -> pulumi.Output[Optional[str]]:
        """
        (required if **payload** is encoded) The encoding used for the payload to be able to include it in the JSON request. Must be either `base64` or `binary`.
        """
        return pulumi.get(self, "payload_content_encoding")

    @property
    @pulumi.getter(name="payloadContentType")
    def payload_content_type(self) -> pulumi.Output[Optional[str]]:
        """
        (required if **payload** is included) The media type for the content of the payload. Must be one of `text/plain`, `text/plain;charset=utf-8`, `text/plain; charset=utf-8`, `application/octet-stream`, `application/pkcs8`.
        """
        return pulumi.get(self, "payload_content_type")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V1 KeyManager client.
        A KeyManager client is needed to create a secret. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        V1 secret.
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
    @pulumi.getter(name="secretType")
    def secret_type(self) -> pulumi.Output[str]:
        """
        Used to indicate the type of secret being stored. For more information see [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
        """
        return pulumi.get(self, "secret_type")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the secret.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The date the secret ACL was last updated.
        """
        return pulumi.get(self, "updated_at")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

