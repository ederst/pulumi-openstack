# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ContainerObject(pulumi.CustomResource):
    container_name: pulumi.Output[str]
    """
    A unique (within an account) name for the container. 
    The container name must be from 1 to 256 characters long and can start
    with any character and contain any pattern. Character set must be UTF-8.
    The container name cannot contain a slash (/) character because this
    character delimits the container and object name. For example, the path
    /v1/account/www/pages specifies the www container, not the www/pages container.
    """
    content: pulumi.Output[str]
    """
    A string representing the content of the object. Conflicts with
    `source` and `copy_from`.
    """
    content_disposition: pulumi.Output[str]
    """
    A string which specifies the override behavior for 
    the browser. For example, this header might specify that the browser use a download
    program to save this file rather than show the file, which is the default.
    """
    content_encoding: pulumi.Output[str]
    """
    A string representing the value of the Content-Encoding
    metadata.
    """
    content_length: pulumi.Output[float]
    """
    If the operation succeeds, this value is zero (0) or the 
    length of informational or error text in the response body.
    """
    content_type: pulumi.Output[str]
    """
    A string which sets the MIME type for the object.
    """
    copy_from: pulumi.Output[str]
    """
    A string representing the name of an object 
    used to create the new object by copying the `copy_from` object. The value is in form
    {container}/{object}. You must UTF-8-encode and then URL-encode the names of the
    container and object before you include them in the header. Conflicts with `source` and
    `content`.
    """
    date: pulumi.Output[str]
    """
    The date and time the system responded to the request, using the preferred 
    format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
    time is always in UTC.
    """
    delete_after: pulumi.Output[float]
    """
    An integer representing the number of seconds after which the
    system removes the object. Internally, the Object Storage system stores this value in
    the X-Delete-At metadata item.
    """
    delete_at: pulumi.Output[str]
    """
    An string representing the date when the system removes the object. 
    For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
    """
    detect_content_type: pulumi.Output[bool]
    """
    If set to true, Object Storage guesses the content 
    type based on the file extension and ignores the value sent in the Content-Type
    header, if present.
    """
    etag: pulumi.Output[str]
    """
    Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
    """
    last_modified: pulumi.Output[str]
    """
    The date and time when the object was last modified. The date and time 
    stamp format is ISO 8601:
    CCYY-MM-DDThh:mm:ss±hh:mm
    For example, 2015-08-27T09:49:58-05:00.
    The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
    example, the offset value is -05:00.
    """
    metadata: pulumi.Output[dict]
    name: pulumi.Output[str]
    """
    A unique name for the object.
    """
    object_manifest: pulumi.Output[str]
    """
    A string set to specify that this is a dynamic large 
    object manifest object. The value is the container and object name prefix of the
    segment objects in the form container/prefix. You must UTF-8-encode and then
    URL-encode the names of the container and prefix before you include them in this
    header.
    """
    region: pulumi.Output[str]
    """
    The region in which to create the container. If
    omitted, the `region` argument of the provider is used. Changing this
    creates a new container.
    """
    source: pulumi.Output[str]
    """
    A string representing the local path of a file which will be used
    as the object's content. Conflicts with `source` and `copy_from`.
    """
    trans_id: pulumi.Output[str]
    """
    A unique transaction ID for this request. Your service provider might 
    need this value if you report a problem.
    """
    def __init__(__self__, resource_name, opts=None, container_name=None, content=None, content_disposition=None, content_encoding=None, content_type=None, copy_from=None, delete_after=None, delete_at=None, detect_content_type=None, etag=None, metadata=None, name=None, object_manifest=None, region=None, source=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V1 container object resource within OpenStack.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/objectstorage_object_v1.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_name: A unique (within an account) name for the container. 
               The container name must be from 1 to 256 characters long and can start
               with any character and contain any pattern. Character set must be UTF-8.
               The container name cannot contain a slash (/) character because this
               character delimits the container and object name. For example, the path
               /v1/account/www/pages specifies the www container, not the www/pages container.
        :param pulumi.Input[str] content: A string representing the content of the object. Conflicts with
               `source` and `copy_from`.
        :param pulumi.Input[str] content_disposition: A string which specifies the override behavior for 
               the browser. For example, this header might specify that the browser use a download
               program to save this file rather than show the file, which is the default.
        :param pulumi.Input[str] content_encoding: A string representing the value of the Content-Encoding
               metadata.
        :param pulumi.Input[str] content_type: A string which sets the MIME type for the object.
        :param pulumi.Input[str] copy_from: A string representing the name of an object 
               used to create the new object by copying the `copy_from` object. The value is in form
               {container}/{object}. You must UTF-8-encode and then URL-encode the names of the
               container and object before you include them in the header. Conflicts with `source` and
               `content`.
        :param pulumi.Input[float] delete_after: An integer representing the number of seconds after which the
               system removes the object. Internally, the Object Storage system stores this value in
               the X-Delete-At metadata item.
        :param pulumi.Input[str] delete_at: An string representing the date when the system removes the object. 
               For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
        :param pulumi.Input[bool] detect_content_type: If set to true, Object Storage guesses the content 
               type based on the file extension and ignores the value sent in the Content-Type
               header, if present.
        :param pulumi.Input[str] etag: Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
        :param pulumi.Input[str] name: A unique name for the object.
        :param pulumi.Input[str] object_manifest: A string set to specify that this is a dynamic large 
               object manifest object. The value is the container and object name prefix of the
               segment objects in the form container/prefix. You must UTF-8-encode and then
               URL-encode the names of the container and prefix before you include them in this
               header.
        :param pulumi.Input[str] region: The region in which to create the container. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new container.
        :param pulumi.Input[str] source: A string representing the local path of a file which will be used
               as the object's content. Conflicts with `source` and `copy_from`.
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

            if container_name is None:
                raise TypeError("Missing required property 'container_name'")
            __props__['container_name'] = container_name
            __props__['content'] = content
            __props__['content_disposition'] = content_disposition
            __props__['content_encoding'] = content_encoding
            __props__['content_type'] = content_type
            __props__['copy_from'] = copy_from
            __props__['delete_after'] = delete_after
            __props__['delete_at'] = delete_at
            __props__['detect_content_type'] = detect_content_type
            __props__['etag'] = etag
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['object_manifest'] = object_manifest
            __props__['region'] = region
            __props__['source'] = source
            __props__['content_length'] = None
            __props__['date'] = None
            __props__['last_modified'] = None
            __props__['trans_id'] = None
        super(ContainerObject, __self__).__init__(
            'openstack:objectstorage/containerObject:ContainerObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, container_name=None, content=None, content_disposition=None, content_encoding=None, content_length=None, content_type=None, copy_from=None, date=None, delete_after=None, delete_at=None, detect_content_type=None, etag=None, last_modified=None, metadata=None, name=None, object_manifest=None, region=None, source=None, trans_id=None):
        """
        Get an existing ContainerObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_name: A unique (within an account) name for the container. 
               The container name must be from 1 to 256 characters long and can start
               with any character and contain any pattern. Character set must be UTF-8.
               The container name cannot contain a slash (/) character because this
               character delimits the container and object name. For example, the path
               /v1/account/www/pages specifies the www container, not the www/pages container.
        :param pulumi.Input[str] content: A string representing the content of the object. Conflicts with
               `source` and `copy_from`.
        :param pulumi.Input[str] content_disposition: A string which specifies the override behavior for 
               the browser. For example, this header might specify that the browser use a download
               program to save this file rather than show the file, which is the default.
        :param pulumi.Input[str] content_encoding: A string representing the value of the Content-Encoding
               metadata.
        :param pulumi.Input[float] content_length: If the operation succeeds, this value is zero (0) or the 
               length of informational or error text in the response body.
        :param pulumi.Input[str] content_type: A string which sets the MIME type for the object.
        :param pulumi.Input[str] copy_from: A string representing the name of an object 
               used to create the new object by copying the `copy_from` object. The value is in form
               {container}/{object}. You must UTF-8-encode and then URL-encode the names of the
               container and object before you include them in the header. Conflicts with `source` and
               `content`.
        :param pulumi.Input[str] date: The date and time the system responded to the request, using the preferred 
               format of RFC 7231 as shown in this example Thu, 16 Jun 2016 15:10:38 GMT. The
               time is always in UTC.
        :param pulumi.Input[float] delete_after: An integer representing the number of seconds after which the
               system removes the object. Internally, the Object Storage system stores this value in
               the X-Delete-At metadata item.
        :param pulumi.Input[str] delete_at: An string representing the date when the system removes the object. 
               For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.
        :param pulumi.Input[bool] detect_content_type: If set to true, Object Storage guesses the content 
               type based on the file extension and ignores the value sent in the Content-Type
               header, if present.
        :param pulumi.Input[str] etag: Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.
        :param pulumi.Input[str] last_modified: The date and time when the object was last modified. The date and time 
               stamp format is ISO 8601:
               CCYY-MM-DDThh:mm:ss±hh:mm
               For example, 2015-08-27T09:49:58-05:00.
               The ±hh:mm value, if included, is the time zone as an offset from UTC. In the previous
               example, the offset value is -05:00.
        :param pulumi.Input[str] name: A unique name for the object.
        :param pulumi.Input[str] object_manifest: A string set to specify that this is a dynamic large 
               object manifest object. The value is the container and object name prefix of the
               segment objects in the form container/prefix. You must UTF-8-encode and then
               URL-encode the names of the container and prefix before you include them in this
               header.
        :param pulumi.Input[str] region: The region in which to create the container. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new container.
        :param pulumi.Input[str] source: A string representing the local path of a file which will be used
               as the object's content. Conflicts with `source` and `copy_from`.
        :param pulumi.Input[str] trans_id: A unique transaction ID for this request. Your service provider might 
               need this value if you report a problem.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["container_name"] = container_name
        __props__["content"] = content
        __props__["content_disposition"] = content_disposition
        __props__["content_encoding"] = content_encoding
        __props__["content_length"] = content_length
        __props__["content_type"] = content_type
        __props__["copy_from"] = copy_from
        __props__["date"] = date
        __props__["delete_after"] = delete_after
        __props__["delete_at"] = delete_at
        __props__["detect_content_type"] = detect_content_type
        __props__["etag"] = etag
        __props__["last_modified"] = last_modified
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["object_manifest"] = object_manifest
        __props__["region"] = region
        __props__["source"] = source
        __props__["trans_id"] = trans_id
        return ContainerObject(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

