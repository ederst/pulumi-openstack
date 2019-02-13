// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to control the share access lists.
 * 
 * ## Example Usage
 * 
 * ### NFS
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const network1 = new openstack.networking.Network("network_1", {
 *     adminStateUp: true,
 * });
 * const subnet1 = new openstack.networking.Subnet("subnet_1", {
 *     cidr: "192.168.199.0/24",
 *     ipVersion: 4,
 *     networkId: network1.id,
 * });
 * const sharenetwork1 = new openstack.sharedfilesystem.ShareNetwork("sharenetwork_1", {
 *     description: "test share network with security services",
 *     neutronNetId: network1.id,
 *     neutronSubnetId: subnet1.id,
 * });
 * const share1 = new openstack.sharedfilesystem.Share("share_1", {
 *     description: "test share description",
 *     shareNetworkId: sharenetwork1.id,
 *     shareProto: "NFS",
 *     size: 1,
 * });
 * const shareAccess1 = new openstack.sharedfilesystem.ShareAccess("share_access_1", {
 *     accessLevel: "rw",
 *     accessTo: "192.168.199.10",
 *     accessType: "ip",
 *     shareId: share1.id,
 * });
 * ```
 * 
 * ### CIFS
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const network1 = new openstack.networking.Network("network_1", {
 *     adminStateUp: true,
 * });
 * const securityservice1 = new openstack.sharedfilesystem.SecurityService("securityservice_1", {
 *     description: "created by terraform",
 *     dnsIp: "192.168.199.10",
 *     domain: "example.com",
 *     ou: "CN=Computers,DC=example,DC=com",
 *     password: "s8cret",
 *     server: "192.168.199.10",
 *     type: "active_directory",
 *     user: "joinDomainUser",
 * });
 * const subnet1 = new openstack.networking.Subnet("subnet_1", {
 *     cidr: "192.168.199.0/24",
 *     ipVersion: 4,
 *     networkId: network1.id,
 * });
 * const sharenetwork1 = new openstack.sharedfilesystem.ShareNetwork("sharenetwork_1", {
 *     description: "share the secure love",
 *     neutronNetId: network1.id,
 *     neutronSubnetId: subnet1.id,
 *     securityServiceIds: [securityservice1.id],
 * });
 * const share1 = new openstack.sharedfilesystem.Share("share_1", {
 *     shareNetworkId: sharenetwork1.id,
 *     shareProto: "CIFS",
 *     size: 1,
 * });
 * const shareAccess1 = new openstack.sharedfilesystem.ShareAccess("share_access_1", {
 *     accessLevel: "ro",
 *     accessTo: "windows",
 *     accessType: "user",
 *     shareId: share1.id,
 * });
 * const shareAccess2 = new openstack.sharedfilesystem.ShareAccess("share_access_2", {
 *     accessLevel: "rw",
 *     accessTo: "linux",
 *     accessType: "user",
 *     shareId: share1.id,
 * });
 * 
 * export const exportLocations = share1.exportLocations;
 * ```
 */
export class ShareAccess extends pulumi.CustomResource {
    /**
     * Get an existing ShareAccess resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareAccessState, opts?: pulumi.CustomResourceOptions): ShareAccess {
        return new ShareAccess(name, <any>state, { ...opts, id: id });
    }

    /**
     * The access level to the share. Can either be `rw` or `ro`.
     */
    public readonly accessLevel: pulumi.Output<string>;
    /**
     * The value that defines the access. Can either be an IP
     * address or a username verified by configured Security Service of the Share Network.
     */
    public readonly accessTo: pulumi.Output<string>;
    /**
     * The access rule type. Can either be an ip, user or cert.
     */
    public readonly accessType: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share access. Changing this
     * creates a new share access.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * The UUID of the share to which you are granted access.
     */
    public readonly shareId: pulumi.Output<string>;

    /**
     * Create a ShareAccess resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareAccessArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareAccessArgs | ShareAccessState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ShareAccessState = argsOrState as ShareAccessState | undefined;
            inputs["accessLevel"] = state ? state.accessLevel : undefined;
            inputs["accessTo"] = state ? state.accessTo : undefined;
            inputs["accessType"] = state ? state.accessType : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["shareId"] = state ? state.shareId : undefined;
        } else {
            const args = argsOrState as ShareAccessArgs | undefined;
            if (!args || args.accessLevel === undefined) {
                throw new Error("Missing required property 'accessLevel'");
            }
            if (!args || args.accessTo === undefined) {
                throw new Error("Missing required property 'accessTo'");
            }
            if (!args || args.accessType === undefined) {
                throw new Error("Missing required property 'accessType'");
            }
            if (!args || args.shareId === undefined) {
                throw new Error("Missing required property 'shareId'");
            }
            inputs["accessLevel"] = args ? args.accessLevel : undefined;
            inputs["accessTo"] = args ? args.accessTo : undefined;
            inputs["accessType"] = args ? args.accessType : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["shareId"] = args ? args.shareId : undefined;
        }
        super("openstack:sharedfilesystem/shareAccess:ShareAccess", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ShareAccess resources.
 */
export interface ShareAccessState {
    /**
     * The access level to the share. Can either be `rw` or `ro`.
     */
    readonly accessLevel?: pulumi.Input<string>;
    /**
     * The value that defines the access. Can either be an IP
     * address or a username verified by configured Security Service of the Share Network.
     */
    readonly accessTo?: pulumi.Input<string>;
    /**
     * The access rule type. Can either be an ip, user or cert.
     */
    readonly accessType?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share access. Changing this
     * creates a new share access.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The UUID of the share to which you are granted access.
     */
    readonly shareId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ShareAccess resource.
 */
export interface ShareAccessArgs {
    /**
     * The access level to the share. Can either be `rw` or `ro`.
     */
    readonly accessLevel: pulumi.Input<string>;
    /**
     * The value that defines the access. Can either be an IP
     * address or a username verified by configured Security Service of the Share Network.
     */
    readonly accessTo: pulumi.Input<string>;
    /**
     * The access rule type. Can either be an ip, user or cert.
     */
    readonly accessType: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share access. Changing this
     * creates a new share access.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The UUID of the share to which you are granted access.
     */
    readonly shareId: pulumi.Input<string>;
}