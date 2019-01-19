// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V1 Magnum cluster resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ### Create a Cluster
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const openstack_containerinfra_cluster_v1_cluster_1 = new openstack.containerinfra.Cluster("cluster_1", {
 *     clusterTemplateId: "b9a45c5c-cd03-4958-82aa-b80bf93cb922",
 *     keypair: "ssh_keypair",
 *     masterCount: 3,
 *     name: "cluster_1",
 *     nodeCount: 5,
 * });
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
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly apiAddress: pulumi.Output<string>;
    public readonly clusterTemplateId: pulumi.Output<string>;
    public /*out*/ readonly coeVersion: pulumi.Output<string>;
    public /*out*/ readonly containerVersion: pulumi.Output<string>;
    public readonly createTimeout: pulumi.Output<number>;
    public /*out*/ readonly createdAt: pulumi.Output<string>;
    public readonly discoveryUrl: pulumi.Output<string>;
    public readonly dockerVolumeSize: pulumi.Output<number>;
    public readonly flavor: pulumi.Output<string>;
    public readonly keypair: pulumi.Output<string>;
    public readonly labels: pulumi.Output<{[key: string]: any}>;
    public /*out*/ readonly masterAddresses: pulumi.Output<string>;
    public readonly masterCount: pulumi.Output<number>;
    public readonly masterFlavor: pulumi.Output<string>;
    public readonly name: pulumi.Output<string>;
    public /*out*/ readonly nodeAddresses: pulumi.Output<string>;
    public readonly nodeCount: pulumi.Output<number>;
    public /*out*/ readonly projectId: pulumi.Output<string>;
    public readonly region: pulumi.Output<string>;
    public /*out*/ readonly stackId: pulumi.Output<string>;
    public /*out*/ readonly updatedAt: pulumi.Output<string>;
    public /*out*/ readonly userId: pulumi.Output<string>;

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
            const state: ClusterState = argsOrState as ClusterState | undefined;
            inputs["apiAddress"] = state ? state.apiAddress : undefined;
            inputs["clusterTemplateId"] = state ? state.clusterTemplateId : undefined;
            inputs["coeVersion"] = state ? state.coeVersion : undefined;
            inputs["containerVersion"] = state ? state.containerVersion : undefined;
            inputs["createTimeout"] = state ? state.createTimeout : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["discoveryUrl"] = state ? state.discoveryUrl : undefined;
            inputs["dockerVolumeSize"] = state ? state.dockerVolumeSize : undefined;
            inputs["flavor"] = state ? state.flavor : undefined;
            inputs["keypair"] = state ? state.keypair : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["masterAddresses"] = state ? state.masterAddresses : undefined;
            inputs["masterCount"] = state ? state.masterCount : undefined;
            inputs["masterFlavor"] = state ? state.masterFlavor : undefined;
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
            inputs["flavor"] = args ? args.flavor : undefined;
            inputs["keypair"] = args ? args.keypair : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["masterCount"] = args ? args.masterCount : undefined;
            inputs["masterFlavor"] = args ? args.masterFlavor : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["nodeCount"] = args ? args.nodeCount : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["apiAddress"] = undefined /*out*/;
            inputs["coeVersion"] = undefined /*out*/;
            inputs["containerVersion"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["masterAddresses"] = undefined /*out*/;
            inputs["nodeAddresses"] = undefined /*out*/;
            inputs["projectId"] = undefined /*out*/;
            inputs["stackId"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
            inputs["userId"] = undefined /*out*/;
        }
        super("openstack:containerinfra/cluster:Cluster", name, inputs, opts);
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
    readonly flavor?: pulumi.Input<string>;
    readonly keypair?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterAddresses?: pulumi.Input<string>;
    readonly masterCount?: pulumi.Input<number>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly nodeAddresses?: pulumi.Input<string>;
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
    readonly flavor?: pulumi.Input<string>;
    readonly keypair?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly masterCount?: pulumi.Input<number>;
    readonly masterFlavor?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly nodeCount?: pulumi.Input<number>;
    readonly region?: pulumi.Input<string>;
}
