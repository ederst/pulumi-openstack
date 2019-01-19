# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
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
    """
    This is the directory where the images will
    be downloaded. Images will be stored with a filename corresponding to
    the url's md5 hash. Defaults to "$HOME/.terraform/image_cache"
    """
    image_source_url: pulumi.Output[str]
    """
    This is the url of the raw image that will
    be downloaded in the `image_cache_path` before being uploaded to Glance.
    Glance is able to download image from internet but the `gophercloud` library
    does not yet provide a way to do so.
    Conflicts with `local_file_path`.
    """
    local_file_path: pulumi.Output[str]
    """
    This is the filepath of the raw image file
    that will be uploaded to Glance. Conflicts with `image_source_url`.
    """
    metadata: pulumi.Output[dict]
    """
    The metadata associated with the image.
    Image metadata allow for meaningfully define the image properties
    and tags. See http://docs.openstack.org/developer/glance/metadefs-concepts.html.
    """
    min_disk_gb: pulumi.Output[int]
    """
    Amount of disk space (in GB) required to boot image.
    Defaults to 0.
    """
    min_ram_mb: pulumi.Output[int]
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
    size_bytes: pulumi.Output[int]
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
    The date the image was last updated.
    """
    verify_checksum: pulumi.Output[bool]
    """
    If false, the checksum will not be verified
    once the image is finished uploading. Defaults to true.
    """
    visibility: pulumi.Output[str]
    """
    The visibility of the image. Must be one of
    "public", "private", "community", or "shared". The ability to set the
    visibility depends upon the configuration of the OpenStack cloud.
    """
    def __init__(__self__, __name__, __opts__=None, container_format=None, disk_format=None, image_cache_path=None, image_source_url=None, local_file_path=None, min_disk_gb=None, min_ram_mb=None, name=None, properties=None, protected=None, region=None, tags=None, verify_checksum=None, visibility=None):
        """
        Manages a V2 Image resource within OpenStack Glance.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] container_format: The container format. Must be one of
               "ami", "ari", "aki", "bare", "ovf".
        :param pulumi.Input[str] disk_format: The disk format. Must be one of
               "ami", "ari", "aki", "vhd", "vmdk", "raw", "qcow2", "vdi", "iso".
        :param pulumi.Input[str] image_cache_path: This is the directory where the images will
               be downloaded. Images will be stored with a filename corresponding to
               the url's md5 hash. Defaults to "$HOME/.terraform/image_cache"
        :param pulumi.Input[str] image_source_url: This is the url of the raw image that will
               be downloaded in the `image_cache_path` before being uploaded to Glance.
               Glance is able to download image from internet but the `gophercloud` library
               does not yet provide a way to do so.
               Conflicts with `local_file_path`.
        :param pulumi.Input[str] local_file_path: This is the filepath of the raw image file
               that will be uploaded to Glance. Conflicts with `image_source_url`.
        :param pulumi.Input[int] min_disk_gb: Amount of disk space (in GB) required to boot image.
               Defaults to 0.
        :param pulumi.Input[int] min_ram_mb: Amount of ram (in MB) required to boot image.
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
               once the image is finished uploading. Defaults to true.
        :param pulumi.Input[str] visibility: The visibility of the image. Must be one of
               "public", "private", "community", or "shared". The ability to set the
               visibility depends upon the configuration of the OpenStack cloud.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not container_format:
            raise TypeError('Missing required property container_format')
        __props__['container_format'] = container_format

        if not disk_format:
            raise TypeError('Missing required property disk_format')
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

        __props__['checksum'] = None
        __props__['created_at'] = None
        __props__['file'] = None
        __props__['metadata'] = None
        __props__['owner'] = None
        __props__['schema'] = None
        __props__['size_bytes'] = None
        __props__['status'] = None
        __props__['update_at'] = None

        super(Image, __self__).__init__(
            'openstack:images/image:Image',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

