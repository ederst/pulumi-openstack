// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available Shared File System share.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const share1 = openstack.sharedfilesystem.getShare({
 *     name: "share1",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/sharedfilesystem_share_v2.html.markdown.
 */
export function getShare(args?: GetShareArgs, opts?: pulumi.InvokeOptions): Promise<GetShareResult> & GetShareResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetShareResult> = pulumi.runtime.invoke("openstack:sharedfilesystem/getShare:getShare", {
        "description": args.description,
        "exportLocationPath": args.exportLocationPath,
        "isPublic": args.isPublic,
        "metadata": args.metadata,
        "name": args.name,
        "region": args.region,
        "shareNetworkId": args.shareNetworkId,
        "snapshotId": args.snapshotId,
        "status": args.status,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getShare.
 */
export interface GetShareArgs {
    /**
     * The human-readable description for the share.
     */
    readonly description?: string;
    /**
     * The export location path of the share. Available
     * since Manila API version 2.35.
     */
    readonly exportLocationPath?: string;
    /**
     * The level of visibility for the share.
     * length.
     */
    readonly isPublic?: boolean;
    /**
     * One or more metadata key and value pairs as a dictionary of
     * strings.
     */
    readonly metadata?: {[key: string]: any};
    /**
     * The name of the share.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V2 Shared File System client.
     */
    readonly region?: string;
    /**
     * The UUID of the share's share network.
     */
    readonly shareNetworkId?: string;
    /**
     * The UUID of the share's base snapshot.
     */
    readonly snapshotId?: string;
    /**
     * A share status filter. A valid value is `creating`,
     * `error`, `available`, `deleting`, `errorDeleting`, `manageStarting`,
     * `manageError`, `unmanageStarting`, `unmanageError`, `unmanaged`,
     * `extending`, `extendingError`, `shrinking`, `shrinkingError`, or
     * `shrinkingPossibleDataLossError`.
     */
    readonly status?: string;
}

/**
 * A collection of values returned by getShare.
 */
export interface GetShareResult {
    /**
     * The share availability zone.
     */
    readonly availabilityZone: string;
    /**
     * See Argument Reference above.
     */
    readonly description: string;
    /**
     * See Argument Reference above.
     */
    readonly exportLocationPath?: string;
    /**
     * A list of export locations. For example, when a share
     * server has more than one network interface, it can have multiple export
     * locations.
     */
    readonly exportLocations: outputs.sharedfilesystem.GetShareExportLocation[];
    /**
     * See Argument Reference above.
     */
    readonly isPublic: boolean;
    /**
     * See Argument Reference above.
     */
    readonly metadata: {[key: string]: any};
    /**
     * See Argument Reference above.
     */
    readonly name: string;
    /**
     * See Argument Reference above.
     */
    readonly projectId: string;
    /**
     * The region in which to obtain the V2 Shared File System client.
     */
    readonly region: string;
    /**
     * See Argument Reference above.
     */
    readonly shareNetworkId: string;
    /**
     * The share protocol.
     */
    readonly shareProto: string;
    /**
     * The share size, in GBs.
     */
    readonly size: number;
    /**
     * See Argument Reference above.
     */
    readonly snapshotId: string;
    /**
     * See Argument Reference above.
     */
    readonly status: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
