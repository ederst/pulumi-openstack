// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a V2 router resource within OpenStack.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const router1 = new openstack.networking.Router("router_1", {
 *     adminStateUp: true,
 *     externalNetworkId: "f67f0d72-0ddf-11e4-9d95-e1f29f417e2f",
 * });
 * ```
 */
export class Router extends pulumi.CustomResource {
    /**
     * Get an existing Router resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RouterState, opts?: pulumi.CustomResourceOptions): Router {
        return new Router(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:networking/router:Router';

    /**
     * Returns true if the given object is an instance of Router.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Router {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Router.__pulumiType;
    }

    /**
     * Administrative up/down status for the router
     * (must be "true" or "false" if provided). Changing this updates the
     * `adminStateUp` of an existing router.
     */
    public readonly adminStateUp!: pulumi.Output<boolean>;
    /**
     * The collection of tags assigned on the router, which have been
     * explicitly and implicitly added.
     */
    public /*out*/ readonly allTags!: pulumi.Output<string[]>;
    /**
     * An availability zone is used to make 
     * network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
     * this creates a new router.
     */
    public readonly availabilityZoneHints!: pulumi.Output<string[]>;
    /**
     * Human-readable description for the router.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether or not to create a
     * distributed router. The default policy setting in Neutron restricts
     * usage of this property to administrative users only.
     */
    public readonly distributed!: pulumi.Output<boolean>;
    /**
     * Enable Source NAT for the router. Valid values are
     * "true" or "false". An `externalNetworkId` has to be set in order to
     * set this property. Changing this updates the `enableSnat` of the router.
     * Setting this value **requires** an **ext-gw-mode** extension to be enabled
     * in OpenStack Neutron.
     */
    public readonly enableSnat!: pulumi.Output<boolean>;
    /**
     * An external fixed IP for the router. This
     * can be repeated. The structure is described below. An `externalNetworkId`
     * has to be set in order to set this property. Changing this updates the
     * external fixed IPs of the router.
     */
    public readonly externalFixedIps!: pulumi.Output<outputs.networking.RouterExternalFixedIp[]>;
    /**
     * The
     * network UUID of an external gateway for the router. A router with an
     * external gateway is required if any compute instances or load balancers
     * will be using floating IPs. Changing this updates the external gateway
     * of an existing router.
     *
     * @deprecated use external_network_id instead
     */
    public readonly externalGateway!: pulumi.Output<string>;
    /**
     * The network UUID of an external gateway
     * for the router. A router with an external gateway is required if any
     * compute instances or load balancers will be using floating IPs. Changing
     * this updates the external gateway of the router.
     */
    public readonly externalNetworkId!: pulumi.Output<string>;
    /**
     * A unique name for the router. Changing this
     * updates the `name` of an existing router.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * A set of string tags for the router.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The owner of the floating IP. Required if admin wants
     * to create a router for another tenant. Changing this creates a new router.
     */
    public readonly tenantId!: pulumi.Output<string>;
    /**
     * Map of additional driver-specific options.
     */
    public readonly valueSpecs!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Map of additional vendor-specific options.
     * Supported options are described below.
     */
    public readonly vendorOptions!: pulumi.Output<outputs.networking.RouterVendorOptions | undefined>;

    /**
     * Create a Router resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RouterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RouterArgs | RouterState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RouterState | undefined;
            inputs["adminStateUp"] = state ? state.adminStateUp : undefined;
            inputs["allTags"] = state ? state.allTags : undefined;
            inputs["availabilityZoneHints"] = state ? state.availabilityZoneHints : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["distributed"] = state ? state.distributed : undefined;
            inputs["enableSnat"] = state ? state.enableSnat : undefined;
            inputs["externalFixedIps"] = state ? state.externalFixedIps : undefined;
            inputs["externalGateway"] = state ? state.externalGateway : undefined;
            inputs["externalNetworkId"] = state ? state.externalNetworkId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
            inputs["vendorOptions"] = state ? state.vendorOptions : undefined;
        } else {
            const args = argsOrState as RouterArgs | undefined;
            inputs["adminStateUp"] = args ? args.adminStateUp : undefined;
            inputs["availabilityZoneHints"] = args ? args.availabilityZoneHints : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["distributed"] = args ? args.distributed : undefined;
            inputs["enableSnat"] = args ? args.enableSnat : undefined;
            inputs["externalFixedIps"] = args ? args.externalFixedIps : undefined;
            inputs["externalGateway"] = args ? args.externalGateway : undefined;
            inputs["externalNetworkId"] = args ? args.externalNetworkId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["vendorOptions"] = args ? args.vendorOptions : undefined;
            inputs["allTags"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Router.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Router resources.
 */
export interface RouterState {
    /**
     * Administrative up/down status for the router
     * (must be "true" or "false" if provided). Changing this updates the
     * `adminStateUp` of an existing router.
     */
    readonly adminStateUp?: pulumi.Input<boolean>;
    /**
     * The collection of tags assigned on the router, which have been
     * explicitly and implicitly added.
     */
    readonly allTags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * An availability zone is used to make 
     * network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
     * this creates a new router.
     */
    readonly availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Human-readable description for the router.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Indicates whether or not to create a
     * distributed router. The default policy setting in Neutron restricts
     * usage of this property to administrative users only.
     */
    readonly distributed?: pulumi.Input<boolean>;
    /**
     * Enable Source NAT for the router. Valid values are
     * "true" or "false". An `externalNetworkId` has to be set in order to
     * set this property. Changing this updates the `enableSnat` of the router.
     * Setting this value **requires** an **ext-gw-mode** extension to be enabled
     * in OpenStack Neutron.
     */
    readonly enableSnat?: pulumi.Input<boolean>;
    /**
     * An external fixed IP for the router. This
     * can be repeated. The structure is described below. An `externalNetworkId`
     * has to be set in order to set this property. Changing this updates the
     * external fixed IPs of the router.
     */
    readonly externalFixedIps?: pulumi.Input<pulumi.Input<inputs.networking.RouterExternalFixedIp>[]>;
    /**
     * The
     * network UUID of an external gateway for the router. A router with an
     * external gateway is required if any compute instances or load balancers
     * will be using floating IPs. Changing this updates the external gateway
     * of an existing router.
     *
     * @deprecated use external_network_id instead
     */
    readonly externalGateway?: pulumi.Input<string>;
    /**
     * The network UUID of an external gateway
     * for the router. A router with an external gateway is required if any
     * compute instances or load balancers will be using floating IPs. Changing
     * this updates the external gateway of the router.
     */
    readonly externalNetworkId?: pulumi.Input<string>;
    /**
     * A unique name for the router. Changing this
     * updates the `name` of an existing router.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of string tags for the router.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The owner of the floating IP. Required if admin wants
     * to create a router for another tenant. Changing this creates a new router.
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * Map of additional driver-specific options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
    /**
     * Map of additional vendor-specific options.
     * Supported options are described below.
     */
    readonly vendorOptions?: pulumi.Input<inputs.networking.RouterVendorOptions>;
}

/**
 * The set of arguments for constructing a Router resource.
 */
export interface RouterArgs {
    /**
     * Administrative up/down status for the router
     * (must be "true" or "false" if provided). Changing this updates the
     * `adminStateUp` of an existing router.
     */
    readonly adminStateUp?: pulumi.Input<boolean>;
    /**
     * An availability zone is used to make 
     * network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
     * this creates a new router.
     */
    readonly availabilityZoneHints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Human-readable description for the router.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Indicates whether or not to create a
     * distributed router. The default policy setting in Neutron restricts
     * usage of this property to administrative users only.
     */
    readonly distributed?: pulumi.Input<boolean>;
    /**
     * Enable Source NAT for the router. Valid values are
     * "true" or "false". An `externalNetworkId` has to be set in order to
     * set this property. Changing this updates the `enableSnat` of the router.
     * Setting this value **requires** an **ext-gw-mode** extension to be enabled
     * in OpenStack Neutron.
     */
    readonly enableSnat?: pulumi.Input<boolean>;
    /**
     * An external fixed IP for the router. This
     * can be repeated. The structure is described below. An `externalNetworkId`
     * has to be set in order to set this property. Changing this updates the
     * external fixed IPs of the router.
     */
    readonly externalFixedIps?: pulumi.Input<pulumi.Input<inputs.networking.RouterExternalFixedIp>[]>;
    /**
     * The
     * network UUID of an external gateway for the router. A router with an
     * external gateway is required if any compute instances or load balancers
     * will be using floating IPs. Changing this updates the external gateway
     * of an existing router.
     *
     * @deprecated use external_network_id instead
     */
    readonly externalGateway?: pulumi.Input<string>;
    /**
     * The network UUID of an external gateway
     * for the router. A router with an external gateway is required if any
     * compute instances or load balancers will be using floating IPs. Changing
     * this updates the external gateway of the router.
     */
    readonly externalNetworkId?: pulumi.Input<string>;
    /**
     * A unique name for the router. Changing this
     * updates the `name` of an existing router.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 networking client.
     * A networking client is needed to create a router. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * router.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of string tags for the router.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The owner of the floating IP. Required if admin wants
     * to create a router for another tenant. Changing this creates a new router.
     */
    readonly tenantId?: pulumi.Input<string>;
    /**
     * Map of additional driver-specific options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
    /**
     * Map of additional vendor-specific options.
     * Supported options are described below.
     */
    readonly vendorOptions?: pulumi.Input<inputs.networking.RouterVendorOptions>;
}
