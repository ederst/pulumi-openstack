// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Associates a floating IP to a port. This is useful for situations
 * where you have a pre-allocated floating IP or are unable to use the
 * `openstack_networking_floatingip_v2` resource to create a floating IP.
 */
export class FloatingIpAssociate extends pulumi.CustomResource {
    /**
     * Get an existing FloatingIpAssociate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpAssociateState): FloatingIpAssociate {
        return new FloatingIpAssociate(name, <any>state, { id });
    }

    /**
     * IP Address of an existing floating IP.
     */
    public readonly floatingIp: pulumi.Output<string>;
    /**
     * ID of an existing port with at least one IP address to
     * associate with this floating IP.
     */
    public readonly portId: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a floating IP that can be used with
     * another networking resource, such as a load balancer. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * floating IP (which may or may not have a different address).
     */
    public readonly region: pulumi.Output<string>;

    /**
     * Create a FloatingIpAssociate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FloatingIpAssociateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FloatingIpAssociateArgs | FloatingIpAssociateState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: FloatingIpAssociateState = argsOrState as FloatingIpAssociateState | undefined;
            inputs["floatingIp"] = state ? state.floatingIp : undefined;
            inputs["portId"] = state ? state.portId : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as FloatingIpAssociateArgs | undefined;
            if (!args || args.floatingIp === undefined) {
                throw new Error("Missing required property 'floatingIp'");
            }
            if (!args || args.portId === undefined) {
                throw new Error("Missing required property 'portId'");
            }
            inputs["floatingIp"] = args ? args.floatingIp : undefined;
            inputs["portId"] = args ? args.portId : undefined;
            inputs["region"] = args ? args.region : undefined;
        }
        super("openstack:networking/floatingIpAssociate:FloatingIpAssociate", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FloatingIpAssociate resources.
 */
export interface FloatingIpAssociateState {
    /**
     * IP Address of an existing floating IP.
     */
    readonly floatingIp?: pulumi.Input<string>;
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
}

/**
 * The set of arguments for constructing a FloatingIpAssociate resource.
 */
export interface FloatingIpAssociateArgs {
    /**
     * IP Address of an existing floating IP.
     */
    readonly floatingIp: pulumi.Input<string>;
    /**
     * ID of an existing port with at least one IP address to
     * associate with this floating IP.
     */
    readonly portId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a floating IP that can be used with
     * another networking resource, such as a load balancer. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * floating IP (which may or may not have a different address).
     */
    readonly region?: pulumi.Input<string>;
}
