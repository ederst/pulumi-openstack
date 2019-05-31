// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V1 load balancer pool resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const pool1 = new openstack.loadbalancer.PoolV1("pool_1", {
 *     lbMethod: "ROUND_ROBIN",
 *     lbProvider: "haproxy",
 *     monitorIds: ["67890"],
 *     protocol: "HTTP",
 *     subnetId: "12345",
 * });
 * ```
 * 
 * ## Complete Load Balancing Stack Example
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const secgroup1 = new openstack.compute.SecGroup("secgroup_1", {
 *     description: "Rules for secgroup_1",
 *     rules: [
 *         {
 *             cidr: "0.0.0.0/0",
 *             fromPort: -1,
 *             ipProtocol: "icmp",
 *             toPort: -1,
 *         },
 *         {
 *             cidr: "0.0.0.0/0",
 *             fromPort: 80,
 *             ipProtocol: "tcp",
 *             toPort: 80,
 *         },
 *     ],
 * });
 * const monitor1 = new openstack.loadbalancer.MonitorV1("monitor_1", {
 *     adminStateUp: "true",
 *     delay: 30,
 *     maxRetries: 3,
 *     timeout: 5,
 *     type: "TCP",
 * });
 * const network1 = new openstack.networking.Network("network_1", {
 *     adminStateUp: true,
 * });
 * const instance1 = new openstack.compute.Instance("instance_1", {
 *     networks: [{
 *         uuid: network1.id,
 *     }],
 *     securityGroups: [
 *         "default",
 *         secgroup1.name,
 *     ],
 * });
 * const instance2 = new openstack.compute.Instance("instance_2", {
 *     networks: [{
 *         uuid: network1.id,
 *     }],
 *     securityGroups: [
 *         "default",
 *         secgroup1.name,
 *     ],
 * });
 * const subnet1 = new openstack.networking.Subnet("subnet_1", {
 *     cidr: "192.168.199.0/24",
 *     ipVersion: 4,
 *     networkId: network1.id,
 * });
 * const pool1 = new openstack.loadbalancer.PoolV1("pool_1", {
 *     lbMethod: "ROUND_ROBIN",
 *     monitorIds: [monitor1.id],
 *     protocol: "TCP",
 *     subnetId: subnet1.id,
 * });
 * const member1 = new openstack.loadbalancer.MemberV1("member_1", {
 *     address: instance1.accessIpV4,
 *     poolId: pool1.id,
 *     port: 80,
 * });
 * const member2 = new openstack.loadbalancer.MemberV1("member_2", {
 *     address: instance2.accessIpV4,
 *     poolId: pool1.id,
 *     port: 80,
 * });
 * const vip1 = new openstack.loadbalancer.Vip("vip_1", {
 *     poolId: pool1.id,
 *     port: 80,
 *     protocol: "TCP",
 *     subnetId: subnet1.id,
 * });
 * ```
 * 
 * ## Notes
 * 
 * The `member` block is deprecated in favor of the `openstack_lb_member_v1` resource.
 */
export class PoolV1 extends pulumi.CustomResource {
    /**
     * Get an existing PoolV1 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PoolV1State, opts?: pulumi.CustomResourceOptions): PoolV1 {
        return new PoolV1(name, <any>state, { ...opts, id: id });
    }

    /**
     * The algorithm used to distribute load between the
     * members of the pool. The current specification supports 'ROUND_ROBIN' and
     * 'LEAST_CONNECTIONS' as valid values for this attribute.
     */
    public readonly lbMethod!: pulumi.Output<string>;
    /**
     * The backend load balancing provider. For example:
     * `haproxy`, `F5`, etc.
     */
    public readonly lbProvider!: pulumi.Output<string>;
    /**
     * A list of IDs of monitors to associate with the
     * pool.
     */
    public readonly monitorIds!: pulumi.Output<string[] | undefined>;
    /**
     * The name of the pool. Changing this updates the name of
     * the existing pool.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The protocol used by the pool members, you can use
     * either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an LB pool. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * LB pool.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The network on which the members of the pool will be
     * located. Only members that are on this network can be added to the pool.
     * Changing this creates a new pool.
     */
    public readonly subnetId!: pulumi.Output<string>;
    /**
     * The owner of the pool. Required if admin wants to
     * create a pool member for another tenant. Changing this creates a new pool.
     */
    public readonly tenantId!: pulumi.Output<string>;

    /**
     * Create a PoolV1 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PoolV1Args, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PoolV1Args | PoolV1State, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as PoolV1State | undefined;
            inputs["lbMethod"] = state ? state.lbMethod : undefined;
            inputs["lbProvider"] = state ? state.lbProvider : undefined;
            inputs["monitorIds"] = state ? state.monitorIds : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
        } else {
            const args = argsOrState as PoolV1Args | undefined;
            if (!args || args.lbMethod === undefined) {
                throw new Error("Missing required property 'lbMethod'");
            }
            if (!args || args.protocol === undefined) {
                throw new Error("Missing required property 'protocol'");
            }
            if (!args || args.subnetId === undefined) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["lbMethod"] = args ? args.lbMethod : undefined;
            inputs["lbProvider"] = args ? args.lbProvider : undefined;
            inputs["monitorIds"] = args ? args.monitorIds : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
        }
        super("openstack:loadbalancer/poolV1:PoolV1", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PoolV1 resources.
 */
export interface PoolV1State {
    /**
     * The algorithm used to distribute load between the
     * members of the pool. The current specification supports 'ROUND_ROBIN' and
     * 'LEAST_CONNECTIONS' as valid values for this attribute.
     */
    readonly lbMethod?: pulumi.Input<string>;
    /**
     * The backend load balancing provider. For example:
     * `haproxy`, `F5`, etc.
     */
    readonly lbProvider?: pulumi.Input<string>;
    /**
     * A list of IDs of monitors to associate with the
     * pool.
     */
    readonly monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the pool. Changing this updates the name of
     * the existing pool.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The protocol used by the pool members, you can use
     * either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
     */
    readonly protocol?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an LB pool. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * LB pool.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The network on which the members of the pool will be
     * located. Only members that are on this network can be added to the pool.
     * Changing this creates a new pool.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * The owner of the pool. Required if admin wants to
     * create a pool member for another tenant. Changing this creates a new pool.
     */
    readonly tenantId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PoolV1 resource.
 */
export interface PoolV1Args {
    /**
     * The algorithm used to distribute load between the
     * members of the pool. The current specification supports 'ROUND_ROBIN' and
     * 'LEAST_CONNECTIONS' as valid values for this attribute.
     */
    readonly lbMethod: pulumi.Input<string>;
    /**
     * The backend load balancing provider. For example:
     * `haproxy`, `F5`, etc.
     */
    readonly lbProvider?: pulumi.Input<string>;
    /**
     * A list of IDs of monitors to associate with the
     * pool.
     */
    readonly monitorIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the pool. Changing this updates the name of
     * the existing pool.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The protocol used by the pool members, you can use
     * either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
     */
    readonly protocol: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create an LB pool. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * LB pool.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The network on which the members of the pool will be
     * located. Only members that are on this network can be added to the pool.
     * Changing this creates a new pool.
     */
    readonly subnetId: pulumi.Input<string>;
    /**
     * The owner of the pool. Required if admin wants to
     * create a pool member for another tenant. Changing this creates a new pool.
     */
    readonly tenantId?: pulumi.Input<string>;
}
