// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 security group resource within OpenStack.
 * 
 * Please note that managing security groups through the OpenStack Compute API
 * has been deprecated. Unless you are using an older OpenStack environment, it is
 * recommended to use the `openstack_networking_secgroup_v2`
 * and `openstack_networking_secgroup_rule_v2`
 * resources instead, which uses the OpenStack Networking API.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const secgroup1 = new openstack.compute.SecGroup("secgroup_1", {
 *     description: "my security group",
 *     rules: [
 *         {
 *             cidr: "0.0.0.0/0",
 *             fromPort: 22,
 *             ipProtocol: "tcp",
 *             toPort: 22,
 *         },
 *         {
 *             cidr: "0.0.0.0/0",
 *             fromPort: 80,
 *             ipProtocol: "tcp",
 *             toPort: 80,
 *         },
 *     ],
 * });
 * ```
 * 
 * ## Notes
 * 
 * ### ICMP Rules
 * 
 * When using ICMP as the `ip_protocol`, the `from_port` sets the ICMP _type_ and the `to_port` sets the ICMP _code_. To allow all ICMP types, set each value to `-1`, like so:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * ```
 * 
 * A list of ICMP types and codes can be found [here](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages).
 * 
 * ### Referencing Security Groups
 * 
 * When referencing a security group in a configuration (for example, a configuration creates a new security group and then needs to apply it to an instance being created in the same configuration), it is currently recommended to reference the security group by name and not by ID, like this:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const test_server = new openstack.compute.Instance("test-server", {
 *     flavorId: "3",
 *     imageId: "ad091b52-742f-469e-8f3c-fd81cadf0743",
 *     keyPair: "my_key_pair_name",
 *     securityGroups: [openstack_compute_secgroup_v2_secgroup_1.name],
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
     * A description for the security group. Changing this
     * updates the `description` of an existing security group.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * A unique name for the security group. Changing this
     * updates the `name` of an existing security group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a security group. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * A rule describing how the security group operates. The
     * rule object structure is documented below. Changing this updates the
     * security group rules. As shown in the example above, multiple rule blocks
     * may be used.
     */
    public readonly rules!: pulumi.Output<{ cidr?: string, fromGroupId?: string, fromPort: number, id: string, ipProtocol: string, self?: boolean, toPort: number }[]>;

    /**
     * Create a SecGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecGroupArgs | SecGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SecGroupState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["rules"] = state ? state.rules : undefined;
        } else {
            const args = argsOrState as SecGroupArgs | undefined;
            if (!args || args.description === undefined) {
                throw new Error("Missing required property 'description'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["rules"] = args ? args.rules : undefined;
        }
        super("openstack:compute/secGroup:SecGroup", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SecGroup resources.
 */
export interface SecGroupState {
    /**
     * A description for the security group. Changing this
     * updates the `description` of an existing security group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A unique name for the security group. Changing this
     * updates the `name` of an existing security group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a security group. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A rule describing how the security group operates. The
     * rule object structure is documented below. Changing this updates the
     * security group rules. As shown in the example above, multiple rule blocks
     * may be used.
     */
    readonly rules?: pulumi.Input<pulumi.Input<{ cidr?: pulumi.Input<string>, fromGroupId?: pulumi.Input<string>, fromPort: pulumi.Input<number>, id?: pulumi.Input<string>, ipProtocol: pulumi.Input<string>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
}

/**
 * The set of arguments for constructing a SecGroup resource.
 */
export interface SecGroupArgs {
    /**
     * A description for the security group. Changing this
     * updates the `description` of an existing security group.
     */
    readonly description: pulumi.Input<string>;
    /**
     * A unique name for the security group. Changing this
     * updates the `name` of an existing security group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a security group. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security group.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A rule describing how the security group operates. The
     * rule object structure is documented below. Changing this updates the
     * security group rules. As shown in the example above, multiple rule blocks
     * may be used.
     */
    readonly rules?: pulumi.Input<pulumi.Input<{ cidr?: pulumi.Input<string>, fromGroupId?: pulumi.Input<string>, fromPort: pulumi.Input<number>, id?: pulumi.Input<string>, ipProtocol: pulumi.Input<string>, self?: pulumi.Input<boolean>, toPort: pulumi.Input<number> }>[]>;
}
