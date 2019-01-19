// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 neutron security group resource within OpenStack.
 * Unlike Nova security groups, neutron separates the group from the rules
 * and also allows an admin to target a specific tenant_id.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const openstack_networking_secgroup_v2_secgroup_1 = new openstack.networking.SecGroup("secgroup_1", {
 *     description: "My neutron security group",
 *     name: "secgroup_1",
 * });
 * ```
 */
export class SecGroup extends pulumi.CustomResource {
    /**
     * Get an existing SecGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecGroupState, opts?: pulumi.CustomResourceOptions): SecGroup {
        return new SecGroup(name, <any>state, { ...opts, id: id });
    }

    /**
     * Whether or not to delete the default
     * egress security rules. This is `false` by default. See the below note
     * for more information.
     */
    public readonly deleteDefaultRules: pulumi.Output<boolean | undefined>;
    /**
     * A unique name for the security group.
     */
    public readonly description: pulumi.Output<string>;
    /**
     * A unique name for the security group.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * A set of string tags for the security group.
     */
    public readonly tags: pulumi.Output<string[] | undefined>;
    /**
     * The owner of the security group. Required if admin
     * wants to create a port for another tenant. Changing this creates a new
     * security group.
     */
    public readonly tenantId: pulumi.Output<string>;

    /**
     * Create a SecGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SecGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecGroupArgs | SecGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SecGroupState = argsOrState as SecGroupState | undefined;
            inputs["deleteDefaultRules"] = state ? state.deleteDefaultRules : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
        } else {
            const args = argsOrState as SecGroupArgs | undefined;
            inputs["deleteDefaultRules"] = args ? args.deleteDefaultRules : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
        }
        super("openstack:networking/secGroup:SecGroup", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SecGroup resources.
 */
export interface SecGroupState {
    /**
     * Whether or not to delete the default
     * egress security rules. This is `false` by default. See the below note
     * for more information.
     */
    readonly deleteDefaultRules?: pulumi.Input<boolean>;
    /**
     * A unique name for the security group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A unique name for the security group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of string tags for the security group.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The owner of the security group. Required if admin
     * wants to create a port for another tenant. Changing this creates a new
     * security group.
     */
    readonly tenantId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SecGroup resource.
 */
export interface SecGroupArgs {
    /**
     * Whether or not to delete the default
     * egress security rules. This is `false` by default. See the below note
     * for more information.
     */
    readonly deleteDefaultRules?: pulumi.Input<boolean>;
    /**
     * A unique name for the security group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A unique name for the security group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of string tags for the security group.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The owner of the security group. Required if admin
     * wants to create a port for another tenant. Changing this creates a new
     * security group.
     */
    readonly tenantId?: pulumi.Input<string>;
}
