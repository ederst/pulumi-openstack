// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 port's security groups within OpenStack. Useful, when the port was
 * created not by Terraform (e.g. Manila or LBaaS). It should not be used, when the
 * port was created directly within Terraform.
 * 
 * When the resource is deleted, Terraform doesn't delete the port, but unsets the
 * list of user defined security group IDs.  However, if `enforce` is set to `true`
 * and the resource is deleted, Terraform will remove all assigned security group
 * IDs.
 * 
 * ## Example Usage
 * 
 * ### Append a security group to an existing port
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const systemPort = pulumi.output(openstack.networking.getPort({
 *     fixedIp: "10.0.0.10",
 * }));
 * const secgroup = pulumi.output(openstack.networking.getSecGroup({
 *     name: "secgroup",
 * }));
 * const port1 = new openstack.networking.PortSecGroupAssociate("port_1", {
 *     portId: systemPort.id,
 *     securityGroupIds: [secgroup.id],
 * });
 * ```
 * 
 * ### Enforce a security group to an existing port
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const systemPort = pulumi.output(openstack.networking.getPort({
 *     fixedIp: "10.0.0.10",
 * }));
 * const secgroup = pulumi.output(openstack.networking.getSecGroup({
 *     name: "secgroup",
 * }));
 * const port1 = new openstack.networking.PortSecGroupAssociate("port_1", {
 *     enforce: true,
 *     portId: systemPort.id,
 *     securityGroupIds: [secgroup.id],
 * });
 * ```
 * 
 * ### Remove all security groups from an existing port
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const systemPort = pulumi.output(openstack.networking.getPort({
 *     fixedIp: "10.0.0.10",
 * }));
 * const port1 = new openstack.networking.PortSecGroupAssociate("port_1", {
 *     enforce: true,
 *     portId: systemPort.id,
 *     securityGroupIds: [],
 * });
 * ```
 */
export class PortSecGroupAssociate extends pulumi.CustomResource {
    /**
     * Get an existing PortSecGroupAssociate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PortSecGroupAssociateState, opts?: pulumi.CustomResourceOptions): PortSecGroupAssociate {
        return new PortSecGroupAssociate(name, <any>state, { ...opts, id: id });
    }

    /**
     * The collection of Security Group IDs on the port
     * which have been explicitly and implicitly added.
     */
    public /*out*/ readonly allSecurityGroupIds!: pulumi.Output<string[]>;
    /**
     * Whether to replace or append the list of security
     * groups, specified in the `security_group_ids`. Defaults to `false`.
     */
    public readonly enforce!: pulumi.Output<boolean | undefined>;
    /**
     * An UUID of the port to apply security groups to.
     */
    public readonly portId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to manage a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * resource.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * A list of security group IDs to apply to
     * the port. The security groups must be specified by ID and not name (as
     * opposed to how they are configured with the Compute Instance).
     */
    public readonly securityGroupIds!: pulumi.Output<string[]>;

    /**
     * Create a PortSecGroupAssociate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PortSecGroupAssociateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PortSecGroupAssociateArgs | PortSecGroupAssociateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PortSecGroupAssociateState | undefined;
            inputs["allSecurityGroupIds"] = state ? state.allSecurityGroupIds : undefined;
            inputs["enforce"] = state ? state.enforce : undefined;
            inputs["portId"] = state ? state.portId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["securityGroupIds"] = state ? state.securityGroupIds : undefined;
        } else {
            const args = argsOrState as PortSecGroupAssociateArgs | undefined;
            if (!args || args.portId === undefined) {
                throw new Error("Missing required property 'portId'");
            }
            if (!args || args.securityGroupIds === undefined) {
                throw new Error("Missing required property 'securityGroupIds'");
            }
            inputs["enforce"] = args ? args.enforce : undefined;
            inputs["portId"] = args ? args.portId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["allSecurityGroupIds"] = undefined /*out*/;
        }
        super("openstack:networking/portSecGroupAssociate:PortSecGroupAssociate", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PortSecGroupAssociate resources.
 */
export interface PortSecGroupAssociateState {
    /**
     * The collection of Security Group IDs on the port
     * which have been explicitly and implicitly added.
     */
    readonly allSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether to replace or append the list of security
     * groups, specified in the `security_group_ids`. Defaults to `false`.
     */
    readonly enforce?: pulumi.Input<boolean>;
    /**
     * An UUID of the port to apply security groups to.
     */
    readonly portId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to manage a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * resource.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A list of security group IDs to apply to
     * the port. The security groups must be specified by ID and not name (as
     * opposed to how they are configured with the Compute Instance).
     */
    readonly securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a PortSecGroupAssociate resource.
 */
export interface PortSecGroupAssociateArgs {
    /**
     * Whether to replace or append the list of security
     * groups, specified in the `security_group_ids`. Defaults to `false`.
     */
    readonly enforce?: pulumi.Input<boolean>;
    /**
     * An UUID of the port to apply security groups to.
     */
    readonly portId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to manage a port. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * resource.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A list of security group IDs to apply to
     * the port. The security groups must be specified by ID and not name (as
     * opposed to how they are configured with the Compute Instance).
     */
    readonly securityGroupIds: pulumi.Input<pulumi.Input<string>[]>;
}
