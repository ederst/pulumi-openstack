// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an OpenStack endpoint.
 * 
 * > **Note:** This usually requires admin privileges.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const endpoint1 = pulumi.output(openstack.identity.getEndpoint({
 *     serviceName: "demo",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_endpoint_v3.html.markdown.
 */
export function getEndpoint(args?: GetEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetEndpointResult> & GetEndpointResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetEndpointResult> = pulumi.runtime.invoke("openstack:identity/getEndpoint:getEndpoint", {
        "endpointRegion": args.endpointRegion,
        "interface": args.interface,
        "name": args.name,
        "region": args.region,
        "serviceId": args.serviceId,
        "serviceName": args.serviceName,
        "serviceType": args.serviceType,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getEndpoint.
 */
export interface GetEndpointArgs {
    /**
     * The region the endpoint is assigned to. The
     * `region` and `endpointRegion` can be different.
     */
    readonly endpointRegion?: string;
    /**
     * The endpoint interface. Valid values are `public`,
     * `internal`, and `admin`. Default value is `public`
     */
    readonly interface?: string;
    /**
     * The name of the endpoint.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V3 Keystone client.
     * If omitted, the `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The service id this endpoint belongs to.
     */
    readonly serviceId?: string;
    /**
     * The service name of the endpoint.
     */
    readonly serviceName?: string;
    /**
     * The service type of the endpoint.
     */
    readonly serviceType?: string;
}

/**
 * A collection of values returned by getEndpoint.
 */
export interface GetEndpointResult {
    /**
     * See Argument Reference above.
     */
    readonly endpointRegion?: string;
    /**
     * See Argument Reference above.
     */
    readonly interface?: string;
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
    readonly serviceId?: string;
    /**
     * See Argument Reference above.
     */
    readonly serviceName?: string;
    /**
     * See Argument Reference above.
     */
    readonly serviceType?: string;
    /**
     * The endpoint URL.
     */
    readonly url: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
