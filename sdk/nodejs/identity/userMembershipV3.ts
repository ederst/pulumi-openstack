// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a user membership to group V3 resource within OpenStack.
 *
 * > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
 * this resource.
 *
 * ***
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const project1 = new openstack.identity.Project("project_1", {});
 * const user1 = new openstack.identity.User("user_1", {
 *     defaultProjectId: project1.id,
 * });
 * const group1 = new openstack.identity.GroupV3("group_1", {
 *     description: "group 1",
 * });
 * const role1 = new openstack.identity.Role("role_1", {});
 * const userMembership1 = new openstack.identity.UserMembershipV3("user_membership_1", {
 *     groupId: group1.id,
 *     userId: user1.id,
 * });
 * const roleAssignment1 = new openstack.identity.RoleAssignment("role_assignment_1", {
 *     groupId: group1.id,
 *     projectId: project1.id,
 *     roleId: role1.id,
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported by specifying all two arguments, separated by a forward slash
 *
 * ```sh
 *  $ pulumi import openstack:identity/userMembershipV3:UserMembershipV3 user_membership_1 <user_id>/<group_id>
 * ```
 */
export class UserMembershipV3 extends pulumi.CustomResource {
    /**
     * Get an existing UserMembershipV3 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserMembershipV3State, opts?: pulumi.CustomResourceOptions): UserMembershipV3 {
        return new UserMembershipV3(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:identity/userMembershipV3:UserMembershipV3';

    /**
     * Returns true if the given object is an instance of UserMembershipV3.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserMembershipV3 {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserMembershipV3.__pulumiType;
    }

    /**
     * The UUID of group to which the user will be added.
     * Changing this creates a new user membership.
     */
    public readonly groupId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V3 Identity client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new user membership.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The UUID of user to use. Changing this creates a new user membership.
     */
    public readonly userId!: pulumi.Output<string>;

    /**
     * Create a UserMembershipV3 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserMembershipV3Args, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserMembershipV3Args | UserMembershipV3State, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as UserMembershipV3State | undefined;
            inputs["groupId"] = state ? state.groupId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["userId"] = state ? state.userId : undefined;
        } else {
            const args = argsOrState as UserMembershipV3Args | undefined;
            if ((!args || args.groupId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'groupId'");
            }
            if ((!args || args.userId === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'userId'");
            }
            inputs["groupId"] = args ? args.groupId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["userId"] = args ? args.userId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(UserMembershipV3.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering UserMembershipV3 resources.
 */
export interface UserMembershipV3State {
    /**
     * The UUID of group to which the user will be added.
     * Changing this creates a new user membership.
     */
    readonly groupId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V3 Identity client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new user membership.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The UUID of user to use. Changing this creates a new user membership.
     */
    readonly userId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a UserMembershipV3 resource.
 */
export interface UserMembershipV3Args {
    /**
     * The UUID of group to which the user will be added.
     * Changing this creates a new user membership.
     */
    readonly groupId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V3 Identity client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new user membership.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The UUID of user to use. Changing this creates a new user membership.
     */
    readonly userId: pulumi.Input<string>;
}
