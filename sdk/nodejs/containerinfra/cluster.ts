// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a V1 Magnum cluster resource within OpenStack.
 *
 * ## Example Usage
 * ### Create a Cluster
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const cluster1 = new openstack.containerinfra.Cluster("cluster_1", {
 *     clusterTemplateId: "b9a45c5c-cd03-4958-82aa-b80bf93cb922",
 *     keypair: "ssh_keypair",
 *     masterCount: 3,
 *     nodeCount: 5,
 * });
 * ```
 * ## Argument reference
 *
 * The following arguments are supported:
 *
 * * `region` - (Optional) The region in which to obtain the V1 Container Infra
 *   client. A Container Infra client is needed to create a cluster. If omitted,
 *   the `region` argument of the provider is used. Changing this creates a new
 *   cluster.
 *
 * * `name` - (Required) The name of the cluster. Changing this updates the name
 *   of the existing cluster template.
 *
 * * `projectId` - (Optional) The project of the cluster. Required if admin wants
 *   to create a cluster in another project. Changing this creates a new
 *   cluster.
 *
 * * `userId` - (Optional) The user of the cluster. Required if admin wants to
 *   create a cluster template for another user. Changing this creates a new
 *   cluster.
 *
 * * `clusterTemplateId` - (Required) The UUID of the V1 Container Infra cluster
 *   template. Changing this creates a new cluster.
 *
 * * `createTimeout` - (Optional) The timeout (in minutes) for creating the
 *   cluster. Changing this creates a new cluster.
 *
 * * `discoveryUrl` - (Optional) The URL used for cluster node discovery.
 *   Changing this creates a new cluster.
 *
 * * `dockerVolumeSize` - (Optional) The size (in GB) of the Docker volume.
 *   Changing this creates a new cluster.
 *
 * * `flavor` - (Optional) The flavor for the nodes of the cluster. Can be set via
 *   the `OS_MAGNUM_FLAVOR` environment variable. Changing this creates a new
 *   cluster.
 *
 * * `masterFlavor` - (Optional) The flavor for the master nodes. Can be set via
 *   the `OS_MAGNUM_MASTER_FLAVOR` environment variable. Changing this creates a
 *   new cluster.
 *
 * * `keypair` - (Optional) The name of the Compute service SSH keypair. Changing
 *   this creates a new cluster.
 *
 * * `labels` - (Optional) The list of key value pairs representing additional
 *   properties of the cluster. Changing this creates a new cluster.
 *
 * * `mergeLabels` - (Optional) Indicates whether the provided labels should be
 *   merged with cluster template labels. Changing this creates a new cluster.
 *
 * * `masterCount` - (Optional) The number of master nodes for the cluster.
 *   Changing this creates a new cluster.
 *
 * * `nodeCount` - (Optional) The number of nodes for the cluster. Changing this
 *   creates a new cluster.
 *
 * * `fixedNetwork` - (Optional) The fixed network that will be attached to the
 *   cluster. Changing this creates a new cluster.
 *
 * * `fixedSubnet` - (Optional) The fixed subnet that will be attached to the
 *   cluster. Changing this creates a new cluster.
 *
 * * `floatingIpEnabled` - (Optional) Indicates whether floating IP should be
 *   created for every cluster node. Changing this creates a new cluster.
 *
 * ## Attributes reference
 *
 * The following attributes are exported:
 *
 * * `region` - See Argument Reference above.
 * * `name` - See Argument Reference above.
 * * `projectId` - See Argument Reference above.
 * * `createdAt` - The time at which cluster was created.
 * * `updatedAt` - The time at which cluster was created.
 * * `apiAddress` - COE API address.
 * * `coeVersion` - COE software version.
 * * `clusterTemplateId` - See Argument Reference above.
 * * `containerVersion` - Container software version.
 * * `createTimeout` - See Argument Reference above.
 * * `discoveryUrl` - See Argument Reference above.
 * * `dockerVolumeSize` - See Argument Reference above.
 * * `flavor` - See Argument Reference above.
 * * `masterFlavor` - See Argument Reference above.
 * * `keypair` - See Argument Reference above.
 * * `labels` - See Argument Reference above.
 * * `mergeLabels` - See Argument Reference above.
 * * `masterCount` - See Argument Reference above.
 * * `nodeCount` - See Argument Reference above.
 * * `fixedNetwork` - See Argument Reference above.
 * * `fixedSubnet` - See Argument Reference above.
 * * `floatingIpEnabled` - See Argument Reference above.
 * * `masterAddresses` - IP addresses of the master node of the cluster.
 * * `nodeAddresses` - IP addresses of the node of the cluster.
 * * `stackId` - UUID of the Orchestration service stack.
 * * `kubeconfig` - The Kubernetes cluster's credentials
 *   * `rawConfig` - The raw kubeconfig file
 *   * `host` - The cluster's API server URL
 *   * `clusterCaCertificate` - The cluster's CA certificate
 *   * `clientKey` - The client's RSA key
 *   * `clientCertificate` - The client's certificate
 *
 * ## Import
 *
 * Clusters can be imported using the `id`, e.g.
 *
 * ```sh
 *  $ pulumi import openstack:containerinfra/cluster:Cluster cluster_1 ce0f9463-dd25-474b-9fe8-94de63e5e42b
 * ```
 */
export class Cluster extends pulumi.CustomResource {
    /**
     * Get an existing Cluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:containerinfra/cluster:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }

    public /*out*/ readonly apiAddress!: pulumi.Output<string>;
    public readonly clusterTemplateId!: pulumi.Output<string>;
    public /*out*/ readonly coeVersion!: pulumi.Output<string>;
    public /*out*/ readonly containerVersion!: pulumi.Output<string>;
    public readonly createTimeout!: pulumi.Output<number>;
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    public readonly discoveryUrl!: pulumi.Output<string>;
    public readonly dockerVolumeSize!: pulumi.Output<number>;
    public readonly fixedNetwork!: pulumi.Output<string>;
    public readonly fixedSubnet!: pulumi.Output<string>;
    public readonly flavor!: pulumi.Output<string>;
    public readonly floatingIpEnabled!: pulumi.Output<boolean>;
    public readonly keypair!: pulumi.Output<string>;
    public /*out*/ readonly kubeconfig!: pulumi.Output<outputs.containerinfra.ClusterKubeconfig>;
    public readonly labels!: pulumi.Output<{[key: string]: any}>;
    public /*out*/ readonly masterAddresses!: pulumi.Output<string[]>;
    public readonly masterCount!: pulumi.Output<number>;
    public readonly masterFlavor!: pulumi.Output<string>;
    public readonly mergeLabels!: pulumi.Output<boolean | undefined>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly nodeAddresses!: pulumi.Output<string[]>;
    public readonly nodeCount!: pulumi.Output<number>;
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    public readonly region!: pulumi.Output<string>;
    public /*out*/ readonly stackId!: pulumi.Output<string>;
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;
    public /*out*/ readonly userId!: pulumi.Output<string>;

    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterArgs | ClusterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ClusterState | undefined;
            inputs["apiAddress"] = state ? state.apiAddress : undefined;
            inputs["clusterTemplateId"] = state ? state.clusterTemplateId : undefined;
            inputs["coeVersion"] = state ? state.coeVersion : undefined;
            inputs["containerVersion"] = state ? state.containerVersion : undefined;
            inputs["createTimeout"] = state ? state.createTimeout : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["discoveryUrl"] = state ? state.discoveryUrl : undefined;
            inputs["dockerVolumeSize"] = state ? state.dockerVolumeSize : undefined;
            inputs["fixedNetwork"] = state ? state.fixedNetwork : undefined;
            inputs["fixedSubnet"] = state ? state.fixedSubnet : undefined;
            inputs["flavor"] = state ? state.flavor : undefined;
            inputs["floatingIpEnabled"] = state ? state.floatingIpEnabled : undefined;
            inputs["keypair"] = state ? state.keypair : undefined;
            inputs["kubeconfig"] = state ? state.kubeconfig : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["masterAddresses"] = state ? state.masterAddresses : undefined;
            inputs["masterCount"] = state ? state.masterCount : undefined;
            inputs["masterFlavor"] = state ? state.masterFlavor : undefined;
            inputs["mergeLabels"] = state ? state.mergeLabels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nodeAddresses"] = state ? state.nodeAddresses : undefined;
            inputs["nodeCount"] = state ? state.nodeCount : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["stackId"] = state ? state.stackId : undefined;
            inputs["updatedAt"] = state ? state.updatedAt : undefined;
            inputs["userId"] = state ? state.userId : undefined;
        } else {
            const args = argsOrState as ClusterArgs | undefined;
            if (!args || args.clusterTemplateId === undefined) {
                throw new Error("Missing required property 'clusterTemplateId'");
            }
            inputs["clusterTemplateId"] = args ? args.clusterTemplateId : undefined;
            inputs["createTimeout"] = args ? args.createTimeout : undefined;
            inputs["discoveryUrl"] = args ? args.discoveryUrl : undefined;
            inputs["dockerVolumeSize"] = args ? args.dockerVolumeSize : undefined;
            inputs["fixedNetwork"] = args ? args.fixedNetwork : undefined;
            inputs["fixedSubnet"] = args ? args.fixedSubnet : undefined;
            inputs["flavor"] = args ? args.flavor : undefined;
            inputs["floatingIpEnabled"] = args ? args.floatingIpEnabled : undefined;
            inputs["keypair"] = args ? args.keypair : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["masterCount"] = args ? args.masterCount : undefined;
            inputs["masterFlavor"] = args ? args.masterFlavor : undefined;
            inputs["mergeLabels"] = args ? args.mergeLabels : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nodeCount"] = args ? args.nodeCount : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["apiAddress"] = undefined /*out*/;
            inputs["coeVersion"] = undefined /*out*/;
            inputs["containerVersion"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["kubeconfig"] = undefined /*out*/;
            inputs["masterAddresses"] = undefined /*out*/;
            inputs["nodeAddresses"] = undefined /*out*/;
            inputs["projectId"] = undefined /*out*/;
            inputs["stackId"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
            inputs["userId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Cluster.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Cluster resources.
 */
export interface ClusterState {
    readonly apiAddress?: pulumi.Input<string>;
    readonly clusterTemplateId?: pulumi.Input<string>;
    readonly coeVersion?: pulumi.Input<string>;
    readonly containerVersion?: pulumi.Input<string>;
    readonly createTimeout?: pulumi.Input<number>;
    readonly createdAt?: pulumi.Input<string>;
    readonly discoveryUrl?: pulumi.Input<string>;
    readonly dockerVolumeSize?: pulumi.Input<number>;
    readonly fixedNetwork?: pulumi.Input<string>;
    readonly fixedSubnet?: pulumi.Input<string>;
    readonly flavor?: pulumi.Input<string>;
    readonly floatingIpEnabled?: pulumi.Input<boolean>;
    readonly keypair?: pulumi.Input<string>;
    readonly kubeconfig?: pulumi.Input<inputs.containerinfra.ClusterKubeconfig>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    readonly masterCount?: pulumi.Input<number>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly mergeLabels?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly nodeAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    readonly nodeCount?: pulumi.Input<number>;
    readonly projectId?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly stackId?: pulumi.Input<string>;
    readonly updatedAt?: pulumi.Input<string>;
    readonly userId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    readonly clusterTemplateId: pulumi.Input<string>;
    readonly createTimeout?: pulumi.Input<number>;
    readonly discoveryUrl?: pulumi.Input<string>;
    readonly dockerVolumeSize?: pulumi.Input<number>;
    readonly fixedNetwork?: pulumi.Input<string>;
    readonly fixedSubnet?: pulumi.Input<string>;
    readonly flavor?: pulumi.Input<string>;
    readonly floatingIpEnabled?: pulumi.Input<boolean>;
    readonly keypair?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterCount?: pulumi.Input<number>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly mergeLabels?: pulumi.Input<boolean>;
    readonly name?: pulumi.Input<string>;
    readonly nodeCount?: pulumi.Input<number>;
    readonly region?: pulumi.Input<string>;
}
