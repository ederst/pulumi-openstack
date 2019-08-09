// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available OpenStack port.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const port1 = pulumi.output(openstack.networking.getPort({
 *     name: "port1",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_port_v2.html.markdown.
 */
export function getPort(args?: GetPortArgs, opts?: pulumi.InvokeOptions): Promise<GetPortResult> & GetPortResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetPortResult> = pulumi.runtime.invoke("openstack:networking/getPort:getPort", {
        "adminStateUp": args.adminStateUp,
        "description": args.description,
        "deviceId": args.deviceId,
        "deviceOwner": args.deviceOwner,
        "dnsName": args.dnsName,
        "fixedIp": args.fixedIp,
        "macAddress": args.macAddress,
        "name": args.name,
        "networkId": args.networkId,
        "portId": args.portId,
        "projectId": args.projectId,
        "region": args.region,
        "securityGroupIds": args.securityGroupIds,
        "status": args.status,
        "tags": args.tags,
        "tenantId": args.tenantId,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getPort.
 */
export interface GetPortArgs {
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
    /**
     * The port DNS name to filter. Available, when Neutron
     * DNS extension is enabled.
     */
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
     * The ID of the port.
     */
    readonly portId?: string;
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
 * A collection of values returned by getPort.
 */
export interface GetPortResult {
    /**
     * See Argument Reference above.
     */
    readonly adminStateUp?: boolean;
    /**
     * The collection of Fixed IP addresses on the port in the
     * order returned by the Network v2 API.
     */
    readonly allFixedIps: string[];
    /**
     * The set of security group IDs applied on the port.
     */
    readonly allSecurityGroupIds: string[];
    /**
     * The set of string tags applied on the port.
     */
    readonly allTags: string[];
    /**
     * An IP/MAC Address pair of additional IP
     * addresses that can be active on this port. The structure is described
     * below.
     */
    readonly allowedAddressPairs: { ipAddress: string, macAddress: string }[];
    /**
     * The port binding information. The structure is described below.
     */
    readonly bindings: { hostId: string, profile: string, vifDetails: {[key: string]: any}, vifType: string, vnicType: string }[];
    /**
     * See Argument Reference above.
     */
    readonly description?: string;
    /**
     * See Argument Reference above.
     */
    readonly deviceId?: string;
    /**
     * See Argument Reference above.
     */
    readonly deviceOwner?: string;
    /**
     * The list of maps representing port DNS assignments.
     */
    readonly dnsAssignments: {[key: string]: any}[];
    /**
     * See Argument Reference above.
     */
    readonly dnsName?: string;
    /**
     * An extra DHCP option configured on the port.
     * The structure is described below.
     */
    readonly extraDhcpOptions: { ipVersion: number, name: string, value: string }[];
    readonly fixedIp?: string;
    /**
     * The additional MAC address.
     */
    readonly macAddress?: string;
    /**
     * Name of the DHCP option.
     */
    readonly name?: string;
    /**
     * See Argument Reference above.
     */
    readonly networkId?: string;
    /**
     * See Argument Reference above.
     */
    readonly portId?: string;
    /**
     * See Argument Reference above.
     */
    readonly projectId?: string;
    /**
     * See Argument Reference above.
     */
    readonly region?: string;
    readonly securityGroupIds?: string[];
    readonly status?: string;
    readonly tags?: string[];
    readonly tenantId?: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
