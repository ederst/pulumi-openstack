// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Manages a V2 Server Group resource within OpenStack.
 */
export class ServerGroup extends pulumi.CustomResource {
    /**
     * Get an existing ServerGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerGroupState): ServerGroup {
        return new ServerGroup(name, <any>state, { id });
    }

    /**
     * The instances that are part of this server group.
     */
    public /*out*/ readonly members: pulumi.Output<string[]>;
    /**
     * A unique name for the server group. Changing this creates
     * a new server group.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The set of policies for the server group. Only two
     * two policies are available right now, and both are mutually exclusive. See
     * the Policies section for more information. Changing this creates a new
     * server group.
     */
    public readonly policies: pulumi.Output<string[] | undefined>;
    /**
     * The region in which to obtain the V2 Compute client.
     * If omitted, the `region` argument of the provider is used. Changing
     * this creates a new server group.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * Map of additional options.
     */
    public readonly valueSpecs: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a ServerGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServerGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerGroupArgs | ServerGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ServerGroupState = argsOrState as ServerGroupState | undefined;
            inputs["members"] = state ? state.members : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policies"] = state ? state.policies : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
        } else {
            const args = argsOrState as ServerGroupArgs | undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policies"] = args ? args.policies : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["members"] = undefined /*out*/;
        }
        super("openstack:compute/serverGroup:ServerGroup", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServerGroup resources.
 */
export interface ServerGroupState {
    /**
     * The instances that are part of this server group.
     */
    readonly members?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A unique name for the server group. Changing this creates
     * a new server group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The set of policies for the server group. Only two
     * two policies are available right now, and both are mutually exclusive. See
     * the Policies section for more information. Changing this creates a new
     * server group.
     */
    readonly policies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region in which to obtain the V2 Compute client.
     * If omitted, the `region` argument of the provider is used. Changing
     * this creates a new server group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a ServerGroup resource.
 */
export interface ServerGroupArgs {
    /**
     * A unique name for the server group. Changing this creates
     * a new server group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The set of policies for the server group. Only two
     * two policies are available right now, and both are mutually exclusive. See
     * the Policies section for more information. Changing this creates a new
     * server group.
     */
    readonly policies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region in which to obtain the V2 Compute client.
     * If omitted, the `region` argument of the provider is used. Changing
     * this creates a new server group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}
