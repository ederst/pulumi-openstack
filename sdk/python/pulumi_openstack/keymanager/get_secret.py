# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class GetSecretResult:
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, acl_only=None, acls=None, algorithm=None, bit_length=None, content_types=None, created_at=None, created_at_filter=None, creator_id=None, expiration=None, expiration_filter=None, id=None, metadata=None, mode=None, name=None, payload=None, payload_content_encoding=None, payload_content_type=None, region=None, secret_ref=None, secret_type=None, status=None, updated_at=None, updated_at_filter=None):
        if acl_only and not isinstance(acl_only, bool):
            raise TypeError("Expected argument 'acl_only' to be a bool")
        __self__.acl_only = acl_only
        """
        See Argument Reference above.
        """
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        __self__.acls = acls
        """
        The list of ACLs assigned to a secret. The `read` structure is described below.
        """
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        __self__.algorithm = algorithm
        """
        See Argument Reference above.
        """
        if bit_length and not isinstance(bit_length, float):
            raise TypeError("Expected argument 'bit_length' to be a float")
        __self__.bit_length = bit_length
        """
        See Argument Reference above.
        """
        if content_types and not isinstance(content_types, dict):
            raise TypeError("Expected argument 'content_types' to be a dict")
        __self__.content_types = content_types
        """
        The map of the content types, assigned on the secret.
        """
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        __self__.created_at = created_at
        """
        The date the secret ACL was created.
        """
        if created_at_filter and not isinstance(created_at_filter, str):
            raise TypeError("Expected argument 'created_at_filter' to be a str")
        __self__.created_at_filter = created_at_filter
        """
        See Argument Reference above.
        """
        if creator_id and not isinstance(creator_id, str):
            raise TypeError("Expected argument 'creator_id' to be a str")
        __self__.creator_id = creator_id
        """
        The creator of the secret.
        """
        if expiration and not isinstance(expiration, str):
            raise TypeError("Expected argument 'expiration' to be a str")
        __self__.expiration = expiration
        """
        The date the secret will expire.
        """
        if expiration_filter and not isinstance(expiration_filter, str):
            raise TypeError("Expected argument 'expiration_filter' to be a str")
        __self__.expiration_filter = expiration_filter
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        __self__.metadata = metadata
        """
        The map of metadata, assigned on the secret, which has been
        explicitly and implicitly added.
        """
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        __self__.mode = mode
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if payload and not isinstance(payload, str):
            raise TypeError("Expected argument 'payload' to be a str")
        __self__.payload = payload
        """
        The secret payload.
        """
        if payload_content_encoding and not isinstance(payload_content_encoding, str):
            raise TypeError("Expected argument 'payload_content_encoding' to be a str")
        __self__.payload_content_encoding = payload_content_encoding
        """
        The Secret encoding.
        """
        if payload_content_type and not isinstance(payload_content_type, str):
            raise TypeError("Expected argument 'payload_content_type' to be a str")
        __self__.payload_content_type = payload_content_type
        """
        The Secret content type.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        See Argument Reference above.
        """
        if secret_ref and not isinstance(secret_ref, str):
            raise TypeError("Expected argument 'secret_ref' to be a str")
        __self__.secret_ref = secret_ref
        """
        The secret reference / where to find the secret.
        """
        if secret_type and not isinstance(secret_type, str):
            raise TypeError("Expected argument 'secret_type' to be a str")
        __self__.secret_type = secret_type
        """
        See Argument Reference above.
        """
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        The status of the secret.
        """
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        __self__.updated_at = updated_at
        """
        The date the secret ACL was last updated.
        """
        if updated_at_filter and not isinstance(updated_at_filter, str):
            raise TypeError("Expected argument 'updated_at_filter' to be a str")
        __self__.updated_at_filter = updated_at_filter
        """
        See Argument Reference above.
        """


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            acl_only=self.acl_only,
            acls=self.acls,
            algorithm=self.algorithm,
            bit_length=self.bit_length,
            content_types=self.content_types,
            created_at=self.created_at,
            created_at_filter=self.created_at_filter,
            creator_id=self.creator_id,
            expiration=self.expiration,
            expiration_filter=self.expiration_filter,
            id=self.id,
            metadata=self.metadata,
            mode=self.mode,
            name=self.name,
            payload=self.payload,
            payload_content_encoding=self.payload_content_encoding,
            payload_content_type=self.payload_content_type,
            region=self.region,
            secret_ref=self.secret_ref,
            secret_type=self.secret_type,
            status=self.status,
            updated_at=self.updated_at,
            updated_at_filter=self.updated_at_filter)


def get_secret(acl_only=None, algorithm=None, bit_length=None, created_at_filter=None, expiration_filter=None, mode=None, name=None, region=None, secret_type=None, updated_at_filter=None, opts=None):
    """
    Use this data source to access information about an existing resource.

    :param bool acl_only: Select the Secret with an ACL that contains the user.
           Project scope is ignored. Defaults to `false`.
    :param str algorithm: The Secret algorithm.
    :param float bit_length: The Secret bit length.
    :param str created_at_filter: Date filter to select the Secret with
           created matching the specified criteria. See Date Filters below for more
           detail.
    :param str expiration_filter: Date filter to select the Secret with
           expiration matching the specified criteria. See Date Filters below for more
           detail.
    :param str mode: The Secret mode.
    :param str name: The Secret name.
    :param str region: The region in which to obtain the V1 KeyManager client.
           A KeyManager client is needed to fetch a secret. If omitted, the `region`
           argument of the provider is used.
    :param str secret_type: The Secret type. For more information see
           [Secret types](https://docs.openstack.org/barbican/latest/api/reference/secret_types.html).
    :param str updated_at_filter: Date filter to select the Secret with
           updated matching the specified criteria. See Date Filters below for more
           detail.
    """
    __args__ = dict()
    __args__['aclOnly'] = acl_only
    __args__['algorithm'] = algorithm
    __args__['bitLength'] = bit_length
    __args__['createdAtFilter'] = created_at_filter
    __args__['expirationFilter'] = expiration_filter
    __args__['mode'] = mode
    __args__['name'] = name
    __args__['region'] = region
    __args__['secretType'] = secret_type
    __args__['updatedAtFilter'] = updated_at_filter
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:keymanager/getSecret:getSecret', __args__, opts=opts).value

    return AwaitableGetSecretResult(
        acl_only=__ret__.get('aclOnly'),
        acls=__ret__.get('acls'),
        algorithm=__ret__.get('algorithm'),
        bit_length=__ret__.get('bitLength'),
        content_types=__ret__.get('contentTypes'),
        created_at=__ret__.get('createdAt'),
        created_at_filter=__ret__.get('createdAtFilter'),
        creator_id=__ret__.get('creatorId'),
        expiration=__ret__.get('expiration'),
        expiration_filter=__ret__.get('expirationFilter'),
        id=__ret__.get('id'),
        metadata=__ret__.get('metadata'),
        mode=__ret__.get('mode'),
        name=__ret__.get('name'),
        payload=__ret__.get('payload'),
        payload_content_encoding=__ret__.get('payloadContentEncoding'),
        payload_content_type=__ret__.get('payloadContentType'),
        region=__ret__.get('region'),
        secret_ref=__ret__.get('secretRef'),
        secret_type=__ret__.get('secretType'),
        status=__ret__.get('status'),
        updated_at=__ret__.get('updatedAt'),
        updated_at_filter=__ret__.get('updatedAtFilter'))
