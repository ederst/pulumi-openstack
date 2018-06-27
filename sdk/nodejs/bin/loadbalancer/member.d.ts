import * as pulumi from "@pulumi/pulumi";
/**
 * Manages a V2 member resource within OpenStack.
 */
export declare class Member extends pulumi.CustomResource {
    /**
     * Get an existing Member resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberState): Member;
    /**
     * The IP address of the member to receive traffic from
     * the load balancer. Changing this creates a new member.
     */
    readonly address: pulumi.Output<string>;
    /**
     * The administrative state of the member.
     * A valid value is true (UP) or false (DOWN).
     */
    readonly adminStateUp: pulumi.Output<boolean | undefined>;
    /**
     * Human-readable name for the member.
     */
    readonly name: pulumi.Output<string>;
    /**
     * The id of the pool that this member will be
     * assigned to.
     */
    readonly poolId: pulumi.Output<string>;
    /**
     * The port on which to listen for client traffic.
     * Changing this creates a new member.
     */
    readonly protocolPort: pulumi.Output<number>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an . If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * member.
     */
    readonly region: pulumi.Output<string>;
    /**
     * The subnet in which to access the member
     */
    readonly subnetId: pulumi.Output<string | undefined>;
    /**
     * Required for admins. The UUID of the tenant who owns
     * the member.  Only administrative users can specify a tenant UUID
     * other than their own. Changing this creates a new member.
     */
    readonly tenantId: pulumi.Output<string>;
    /**
     * A positive integer value that indicates the relative
     * portion of traffic that this member should receive from the pool. For
     * example, a member with a weight of 10 receives five times as much traffic
     * as a member with a weight of 2.
     */
    readonly weight: pulumi.Output<number>;
    /**
     * Create a Member resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MemberArgs, opts?: pulumi.ResourceOptions);
}
/**
 * Input properties used for looking up and filtering Member resources.
 */
export interface MemberState {
    /**
     * The IP address of the member to receive traffic from
     * the load balancer. Changing this creates a new member.
     */
    readonly address?: pulumi.Input<string>;
    /**
     * The administrative state of the member.
     * A valid value is true (UP) or false (DOWN).
     */
    readonly adminStateUp?: pulumi.Input<boolean>;
    /**
     * Human-readable name for the member.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The id of the pool that this member will be
     * assigned to.
     */
    readonly poolId?: pulumi.Input<string>;
    /**
     * The port on which to listen for client traffic.
     * Changing this creates a new member.
     */
    readonly protocolPort?: pulumi.Input<number>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an . If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * member.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The subnet in which to access the member
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * Required for admins. The UUID of the tenant who owns
     * the member.  Only administrative users can specify a tenant UUID
     * other than their own. Changing this creates a new member.
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * A positive integer value that indicates the relative
     * portion of traffic that this member should receive from the pool. For
     * example, a member with a weight of 10 receives five times as much traffic
     * as a member with a weight of 2.
     */
    readonly weight?: pulumi.Input<number>;
}
/**
 * The set of arguments for constructing a Member resource.
 */
export interface MemberArgs {
    /**
     * The IP address of the member to receive traffic from
     * the load balancer. Changing this creates a new member.
     */
    readonly address: pulumi.Input<string>;
    /**
     * The administrative state of the member.
     * A valid value is true (UP) or false (DOWN).
     */
    readonly adminStateUp?: pulumi.Input<boolean>;
    /**
     * Human-readable name for the member.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The id of the pool that this member will be
     * assigned to.
     */
    readonly poolId: pulumi.Input<string>;
    /**
     * The port on which to listen for client traffic.
     * Changing this creates a new member.
     */
    readonly protocolPort: pulumi.Input<number>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an . If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * member.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The subnet in which to access the member
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * Required for admins. The UUID of the tenant who owns
     * the member.  Only administrative users can specify a tenant UUID
     * other than their own. Changing this creates a new member.
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * A positive integer value that indicates the relative
     * portion of traffic that this member should receive from the pool. For
     * example, a member with a weight of 10 receives five times as much traffic
     * as a member with a weight of 2.
     */
    readonly weight?: pulumi.Input<number>;
}