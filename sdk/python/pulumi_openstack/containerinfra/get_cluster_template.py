# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetClusterTemplateResult(object):
    """
    A collection of values returned by getClusterTemplate.
    """
    def __init__(__self__, apiserver_port=None, cluster_distro=None, coe=None, created_at=None, dns_nameserver=None, docker_storage_driver=None, docker_volume_size=None, external_network_id=None, fixed_network=None, fixed_subnet=None, flavor=None, floating_ip_enabled=None, http_proxy=None, https_proxy=None, image=None, insecure_registry=None, keypair_id=None, labels=None, master_flavor=None, master_lb_enabled=None, network_driver=None, no_proxy=None, project_id=None, public=None, region=None, registry_enabled=None, server_type=None, tls_disabled=None, updated_at=None, user_id=None, volume_driver=None, id=None):
        if apiserver_port and not isinstance(apiserver_port, int):
            raise TypeError('Expected argument apiserver_port to be a int')
        __self__.apiserver_port = apiserver_port
        """
        The API server port for the Container Orchestration
        Engine for this cluster template.
        """
        if cluster_distro and not isinstance(cluster_distro, str):
            raise TypeError('Expected argument cluster_distro to be a str')
        __self__.cluster_distro = cluster_distro
        """
        The distro for the cluster (fedora-atomic, coreos, etc.).
        """
        if coe and not isinstance(coe, str):
            raise TypeError('Expected argument coe to be a str')
        __self__.coe = coe
        """
        The Container Orchestration Engine for this cluster template.
        """
        if created_at and not isinstance(created_at, str):
            raise TypeError('Expected argument created_at to be a str')
        __self__.created_at = created_at
        """
        The time at which cluster template was created.
        """
        if dns_nameserver and not isinstance(dns_nameserver, str):
            raise TypeError('Expected argument dns_nameserver to be a str')
        __self__.dns_nameserver = dns_nameserver
        """
        Address of the DNS nameserver that is used in nodes of the
        cluster.
        """
        if docker_storage_driver and not isinstance(docker_storage_driver, str):
            raise TypeError('Expected argument docker_storage_driver to be a str')
        __self__.docker_storage_driver = docker_storage_driver
        """
        Docker storage driver. Changing this updates the
        Docker storage driver of the existing cluster template.
        """
        if docker_volume_size and not isinstance(docker_volume_size, int):
            raise TypeError('Expected argument docker_volume_size to be a int')
        __self__.docker_volume_size = docker_volume_size
        """
        The size (in GB) of the Docker volume.
        """
        if external_network_id and not isinstance(external_network_id, str):
            raise TypeError('Expected argument external_network_id to be a str')
        __self__.external_network_id = external_network_id
        """
        The ID of the external network that will be used for
        the cluster.
        """
        if fixed_network and not isinstance(fixed_network, str):
            raise TypeError('Expected argument fixed_network to be a str')
        __self__.fixed_network = fixed_network
        """
        The fixed network that will be attached to the cluster.
        """
        if fixed_subnet and not isinstance(fixed_subnet, str):
            raise TypeError('Expected argument fixed_subnet to be a str')
        __self__.fixed_subnet = fixed_subnet
        """
        =The fixed subnet that will be attached to the cluster.
        """
        if flavor and not isinstance(flavor, str):
            raise TypeError('Expected argument flavor to be a str')
        __self__.flavor = flavor
        """
        The flavor for the nodes of the cluster.
        """
        if floating_ip_enabled and not isinstance(floating_ip_enabled, bool):
            raise TypeError('Expected argument floating_ip_enabled to be a bool')
        __self__.floating_ip_enabled = floating_ip_enabled
        """
        Indicates whether created cluster should create IP
        floating IP for every node or not.
        """
        if http_proxy and not isinstance(http_proxy, str):
            raise TypeError('Expected argument http_proxy to be a str')
        __self__.http_proxy = http_proxy
        """
        The address of a proxy for receiving all HTTP requests and
        relay them.
        """
        if https_proxy and not isinstance(https_proxy, str):
            raise TypeError('Expected argument https_proxy to be a str')
        __self__.https_proxy = https_proxy
        """
        The address of a proxy for receiving all HTTPS requests and
        relay them.
        """
        if image and not isinstance(image, str):
            raise TypeError('Expected argument image to be a str')
        __self__.image = image
        """
        The reference to an image that is used for nodes of the cluster.
        """
        if insecure_registry and not isinstance(insecure_registry, str):
            raise TypeError('Expected argument insecure_registry to be a str')
        __self__.insecure_registry = insecure_registry
        """
        The insecure registry URL for the cluster template.
        """
        if keypair_id and not isinstance(keypair_id, str):
            raise TypeError('Expected argument keypair_id to be a str')
        __self__.keypair_id = keypair_id
        """
        The name of the Compute service SSH keypair.
        """
        if labels and not isinstance(labels, dict):
            raise TypeError('Expected argument labels to be a dict')
        __self__.labels = labels
        """
        The list of key value pairs representing additional properties
        of the cluster template.
        """
        if master_flavor and not isinstance(master_flavor, str):
            raise TypeError('Expected argument master_flavor to be a str')
        __self__.master_flavor = master_flavor
        """
        The flavor for the master nodes.
        """
        if master_lb_enabled and not isinstance(master_lb_enabled, bool):
            raise TypeError('Expected argument master_lb_enabled to be a bool')
        __self__.master_lb_enabled = master_lb_enabled
        """
        Indicates whether created cluster should has a
        loadbalancer for master nodes or not.
        """
        if network_driver and not isinstance(network_driver, str):
            raise TypeError('Expected argument network_driver to be a str')
        __self__.network_driver = network_driver
        """
        The name of the driver for the container network.
        """
        if no_proxy and not isinstance(no_proxy, str):
            raise TypeError('Expected argument no_proxy to be a str')
        __self__.no_proxy = no_proxy
        """
        A comma-separated list of IP addresses that shouldn't be used in
        the cluster.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError('Expected argument project_id to be a str')
        __self__.project_id = project_id
        """
        The project of the cluster template.
        """
        if public and not isinstance(public, bool):
            raise TypeError('Expected argument public to be a bool')
        __self__.public = public
        """
        Indicates whether cluster template should be public.
        """
        if region and not isinstance(region, str):
            raise TypeError('Expected argument region to be a str')
        __self__.region = region
        """
        See Argument Reference above.
        """
        if registry_enabled and not isinstance(registry_enabled, bool):
            raise TypeError('Expected argument registry_enabled to be a bool')
        __self__.registry_enabled = registry_enabled
        """
        Indicates whether Docker registry is enabled in the
        cluster.
        """
        if server_type and not isinstance(server_type, str):
            raise TypeError('Expected argument server_type to be a str')
        __self__.server_type = server_type
        """
        The server type for the cluster template.
        """
        if tls_disabled and not isinstance(tls_disabled, bool):
            raise TypeError('Expected argument tls_disabled to be a bool')
        __self__.tls_disabled = tls_disabled
        """
        Indicates whether the TLS should be disabled in the cluster.
        """
        if updated_at and not isinstance(updated_at, str):
            raise TypeError('Expected argument updated_at to be a str')
        __self__.updated_at = updated_at
        """
        The time at which cluster template was updated.
        """
        if user_id and not isinstance(user_id, str):
            raise TypeError('Expected argument user_id to be a str')
        __self__.user_id = user_id
        """
        The user of the cluster template.
        """
        if volume_driver and not isinstance(volume_driver, str):
            raise TypeError('Expected argument volume_driver to be a str')
        __self__.volume_driver = volume_driver
        """
        The name of the driver that is used for the volumes of the
        cluster nodes.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_cluster_template(name=None, region=None):
    """
    Use this data source to get the ID of an available OpenStack Magnum cluster
    template.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['region'] = region
    __ret__ = await pulumi.runtime.invoke('openstack:containerinfra/getClusterTemplate:getClusterTemplate', __args__)

    return GetClusterTemplateResult(
        apiserver_port=__ret__.get('apiserverPort'),
        cluster_distro=__ret__.get('clusterDistro'),
        coe=__ret__.get('coe'),
        created_at=__ret__.get('createdAt'),
        dns_nameserver=__ret__.get('dnsNameserver'),
        docker_storage_driver=__ret__.get('dockerStorageDriver'),
        docker_volume_size=__ret__.get('dockerVolumeSize'),
        external_network_id=__ret__.get('externalNetworkId'),
        fixed_network=__ret__.get('fixedNetwork'),
        fixed_subnet=__ret__.get('fixedSubnet'),
        flavor=__ret__.get('flavor'),
        floating_ip_enabled=__ret__.get('floatingIpEnabled'),
        http_proxy=__ret__.get('httpProxy'),
        https_proxy=__ret__.get('httpsProxy'),
        image=__ret__.get('image'),
        insecure_registry=__ret__.get('insecureRegistry'),
        keypair_id=__ret__.get('keypairId'),
        labels=__ret__.get('labels'),
        master_flavor=__ret__.get('masterFlavor'),
        master_lb_enabled=__ret__.get('masterLbEnabled'),
        network_driver=__ret__.get('networkDriver'),
        no_proxy=__ret__.get('noProxy'),
        project_id=__ret__.get('projectId'),
        public=__ret__.get('public'),
        region=__ret__.get('region'),
        registry_enabled=__ret__.get('registryEnabled'),
        server_type=__ret__.get('serverType'),
        tls_disabled=__ret__.get('tlsDisabled'),
        updated_at=__ret__.get('updatedAt'),
        user_id=__ret__.get('userId'),
        volume_driver=__ret__.get('volumeDriver'),
        id=__ret__.get('id'))
