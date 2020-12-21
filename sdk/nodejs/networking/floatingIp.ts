// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 floating IP resource within OpenStack Neutron (networking)
 * that can be used for load balancers.
 * These are similar to Nova (compute) floating IP resources,
 * but only compute floating IPs can be used with compute instances.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const floatip1 = new openstack.networking.FloatingIp("floatip_1", {
 *     pool: "public",
 * });
 * ```
 *
 * ## Import
 *
 * Floating IPs can be imported using the `id`, e.g.
 *
 * ```sh
 *  $ pulumi import openstack:networking/floatingIp:FloatingIp floatip_1 2c7f39f3-702b-48d1-940c-b50384177ee1
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
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpState, opts?: pulumi.CustomResourceOptions): FloatingIp {
        return new FloatingIp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:networking/floatingIp:FloatingIp';

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
     * The actual/specific floating IP to obtain. By default,
     * non-admin users are not able to specify a floating IP, so you must either be
     * an admin user or have had a custom policy or role applied to your OpenStack
     * user or project.
     */
    public readonly address!: pulumi.Output<string>;
    /**
     * The collection of tags assigned on the floating IP, which have
     * been explicitly and implicitly added.
     */
    public /*out*/ readonly allTags!: pulumi.Output<string[]>;
    /**
     * Human-readable description for the floating IP.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The floating IP DNS domain. Available, when Neutron
     * DNS extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    public readonly dnsDomain!: pulumi.Output<string>;
    /**
     * The floating IP DNS name. Available, when Neutron DNS
     * extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    public readonly dnsName!: pulumi.Output<string>;
    /**
     * Fixed IP of the port to associate with this floating IP. Required if
     * the port has multiple fixed IPs.
     */
    public readonly fixedIp!: pulumi.Output<string>;
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    public readonly pool!: pulumi.Output<string>;
    /**
     * ID of an existing port with at least one IP address to
     * associate with this floating IP.
     */
    public readonly portId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a floating IP that can be used with
     * another networking resource, such as a load balancer. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * floating IP (which may or may not have a different address).
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The subnet ID of the floating IP pool. Specify this if
     * the floating IP network has multiple subnets.
     */
    public readonly subnetId!: pulumi.Output<string | undefined>;
    /**
     * A set of string tags for the floating IP.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The target tenant ID in which to allocate the floating
     * IP, if you specify this together with a port_id, make sure the target port
     * belongs to the same tenant. Changing this creates a new floating IP (which
     * may or may not have a different address)
     */
    public readonly tenantId!: pulumi.Output<string>;
    /**
     * Map of additional options.
     */
    public readonly valueSpecs!: pulumi.Output<{[key: string]: any} | undefined>;

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
            inputs["allTags"] = state ? state.allTags : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsDomain"] = state ? state.dnsDomain : undefined;
            inputs["dnsName"] = state ? state.dnsName : undefined;
            inputs["fixedIp"] = state ? state.fixedIp : undefined;
            inputs["pool"] = state ? state.pool : undefined;
            inputs["portId"] = state ? state.portId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
        } else {
            const args = argsOrState as FloatingIpArgs | undefined;
            if ((!args || args.pool === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'pool'");
            }
            inputs["address"] = args ? args.address : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsDomain"] = args ? args.dnsDomain : undefined;
            inputs["dnsName"] = args ? args.dnsName : undefined;
            inputs["fixedIp"] = args ? args.fixedIp : undefined;
            inputs["pool"] = args ? args.pool : undefined;
            inputs["portId"] = args ? args.portId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["allTags"] = undefined /*out*/;
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
     * The actual/specific floating IP to obtain. By default,
     * non-admin users are not able to specify a floating IP, so you must either be
     * an admin user or have had a custom policy or role applied to your OpenStack
     * user or project.
     */
    readonly address?: pulumi.Input<string>;
    /**
     * The collection of tags assigned on the floating IP, which have
     * been explicitly and implicitly added.
     */
    readonly allTags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Human-readable description for the floating IP.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The floating IP DNS domain. Available, when Neutron
     * DNS extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    readonly dnsDomain?: pulumi.Input<string>;
    /**
     * The floating IP DNS name. Available, when Neutron DNS
     * extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    readonly dnsName?: pulumi.Input<string>;
    /**
     * Fixed IP of the port to associate with this floating IP. Required if
     * the port has multiple fixed IPs.
     */
    readonly fixedIp?: pulumi.Input<string>;
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    readonly pool?: pulumi.Input<string>;
    /**
     * ID of an existing port with at least one IP address to
     * associate with this floating IP.
     */
    readonly portId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a floating IP that can be used with
     * another networking resource, such as a load balancer. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * floating IP (which may or may not have a different address).
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The subnet ID of the floating IP pool. Specify this if
     * the floating IP network has multiple subnets.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * A set of string tags for the floating IP.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The target tenant ID in which to allocate the floating
     * IP, if you specify this together with a port_id, make sure the target port
     * belongs to the same tenant. Changing this creates a new floating IP (which
     * may or may not have a different address)
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a FloatingIp resource.
 */
export interface FloatingIpArgs {
    /**
     * The actual/specific floating IP to obtain. By default,
     * non-admin users are not able to specify a floating IP, so you must either be
     * an admin user or have had a custom policy or role applied to your OpenStack
     * user or project.
     */
    readonly address?: pulumi.Input<string>;
    /**
     * Human-readable description for the floating IP.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The floating IP DNS domain. Available, when Neutron
     * DNS extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    readonly dnsDomain?: pulumi.Input<string>;
    /**
     * The floating IP DNS name. Available, when Neutron DNS
     * extension is enabled. The data in this attribute will be published in an
     * external DNS service when Neutron is configured to integrate with such a
     * service. Changing this creates a new floating IP.
     */
    readonly dnsName?: pulumi.Input<string>;
    /**
     * Fixed IP of the port to associate with this floating IP. Required if
     * the port has multiple fixed IPs.
     */
    readonly fixedIp?: pulumi.Input<string>;
    /**
     * The name of the pool from which to obtain the floating
     * IP. Changing this creates a new floating IP.
     */
    readonly pool: pulumi.Input<string>;
    /**
     * ID of an existing port with at least one IP address to
     * associate with this floating IP.
     */
    readonly portId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a floating IP that can be used with
     * another networking resource, such as a load balancer. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * floating IP (which may or may not have a different address).
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The subnet ID of the floating IP pool. Specify this if
     * the floating IP network has multiple subnets.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * A set of string tags for the floating IP.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The target tenant ID in which to allocate the floating
     * IP, if you specify this together with a port_id, make sure the target port
     * belongs to the same tenant. Changing this creates a new floating IP (which
     * may or may not have a different address)
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}
