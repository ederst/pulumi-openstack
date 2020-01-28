// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about an existing volume.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volume1 = openstack.blockstorage.getVolumeV2({
 *     name: "volume1",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_volume_v2.html.markdown.
 */
export function getVolumeV2(args?: GetVolumeV2Args, opts?: pulumi.InvokeOptions): Promise<GetVolumeV2Result> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:blockstorage/getVolumeV2:getVolumeV2", {
        "bootable": args.bootable,
        "metadata": args.metadata,
        "name": args.name,
        "region": args.region,
        "status": args.status,
        "volumeType": args.volumeType,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolumeV2.
 */
export interface GetVolumeV2Args {
    readonly bootable?: string;
    /**
     * Metadata key/value pairs associated with the volume.
     */
    readonly metadata?: {[key: string]: any};
    /**
     * The name of the volume.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V2 Block Storage
     * client. If omitted, the `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The status of the volume.
     */
    readonly status?: string;
    readonly volumeType?: string;
}

/**
 * A collection of values returned by getVolumeV2.
 */
export interface GetVolumeV2Result {
    /**
     * Indicates if the volume is bootable.
     */
    readonly bootable: string;
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
    readonly region: string;
    /**
     * The size of the volume in GBs.
     */
    readonly size: number;
    /**
     * The ID of the volume from which the current volume was created.
     */
    readonly sourceVolumeId: string;
    /**
     * See Argument Reference above.
     */
    readonly status: string;
    /**
     * The type of the volume.
     */
    readonly volumeType: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
