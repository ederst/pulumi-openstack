// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V1 Magnum cluster template resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ### Create a Cluster template
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const clustertemplate1 = new openstack.containerinfra.ClusterTemplate("clustertemplate_1", {
 *     coe: "kubernetes",
 *     dnsNameserver: "1.1.1.1",
 *     dockerStorageDriver: "devicemapper",
 *     dockerVolumeSize: 10,
 *     flavor: "m1.small",
 *     floatingIpEnabled: false,
 *     image: "Fedora-Atomic-27",
 *     labels: {
 *         influx_grafana_dashboard_enabled: "true",
 *         kube_dashboard_enabled: "true",
 *         kube_tag: "1.11.1",
 *         prometheus_monitoring: "true",
 *     },
 *     masterFlavor: "m1.medium",
 *     masterLbEnabled: true,
 *     networkDriver: "flannel",
 *     serverType: "vm",
 *     volumeDriver: "cinder",
 * });
 * ```
 * 
 * ## Argument reference
 * 
 * The following arguments are supported:
 * 
 * * `region` - (Optional) The region in which to obtain the V1 Container Infra
 *     client. A Container Infra client is needed to create a cluster template. If
 *     omitted,the `region` argument of the provider is used. Changing this
 *     creates a new cluster template.
 * 
 * * `name` - (Required) The name of the cluster template. Changing this updates
 *     the name of the existing cluster template.
 * 
 * * `project_id` - (Optional) The project of the cluster template. Required if
 *     admin wants to create a cluster template in another project. Changing this
 *     creates a new cluster template.
 * 
 * * `user_id` - (Optional) The user of the cluster template. Required if admin
 *     wants to create a cluster template for another user. Changing this creates
 *     a new cluster template.
 * 
 * * `apiserver_port` - (Optional) The API server port for the Container
 *     Orchestration Engine for this cluster template. Changing this updates the
 *     API server port of the existing cluster template.
 * 
 * * `coe` - (Required) The Container Orchestration Engine for this cluster
 *     template. Changing this updates the engine of the existing cluster
 *     template.
 * 
 * * `cluster_distro` - (Optional) The distro for the cluster (fedora-atomic,
 *     coreos, etc.). Changing this updates the cluster distro of the existing
 *     cluster template.
 * 
 * * `dns_nameserver` - (Optional) Address of the DNS nameserver that is used in
 *     nodes of the cluster. Changing this updates the DNS nameserver of the
 *     existing cluster template.
 * 
 * * `docker_storage_driver` - (Optional) Docker storage driver. Changing this
 *     updates the Docker storage driver of the existing cluster template.
 * 
 * * `docker_volume_size` - (Optional) The size (in GB) of the Docker volume.
 *     Changing this updates the Docker volume size of the existing cluster
 *     template.
 * 
 * * `external_network_id` - (Optional) The ID of the external network that will
 *     be used for the cluster. Changing this updates the external network ID of
 *     the existing cluster template.
 * 
 * * `fixed_network` - (Optional) The fixed network that will be attached to the
 *     cluster. Changing this updates the fixed network of the existing cluster
 *     template.
 * 
 * * `fixed_subnet` - (Optional) The fixed subnet that will be attached to the
 *     cluster. Changing this updates the fixed subnet of the existing cluster
 *     template.
 * 
 * * `flavor` - (Optional) The flavor for the nodes of the cluster. Can be set via
 *     the `OS_MAGNUM_FLAVOR` environment variable. Changing this updates the
 *     flavor of the existing cluster template.
 * 
 * * `master_flavor` - (Optional) The flavor for the master nodes. Can be set via
 *     the `OS_MAGNUM_MASTER_FLAVOR` environment variable. Changing this updates
 *     the master flavor of the existing cluster template.
 * 
 * * `floating_ip_enabled` - (Optional) Indicates whether created cluster should
 *     create floating IP for every node or not. Changing this updates the
 *     floating IP enabled attribute of the existing cluster template.
 * 
 * * `http_proxy` - (Optional) The address of a proxy for receiving all HTTP
 *     requests and relay them. Changing this updates the HTTP proxy address of
 *     the existing cluster template.
 * 
 * * `https_proxy` - (Optional) The address of a proxy for receiving all HTTPS
 *     requests and relay them. Changing this updates the HTTPS proxy address of
 *     the existing cluster template.
 * 
 * * `image` - (Required) The reference to an image that is used for nodes of the
 *     cluster. Can be set via the `OS_MAGNUM_IMAGE` environment variable.
 *     Changing this updates the image attribute of the existing cluster template.
 * 
 * * `insecure_registry` - (Optional) The insecure registry URL for the cluster
 *     template. Changing this updates the insecure registry attribute of the
 *     existing cluster template.
 * 
 * * `keypair_id` - (Optional) The name of the Compute service SSH keypair.
 *     Changing this updates the keypair of the existing cluster template.
 * 
 * * `labels` - (Optional) The list of key value pairs representing additional
 *     properties of the cluster template. Changing this updates the labels of the
 *     existing cluster template.
 * 
 * * `master_lb_enabled` - (Optional) Indicates whether created cluster should
 *     has a loadbalancer for master nodes or not. Changing this updates the
 *     attribute of the existing cluster template.
 * 
 * * `network_driver` - (Optional) The name of the driver for the container
 *     network. Changing this updates the network driver of the existing cluster
 *     template.
 * 
 * * `no_proxy` - (Optional) A comma-separated list of IP addresses that shouldn't
 *     be used in the cluster. Changing this updates the no proxy list of the
 *     existing cluster template.
 * 
 * * `public` - (Optional) Indicates whether cluster template should be public.
 *     Changing this updates the public attribute of the existing cluster
 *     template.
 * 
 * * `registry_enabled` - (Optional) Indicates whether Docker registry is enabled
 *     in the cluster. Changing this updates the registry enabled attribute of the
 *     existing cluster template.
 * 
 * * `server_type` - (Optional) The server type for the cluster template. Changing
 *     this updates the server type of the existing cluster template.
 * 
 * * `tls_disabled` - (Optional) Indicates whether the TLS should be disabled in
 *     the cluster. Changing this updates the attribute of the existing cluster.
 * 
 * * `volume_driver` - (Optional) The name of the driver that is used for the
 *     volumes of the cluster nodes. Changing this updates the volume driver of
 *     the existing cluster template.
 * 
 * ## Attributes reference
 * 
 * The following attributes are exported:
 * 
 * * `region` - See Argument Reference above.
 * * `name` - See Argument Reference above.
 * * `project_id` - See Argument Reference above.
 * * `created_at` - The time at which cluster template was created.
 * * `updated_at` - The time at which cluster template was created.
 * * `apiserver_port` - See Argument Reference above.
 * * `coe` - See Argument Reference above.
 * * `cluster_distro` - See Argument Reference above.
 * * `dns_nameserver` - See Argument Reference above.
 * * `docker_storage_driver` - See Argument Reference above.
 * * `docker_volume_size` - See Argument Reference above.
 * * `external_network_id` - See Argument Reference above.
 * * `fixed_network` - See Argument Reference above.
 * * `fixed_subnet` - See Argument Reference above.
 * * `flavor` - See Argument Reference above.
 * * `master_flavor` - See Argument Reference above.
 * * `floating_ip_enabled` - See Argument Reference above.
 * * `http_proxy` - See Argument Reference above.
 * * `https_proxy` - See Argument Reference above.
 * * `image` - See Argument Reference above.
 * * `insecure_registry` - See Argument Reference above.
 * * `keypair_id` - See Argument Reference above.
 * * `labels` - See Argument Reference above.
 * * `links` - A list containing associated cluster template links.
 * * `master_lb_enabled` - See Argument Reference above.
 * * `network_driver` - See Argument Reference above.
 * * `no_proxy` - See Argument Reference above.
 * * `public` - See Argument Reference above.
 * * `registry_enabled` - See Argument Reference above.
 * * `server_type` - See Argument Reference above.
 * * `tls_disabled` - See Argument Reference above.
 * * `volume_driver` - See Argument Reference above.
 */
export class ClusterTemplate extends pulumi.CustomResource {
    /**
     * Get an existing ClusterTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterTemplateState, opts?: pulumi.CustomResourceOptions): ClusterTemplate {
        return new ClusterTemplate(name, <any>state, { ...opts, id: id });
    }

    public readonly apiserverPort: pulumi.Output<number | undefined>;
    public readonly clusterDistro: pulumi.Output<string>;
    public readonly coe: pulumi.Output<string>;
    public /*out*/ readonly createdAt: pulumi.Output<string>;
    public readonly dnsNameserver: pulumi.Output<string | undefined>;
    public readonly dockerStorageDriver: pulumi.Output<string | undefined>;
    public readonly dockerVolumeSize: pulumi.Output<number | undefined>;
    public readonly externalNetworkId: pulumi.Output<string | undefined>;
    public readonly fixedNetwork: pulumi.Output<string | undefined>;
    public readonly fixedSubnet: pulumi.Output<string | undefined>;
    public readonly flavor: pulumi.Output<string | undefined>;
    public readonly floatingIpEnabled: pulumi.Output<boolean | undefined>;
    public readonly httpProxy: pulumi.Output<string | undefined>;
    public readonly httpsProxy: pulumi.Output<string | undefined>;
    public readonly image: pulumi.Output<string>;
    public readonly insecureRegistry: pulumi.Output<string | undefined>;
    public readonly keypairId: pulumi.Output<string | undefined>;
    public readonly labels: pulumi.Output<{[key: string]: any} | undefined>;
    public readonly masterFlavor: pulumi.Output<string | undefined>;
    public readonly masterLbEnabled: pulumi.Output<boolean | undefined>;
    public readonly name: pulumi.Output<string>;
    public readonly networkDriver: pulumi.Output<string>;
    public readonly noProxy: pulumi.Output<string | undefined>;
    public /*out*/ readonly projectId: pulumi.Output<string>;
    public readonly public: pulumi.Output<boolean | undefined>;
    public readonly region: pulumi.Output<string>;
    public readonly registryEnabled: pulumi.Output<boolean | undefined>;
    public readonly serverType: pulumi.Output<string>;
    public readonly tlsDisabled: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly updatedAt: pulumi.Output<string>;
    public /*out*/ readonly userId: pulumi.Output<string>;
    public readonly volumeDriver: pulumi.Output<string | undefined>;

    /**
     * Create a ClusterTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterTemplateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterTemplateArgs | ClusterTemplateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ClusterTemplateState = argsOrState as ClusterTemplateState | undefined;
            inputs["apiserverPort"] = state ? state.apiserverPort : undefined;
            inputs["clusterDistro"] = state ? state.clusterDistro : undefined;
            inputs["coe"] = state ? state.coe : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["dnsNameserver"] = state ? state.dnsNameserver : undefined;
            inputs["dockerStorageDriver"] = state ? state.dockerStorageDriver : undefined;
            inputs["dockerVolumeSize"] = state ? state.dockerVolumeSize : undefined;
            inputs["externalNetworkId"] = state ? state.externalNetworkId : undefined;
            inputs["fixedNetwork"] = state ? state.fixedNetwork : undefined;
            inputs["fixedSubnet"] = state ? state.fixedSubnet : undefined;
            inputs["flavor"] = state ? state.flavor : undefined;
            inputs["floatingIpEnabled"] = state ? state.floatingIpEnabled : undefined;
            inputs["httpProxy"] = state ? state.httpProxy : undefined;
            inputs["httpsProxy"] = state ? state.httpsProxy : undefined;
            inputs["image"] = state ? state.image : undefined;
            inputs["insecureRegistry"] = state ? state.insecureRegistry : undefined;
            inputs["keypairId"] = state ? state.keypairId : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["masterFlavor"] = state ? state.masterFlavor : undefined;
            inputs["masterLbEnabled"] = state ? state.masterLbEnabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkDriver"] = state ? state.networkDriver : undefined;
            inputs["noProxy"] = state ? state.noProxy : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["public"] = state ? state.public : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["registryEnabled"] = state ? state.registryEnabled : undefined;
            inputs["serverType"] = state ? state.serverType : undefined;
            inputs["tlsDisabled"] = state ? state.tlsDisabled : undefined;
            inputs["updatedAt"] = state ? state.updatedAt : undefined;
            inputs["userId"] = state ? state.userId : undefined;
            inputs["volumeDriver"] = state ? state.volumeDriver : undefined;
        } else {
            const args = argsOrState as ClusterTemplateArgs | undefined;
            if (!args || args.coe === undefined) {
                throw new Error("Missing required property 'coe'");
            }
            if (!args || args.image === undefined) {
                throw new Error("Missing required property 'image'");
            }
            inputs["apiserverPort"] = args ? args.apiserverPort : undefined;
            inputs["clusterDistro"] = args ? args.clusterDistro : undefined;
            inputs["coe"] = args ? args.coe : undefined;
            inputs["dnsNameserver"] = args ? args.dnsNameserver : undefined;
            inputs["dockerStorageDriver"] = args ? args.dockerStorageDriver : undefined;
            inputs["dockerVolumeSize"] = args ? args.dockerVolumeSize : undefined;
            inputs["externalNetworkId"] = args ? args.externalNetworkId : undefined;
            inputs["fixedNetwork"] = args ? args.fixedNetwork : undefined;
            inputs["fixedSubnet"] = args ? args.fixedSubnet : undefined;
            inputs["flavor"] = args ? args.flavor : undefined;
            inputs["floatingIpEnabled"] = args ? args.floatingIpEnabled : undefined;
            inputs["httpProxy"] = args ? args.httpProxy : undefined;
            inputs["httpsProxy"] = args ? args.httpsProxy : undefined;
            inputs["image"] = args ? args.image : undefined;
            inputs["insecureRegistry"] = args ? args.insecureRegistry : undefined;
            inputs["keypairId"] = args ? args.keypairId : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["masterFlavor"] = args ? args.masterFlavor : undefined;
            inputs["masterLbEnabled"] = args ? args.masterLbEnabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkDriver"] = args ? args.networkDriver : undefined;
            inputs["noProxy"] = args ? args.noProxy : undefined;
            inputs["public"] = args ? args.public : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["registryEnabled"] = args ? args.registryEnabled : undefined;
            inputs["serverType"] = args ? args.serverType : undefined;
            inputs["tlsDisabled"] = args ? args.tlsDisabled : undefined;
            inputs["volumeDriver"] = args ? args.volumeDriver : undefined;
            inputs["createdAt"] = undefined /*out*/;
            inputs["projectId"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
            inputs["userId"] = undefined /*out*/;
        }
        super("openstack:containerinfra/clusterTemplate:ClusterTemplate", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ClusterTemplate resources.
 */
export interface ClusterTemplateState {
    readonly apiserverPort?: pulumi.Input<number>;
    readonly clusterDistro?: pulumi.Input<string>;
    readonly coe?: pulumi.Input<string>;
    readonly createdAt?: pulumi.Input<string>;
    readonly dnsNameserver?: pulumi.Input<string>;
    readonly dockerStorageDriver?: pulumi.Input<string>;
    readonly dockerVolumeSize?: pulumi.Input<number>;
    readonly externalNetworkId?: pulumi.Input<string>;
    readonly fixedNetwork?: pulumi.Input<string>;
    readonly fixedSubnet?: pulumi.Input<string>;
    readonly flavor?: pulumi.Input<string>;
    readonly floatingIpEnabled?: pulumi.Input<boolean>;
    readonly httpProxy?: pulumi.Input<string>;
    readonly httpsProxy?: pulumi.Input<string>;
    readonly image?: pulumi.Input<string>;
    readonly insecureRegistry?: pulumi.Input<string>;
    readonly keypairId?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly masterLbEnabled?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly networkDriver?: pulumi.Input<string>;
    readonly noProxy?: pulumi.Input<string>;
    readonly projectId?: pulumi.Input<string>;
    readonly public?: pulumi.Input<boolean>;
    readonly region?: pulumi.Input<string>;
    readonly registryEnabled?: pulumi.Input<boolean>;
    readonly serverType?: pulumi.Input<string>;
    readonly tlsDisabled?: pulumi.Input<boolean>;
    readonly updatedAt?: pulumi.Input<string>;
    readonly userId?: pulumi.Input<string>;
    readonly volumeDriver?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ClusterTemplate resource.
 */
export interface ClusterTemplateArgs {
    readonly apiserverPort?: pulumi.Input<number>;
    readonly clusterDistro?: pulumi.Input<string>;
    readonly coe: pulumi.Input<string>;
    readonly dnsNameserver?: pulumi.Input<string>;
    readonly dockerStorageDriver?: pulumi.Input<string>;
    readonly dockerVolumeSize?: pulumi.Input<number>;
    readonly externalNetworkId?: pulumi.Input<string>;
    readonly fixedNetwork?: pulumi.Input<string>;
    readonly fixedSubnet?: pulumi.Input<string>;
    readonly flavor?: pulumi.Input<string>;
    readonly floatingIpEnabled?: pulumi.Input<boolean>;
    readonly httpProxy?: pulumi.Input<string>;
    readonly httpsProxy?: pulumi.Input<string>;
    readonly image: pulumi.Input<string>;
    readonly insecureRegistry?: pulumi.Input<string>;
    readonly keypairId?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly masterLbEnabled?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly networkDriver?: pulumi.Input<string>;
    readonly noProxy?: pulumi.Input<string>;
    readonly public?: pulumi.Input<boolean>;
    readonly region?: pulumi.Input<string>;
    readonly registryEnabled?: pulumi.Input<boolean>;
    readonly serverType?: pulumi.Input<string>;
    readonly tlsDisabled?: pulumi.Input<boolean>;
    readonly volumeDriver?: pulumi.Input<string>;
}
