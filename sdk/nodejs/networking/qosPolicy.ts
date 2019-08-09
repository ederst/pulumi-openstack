// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 Neutron QoS policy resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ### Create a QoS Policy
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const qosPolicy1 = new openstack.networking.QosPolicy("qosPolicy1", {
 *     description: "bwLimit",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_qos_policy_v2.html.markdown.
 */
export class QosPolicy extends pulumi.CustomResource {
    /**
     * Get an existing QosPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QosPolicyState, opts?: pulumi.CustomResourceOptions): QosPolicy {
        return new QosPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:networking/qosPolicy:QosPolicy';

    /**
     * Returns true if the given object is an instance of QosPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QosPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QosPolicy.__pulumiType;
    }

    /**
     * The collection of tags assigned on the QoS policy, which have been
     * explicitly and implicitly added.
     */
    public /*out*/ readonly allTags!: pulumi.Output<string[]>;
    /**
     * The time at which QoS policy was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The human-readable description for the QoS policy.
     * Changing this updates the description of the existing QoS policy.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the QoS policy is default
     * QoS policy or not. Changing this updates the default status of the existing
     * QoS policy.
     */
    public readonly isDefault!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the QoS policy. Changing this updates the name of
     * the existing QoS policy.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The owner of the QoS policy. Required if admin wants to
     * create a QoS policy for another project. Changing this creates a new QoS policy.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron Qos policy. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * QoS policy.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The revision number of the QoS policy.
     */
    public /*out*/ readonly revisionNumber!: pulumi.Output<number>;
    /**
     * Indicates whether this QoS policy is shared across
     * all projects. Changing this updates the shared status of the existing
     * QoS policy.
     */
    public readonly shared!: pulumi.Output<boolean | undefined>;
    /**
     * A set of string tags for the QoS policy.
     */
    public readonly tags!: pulumi.Output<string[] | undefined>;
    /**
     * The time at which QoS policy was created.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;
    /**
     * Map of additional options.
     */
    public readonly valueSpecs!: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a QosPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: QosPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: QosPolicyArgs | QosPolicyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as QosPolicyState | undefined;
            inputs["allTags"] = state ? state.allTags : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["isDefault"] = state ? state.isDefault : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["revisionNumber"] = state ? state.revisionNumber : undefined;
            inputs["shared"] = state ? state.shared : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["updatedAt"] = state ? state.updatedAt : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
        } else {
            const args = argsOrState as QosPolicyArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["isDefault"] = args ? args.isDefault : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["shared"] = args ? args.shared : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["allTags"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["revisionNumber"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(QosPolicy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering QosPolicy resources.
 */
export interface QosPolicyState {
    /**
     * The collection of tags assigned on the QoS policy, which have been
     * explicitly and implicitly added.
     */
    readonly allTags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time at which QoS policy was created.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The human-readable description for the QoS policy.
     * Changing this updates the description of the existing QoS policy.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Indicates whether the QoS policy is default
     * QoS policy or not. Changing this updates the default status of the existing
     * QoS policy.
     */
    readonly isDefault?: pulumi.Input<boolean>;
    /**
     * The name of the QoS policy. Changing this updates the name of
     * the existing QoS policy.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The owner of the QoS policy. Required if admin wants to
     * create a QoS policy for another project. Changing this creates a new QoS policy.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron Qos policy. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * QoS policy.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The revision number of the QoS policy.
     */
    readonly revisionNumber?: pulumi.Input<number>;
    /**
     * Indicates whether this QoS policy is shared across
     * all projects. Changing this updates the shared status of the existing
     * QoS policy.
     */
    readonly shared?: pulumi.Input<boolean>;
    /**
     * A set of string tags for the QoS policy.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The time at which QoS policy was created.
     */
    readonly updatedAt?: pulumi.Input<string>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a QosPolicy resource.
 */
export interface QosPolicyArgs {
    /**
     * The human-readable description for the QoS policy.
     * Changing this updates the description of the existing QoS policy.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Indicates whether the QoS policy is default
     * QoS policy or not. Changing this updates the default status of the existing
     * QoS policy.
     */
    readonly isDefault?: pulumi.Input<boolean>;
    /**
     * The name of the QoS policy. Changing this updates the name of
     * the existing QoS policy.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The owner of the QoS policy. Required if admin wants to
     * create a QoS policy for another project. Changing this creates a new QoS policy.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron Qos policy. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * QoS policy.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * Indicates whether this QoS policy is shared across
     * all projects. Changing this updates the shared status of the existing
     * QoS policy.
     */
    readonly shared?: pulumi.Input<boolean>;
    /**
     * A set of string tags for the QoS policy.
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Map of additional options.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
}