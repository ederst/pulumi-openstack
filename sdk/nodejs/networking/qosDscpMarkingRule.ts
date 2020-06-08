// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V2 Neutron QoS DSCP marking rule resource within OpenStack.
 *
 * ## Example Usage
 *
 * ### Create a QoS Policy with some DSCP marking rule
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const qosPolicy1 = new openstack.networking.QosPolicy("qosPolicy1", {
 *     description: "dscpMark",
 * });
 * const dscpMarkingRule1 = new openstack.networking.QosDscpMarkingRule("dscpMarkingRule1", {
 *     dscpMark: 26,
 *     qosPolicyId: qosPolicy1.id,
 * });
 * ```
 */
export class QosDscpMarkingRule extends pulumi.CustomResource {
    /**
     * Get an existing QosDscpMarkingRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QosDscpMarkingRuleState, opts?: pulumi.CustomResourceOptions): QosDscpMarkingRule {
        return new QosDscpMarkingRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:networking/qosDscpMarkingRule:QosDscpMarkingRule';

    /**
     * Returns true if the given object is an instance of QosDscpMarkingRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QosDscpMarkingRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QosDscpMarkingRule.__pulumiType;
    }

    /**
     * The value of DSCP mark. Changing this updates the DSCP mark value existing
     * QoS DSCP marking rule.
     */
    public readonly dscpMark!: pulumi.Output<number>;
    /**
     * The QoS policy reference. Changing this creates a new QoS DSCP marking rule.
     */
    public readonly qosPolicyId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new QoS DSCP marking rule.
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a QosDscpMarkingRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QosDscpMarkingRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: QosDscpMarkingRuleArgs | QosDscpMarkingRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as QosDscpMarkingRuleState | undefined;
            inputs["dscpMark"] = state ? state.dscpMark : undefined;
            inputs["qosPolicyId"] = state ? state.qosPolicyId : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as QosDscpMarkingRuleArgs | undefined;
            if (!args || args.dscpMark === undefined) {
                throw new Error("Missing required property 'dscpMark'");
            }
            if (!args || args.qosPolicyId === undefined) {
                throw new Error("Missing required property 'qosPolicyId'");
            }
            inputs["dscpMark"] = args ? args.dscpMark : undefined;
            inputs["qosPolicyId"] = args ? args.qosPolicyId : undefined;
            inputs["region"] = args ? args.region : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(QosDscpMarkingRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering QosDscpMarkingRule resources.
 */
export interface QosDscpMarkingRuleState {
    /**
     * The value of DSCP mark. Changing this updates the DSCP mark value existing
     * QoS DSCP marking rule.
     */
    readonly dscpMark?: pulumi.Input<number>;
    /**
     * The QoS policy reference. Changing this creates a new QoS DSCP marking rule.
     */
    readonly qosPolicyId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new QoS DSCP marking rule.
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a QosDscpMarkingRule resource.
 */
export interface QosDscpMarkingRuleArgs {
    /**
     * The value of DSCP mark. Changing this updates the DSCP mark value existing
     * QoS DSCP marking rule.
     */
    readonly dscpMark: pulumi.Input<number>;
    /**
     * The QoS policy reference. Changing this creates a new QoS DSCP marking rule.
     */
    readonly qosPolicyId: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Networking client.
     * A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new QoS DSCP marking rule.
     */
    readonly region?: pulumi.Input<string>;
}
