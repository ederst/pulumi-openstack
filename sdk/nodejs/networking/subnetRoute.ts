// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a routing entry on a OpenStack V2 subnet.
 */
export class SubnetRoute extends pulumi.CustomResource {
    /**
     * Get an existing SubnetRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetRouteState, opts?: pulumi.CustomResourceOptions): SubnetRoute {
        return new SubnetRoute(name, <any>state, { ...opts, id: id });
    }

    /**
     * CIDR block to match on the packet’s destination IP. Changing
     * this creates a new routing entry.
     */
    public readonly destinationCidr: pulumi.Output<string>;
    /**
     * IP address of the next hop gateway.  Changing
     * this creates a new routing entry.
     */
    public readonly nextHop: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to configure a routing entry on a subnet. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * routing entry.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * ID of the subnet this routing entry belongs to. Changing
     * this creates a new routing entry.
     */
    public readonly subnetId: pulumi.Output<string>;

    /**
     * Create a SubnetRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubnetRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SubnetRouteArgs | SubnetRouteState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SubnetRouteState = argsOrState as SubnetRouteState | undefined;
            inputs["destinationCidr"] = state ? state.destinationCidr : undefined;
            inputs["nextHop"] = state ? state.nextHop : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
        } else {
            const args = argsOrState as SubnetRouteArgs | undefined;
            if (!args || args.destinationCidr === undefined) {
                throw new Error("Missing required property 'destinationCidr'");
            }
            if (!args || args.nextHop === undefined) {
                throw new Error("Missing required property 'nextHop'");
            }
            if (!args || args.subnetId === undefined) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["destinationCidr"] = args ? args.destinationCidr : undefined;
            inputs["nextHop"] = args ? args.nextHop : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
        }
        super("openstack:networking/subnetRoute:SubnetRoute", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SubnetRoute resources.
 */
export interface SubnetRouteState {
    /**
     * CIDR block to match on the packet’s destination IP. Changing
     * this creates a new routing entry.
     */
    readonly destinationCidr?: pulumi.Input<string>;
    /**
     * IP address of the next hop gateway.  Changing
     * this creates a new routing entry.
     */
    readonly nextHop?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to configure a routing entry on a subnet. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * routing entry.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * ID of the subnet this routing entry belongs to. Changing
     * this creates a new routing entry.
     */
    readonly subnetId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SubnetRoute resource.
 */
export interface SubnetRouteArgs {
    /**
     * CIDR block to match on the packet’s destination IP. Changing
     * this creates a new routing entry.
     */
    readonly destinationCidr: pulumi.Input<string>;
    /**
     * IP address of the next hop gateway.  Changing
     * this creates a new routing entry.
     */
    readonly nextHop: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to configure a routing entry on a subnet. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * routing entry.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * ID of the subnet this routing entry belongs to. Changing
     * this creates a new routing entry.
     */
    readonly subnetId: pulumi.Input<string>;
}
