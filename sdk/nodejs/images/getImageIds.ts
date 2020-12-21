// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to get a list of Openstack Image IDs matching the
 * specified criteria.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const images = pulumi.output(openstack.images.getImageIds({
 *     nameRegex: "^Ubuntu 16\\.04.*-amd64",
 *     properties: {
 *         key: "value",
 *     },
 *     sort: "updated_at",
 * }, { async: true }));
 * ```
 */
export function getImageIds(args?: GetImageIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetImageIdsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:images/getImageIds:getImageIds", {
        "memberStatus": args.memberStatus,
        "name": args.name,
        "nameRegex": args.nameRegex,
        "owner": args.owner,
        "properties": args.properties,
        "region": args.region,
        "sizeMax": args.sizeMax,
        "sizeMin": args.sizeMin,
        "sort": args.sort,
        "sortDirection": args.sortDirection,
        "sortKey": args.sortKey,
        "tag": args.tag,
        "visibility": args.visibility,
    }, opts);
}

/**
 * A collection of arguments for invoking getImageIds.
 */
export interface GetImageIdsArgs {
    /**
     * The status of the image. Must be one of
     * "accepted", "pending", "rejected", or "all".
     */
    readonly memberStatus?: string;
    /**
     * The name of the image. Cannot be used simultaneously
     * with `nameRegex`.
     */
    readonly name?: string;
    /**
     * The regular expressian of the name of the image.
     * Cannot be used simultaneously with `name`. Unlike filtering by `name` the
     * `nameRegex` filtering does by client on the result of OpenStack search
     * query.
     */
    readonly nameRegex?: string;
    /**
     * The owner (UUID) of the image.
     */
    readonly owner?: string;
    /**
     * a map of key/value pairs to match an image with.
     * All specified properties must be matched. Unlike other options filtering
     * by `properties` does by client on the result of OpenStack search query.
     */
    readonly properties?: {[key: string]: any};
    /**
     * The region in which to obtain the V2 Glance client.
     * A Glance client is needed to create an Image that can be used with
     * a compute instance. If omitted, the `region` argument of the provider
     * is used.
     */
    readonly region?: string;
    /**
     * The maximum size (in bytes) of the image to return.
     */
    readonly sizeMax?: number;
    /**
     * The minimum size (in bytes) of the image to return.
     */
    readonly sizeMin?: number;
    /**
     * Sorts the response by one or more attribute and sort
     * direction combinations. You can also set multiple sort keys and directions.
     * Default direction is `desc`. Use the comma (,) character to separate
     * multiple values. For example expression `sort = "name:asc,status"`
     * sorts ascending by name and descending by status. `sort` cannot be used
     * simultaneously with `sortKey`. If both are present in a configuration
     * then only `sort` will be used.
     */
    readonly sort?: string;
    /**
     * Order the results in either `asc` or `desc`.
     * Can be applied only with `sortKey`. Defaults to `asc`
     *
     * @deprecated Use option 'sort' instead.
     */
    readonly sortDirection?: string;
    /**
     * Sort images based on a certain key. Defaults to
     * `name`. `sortKey` cannot be used simultaneously with `sort`. If both
     * are present in a configuration then only `sort` will be used.
     *
     * @deprecated Use option 'sort' instead.
     */
    readonly sortKey?: string;
    /**
     * Search for images with a specific tag.
     */
    readonly tag?: string;
    /**
     * The visibility of the image. Must be one of
     * "public", "private", "community", or "shared". Defaults to "private".
     */
    readonly visibility?: string;
}

/**
 * A collection of values returned by getImageIds.
 */
export interface GetImageIdsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ids: string[];
    readonly memberStatus?: string;
    readonly name?: string;
    readonly nameRegex?: string;
    readonly owner?: string;
    readonly properties?: {[key: string]: any};
    readonly region: string;
    readonly sizeMax?: number;
    readonly sizeMin?: number;
    readonly sort?: string;
    /**
     * @deprecated Use option 'sort' instead.
     */
    readonly sortDirection?: string;
    /**
     * @deprecated Use option 'sort' instead.
     */
    readonly sortKey?: string;
    readonly tag?: string;
    readonly visibility?: string;
}
