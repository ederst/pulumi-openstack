// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available OpenStack subnet.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const subnet1 = pulumi.output(openstack.networking.getSubnet({
 *     name: "subnet1",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_subnet_v2.html.markdown.
 */
export function getSubnet(args?: GetSubnetArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetResult> & GetSubnetResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetSubnetResult> = pulumi.runtime.invoke("openstack:networking/getSubnet:getSubnet", {
        "cidr": args.cidr,
        "description": args.description,
        "dhcpDisabled": args.dhcpDisabled,
        "dhcpEnabled": args.dhcpEnabled,
        "gatewayIp": args.gatewayIp,
        "ipVersion": args.ipVersion,
        "ipv6AddressMode": args.ipv6AddressMode,
        "ipv6RaMode": args.ipv6RaMode,
        "name": args.name,
        "networkId": args.networkId,
        "region": args.region,
        "subnetId": args.subnetId,
        "subnetpoolId": args.subnetpoolId,
        "tags": args.tags,
        "tenantId": args.tenantId,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getSubnet.
 */
export interface GetSubnetArgs {
    /**
     * The CIDR of the subnet.
     */
    readonly cidr?: string;
    /**
     * Human-readable description for the subnet.
     */
    readonly description?: string;
    /**
     * If the subnet has DHCP disabled.
     */
    readonly dhcpDisabled?: boolean;
    /**
     * If the subnet has DHCP enabled.
     */
    readonly dhcpEnabled?: boolean;
    /**
     * The IP of the subnet's gateway.
     */
    readonly gatewayIp?: string;
    /**
     * The IP version of the subnet (either 4 or 6).
     */
    readonly ipVersion?: number;
    /**
     * The IPv6 address mode. Valid values are
     * `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
     */
    readonly ipv6AddressMode?: string;
    /**
     * The IPv6 Router Advertisement mode. Valid values
     * are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
     */
    readonly ipv6RaMode?: string;
    /**
     * The name of the subnet.
     */
    readonly name?: string;
    /**
     * The ID of the network the subnet belongs to.
     */
    readonly networkId?: string;
    /**
     * The region in which to obtain the V2 Neutron client.
     * A Neutron client is needed to retrieve subnet ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: string;
    /**
     * The ID of the subnet.
     */
    readonly subnetId?: string;
    /**
     * The ID of the subnetpool associated with the subnet.
     */
    readonly subnetpoolId?: string;
    /**
     * The list of subnet tags to filter.
     */
    readonly tags?: string[];
    /**
     * The owner of the subnet.
     */
    readonly tenantId?: string;
}

/**
 * A collection of values returned by getSubnet.
 */
export interface GetSubnetResult {
    /**
     * A set of string tags applied on the subnet.
     */
    readonly allTags: string[];
    /**
     * Allocation pools of the subnet.
     */
    readonly allocationPools: { end: string, start: string }[];
    readonly cidr: string;
    readonly description: string;
    readonly dhcpDisabled?: boolean;
    readonly dhcpEnabled?: boolean;
    /**
     * DNS Nameservers of the subnet.
     */
    readonly dnsNameservers: string[];
    /**
     * Whether the subnet has DHCP enabled or not.
     */
    readonly enableDhcp: boolean;
    readonly gatewayIp: string;
    /**
     * Host Routes of the subnet.
     */
    readonly hostRoutes: { destinationCidr: string, nextHop: string }[];
    readonly ipVersion: number;
    readonly ipv6AddressMode: string;
    readonly ipv6RaMode: string;
    readonly name: string;
    readonly networkId: string;
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    readonly subnetId: string;
    readonly subnetpoolId: string;
    readonly tags?: string[];
    readonly tenantId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
