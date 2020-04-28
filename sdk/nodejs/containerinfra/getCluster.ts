// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available OpenStack Magnum cluster.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const cluster1 = pulumi.output(openstack.containerinfra.getCluster({
 *     name: "cluster1",
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/containerinfra_cluster_v1.html.markdown.
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:containerinfra/getCluster:getCluster", {
        "name": args.name,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterArgs {
    /**
     * The name of the cluster.
     */
    readonly name: string;
    /**
     * The region in which to obtain the V1 Container Infra
     * client.
     * If omitted, the `region` argument of the provider is used.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    /**
     * COE API address.
     */
    readonly apiAddress: string;
    /**
     * The UUID of the V1 Container Infra cluster template.
     */
    readonly clusterTemplateId: string;
    /**
     * COE software version.
     */
    readonly coeVersion: string;
    readonly containerVersion: string;
    /**
     * The timeout (in minutes) for creating the cluster.
     */
    readonly createTimeout: number;
    /**
     * The time at which cluster was created.
     */
    readonly createdAt: string;
    /**
     * The URL used for cluster node discovery.
     */
    readonly discoveryUrl: string;
    /**
     * The size (in GB) of the Docker volume.
     */
    readonly dockerVolumeSize: number;
    /**
     * The fixed network that is attached to the cluster.
     */
    readonly fixedNetwork: string;
    /**
     * The fixed subnet that is attached to the cluster.
     */
    readonly fixedSubnet: string;
    /**
     * The flavor for the nodes of the cluster.
     */
    readonly flavor: string;
    /**
     * The name of the Compute service SSH keypair.
     */
    readonly keypair: string;
    /**
     * The list of key value pairs representing additional properties of
     * the cluster.
     */
    readonly labels: {[key: string]: any};
    /**
     * IP addresses of the master node of the cluster.
     */
    readonly masterAddresses: string;
    /**
     * The number of master nodes for the cluster.
     */
    readonly masterCount: number;
    /**
     * The flavor for the master nodes.
     */
    readonly masterFlavor: string;
    /**
     * See Argument Reference above.
     */
    readonly name: string;
    /**
     * IP addresses of the node of the cluster.
     */
    readonly nodeAddresses: string;
    /**
     * The number of nodes for the cluster.
     */
    readonly nodeCount: number;
    /**
     * The project of the cluster.
     */
    readonly projectId: string;
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    /**
     * UUID of the Orchestration service stack.
     */
    readonly stackId: string;
    /**
     * The time at which cluster was updated.
     */
    readonly updatedAt: string;
    /**
     * The user of the cluster.
     */
    readonly userId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
