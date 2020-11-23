// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Associate a floating IP to an instance. This can be used instead of the
 * `floatingIp` options in `openstack.compute.Instance`.
 *
 * ## Example Usage
 * ### Automatically detect the correct network
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const instance1 = new openstack.compute.Instance("instance_1", {
 *     flavorId: "3",
 *     imageId: "ad091b52-742f-469e-8f3c-fd81cadf0743",
 *     keyPair: "my_key_pair_name",
 *     securityGroups: ["default"],
 * });
 * const fip1FloatingIp = new openstack.networking.FloatingIp("fip_1", {
 *     pool: "my_pool",
 * });
 * const fip1FloatingIpAssociate = new openstack.compute.FloatingIpAssociate("fip_1", {
 *     floatingIp: fip1FloatingIp.address,
 *     instanceId: instance1.id,
 * });
 * ```
 * ### Explicitly set the network to attach to
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const instance1 = new openstack.compute.Instance("instance_1", {
 *     flavorId: "3",
 *     imageId: "ad091b52-742f-469e-8f3c-fd81cadf0743",
 *     keyPair: "my_key_pair_name",
 *     networks: [
 *         {
 *             name: "my_network",
 *         },
 *         {
 *             name: "default",
 *         },
 *     ],
 *     securityGroups: ["default"],
 * });
 * const fip1FloatingIp = new openstack.networking.FloatingIp("fip_1", {
 *     pool: "my_pool",
 * });
 * const fip1FloatingIpAssociate = new openstack.compute.FloatingIpAssociate("fip_1", {
 *     fixedIp: instance1.networks.apply(networks => networks[1].fixedIpV4!),
 *     floatingIp: fip1FloatingIp.address,
 *     instanceId: instance1.id,
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported by specifying all three arguments, separated by a forward slash
 *
 * ```sh
 *  $ pulumi import openstack:compute/floatingIpAssociate:FloatingIpAssociate fip_1 <floating_ip>/<instance_id>/<fixed_ip>
 * ```
 */
export class FloatingIpAssociate extends pulumi.CustomResource {
    /**
     * Get an existing FloatingIpAssociate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpAssociateState, opts?: pulumi.CustomResourceOptions): FloatingIpAssociate {
        return new FloatingIpAssociate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:compute/floatingIpAssociate:FloatingIpAssociate';

    /**
     * Returns true if the given object is an instance of FloatingIpAssociate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FloatingIpAssociate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FloatingIpAssociate.__pulumiType;
    }

    /**
     * The specific IP address to direct traffic to.
     */
    public readonly fixedIp!: pulumi.Output<string | undefined>;
    /**
     * The floating IP to associate.
     */
    public readonly floatingIp!: pulumi.Output<string>;
    /**
     * The instance to associte the floating IP with.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * Keypairs are associated with accounts, but a Compute client is needed to
     * create one. If omitted, the `region` argument of the provider is used.
     * Changing this creates a new floatingip_associate.
     */
    public readonly region!: pulumi.Output<string>;
    public readonly waitUntilAssociated!: pulumi.Output<boolean | undefined>;

    /**
     * Create a FloatingIpAssociate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FloatingIpAssociateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FloatingIpAssociateArgs | FloatingIpAssociateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FloatingIpAssociateState | undefined;
            inputs["fixedIp"] = state ? state.fixedIp : undefined;
            inputs["floatingIp"] = state ? state.floatingIp : undefined;
            inputs["instanceId"] = state ? state.instanceId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["waitUntilAssociated"] = state ? state.waitUntilAssociated : undefined;
        } else {
            const args = argsOrState as FloatingIpAssociateArgs | undefined;
            if (!args || args.floatingIp === undefined) {
                throw new Error("Missing required property 'floatingIp'");
            }
            if (!args || args.instanceId === undefined) {
                throw new Error("Missing required property 'instanceId'");
            }
            inputs["fixedIp"] = args ? args.fixedIp : undefined;
            inputs["floatingIp"] = args ? args.floatingIp : undefined;
            inputs["instanceId"] = args ? args.instanceId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["waitUntilAssociated"] = args ? args.waitUntilAssociated : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(FloatingIpAssociate.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FloatingIpAssociate resources.
 */
export interface FloatingIpAssociateState {
    /**
     * The specific IP address to direct traffic to.
     */
    readonly fixedIp?: pulumi.Input<string>;
    /**
     * The floating IP to associate.
     */
    readonly floatingIp?: pulumi.Input<string>;
    /**
     * The instance to associte the floating IP with.
     */
    readonly instanceId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * Keypairs are associated with accounts, but a Compute client is needed to
     * create one. If omitted, the `region` argument of the provider is used.
     * Changing this creates a new floatingip_associate.
     */
    readonly region?: pulumi.Input<string>;
    readonly waitUntilAssociated?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a FloatingIpAssociate resource.
 */
export interface FloatingIpAssociateArgs {
    /**
     * The specific IP address to direct traffic to.
     */
    readonly fixedIp?: pulumi.Input<string>;
    /**
     * The floating IP to associate.
     */
    readonly floatingIp: pulumi.Input<string>;
    /**
     * The instance to associte the floating IP with.
     */
    readonly instanceId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * Keypairs are associated with accounts, but a Compute client is needed to
     * create one. If omitted, the `region` argument of the provider is used.
     * Changing this creates a new floatingip_associate.
     */
    readonly region?: pulumi.Input<string>;
    readonly waitUntilAssociated?: pulumi.Input<boolean>;
}
