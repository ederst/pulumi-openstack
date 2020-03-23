# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

_SNAKE_TO_CAMEL_CASE_TABLE = {
    "access_ip_v4": "accessIpV4",
    "access_ip_v6": "accessIpV6",
    "access_key": "accessKey",
    "access_level": "accessLevel",
    "access_rules": "accessRules",
    "access_to": "accessTo",
    "access_type": "accessType",
    "address_scope_id": "addressScopeId",
    "admin_pass": "adminPass",
    "admin_state_up": "adminStateUp",
    "all_fixed_ips": "allFixedIps",
    "all_metadata": "allMetadata",
    "all_security_group_ids": "allSecurityGroupIds",
    "all_tags": "allTags",
    "allocation_pools": "allocationPools",
    "allocation_pools_collection": "allocationPoolsCollection",
    "allow_reauth": "allowReauth",
    "allowed_address_pairs": "allowedAddressPairs",
    "api_address": "apiAddress",
    "apiserver_port": "apiserverPort",
    "application_credential_id": "applicationCredentialId",
    "application_credential_name": "applicationCredentialName",
    "application_credential_secret": "applicationCredentialSecret",
    "associated_routers": "associatedRouters",
    "attach_mode": "attachMode",
    "auth_algorithm": "authAlgorithm",
    "auth_url": "authUrl",
    "availability_zone": "availabilityZone",
    "availability_zone_hints": "availabilityZoneHints",
    "backup_gigabytes": "backupGigabytes",
    "bit_length": "bitLength",
    "block_devices": "blockDevices",
    "cacert_file": "cacertFile",
    "cluster_distro": "clusterDistro",
    "cluster_template_id": "clusterTemplateId",
    "coe_version": "coeVersion",
    "compare_type": "compareType",
    "config_drive": "configDrive",
    "configuration_id": "configurationId",
    "conn_limit": "connLimit",
    "connection_limit": "connectionLimit",
    "consistency_group_id": "consistencyGroupId",
    "container_format": "containerFormat",
    "container_name": "containerName",
    "container_read": "containerRead",
    "container_ref": "containerRef",
    "container_sync_key": "containerSyncKey",
    "container_sync_to": "containerSyncTo",
    "container_version": "containerVersion",
    "container_write": "containerWrite",
    "content_disposition": "contentDisposition",
    "content_encoding": "contentEncoding",
    "content_length": "contentLength",
    "content_type": "contentType",
    "content_types": "contentTypes",
    "copy_from": "copyFrom",
    "create_timeout": "createTimeout",
    "created_at": "createdAt",
    "creation_time": "creationTime",
    "creator_id": "creatorId",
    "default_domain": "defaultDomain",
    "default_pool_id": "defaultPoolId",
    "default_prefixlen": "defaultPrefixlen",
    "default_project_id": "defaultProjectId",
    "default_quota": "defaultQuota",
    "default_tls_container_ref": "defaultTlsContainerRef",
    "delayed_auth": "delayedAuth",
    "delete_after": "deleteAfter",
    "delete_at": "deleteAt",
    "delete_default_rules": "deleteDefaultRules",
    "destination_cidr": "destinationCidr",
    "destination_ip_address": "destinationIpAddress",
    "destination_port": "destinationPort",
    "detect_content_type": "detectContentType",
    "device_id": "deviceId",
    "device_owner": "deviceOwner",
    "disable_no_cache_header": "disableNoCacheHeader",
    "disable_rollback": "disableRollback",
    "discovery_url": "discoveryUrl",
    "disk_format": "diskFormat",
    "dns_assignments": "dnsAssignments",
    "dns_domain": "dnsDomain",
    "dns_ip": "dnsIp",
    "dns_name": "dnsName",
    "dns_nameserver": "dnsNameserver",
    "dns_nameservers": "dnsNameservers",
    "docker_storage_driver": "dockerStorageDriver",
    "docker_volume_size": "dockerVolumeSize",
    "domain_id": "domainId",
    "domain_name": "domainName",
    "driver_volume_type": "driverVolumeType",
    "dscp_mark": "dscpMark",
    "enable_dhcp": "enableDhcp",
    "enable_online_resize": "enableOnlineResize",
    "enable_snat": "enableSnat",
    "encapsulation_mode": "encapsulationMode",
    "encryption_algorithm": "encryptionAlgorithm",
    "endpoint_overrides": "endpointOverrides",
    "endpoint_region": "endpointRegion",
    "endpoint_type": "endpointType",
    "environment_opts": "environmentOpts",
    "expected_codes": "expectedCodes",
    "expires_at": "expiresAt",
    "export_locations": "exportLocations",
    "external_fixed_ips": "externalFixedIps",
    "external_gateway": "externalGateway",
    "external_network_id": "externalNetworkId",
    "external_v4_ip": "externalV4Ip",
    "external_v6_ip": "externalV6Ip",
    "extra_dhcp_options": "extraDhcpOptions",
    "extra_specs": "extraSpecs",
    "fixed_ip": "fixedIp",
    "fixed_ips": "fixedIps",
    "fixed_network": "fixedNetwork",
    "fixed_subnet": "fixedSubnet",
    "flavor_id": "flavorId",
    "flavor_name": "flavorName",
    "floating_ip": "floatingIp",
    "floating_ip_enabled": "floatingIpEnabled",
    "floating_ips": "floatingIps",
    "force_delete": "forceDelete",
    "force_destroy": "forceDestroy",
    "gateway_ip": "gatewayIp",
    "group_id": "groupId",
    "has_replicas": "hasReplicas",
    "host_name": "hostName",
    "host_routes": "hostRoutes",
    "http_method": "httpMethod",
    "http_proxy": "httpProxy",
    "https_proxy": "httpsProxy",
    "ignore_change_password_upon_first_use": "ignoreChangePasswordUponFirstUse",
    "ignore_lockout_failure_attempts": "ignoreLockoutFailureAttempts",
    "ignore_password_expiry": "ignorePasswordExpiry",
    "ike_version": "ikeVersion",
    "ikepolicy_id": "ikepolicyId",
    "image_cache_path": "imageCachePath",
    "image_id": "imageId",
    "image_name": "imageName",
    "image_source_url": "imageSourceUrl",
    "injected_file_content_bytes": "injectedFileContentBytes",
    "injected_file_path_bytes": "injectedFilePathBytes",
    "injected_files": "injectedFiles",
    "insecure_registry": "insecureRegistry",
    "insert_headers": "insertHeaders",
    "instance_id": "instanceId",
    "ip_address": "ipAddress",
    "ip_version": "ipVersion",
    "ipsecpolicy_id": "ipsecpolicyId",
    "ipv6_address_mode": "ipv6AddressMode",
    "ipv6_ra_mode": "ipv6RaMode",
    "is_default": "isDefault",
    "is_domain": "isDomain",
    "is_public": "isPublic",
    "key_pair": "keyPair",
    "key_pairs": "keyPairs",
    "keypair_id": "keypairId",
    "l7policy_id": "l7policyId",
    "last_modified": "lastModified",
    "lb_method": "lbMethod",
    "lb_provider": "lbProvider",
    "listener_id": "listenerId",
    "loadbalancer_id": "loadbalancerId",
    "loadbalancer_provider": "loadbalancerProvider",
    "local_ep_group_id": "localEpGroupId",
    "local_file_path": "localFilePath",
    "local_id": "localId",
    "mac_address": "macAddress",
    "master_addresses": "masterAddresses",
    "master_count": "masterCount",
    "master_flavor": "masterFlavor",
    "master_lb_enabled": "masterLbEnabled",
    "max_burst_kbps": "maxBurstKbps",
    "max_kbps": "maxKbps",
    "max_prefixlen": "maxPrefixlen",
    "max_retries": "maxRetries",
    "max_retries_down": "maxRetriesDown",
    "member_id": "memberId",
    "metadata_items": "metadataItems",
    "min_disk_gb": "minDiskGb",
    "min_kbps": "minKbps",
    "min_prefixlen": "minPrefixlen",
    "min_ram_mb": "minRamMb",
    "monitor_ids": "monitorIds",
    "mount_point_base": "mountPointBase",
    "multi_factor_auth_enabled": "multiFactorAuthEnabled",
    "multi_factor_auth_rules": "multiFactorAuthRules",
    "network_driver": "networkDriver",
    "network_id": "networkId",
    "network_type": "networkType",
    "neutron_net_id": "neutronNetId",
    "neutron_subnet_id": "neutronSubnetId",
    "next_hop": "nextHop",
    "no_fixed_ip": "noFixedIp",
    "no_gateway": "noGateway",
    "no_proxy": "noProxy",
    "no_routers": "noRouters",
    "no_security_groups": "noSecurityGroups",
    "node_addresses": "nodeAddresses",
    "node_count": "nodeCount",
    "notification_topics": "notificationTopics",
    "object_id": "objectId",
    "object_manifest": "objectManifest",
    "object_type": "objectType",
    "os_type": "osType",
    "parent_id": "parentId",
    "payload_content_encoding": "payloadContentEncoding",
    "payload_content_type": "payloadContentType",
    "peer_address": "peerAddress",
    "peer_cidrs": "peerCidrs",
    "peer_ep_group_id": "peerEpGroupId",
    "peer_id": "peerId",
    "per_volume_gigabytes": "perVolumeGigabytes",
    "phase1_negotiation_mode": "phase1NegotiationMode",
    "policy_id": "policyId",
    "pool_id": "poolId",
    "port_id": "portId",
    "port_range_max": "portRangeMax",
    "port_range_min": "portRangeMin",
    "port_security_enabled": "portSecurityEnabled",
    "power_state": "powerState",
    "prefix_length": "prefixLength",
    "private_key": "privateKey",
    "project_domain_id": "projectDomainId",
    "project_domain_name": "projectDomainName",
    "project_id": "projectId",
    "protocol_port": "protocolPort",
    "public_key": "publicKey",
    "qos_policy_id": "qosPolicyId",
    "rbac_policy": "rbacPolicy",
    "redirect_pool_id": "redirectPoolId",
    "redirect_url": "redirectUrl",
    "registry_enabled": "registryEnabled",
    "remote_group_id": "remoteGroupId",
    "remote_ip_prefix": "remoteIpPrefix",
    "replication_type": "replicationType",
    "revision_number": "revisionNumber",
    "role_id": "roleId",
    "router_id": "routerId",
    "rx_tx_factor": "rxTxFactor",
    "scheduler_hints": "schedulerHints",
    "secret_ref": "secretRef",
    "secret_refs": "secretRefs",
    "secret_type": "secretType",
    "security_group": "securityGroup",
    "security_group_id": "securityGroupId",
    "security_group_ids": "securityGroupIds",
    "security_group_rule": "securityGroupRule",
    "security_group_rules": "securityGroupRules",
    "security_groups": "securityGroups",
    "security_service_ids": "securityServiceIds",
    "segmentation_id": "segmentationId",
    "server_group_members": "serverGroupMembers",
    "server_groups": "serverGroups",
    "server_type": "serverType",
    "service_id": "serviceId",
    "service_name": "serviceName",
    "service_type": "serviceType",
    "share_id": "shareId",
    "share_network_id": "shareNetworkId",
    "share_proto": "shareProto",
    "share_server_id": "shareServerId",
    "share_type": "shareType",
    "size_bytes": "sizeBytes",
    "snapshot_id": "snapshotId",
    "sni_container_refs": "sniContainerRefs",
    "source_ip_address": "sourceIpAddress",
    "source_port": "sourcePort",
    "source_replica": "sourceReplica",
    "source_vol_id": "sourceVolId",
    "stack_id": "stackId",
    "status_reason": "statusReason",
    "stop_before_destroy": "stopBeforeDestroy",
    "sub_ports": "subPorts",
    "subnet_id": "subnetId",
    "subnetpool_id": "subnetpoolId",
    "target_tenant": "targetTenant",
    "template_description": "templateDescription",
    "template_opts": "templateOpts",
    "tenant_id": "tenantId",
    "tenant_name": "tenantName",
    "timeout_client_data": "timeoutClientData",
    "timeout_member_connect": "timeoutMemberConnect",
    "timeout_member_data": "timeoutMemberData",
    "timeout_tcp_inspect": "timeoutTcpInspect",
    "tls_disabled": "tlsDisabled",
    "trans_id": "transId",
    "transform_protocol": "transformProtocol",
    "transparent_vlan": "transparentVlan",
    "update_at": "updateAt",
    "updated_at": "updatedAt",
    "updated_time": "updatedTime",
    "url_path": "urlPath",
    "use_octavia": "useOctavia",
    "user_data": "userData",
    "user_domain_id": "userDomainId",
    "user_domain_name": "userDomainName",
    "user_id": "userId",
    "user_name": "userName",
    "value_specs": "valueSpecs",
    "vendor_options": "vendorOptions",
    "verify_checksum": "verifyChecksum",
    "vip_address": "vipAddress",
    "vip_port_id": "vipPortId",
    "vip_subnet_id": "vipSubnetId",
    "volume_driver": "volumeDriver",
    "volume_id": "volumeId",
    "volume_type": "volumeType",
    "vpnservice_id": "vpnserviceId",
    "wait_until_associated": "waitUntilAssociated",
    "zone_id": "zoneId",
}

