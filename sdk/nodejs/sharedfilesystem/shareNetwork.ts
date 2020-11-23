// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to configure a share network.
 *
 * A share network stores network information that share servers can use when
 * shares are created.
 *
 * ## Example Usage
 * ### Basic share network
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
 *     description: "test share network",
 *     neutronNetId: network1.id,
 *     neutronSubnetId: subnet1.id,
 * });
 * ```
 * ### Share network with associated security services
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
 * const sharenetwork1 = new openstack.sharedfilesystem.ShareNetwork("sharenetwork_1", {
 *     description: "test share network with security services",
 *     neutronNetId: network1.id,
 *     neutronSubnetId: subnet1.id,
 *     securityServiceIds: [securityservice1.id],
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported by specifying the ID of the share network
 *
 * ```sh
 *  $ pulumi import openstack:sharedfilesystem/shareNetwork:ShareNetwork sharenetwork_1 <id>
 * ```
 */
export class ShareNetwork extends pulumi.CustomResource {
    /**
     * Get an existing ShareNetwork resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareNetworkState, opts?: pulumi.CustomResourceOptions): ShareNetwork {
        return new ShareNetwork(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:sharedfilesystem/shareNetwork:ShareNetwork';

    /**
     * Returns true if the given object is an instance of ShareNetwork.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ShareNetwork {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ShareNetwork.__pulumiType;
    }

    /**
     * The share network CIDR.
     */
    public /*out*/ readonly cidr!: pulumi.Output<string>;
    /**
     * The human-readable description for the share network.
     * Changing this updates the description of the existing share network.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The IP version of the share network. Can either be 4 or 6.
     */
    public /*out*/ readonly ipVersion!: pulumi.Output<number>;
    /**
     * The name for the share network. Changing this updates the name
     * of the existing share network.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The share network type. Can either be VLAN, VXLAN, GRE, or flat.
     */
    public /*out*/ readonly networkType!: pulumi.Output<string>;
    /**
     * The UUID of a neutron network when setting up or updating
     * a share network. Changing this updates the existing share network if it's not used by
     * shares.
     */
    public readonly neutronNetId!: pulumi.Output<string>;
    /**
     * The UUID of the neutron subnet when setting up or
     * updating a share network. Changing this updates the existing share network if it's
     * not used by shares.
     */
    public readonly neutronSubnetId!: pulumi.Output<string>;
    /**
     * The owner of the Share Network.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share network. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * share network.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The list of security service IDs to associate with
     * the share network. The security service must be specified by ID and not name.
     */
    public readonly securityServiceIds!: pulumi.Output<string[] | undefined>;
    /**
     * The share network segmentation ID.
     */
    public /*out*/ readonly segmentationId!: pulumi.Output<number>;

    /**
     * Create a ShareNetwork resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareNetworkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareNetworkArgs | ShareNetworkState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ShareNetworkState | undefined;
            inputs["cidr"] = state ? state.cidr : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["ipVersion"] = state ? state.ipVersion : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkType"] = state ? state.networkType : undefined;
            inputs["neutronNetId"] = state ? state.neutronNetId : undefined;
            inputs["neutronSubnetId"] = state ? state.neutronSubnetId : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["securityServiceIds"] = state ? state.securityServiceIds : undefined;
            inputs["segmentationId"] = state ? state.segmentationId : undefined;
        } else {
            const args = argsOrState as ShareNetworkArgs | undefined;
            if (!args || args.neutronNetId === undefined) {
                throw new Error("Missing required property 'neutronNetId'");
            }
            if (!args || args.neutronSubnetId === undefined) {
                throw new Error("Missing required property 'neutronSubnetId'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["neutronNetId"] = args ? args.neutronNetId : undefined;
            inputs["neutronSubnetId"] = args ? args.neutronSubnetId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["securityServiceIds"] = args ? args.securityServiceIds : undefined;
            inputs["cidr"] = undefined /*out*/;
            inputs["ipVersion"] = undefined /*out*/;
            inputs["networkType"] = undefined /*out*/;
            inputs["projectId"] = undefined /*out*/;
            inputs["segmentationId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ShareNetwork.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ShareNetwork resources.
 */
export interface ShareNetworkState {
    /**
     * The share network CIDR.
     */
    readonly cidr?: pulumi.Input<string>;
    /**
     * The human-readable description for the share network.
     * Changing this updates the description of the existing share network.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The IP version of the share network. Can either be 4 or 6.
     */
    readonly ipVersion?: pulumi.Input<number>;
    /**
     * The name for the share network. Changing this updates the name
     * of the existing share network.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The share network type. Can either be VLAN, VXLAN, GRE, or flat.
     */
    readonly networkType?: pulumi.Input<string>;
    /**
     * The UUID of a neutron network when setting up or updating
     * a share network. Changing this updates the existing share network if it's not used by
     * shares.
     */
    readonly neutronNetId?: pulumi.Input<string>;
    /**
     * The UUID of the neutron subnet when setting up or
     * updating a share network. Changing this updates the existing share network if it's
     * not used by shares.
     */
    readonly neutronSubnetId?: pulumi.Input<string>;
    /**
     * The owner of the Share Network.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share network. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * share network.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The list of security service IDs to associate with
     * the share network. The security service must be specified by ID and not name.
     */
    readonly securityServiceIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The share network segmentation ID.
     */
    readonly segmentationId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a ShareNetwork resource.
 */
export interface ShareNetworkArgs {
    /**
     * The human-readable description for the share network.
     * Changing this updates the description of the existing share network.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name for the share network. Changing this updates the name
     * of the existing share network.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The UUID of a neutron network when setting up or updating
     * a share network. Changing this updates the existing share network if it's not used by
     * shares.
     */
    readonly neutronNetId: pulumi.Input<string>;
    /**
     * The UUID of the neutron subnet when setting up or
     * updating a share network. Changing this updates the existing share network if it's
     * not used by shares.
     */
    readonly neutronSubnetId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share network. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * share network.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The list of security service IDs to associate with
     * the share network. The security service must be specified by ID and not name.
     */
    readonly securityServiceIds?: pulumi.Input<pulumi.Input<string>[]>;
}
