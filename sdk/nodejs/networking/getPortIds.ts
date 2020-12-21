// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to get a list of Openstack Port IDs matching the
 * specified criteria.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const ports = pulumi.output(openstack.networking.getPortIds({
 *     name: "port",
 * }, { async: true }));
 * ```
 */
export function getPortIds(args?: GetPortIdsArgs, opts?: pulumi.InvokeOptions): Promise<GetPortIdsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:networking/getPortIds:getPortIds", {
        "adminStateUp": args.adminStateUp,
        "description": args.description,
        "deviceId": args.deviceId,
        "deviceOwner": args.deviceOwner,
        "dnsName": args.dnsName,
        "fixedIp": args.fixedIp,
        "macAddress": args.macAddress,
        "name": args.name,
        "networkId": args.networkId,
        "projectId": args.projectId,
        "region": args.region,
        "securityGroupIds": args.securityGroupIds,
        "sortDirection": args.sortDirection,
        "sortKey": args.sortKey,
        "status": args.status,
        "tags": args.tags,
        "tenantId": args.tenantId,
    }, opts);
}

/**
 * A collection of arguments for invoking getPortIds.
 */
export interface GetPortIdsArgs {
    /**
     * The administrative state of the port.
     */
    readonly adminStateUp?: boolean;
    /**
     * Human-readable description of the port.
     */
    readonly description?: string;
    /**
     * The ID of the device the port belongs to.
     */
    readonly deviceId?: string;
    /**
     * The device owner of the port.
     */
    readonly deviceOwner?: string;
    readonly dnsName?: string;
    /**
     * The port IP address filter.
     */
    readonly fixedIp?: string;
    /**
     * The MAC address of the port.
     */
    readonly macAddress?: string;
    /**
     * The name of the port.
     */
    readonly name?: string;
    /**
     * The ID of the network the port belongs to.
     */
    readonly networkId?: string;
    /**
     * The owner of the port.
     */
    readonly projectId?: string;
    /**
     * The region in which to obtain the V2 Neutron client.
     * A Neutron client is needed to retrieve port ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The list of port security group IDs to filter.
     */
    readonly securityGroupIds?: string[];
    /**
     * Order the results in either `asc` or `desc`.
     * Defaults to none.
     */
    readonly sortDirection?: string;
    /**
     * Sort ports based on a certain key. Defaults to none.
     */
    readonly sortKey?: string;
    /**
     * The status of the port.
     */
    readonly status?: string;
    /**
     * The list of port tags to filter.
     */
    readonly tags?: string[];
    readonly tenantId?: string;
}

/**
 * A collection of values returned by getPortIds.
 */
export interface GetPortIdsResult {
    readonly adminStateUp?: boolean;
    readonly description?: string;
    readonly deviceId?: string;
    readonly deviceOwner?: string;
    readonly dnsName?: string;
    readonly fixedIp?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly ids: string[];
    readonly macAddress?: string;
    readonly name?: string;
    readonly networkId?: string;
    readonly projectId?: string;
    readonly region?: string;
    readonly securityGroupIds?: string[];
    readonly sortDirection?: string;
    readonly sortKey?: string;
    readonly status?: string;
    readonly tags?: string[];
    readonly tenantId?: string;
}
