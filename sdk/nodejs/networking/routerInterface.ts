// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Manages a V2 router interface resource within OpenStack.
 */
export class RouterInterface extends pulumi.CustomResource {
    /**
     * Get an existing RouterInterface resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterInterfaceState): RouterInterface {
        return new RouterInterface(name, <any>state, { id });
    }

    /**
     * ID of the port this interface connects to. Changing
     * this creates a new router interface.
     */
    public readonly portId: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router interface.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * ID of the router this interface belongs to. Changing
     * this creates a new router interface.
     */
    public readonly routerId: pulumi.Output<string>;
    /**
     * ID of the subnet this interface connects to. Changing
     * this creates a new router interface.
     */
    public readonly subnetId: pulumi.Output<string>;

    /**
     * Create a RouterInterface resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouterInterfaceArgs, opts?: pulumi.ResourceOptions)
    constructor(name: string, argsOrState?: RouterInterfaceArgs | RouterInterfaceState, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: RouterInterfaceState = argsOrState as RouterInterfaceState | undefined;
            inputs["portId"] = state ? state.portId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["routerId"] = state ? state.routerId : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
        } else {
            const args = argsOrState as RouterInterfaceArgs | undefined;
            if (!args || args.routerId === undefined) {
                throw new Error("Missing required property 'routerId'");
            }
            inputs["portId"] = args ? args.portId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["routerId"] = args ? args.routerId : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
        }
        super("openstack:networking/routerInterface:RouterInterface", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RouterInterface resources.
 */
export interface RouterInterfaceState {
    /**
     * ID of the port this interface connects to. Changing
     * this creates a new router interface.
     */
    readonly portId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router interface.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * ID of the router this interface belongs to. Changing
     * this creates a new router interface.
     */
    readonly routerId?: pulumi.Input<string>;
    /**
     * ID of the subnet this interface connects to. Changing
     * this creates a new router interface.
     */
    readonly subnetId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RouterInterface resource.
 */
export interface RouterInterfaceArgs {
    /**
     * ID of the port this interface connects to. Changing
     * this creates a new router interface.
     */
    readonly portId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router interface.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * ID of the router this interface belongs to. Changing
     * this creates a new router interface.
     */
    readonly routerId: pulumi.Input<string>;
    /**
     * ID of the subnet this interface connects to. Changing
     * this creates a new router interface.
     */
    readonly subnetId?: pulumi.Input<string>;
}