# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ConfigurationConfiguration',
    'ConfigurationDatastore',
    'InstanceDatabase',
    'InstanceDatastore',
    'InstanceNetwork',
    'InstanceUser',
]

@pulumi.output_type
class ConfigurationConfiguration(dict):
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        :param str name: Configuration parameter name. Changing this creates a new resource.
        :param str value: Configuration parameter value. Changing this creates a new resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Configuration parameter name. Changing this creates a new resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Configuration parameter value. Changing this creates a new resource.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ConfigurationDatastore(dict):
    def __init__(__self__, *,
                 type: str,
                 version: str):
        """
        :param str type: Database engine type to be used with this configuration. Changing this creates a new resource.
        :param str version: Version of database engine type to be used with this configuration. Changing this creates a new resource.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Database engine type to be used with this configuration. Changing this creates a new resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of database engine type to be used with this configuration. Changing this creates a new resource.
        """
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceDatabase(dict):
    def __init__(__self__, *,
                 name: str,
                 charset: Optional[str] = None,
                 collate: Optional[str] = None):
        """
        :param str name: Database to be created on new instance. Changing this creates a
               new instance.
        :param str charset: Database character set. Changing this creates a
               new instance.
        :param str collate: Database collation. Changing this creates a new instance.
        """
        pulumi.set(__self__, "name", name)
        if charset is not None:
            pulumi.set(__self__, "charset", charset)
        if collate is not None:
            pulumi.set(__self__, "collate", collate)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Database to be created on new instance. Changing this creates a
        new instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def charset(self) -> Optional[str]:
        """
        Database character set. Changing this creates a
        new instance.
        """
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter
    def collate(self) -> Optional[str]:
        """
        Database collation. Changing this creates a new instance.
        """
        return pulumi.get(self, "collate")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceDatastore(dict):
    def __init__(__self__, *,
                 type: str,
                 version: str):
        """
        :param str type: Database engine type to be used in new instance. Changing this
               creates a new instance.
        :param str version: Version of database engine type to be used in new instance.
               Changing this creates a new instance.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Database engine type to be used in new instance. Changing this
        creates a new instance.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of database engine type to be used in new instance.
        Changing this creates a new instance.
        """
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceNetwork(dict):
    def __init__(__self__, *,
                 fixed_ip_v4: Optional[str] = None,
                 fixed_ip_v6: Optional[str] = None,
                 port: Optional[str] = None,
                 uuid: Optional[str] = None):
        """
        :param str fixed_ip_v4: Specifies a fixed IPv4 address to be used on this
               network. Changing this creates a new instance.
        :param str fixed_ip_v6: Specifies a fixed IPv6 address to be used on this
               network. Changing this creates a new instance.
        :param str port: The port UUID of a
               network to attach to the instance. Changing this creates a new instance.
        :param str uuid: The network UUID to
               attach to the instance. Changing this creates a new instance.
        """
        if fixed_ip_v4 is not None:
            pulumi.set(__self__, "fixed_ip_v4", fixed_ip_v4)
        if fixed_ip_v6 is not None:
            pulumi.set(__self__, "fixed_ip_v6", fixed_ip_v6)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="fixedIpV4")
    def fixed_ip_v4(self) -> Optional[str]:
        """
        Specifies a fixed IPv4 address to be used on this
        network. Changing this creates a new instance.
        """
        return pulumi.get(self, "fixed_ip_v4")

    @property
    @pulumi.getter(name="fixedIpV6")
    def fixed_ip_v6(self) -> Optional[str]:
        """
        Specifies a fixed IPv6 address to be used on this
        network. Changing this creates a new instance.
        """
        return pulumi.get(self, "fixed_ip_v6")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        The port UUID of a
        network to attach to the instance. Changing this creates a new instance.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        The network UUID to
        attach to the instance. Changing this creates a new instance.
        """
        return pulumi.get(self, "uuid")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceUser(dict):
    def __init__(__self__, *,
                 name: str,
                 databases: Optional[Sequence[str]] = None,
                 host: Optional[str] = None,
                 password: Optional[str] = None):
        """
        :param str name: Database to be created on new instance. Changing this creates a
               new instance.
        :param Sequence[str] databases: A list of databases that user will have access to. If not specified, 
               user has access to all databases on th einstance. Changing this creates a new instance.
        :param str host: An ip address or % sign indicating what ip addresses can connect with
               this user credentials. Changing this creates a new instance.
        :param str password: User's password. Changing this creates a
               new instance.
        """
        pulumi.set(__self__, "name", name)
        if databases is not None:
            pulumi.set(__self__, "databases", databases)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Database to be created on new instance. Changing this creates a
        new instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def databases(self) -> Optional[Sequence[str]]:
        """
        A list of databases that user will have access to. If not specified, 
        user has access to all databases on th einstance. Changing this creates a new instance.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def host(self) -> Optional[str]:
        """
        An ip address or % sign indicating what ip addresses can connect with
        this user credentials. Changing this creates a new instance.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        User's password. Changing this creates a
        new instance.
        """
        return pulumi.get(self, "password")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


