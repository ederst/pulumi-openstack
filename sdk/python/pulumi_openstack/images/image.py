# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Image(pulumi.CustomResource):
    checksum: pulumi.Output[str]
    """
    The checksum of the data associated with the image.
    """
    container_format: pulumi.Output[str]
    """
    The container format. Must be one of
    "ami", "ari", "aki", "bare", "ovf".
    """
    created_at: pulumi.Output[str]
    """
    The date the image was created.
    """
    disk_format: pulumi.Output[str]
    """
    The disk format. Must be one of
    "ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".
    """
    file: pulumi.Output[str]
    """
    the trailing path after the glance
    endpoint that represent the location of the image
    or the path to retrieve it.
    """
    image_cache_path: pulumi.Output[str]
    image_source_url: pulumi.Output[str]
    """
    This is the url of the raw image. If `web_download`
    is not used, then the image will be downloaded in the `image_cache_path` before
    being uploaded to Glance.
    Conflicts with `local_file_path`.
    """
    local_file_path: pulumi.Output[str]
    """
    This is the filepath of the raw image file
    that will be uploaded to Glance. Conflicts with `image_source_url` and
    `web_download`.
    """
    metadata: pulumi.Output[dict]
    """
    The metadata associated with the image.
    Image metadata allow for meaningfully define the image properties
    and tags. See https://docs.openstack.org/glance/latest/user/metadefs-concepts.html.
    """
    min_disk_gb: pulumi.Output[float]
    """
    Amount of disk space (in GB) required to boot image.
    Defaults to 0.
    """
    min_ram_mb: pulumi.Output[float]
    """
    Amount of ram (in MB) required to boot image.
    Defauts to 0.
    """
    name: pulumi.Output[str]
    """
    The name of the image.
    """
    owner: pulumi.Output[str]
    """
    The id of the openstack user who owns the image.
    """
    properties: pulumi.Output[dict]
    """
    A map of key/value pairs to set freeform
    information about an image. See the "Notes" section for further
    information about properties.
    """
    protected: pulumi.Output[bool]
    """
    If true, image will not be deletable.
    Defaults to false.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Glance client.
    A Glance client is needed to create an Image that can be used with
    a compute instance. If omitted, the `region` argument of the provider
    is used. Changing this creates a new Image.
    """
    schema: pulumi.Output[str]
    """
    The path to the JSON-schema that represent
    the image or image
    """
    size_bytes: pulumi.Output[float]
    """
    The size in bytes of the data associated with the image.
    """
    status: pulumi.Output[str]
    """
    The status of the image. It can be "queued", "active"
    or "saving".
    """
    tags: pulumi.Output[list]
    """
    The tags of the image. It must be a list of strings.
    At this time, it is not possible to delete all tags of an image.
    """
    update_at: pulumi.Output[str]
    """
    (**Deprecated** - use `updated_at` instead)
    """
    updated_at: pulumi.Output[str]
    """
    The date the image was last updated.
    """
    verify_checksum: pulumi.Output[bool]
    """
    If false, the checksum will not be verified
    once the image is finished uploading. Conflicts with `web_download`.
    Defaults to true when not using `web_download`.
    """
    visibility: pulumi.Output[str]
    """
    The visibility of the image. Must be one of
    "public", "private", "community", or "shared". The ability to set the
    visibility depends upon the configuration of the OpenStack cloud.
    """
    web_download: pulumi.Output[bool]
    """
    If true, the "web-download" import method will
    be used to let Openstack download the image directly from the remote source.
    Conflicts with `local_file_path`. Defaults to false.
    """
    def __init__(__self__, resource_name, opts=None, container_format=None, disk_format=None, image_cache_path=None, image_source_url=None, local_file_path=None, min_disk_gb=None, min_ram_mb=None, name=None, properties=None, protected=None, region=None, tags=None, verify_checksum=None, visibility=None, web_download=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 Image resource within OpenStack Glance.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_openstack as openstack

        rancheros = openstack.images.Image("rancheros",
            container_format="bare",
            disk_format="qcow2",
            image_source_url="https://releases.rancher.com/os/latest/rancheros-openstack.img",
            properties={
                "key": "value",
            })
        ```

        ## Notes

        ### Properties

        This resource supports the ability to add properties to a resource during
        creation as well as add, update, and delete properties during an update of this
        resource.

        Newer versions of OpenStack are adding some read-only properties to each image.
        These properties start with the prefix `os_`. If these properties are detected,
        this resource will automatically reconcile these with the user-provided
        properties.

        In addition, the `direct_url` property is also automatically reconciled if the
        Image Service set it.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_format: The container format. Must be one of
               "ami", "ari", "aki", "bare", "ovf".
        :param pulumi.Input[str] disk_format: The disk format. Must be one of
               "ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".
        :param pulumi.Input[str] image_source_url: This is the url of the raw image. If `web_download`
               is not used, then the image will be downloaded in the `image_cache_path` before
               being uploaded to Glance.
               Conflicts with `local_file_path`.
        :param pulumi.Input[str] local_file_path: This is the filepath of the raw image file
               that will be uploaded to Glance. Conflicts with `image_source_url` and
               `web_download`.
        :param pulumi.Input[float] min_disk_gb: Amount of disk space (in GB) required to boot image.
               Defaults to 0.
        :param pulumi.Input[float] min_ram_mb: Amount of ram (in MB) required to boot image.
               Defauts to 0.
        :param pulumi.Input[str] name: The name of the image.
        :param pulumi.Input[dict] properties: A map of key/value pairs to set freeform
               information about an image. See the "Notes" section for further
               information about properties.
        :param pulumi.Input[bool] protected: If true, image will not be deletable.
               Defaults to false.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Glance client.
               A Glance client is needed to create an Image that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new Image.
        :param pulumi.Input[list] tags: The tags of the image. It must be a list of strings.
               At this time, it is not possible to delete all tags of an image.
        :param pulumi.Input[bool] verify_checksum: If false, the checksum will not be verified
               once the image is finished uploading. Conflicts with `web_download`.
               Defaults to true when not using `web_download`.
        :param pulumi.Input[str] visibility: The visibility of the image. Must be one of
               "public", "private", "community", or "shared". The ability to set the
               visibility depends upon the configuration of the OpenStack cloud.
        :param pulumi.Input[bool] web_download: If true, the "web-download" import method will
               be used to let Openstack download the image directly from the remote source.
               Conflicts with `local_file_path`. Defaults to false.
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

            if container_format is None:
                raise TypeError("Missing required property 'container_format'")
            __props__['container_format'] = container_format
            if disk_format is None:
                raise TypeError("Missing required property 'disk_format'")
            __props__['disk_format'] = disk_format
            __props__['image_cache_path'] = image_cache_path
            __props__['image_source_url'] = image_source_url
            __props__['local_file_path'] = local_file_path
            __props__['min_disk_gb'] = min_disk_gb
            __props__['min_ram_mb'] = min_ram_mb
            __props__['name'] = name
            __props__['properties'] = properties
            __props__['protected'] = protected
            __props__['region'] = region
            __props__['tags'] = tags
            __props__['verify_checksum'] = verify_checksum
            __props__['visibility'] = visibility
            __props__['web_download'] = web_download
            __props__['checksum'] = None
            __props__['created_at'] = None
            __props__['file'] = None
            __props__['metadata'] = None
            __props__['owner'] = None
            __props__['schema'] = None
            __props__['size_bytes'] = None
            __props__['status'] = None
            __props__['update_at'] = None
            __props__['updated_at'] = None
        super(Image, __self__).__init__(
            'openstack:images/image:Image',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, checksum=None, container_format=None, created_at=None, disk_format=None, file=None, image_cache_path=None, image_source_url=None, local_file_path=None, metadata=None, min_disk_gb=None, min_ram_mb=None, name=None, owner=None, properties=None, protected=None, region=None, schema=None, size_bytes=None, status=None, tags=None, update_at=None, updated_at=None, verify_checksum=None, visibility=None, web_download=None):
        """
        Get an existing Image resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] checksum: The checksum of the data associated with the image.
        :param pulumi.Input[str] container_format: The container format. Must be one of
               "ami", "ari", "aki", "bare", "ovf".
        :param pulumi.Input[str] created_at: The date the image was created.
        :param pulumi.Input[str] disk_format: The disk format. Must be one of
               "ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".
        :param pulumi.Input[str] file: the trailing path after the glance
               endpoint that represent the location of the image
               or the path to retrieve it.
        :param pulumi.Input[str] image_source_url: This is the url of the raw image. If `web_download`
               is not used, then the image will be downloaded in the `image_cache_path` before
               being uploaded to Glance.
               Conflicts with `local_file_path`.
        :param pulumi.Input[str] local_file_path: This is the filepath of the raw image file
               that will be uploaded to Glance. Conflicts with `image_source_url` and
               `web_download`.
        :param pulumi.Input[dict] metadata: The metadata associated with the image.
               Image metadata allow for meaningfully define the image properties
               and tags. See https://docs.openstack.org/glance/latest/user/metadefs-concepts.html.
        :param pulumi.Input[float] min_disk_gb: Amount of disk space (in GB) required to boot image.
               Defaults to 0.
        :param pulumi.Input[float] min_ram_mb: Amount of ram (in MB) required to boot image.
               Defauts to 0.
        :param pulumi.Input[str] name: The name of the image.
        :param pulumi.Input[str] owner: The id of the openstack user who owns the image.
        :param pulumi.Input[dict] properties: A map of key/value pairs to set freeform
               information about an image. See the "Notes" section for further
               information about properties.
        :param pulumi.Input[bool] protected: If true, image will not be deletable.
               Defaults to false.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Glance client.
               A Glance client is needed to create an Image that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new Image.
        :param pulumi.Input[str] schema: The path to the JSON-schema that represent
               the image or image
        :param pulumi.Input[float] size_bytes: The size in bytes of the data associated with the image.
        :param pulumi.Input[str] status: The status of the image. It can be "queued", "active"
               or "saving".
        :param pulumi.Input[list] tags: The tags of the image. It must be a list of strings.
               At this time, it is not possible to delete all tags of an image.
        :param pulumi.Input[str] update_at: (**Deprecated** - use `updated_at` instead)
        :param pulumi.Input[str] updated_at: The date the image was last updated.
        :param pulumi.Input[bool] verify_checksum: If false, the checksum will not be verified
               once the image is finished uploading. Conflicts with `web_download`.
               Defaults to true when not using `web_download`.
        :param pulumi.Input[str] visibility: The visibility of the image. Must be one of
               "public", "private", "community", or "shared". The ability to set the
               visibility depends upon the configuration of the OpenStack cloud.
        :param pulumi.Input[bool] web_download: If true, the "web-download" import method will
               be used to let Openstack download the image directly from the remote source.
               Conflicts with `local_file_path`. Defaults to false.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["checksum"] = checksum
        __props__["container_format"] = container_format
        __props__["created_at"] = created_at
        __props__["disk_format"] = disk_format
        __props__["file"] = file
        __props__["image_cache_path"] = image_cache_path
        __props__["image_source_url"] = image_source_url
        __props__["local_file_path"] = local_file_path
        __props__["metadata"] = metadata
        __props__["min_disk_gb"] = min_disk_gb
        __props__["min_ram_mb"] = min_ram_mb
        __props__["name"] = name
        __props__["owner"] = owner
        __props__["properties"] = properties
        __props__["protected"] = protected
        __props__["region"] = region
        __props__["schema"] = schema
        __props__["size_bytes"] = size_bytes
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["update_at"] = update_at
        __props__["updated_at"] = updated_at
        __props__["verify_checksum"] = verify_checksum
        __props__["visibility"] = visibility
        __props__["web_download"] = web_download
        return Image(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

