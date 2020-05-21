// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 floating IP resource within OpenStack Nova (compute)
 * that can be used for compute instances.
 *
 * Please note that managing floating IPs through the OpenStack Compute API has
 * been deprecated. Unless you are using an older OpenStack environment, it is
 * recommended to use the `openstack.networking.FloatingIp`
 * resource instead, which uses the OpenStack Networking API.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const floatip1 = new openstack.compute.FloatingIp("floatip1", {
 *     pool: "public",
 * });
 * ```
 */
export class FloatingIp extends pulumi.CustomResource {
    /**
     * Get an existing FloatingIp resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpState, opts?: pulumi.CustomResourceOptions): FloatingIp {
        return new FloatingIp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:compute/floatingIp:FloatingIp';

    /**
     * Returns true if the given object is an instance of FloatingIp.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FloatingIp {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FloatingIp.__pulumiType;
    }

    /**
     * The actual floating IP address itself.
     */
    public /*out*/ readonly address!: pulumi.Output<string>;
    /**
     * The fixed IP address corresponding to the floating IP.
     */
    public /*out*/ readonly fixedIp!: pulumi.Output<string>;
    /**
     * UUID of the compute instance associated with the floating IP.
     */
    public /*out*/ readonly instanceId!: pulumi.Output<string>;
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    public readonly pool!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a floating IP that can be used with
     * a compute instance. If omitted, the `region` argument of the provider
     * is used. Changing this creates a new floating IP (which may or may not
     * have a different address).
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a FloatingIp resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FloatingIpArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FloatingIpArgs | FloatingIpState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FloatingIpState | undefined;
            inputs["address"] = state ? state.address : undefined;
            inputs["fixedIp"] = state ? state.fixedIp : undefined;
            inputs["instanceId"] = state ? state.instanceId : undefined;
            inputs["pool"] = state ? state.pool : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as FloatingIpArgs | undefined;
            if (!args || args.pool === undefined) {
                throw new Error("Missing required property 'pool'");
            }
            inputs["pool"] = args ? args.pool : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["address"] = undefined /*out*/;
            inputs["fixedIp"] = undefined /*out*/;
            inputs["instanceId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(FloatingIp.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FloatingIp resources.
 */
export interface FloatingIpState {
    /**
     * The actual floating IP address itself.
     */
    readonly address?: pulumi.Input<string>;
    /**
     * The fixed IP address corresponding to the floating IP.
     */
    readonly fixedIp?: pulumi.Input<string>;
    /**
     * UUID of the compute instance associated with the floating IP.
     */
    readonly instanceId?: pulumi.Input<string>;
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    readonly pool?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a floating IP that can be used with
     * a compute instance. If omitted, the `region` argument of the provider
     * is used. Changing this creates a new floating IP (which may or may not
     * have a different address).
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FloatingIp resource.
 */
export interface FloatingIpArgs {
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    readonly pool: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a floating IP that can be used with
     * a compute instance. If omitted, the `region` argument of the provider
     * is used. Changing this creates a new floating IP (which may or may not
     * have a different address).
     */
    readonly region?: pulumi.Input<string>;
}
