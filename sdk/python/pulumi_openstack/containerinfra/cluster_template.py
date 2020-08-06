# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class ClusterTemplate(pulumi.CustomResource):
    apiserver_port: pulumi.Output[float]
    cluster_distro: pulumi.Output[str]
    coe: pulumi.Output[str]
    created_at: pulumi.Output[str]
    dns_nameserver: pulumi.Output[str]
    docker_storage_driver: pulumi.Output[str]
    docker_volume_size: pulumi.Output[float]
    external_network_id: pulumi.Output[str]
    fixed_network: pulumi.Output[str]
    fixed_subnet: pulumi.Output[str]
    flavor: pulumi.Output[str]
    floating_ip_enabled: pulumi.Output[bool]
    http_proxy: pulumi.Output[str]
    https_proxy: pulumi.Output[str]
    image: pulumi.Output[str]
    insecure_registry: pulumi.Output[str]
    keypair_id: pulumi.Output[str]
    labels: pulumi.Output[dict]
    master_flavor: pulumi.Output[str]
    master_lb_enabled: pulumi.Output[bool]
    name: pulumi.Output[str]
    network_driver: pulumi.Output[str]
    no_proxy: pulumi.Output[str]
    project_id: pulumi.Output[str]
    public: pulumi.Output[bool]
    region: pulumi.Output[str]
    registry_enabled: pulumi.Output[bool]
    server_type: pulumi.Output[str]
    tls_disabled: pulumi.Output[bool]
    updated_at: pulumi.Output[str]
    user_id: pulumi.Output[str]
    volume_driver: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, apiserver_port=None, cluster_distro=None, coe=None, dns_nameserver=None, docker_storage_driver=None, docker_volume_size=None, external_network_id=None, fixed_network=None, fixed_subnet=None, flavor=None, floating_ip_enabled=None, http_proxy=None, https_proxy=None, image=None, insecure_registry=None, keypair_id=None, labels=None, master_flavor=None, master_lb_enabled=None, name=None, network_driver=None, no_proxy=None, public=None, region=None, registry_enabled=None, server_type=None, tls_disabled=None, volume_driver=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V1 Magnum cluster template resource within OpenStack.

        ## Example Usage
        ### Create a Cluster template

        ```python
        import pulumi
        import pulumi_openstack as openstack

        clustertemplate1 = openstack.containerinfra.ClusterTemplate("clustertemplate1",
            coe="kubernetes",
            dns_nameserver="1.1.1.1",
            docker_storage_driver="devicemapper",
            docker_volume_size=10,
            flavor="m1.small",
            floating_ip_enabled=False,
            image="Fedora-Atomic-27",
            labels={
                "influx_grafana_dashboard_enabled": "true",
                "kube_dashboard_enabled": "true",
                "kube_tag": "1.11.1",
                "prometheus_monitoring": "true",
            },
            master_flavor="m1.medium",
            master_lb_enabled=True,
            network_driver="flannel",
            server_type="vm",
            volume_driver="cinder")
        ```
        ## Argument reference

        The following arguments are supported:

        * `region` - (Optional) The region in which to obtain the V1 Container Infra
          client. A Container Infra client is needed to create a cluster template. If
          omitted,the `region` argument of the provider is used. Changing this
          creates a new cluster template.

        * `name` - (Required) The name of the cluster template. Changing this updates
          the name of the existing cluster template.

        * `project_id` - (Optional) The project of the cluster template. Required if
          admin wants to create a cluster template in another project. Changing this
          creates a new cluster template.

        * `user_id` - (Optional) The user of the cluster template. Required if admin
          wants to create a cluster template for another user. Changing this creates
          a new cluster template.

        * `apiserver_port` - (Optional) The API server port for the Container
          Orchestration Engine for this cluster template. Changing this updates the
          API server port of the existing cluster template.

        * `coe` - (Required) The Container Orchestration Engine for this cluster
          template. Changing this updates the engine of the existing cluster
          template.

        * `cluster_distro` - (Optional) The distro for the cluster (fedora-atomic,
          coreos, etc.). Changing this updates the cluster distro of the existing
          cluster template.

        * `dns_nameserver` - (Optional) Address of the DNS nameserver that is used in
          nodes of the cluster. Changing this updates the DNS nameserver of the
          existing cluster template.

        * `docker_storage_driver` - (Optional) Docker storage driver. Changing this
          updates the Docker storage driver of the existing cluster template.

        * `docker_volume_size` - (Optional) The size (in GB) of the Docker volume.
          Changing this updates the Docker volume size of the existing cluster
          template.

        * `external_network_id` - (Optional) The ID of the external network that will
          be used for the cluster. Changing this updates the external network ID of
          the existing cluster template.

        * `fixed_network` - (Optional) The fixed network that will be attached to the
          cluster. Changing this updates the fixed network of the existing cluster
          template.

        * `fixed_subnet` - (Optional) The fixed subnet that will be attached to the
          cluster. Changing this updates the fixed subnet of the existing cluster
          template.

        * `flavor` - (Optional) The flavor for the nodes of the cluster. Can be set via
          the `OS_MAGNUM_FLAVOR` environment variable. Changing this updates the
          flavor of the existing cluster template.

        * `master_flavor` - (Optional) The flavor for the master nodes. Can be set via
          the `OS_MAGNUM_MASTER_FLAVOR` environment variable. Changing this updates
          the master flavor of the existing cluster template.

        * `floating_ip_enabled` - (Optional) Indicates whether created cluster should
          create floating IP for every node or not. Changing this updates the
          floating IP enabled attribute of the existing cluster template.

        * `http_proxy` - (Optional) The address of a proxy for receiving all HTTP
          requests and relay them. Changing this updates the HTTP proxy address of
          the existing cluster template.

        * `https_proxy` - (Optional) The address of a proxy for receiving all HTTPS
          requests and relay them. Changing this updates the HTTPS proxy address of
          the existing cluster template.

        * `image` - (Required) The reference to an image that is used for nodes of the
          cluster. Can be set via the `OS_MAGNUM_IMAGE` environment variable.
          Changing this updates the image attribute of the existing cluster template.

        * `insecure_registry` - (Optional) The insecure registry URL for the cluster
          template. Changing this updates the insecure registry attribute of the
          existing cluster template.

        * `keypair_id` - (Optional) The name of the Compute service SSH keypair.
          Changing this updates the keypair of the existing cluster template.

        * `labels` - (Optional) The list of key value pairs representing additional
          properties of the cluster template. Changing this updates the labels of the
          existing cluster template.

        * `master_lb_enabled` - (Optional) Indicates whether created cluster should
          has a loadbalancer for master nodes or not. Changing this updates the
          attribute of the existing cluster template.

        * `network_driver` - (Optional) The name of the driver for the container
          network. Changing this updates the network driver of the existing cluster
          template.

        * `no_proxy` - (Optional) A comma-separated list of IP addresses that shouldn't
          be used in the cluster. Changing this updates the no proxy list of the
          existing cluster template.

        * `public` - (Optional) Indicates whether cluster template should be public.
          Changing this updates the public attribute of the existing cluster
          template.

        * `registry_enabled` - (Optional) Indicates whether Docker registry is enabled
          in the cluster. Changing this updates the registry enabled attribute of the
          existing cluster template.

        * `server_type` - (Optional) The server type for the cluster template. Changing
          this updates the server type of the existing cluster template.

        * `tls_disabled` - (Optional) Indicates whether the TLS should be disabled in
          the cluster. Changing this updates the attribute of the existing cluster.

        * `volume_driver` - (Optional) The name of the driver that is used for the
          volumes of the cluster nodes. Changing this updates the volume driver of
          the existing cluster template.

        ## Attributes reference

        The following attributes are exported:

        * `region` - See Argument Reference above.
        * `name` - See Argument Reference above.
        * `project_id` - See Argument Reference above.
        * `created_at` - The time at which cluster template was created.
        * `updated_at` - The time at which cluster template was created.
        * `apiserver_port` - See Argument Reference above.
        * `coe` - See Argument Reference above.
        * `cluster_distro` - See Argument Reference above.
        * `dns_nameserver` - See Argument Reference above.
        * `docker_storage_driver` - See Argument Reference above.
        * `docker_volume_size` - See Argument Reference above.
        * `external_network_id` - See Argument Reference above.
        * `fixed_network` - See Argument Reference above.
        * `fixed_subnet` - See Argument Reference above.
        * `flavor` - See Argument Reference above.
        * `master_flavor` - See Argument Reference above.
        * `floating_ip_enabled` - See Argument Reference above.
        * `http_proxy` - See Argument Reference above.
        * `https_proxy` - See Argument Reference above.
        * `image` - See Argument Reference above.
        * `insecure_registry` - See Argument Reference above.
        * `keypair_id` - See Argument Reference above.
        * `labels` - See Argument Reference above.
        * `links` - A list containing associated cluster template links.
        * `master_lb_enabled` - See Argument Reference above.
        * `network_driver` - See Argument Reference above.
        * `no_proxy` - See Argument Reference above.
        * `public` - See Argument Reference above.
        * `registry_enabled` - See Argument Reference above.
        * `server_type` - See Argument Reference above.
        * `tls_disabled` - See Argument Reference above.
        * `volume_driver` - See Argument Reference above.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
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

            __props__['apiserver_port'] = apiserver_port
            __props__['cluster_distro'] = cluster_distro
            if coe is None:
                raise TypeError("Missing required property 'coe'")
            __props__['coe'] = coe
            __props__['dns_nameserver'] = dns_nameserver
            __props__['docker_storage_driver'] = docker_storage_driver
            __props__['docker_volume_size'] = docker_volume_size
            __props__['external_network_id'] = external_network_id
            __props__['fixed_network'] = fixed_network
            __props__['fixed_subnet'] = fixed_subnet
            __props__['flavor'] = flavor
            __props__['floating_ip_enabled'] = floating_ip_enabled
            __props__['http_proxy'] = http_proxy
            __props__['https_proxy'] = https_proxy
            if image is None:
                raise TypeError("Missing required property 'image'")
            __props__['image'] = image
            __props__['insecure_registry'] = insecure_registry
            __props__['keypair_id'] = keypair_id
            __props__['labels'] = labels
            __props__['master_flavor'] = master_flavor
            __props__['master_lb_enabled'] = master_lb_enabled
            __props__['name'] = name
            __props__['network_driver'] = network_driver
            __props__['no_proxy'] = no_proxy
            __props__['public'] = public
            __props__['region'] = region
            __props__['registry_enabled'] = registry_enabled
            __props__['server_type'] = server_type
            __props__['tls_disabled'] = tls_disabled
            __props__['volume_driver'] = volume_driver
            __props__['created_at'] = None
            __props__['project_id'] = None
            __props__['updated_at'] = None
            __props__['user_id'] = None
        super(ClusterTemplate, __self__).__init__(
            'openstack:containerinfra/clusterTemplate:ClusterTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, apiserver_port=None, cluster_distro=None, coe=None, created_at=None, dns_nameserver=None, docker_storage_driver=None, docker_volume_size=None, external_network_id=None, fixed_network=None, fixed_subnet=None, flavor=None, floating_ip_enabled=None, http_proxy=None, https_proxy=None, image=None, insecure_registry=None, keypair_id=None, labels=None, master_flavor=None, master_lb_enabled=None, name=None, network_driver=None, no_proxy=None, project_id=None, public=None, region=None, registry_enabled=None, server_type=None, tls_disabled=None, updated_at=None, user_id=None, volume_driver=None):
        """
        Get an existing ClusterTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["apiserver_port"] = apiserver_port
        __props__["cluster_distro"] = cluster_distro
        __props__["coe"] = coe
        __props__["created_at"] = created_at
        __props__["dns_nameserver"] = dns_nameserver
        __props__["docker_storage_driver"] = docker_storage_driver
        __props__["docker_volume_size"] = docker_volume_size
        __props__["external_network_id"] = external_network_id
        __props__["fixed_network"] = fixed_network
        __props__["fixed_subnet"] = fixed_subnet
        __props__["flavor"] = flavor
        __props__["floating_ip_enabled"] = floating_ip_enabled
        __props__["http_proxy"] = http_proxy
        __props__["https_proxy"] = https_proxy
        __props__["image"] = image
        __props__["insecure_registry"] = insecure_registry
        __props__["keypair_id"] = keypair_id
        __props__["labels"] = labels
        __props__["master_flavor"] = master_flavor
        __props__["master_lb_enabled"] = master_lb_enabled
        __props__["name"] = name
        __props__["network_driver"] = network_driver
        __props__["no_proxy"] = no_proxy
        __props__["project_id"] = project_id
        __props__["public"] = public
        __props__["region"] = region
        __props__["registry_enabled"] = registry_enabled
        __props__["server_type"] = server_type
        __props__["tls_disabled"] = tls_disabled
        __props__["updated_at"] = updated_at
        __props__["user_id"] = user_id
        __props__["volume_driver"] = volume_driver
        return ClusterTemplate(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
