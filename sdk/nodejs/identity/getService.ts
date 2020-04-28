// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an OpenStack service.
 * 
 * > **Note:** This usually requires admin privileges.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const service1 = pulumi.output(openstack.identity.getService({
 *     name: "keystone",
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_service_v3.html.markdown.
 */
export function getService(args?: GetServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:identity/getService:getService", {
        "enabled": args.enabled,
        "name": args.name,
        "region": args.region,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getService.
 */
export interface GetServiceArgs {
    /**
     * The service status.
     */
    readonly enabled?: boolean;
    /**
     * The service name.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V3 Keystone client.
     * If omitted, the `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The service type.
     */
    readonly type?: string;
}

/**
 * A collection of values returned by getService.
 */
export interface GetServiceResult {
    /**
     * The service description.
     */
    readonly description: string;
    /**
     * See Argument Reference above.
     */
    readonly enabled?: boolean;
    /**
     * See Argument Reference above.
     */
    readonly name?: string;
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    /**
     * See Argument Reference above.
     */
    readonly type?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