_CAMEL_TO_SNAKE_CASE_TABLE = {
    "accessIpV4": "access_ip_v4",
    "accessIpV6": "access_ip_v6",
    "accessKey": "access_key",
    "accessLevel": "access_level",
    "accessRules": "access_rules",
    "accessTo": "access_to",
    "accessType": "access_type",
    "addressScopeId": "address_scope_id",
    "adminPass": "admin_pass",
    "adminStateUp": "admin_state_up",
    "allFixedIps": "all_fixed_ips",
    "allMetadata": "all_metadata",
    "allSecurityGroupIds": "all_security_group_ids",
    "allTags": "all_tags",
    "allocationPools": "allocation_pools",
    "allocationPoolsCollection": "allocation_pools_collection",
    "allowReauth": "allow_reauth",
    "allowedAddressPairs": "allowed_address_pairs",
    "apiAddress": "api_address",
    "apiserverPort": "apiserver_port",
    "applicationCredentialId": "application_credential_id",
    "applicationCredentialName": "application_credential_name",
    "applicationCredentialSecret": "application_credential_secret",
    "associatedRouters": "associated_routers",
    "attachMode": "attach_mode",
    "authAlgorithm": "auth_algorithm",
    "authUrl": "auth_url",
    "availabilityZone": "availability_zone",
    "availabilityZoneHints": "availability_zone_hints",
    "backupGigabytes": "backup_gigabytes",
    "bitLength": "bit_length",
    "blockDevices": "block_devices",
    "cacertFile": "cacert_file",
    "clusterDistro": "cluster_distro",
    "clusterTemplateId": "cluster_template_id",
    "coeVersion": "coe_version",
    "compareType": "compare_type",
    "configDrive": "config_drive",
    "configurationId": "configuration_id",
    "connLimit": "conn_limit",
    "connectionLimit": "connection_limit",
    "consistencyGroupId": "consistency_group_id",
    "containerFormat": "container_format",
    "containerName": "container_name",
    "containerRead": "container_read",
    "containerRef": "container_ref",
    "containerSyncKey": "container_sync_key",
    "containerSyncTo": "container_sync_to",
    "containerVersion": "container_version",
    "containerWrite": "container_write",
    "contentDisposition": "content_disposition",
    "contentEncoding": "content_encoding",
    "contentLength": "content_length",
    "contentType": "content_type",
    "contentTypes": "content_types",
    "copyFrom": "copy_from",
    "createTimeout": "create_timeout",
    "createdAt": "created_at",
    "creationTime": "creation_time",
    "creatorId": "creator_id",
    "defaultDomain": "default_domain",
    "defaultPoolId": "default_pool_id",
    "defaultPrefixlen": "default_prefixlen",
    "defaultProjectId": "default_project_id",
    "defaultQuota": "default_quota",
    "defaultTlsContainerRef": "default_tls_container_ref",
    "delayedAuth": "delayed_auth",
    "deleteAfter": "delete_after",
    "deleteAt": "delete_at",
    "deleteDefaultRules": "delete_default_rules",
    "destinationCidr": "destination_cidr",
    "destinationIpAddress": "destination_ip_address",
    "destinationPort": "destination_port",
    "detectContentType": "detect_content_type",
    "deviceId": "device_id",
    "deviceOwner": "device_owner",
    "disableNoCacheHeader": "disable_no_cache_header",
    "disableRollback": "disable_rollback",
    "discoveryUrl": "discovery_url",
    "diskFormat": "disk_format",
    "dnsAssignments": "dns_assignments",
    "dnsDomain": "dns_domain",
    "dnsIp": "dns_ip",
    "dnsName": "dns_name",
    "dnsNameserver": "dns_nameserver",
    "dnsNameservers": "dns_nameservers",
    "dockerStorageDriver": "docker_storage_driver",
    "dockerVolumeSize": "docker_volume_size",
    "domainId": "domain_id",
    "domainName": "domain_name",
    "driverVolumeType": "driver_volume_type",
    "dscpMark": "dscp_mark",
    "enableDhcp": "enable_dhcp",
    "enableOnlineResize": "enable_online_resize",
    "enableSnat": "enable_snat",
    "encapsulationMode": "encapsulation_mode",
    "encryptionAlgorithm": "encryption_algorithm",
    "endpointOverrides": "endpoint_overrides",
    "endpointRegion": "endpoint_region",
    "endpointType": "endpoint_type",
    "environmentOpts": "environment_opts",
    "expectedCodes": "expected_codes",
    "expiresAt": "expires_at",
    "exportLocations": "export_locations",
    "externalFixedIps": "external_fixed_ips",
    "externalGateway": "external_gateway",
    "externalNetworkId": "external_network_id",
    "externalV4Ip": "external_v4_ip",
    "externalV6Ip": "external_v6_ip",
    "extraDhcpOptions": "extra_dhcp_options",
    "extraSpecs": "extra_specs",
    "fixedIp": "fixed_ip",
    "fixedIps": "fixed_ips",
    "fixedNetwork": "fixed_network",
    "fixedSubnet": "fixed_subnet",
    "flavorId": "flavor_id",
    "flavorName": "flavor_name",
    "floatingIp": "floating_ip",
    "floatingIpEnabled": "floating_ip_enabled",
    "floatingIps": "floating_ips",
    "forceDelete": "force_delete",
    "forceDestroy": "force_destroy",
    "gatewayIp": "gateway_ip",
    "groupId": "group_id",
    "hasReplicas": "has_replicas",
    "hostName": "host_name",
    "hostRoutes": "host_routes",
    "httpMethod": "http_method",
    "httpProxy": "http_proxy",
    "httpsProxy": "https_proxy",
    "ignoreChangePasswordUponFirstUse": "ignore_change_password_upon_first_use",
    "ignoreLockoutFailureAttempts": "ignore_lockout_failure_attempts",
    "ignorePasswordExpiry": "ignore_password_expiry",
    "ikeVersion": "ike_version",
    "ikepolicyId": "ikepolicy_id",
    "imageCachePath": "image_cache_path",
    "imageId": "image_id",
    "imageName": "image_name",
    "imageSourceUrl": "image_source_url",
    "injectedFileContentBytes": "injected_file_content_bytes",
    "injectedFilePathBytes": "injected_file_path_bytes",
    "injectedFiles": "injected_files",
    "insecureRegistry": "insecure_registry",
    "insertHeaders": "insert_headers",
    "instanceId": "instance_id",
    "ipAddress": "ip_address",
    "ipVersion": "ip_version",
    "ipsecpolicyId": "ipsecpolicy_id",
    "ipv6AddressMode": "ipv6_address_mode",
    "ipv6RaMode": "ipv6_ra_mode",
    "isDefault": "is_default",
    "isDomain": "is_domain",
    "isPublic": "is_public",
    "keyPair": "key_pair",
    "keyPairs": "key_pairs",
    "keypairId": "keypair_id",
    "l7policyId": "l7policy_id",
    "lastModified": "last_modified",
    "lbMethod": "lb_method",
    "lbProvider": "lb_provider",
    "listenerId": "listener_id",
    "loadbalancerId": "loadbalancer_id",
    "loadbalancerProvider": "loadbalancer_provider",
    "localEpGroupId": "local_ep_group_id",
    "localFilePath": "local_file_path",
    "localId": "local_id",
    "macAddress": "mac_address",
    "masterAddresses": "master_addresses",
    "masterCount": "master_count",
    "masterFlavor": "master_flavor",
    "masterLbEnabled": "master_lb_enabled",
    "maxBurstKbps": "max_burst_kbps",
    "maxKbps": "max_kbps",
    "maxPrefixlen": "max_prefixlen",
    "maxRetries": "max_retries",
    "maxRetriesDown": "max_retries_down",
    "memberId": "member_id",
    "metadataItems": "metadata_items",
    "minDiskGb": "min_disk_gb",
    "minKbps": "min_kbps",
    "minPrefixlen": "min_prefixlen",
    "minRamMb": "min_ram_mb",
    "monitorIds": "monitor_ids",
    "mountPointBase": "mount_point_base",
    "multiFactorAuthEnabled": "multi_factor_auth_enabled",
    "multiFactorAuthRules": "multi_factor_auth_rules",
    "networkDriver": "network_driver",
    "networkId": "network_id",
    "networkType": "network_type",
    "neutronNetId": "neutron_net_id",
    "neutronSubnetId": "neutron_subnet_id",
    "nextHop": "next_hop",
    "noFixedIp": "no_fixed_ip",
    "noGateway": "no_gateway",
    "noProxy": "no_proxy",
    "noRouters": "no_routers",
    "noSecurityGroups": "no_security_groups",
    "nodeAddresses": "node_addresses",
    "nodeCount": "node_count",
    "notificationTopics": "notification_topics",
    "objectId": "object_id",
    "objectManifest": "object_manifest",
    "objectType": "object_type",
    "osType": "os_type",
    "parentId": "parent_id",
    "payloadContentEncoding": "payload_content_encoding",
    "payloadContentType": "payload_content_type",
    "peerAddress": "peer_address",
    "peerCidrs": "peer_cidrs",
    "peerEpGroupId": "peer_ep_group_id",
    "peerId": "peer_id",
    "perVolumeGigabytes": "per_volume_gigabytes",
    "phase1NegotiationMode": "phase1_negotiation_mode",
    "policyId": "policy_id",
    "poolId": "pool_id",
    "portId": "port_id",
    "portRangeMax": "port_range_max",
    "portRangeMin": "port_range_min",
    "portSecurityEnabled": "port_security_enabled",
    "powerState": "power_state",
    "prefixLength": "prefix_length",
    "privateKey": "private_key",
    "projectDomainId": "project_domain_id",
    "projectDomainName": "project_domain_name",
    "projectId": "project_id",
    "protocolPort": "protocol_port",
    "publicKey": "public_key",
    "qosPolicyId": "qos_policy_id",
    "rbacPolicy": "rbac_policy",
    "redirectPoolId": "redirect_pool_id",
    "redirectUrl": "redirect_url",
    "registryEnabled": "registry_enabled",
    "remoteGroupId": "remote_group_id",
    "remoteIpPrefix": "remote_ip_prefix",
    "replicationType": "replication_type",
    "revisionNumber": "revision_number",
    "roleId": "role_id",
    "routerId": "router_id",
    "rxTxFactor": "rx_tx_factor",
    "schedulerHints": "scheduler_hints",
    "secretRef": "secret_ref",
    "secretRefs": "secret_refs",
    "secretType": "secret_type",
    "securityGroup": "security_group",
    "securityGroupId": "security_group_id",
    "securityGroupIds": "security_group_ids",
    "securityGroupRule": "security_group_rule",
    "securityGroupRules": "security_group_rules",
    "securityGroups": "security_groups",
    "securityServiceIds": "security_service_ids",
    "segmentationId": "segmentation_id",
    "serverGroupMembers": "server_group_members",
    "serverGroups": "server_groups",
    "serverType": "server_type",
    "serviceId": "service_id",
    "serviceName": "service_name",
    "serviceType": "service_type",
    "shareId": "share_id",
    "shareNetworkId": "share_network_id",
    "shareProto": "share_proto",
    "shareServerId": "share_server_id",
    "shareType": "share_type",
    "sizeBytes": "size_bytes",
    "snapshotId": "snapshot_id",
    "sniContainerRefs": "sni_container_refs",
    "sourceIpAddress": "source_ip_address",
    "sourcePort": "source_port",
    "sourceReplica": "source_replica",
    "sourceVolId": "source_vol_id",
    "stackId": "stack_id",
    "statusReason": "status_reason",
    "stopBeforeDestroy": "stop_before_destroy",
    "subPorts": "sub_ports",
    "subnetId": "subnet_id",
    "subnetpoolId": "subnetpool_id",
    "targetTenant": "target_tenant",
    "templateDescription": "template_description",
    "templateOpts": "template_opts",
    "tenantId": "tenant_id",
    "tenantName": "tenant_name",
    "timeoutClientData": "timeout_client_data",
    "timeoutMemberConnect": "timeout_member_connect",
    "timeoutMemberData": "timeout_member_data",
    "timeoutTcpInspect": "timeout_tcp_inspect",
    "tlsDisabled": "tls_disabled",
    "transId": "trans_id",
    "transformProtocol": "transform_protocol",
    "transparentVlan": "transparent_vlan",
    "updateAt": "update_at",
    "updatedAt": "updated_at",
    "updatedTime": "updated_time",
    "urlPath": "url_path",
    "useOctavia": "use_octavia",
    "userData": "user_data",
    "userDomainId": "user_domain_id",
    "userDomainName": "user_domain_name",
    "userId": "user_id",
    "userName": "user_name",
    "valueSpecs": "value_specs",
    "vendorOptions": "vendor_options",
    "verifyChecksum": "verify_checksum",
    "vipAddress": "vip_address",
    "vipPortId": "vip_port_id",
    "vipSubnetId": "vip_subnet_id",
    "volumeDriver": "volume_driver",
    "volumeId": "volume_id",
    "volumeType": "volume_type",
    "vpnserviceId": "vpnservice_id",
    "waitUntilAssociated": "wait_until_associated",
    "zoneId": "zone_id",
}
