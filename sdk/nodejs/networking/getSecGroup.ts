// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available OpenStack security group.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const secgroup = pulumi.output(openstack.networking.getSecGroup({
 *     name: "tfTestSecgroup",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_secgroup_v2.html.markdown.
 */
export function getSecGroup(args?: GetSecGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetSecGroupResult> & GetSecGroupResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetSecGroupResult> = pulumi.runtime.invoke("openstack:networking/getSecGroup:getSecGroup", {
        "description": args.description,
        "name": args.name,
        "region": args.region,
        "secgroupId": args.secgroupId,
        "tags": args.tags,
        "tenantId": args.tenantId,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getSecGroup.
 */
export interface GetSecGroupArgs {
    /**
     * Human-readable description the the subnet.
     */
    readonly description?: string;
    /**
     * The name of the security group.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V2 Neutron client.
     * A Neutron client is needed to retrieve security groups ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The ID of the security group.
     */
    readonly secgroupId?: string;
    /**
     * The list of security group tags to filter.
     */
    readonly tags?: string[];
    /**
     * The owner of the security group.
     */
    readonly tenantId?: string;
}

/**
 * A collection of values returned by getSecGroup.
 */
export interface GetSecGroupResult {
    /**
     * The set of string tags applied on the security group.
     */
    readonly allTags: string[];
    readonly description?: string;
    /**
     * See Argument Reference above.
     * * `description`- See Argument Reference above.
     */
    readonly name?: string;
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    readonly secgroupId?: string;
    readonly tags?: string[];
    readonly tenantId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
