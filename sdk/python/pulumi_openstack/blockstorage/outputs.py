# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'VolumeAttachment',
    'VolumeSchedulerHint',
    'VolumeV1Attachment',
    'VolumeV2Attachment',
    'VolumeV2SchedulerHint',
]

@pulumi.output_type
class VolumeAttachment(dict):
    def __init__(__self__, *,
                 device: Optional[str] = None,
                 id: Optional[str] = None,
                 instance_id: Optional[str] = None):
        if device is not None:
            pulumi.set(__self__, "device", device)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter
    def device(self) -> Optional[str]:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeSchedulerHint(dict):
    def __init__(__self__, *,
                 additional_properties: Optional[Mapping[str, Any]] = None,
                 different_hosts: Optional[Sequence[str]] = None,
                 local_to_instance: Optional[str] = None,
                 query: Optional[str] = None,
                 same_hosts: Optional[Sequence[str]] = None):
        """
        :param Mapping[str, Any] additional_properties: Arbitrary key/value pairs of additional
               properties to pass to the scheduler.
        :param Sequence[str] different_hosts: The volume should be scheduled on a 
               different host from the set of volumes specified in the list provided.
        :param str local_to_instance: An instance UUID. The volume should be 
               scheduled on the same host as the instance.
        :param str query: A conditional query that a back-end must pass in
               order to host a volume. The query must use the `JsonFilter` syntax
               which is described
               [here](https://docs.openstack.org/cinder/latest/configuration/block-storage/scheduler-filters.html#jsonfilter).
               At this time, only simple queries are supported. Compound queries using
               `and`, `or`, or `not` are not supported. An example of a simple query is:
        :param Sequence[str] same_hosts: A list of volume UUIDs. The volume should be
               scheduled on the same host as another volume specified in the list provided.
        """
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if different_hosts is not None:
            pulumi.set(__self__, "different_hosts", different_hosts)
        if local_to_instance is not None:
            pulumi.set(__self__, "local_to_instance", local_to_instance)
        if query is not None:
            pulumi.set(__self__, "query", query)
        if same_hosts is not None:
            pulumi.set(__self__, "same_hosts", same_hosts)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[Mapping[str, Any]]:
        """
        Arbitrary key/value pairs of additional
        properties to pass to the scheduler.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter(name="differentHosts")
    def different_hosts(self) -> Optional[Sequence[str]]:
        """
        The volume should be scheduled on a 
        different host from the set of volumes specified in the list provided.
        """
        return pulumi.get(self, "different_hosts")

    @property
    @pulumi.getter(name="localToInstance")
    def local_to_instance(self) -> Optional[str]:
        """
        An instance UUID. The volume should be 
        scheduled on the same host as the instance.
        """
        return pulumi.get(self, "local_to_instance")

    @property
    @pulumi.getter
    def query(self) -> Optional[str]:
        """
        A conditional query that a back-end must pass in
        order to host a volume. The query must use the `JsonFilter` syntax
        which is described
        [here](https://docs.openstack.org/cinder/latest/configuration/block-storage/scheduler-filters.html#jsonfilter).
        At this time, only simple queries are supported. Compound queries using
        `and`, `or`, or `not` are not supported. An example of a simple query is:
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="sameHosts")
    def same_hosts(self) -> Optional[Sequence[str]]:
        """
        A list of volume UUIDs. The volume should be
        scheduled on the same host as another volume specified in the list provided.
        """
        return pulumi.get(self, "same_hosts")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeV1Attachment(dict):
    def __init__(__self__, *,
                 device: Optional[str] = None,
                 id: Optional[str] = None,
                 instance_id: Optional[str] = None):
        if device is not None:
            pulumi.set(__self__, "device", device)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter
    def device(self) -> Optional[str]:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeV2Attachment(dict):
    def __init__(__self__, *,
                 device: Optional[str] = None,
                 id: Optional[str] = None,
                 instance_id: Optional[str] = None):
        if device is not None:
            pulumi.set(__self__, "device", device)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)

    @property
    @pulumi.getter
    def device(self) -> Optional[str]:
        return pulumi.get(self, "device")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        return pulumi.get(self, "instance_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class VolumeV2SchedulerHint(dict):
    def __init__(__self__, *,
                 additional_properties: Optional[Mapping[str, Any]] = None,
                 different_hosts: Optional[Sequence[str]] = None,
                 local_to_instance: Optional[str] = None,
                 query: Optional[str] = None,
                 same_hosts: Optional[Sequence[str]] = None):
        """
        :param Mapping[str, Any] additional_properties: Arbitrary key/value pairs of additional
               properties to pass to the scheduler.
        :param Sequence[str] different_hosts: The volume should be scheduled on a 
               different host from the set of volumes specified in the list provided.
        :param str local_to_instance: An instance UUID. The volume should be 
               scheduled on the same host as the instance.
        :param str query: A conditional query that a back-end must pass in
               order to host a volume. The query must use the `JsonFilter` syntax
               which is described
               [here](https://docs.openstack.org/cinder/latest/configuration/block-storage/scheduler-filters.html#jsonfilter).
               At this time, only simple queries are supported. Compound queries using
               `and`, `or`, or `not` are not supported. An example of a simple query is:
        :param Sequence[str] same_hosts: A list of volume UUIDs. The volume should be
               scheduled on the same host as another volume specified in the list provided.
        """
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if different_hosts is not None:
            pulumi.set(__self__, "different_hosts", different_hosts)
        if local_to_instance is not None:
            pulumi.set(__self__, "local_to_instance", local_to_instance)
        if query is not None:
            pulumi.set(__self__, "query", query)
        if same_hosts is not None:
            pulumi.set(__self__, "same_hosts", same_hosts)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[Mapping[str, Any]]:
        """
        Arbitrary key/value pairs of additional
        properties to pass to the scheduler.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter(name="differentHosts")
    def different_hosts(self) -> Optional[Sequence[str]]:
        """
        The volume should be scheduled on a 
        different host from the set of volumes specified in the list provided.
        """
        return pulumi.get(self, "different_hosts")

    @property
    @pulumi.getter(name="localToInstance")
    def local_to_instance(self) -> Optional[str]:
        """
        An instance UUID. The volume should be 
        scheduled on the same host as the instance.
        """
        return pulumi.get(self, "local_to_instance")

    @property
    @pulumi.getter
    def query(self) -> Optional[str]:
        """
        A conditional query that a back-end must pass in
        order to host a volume. The query must use the `JsonFilter` syntax
        which is described
        [here](https://docs.openstack.org/cinder/latest/configuration/block-storage/scheduler-filters.html#jsonfilter).
        At this time, only simple queries are supported. Compound queries using
        `and`, `or`, or `not` are not supported. An example of a simple query is:
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="sameHosts")
    def same_hosts(self) -> Optional[Sequence[str]]:
        """
        A list of volume UUIDs. The volume should be
        scheduled on the same host as another volume specified in the list provided.
        """
        return pulumi.get(self, "same_hosts")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


