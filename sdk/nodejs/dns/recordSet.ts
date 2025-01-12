// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a DNS record set in the OpenStack DNS Service.
 *
 * ## Example Usage
 * ### Automatically detect the correct network
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const exampleZone = new openstack.dns.Zone("example_zone", {
 *     description: "a zone",
 *     email: "email2@example.com",
 *     ttl: 6000,
 *     type: "PRIMARY",
 * });
 * const rsExampleCom = new openstack.dns.RecordSet("rs_example_com", {
 *     description: "An example record set",
 *     records: ["10.0.0.1"],
 *     ttl: 3000,
 *     type: "A",
 *     zoneId: exampleZone.id,
 * });
 * ```
 *
 * ## Import
 *
 * This resource can be imported by specifying the zone ID and recordset ID, separated by a forward slash.
 *
 * ```sh
 *  $ pulumi import openstack:dns/recordSet:RecordSet recordset_1 <zone_id>/<recordset_id>
 * ```
 */
export class RecordSet extends pulumi.CustomResource {
    /**
     * Get an existing RecordSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RecordSetState, opts?: pulumi.CustomResourceOptions): RecordSet {
        return new RecordSet(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:dns/recordSet:RecordSet';

    /**
     * Returns true if the given object is an instance of RecordSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RecordSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RecordSet.__pulumiType;
    }

    /**
     * A description of the  record set.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the record set. Note the `.` at the end of the name.
     * Changing this creates a new DNS  record set.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * An array of DNS records. _Note:_ if an IPv6 address
     * contains brackets (`[ ]`), the brackets will be stripped and the modified
     * address will be recorded in the state.
     */
    public readonly records!: pulumi.Output<string[] | undefined>;
    /**
     * The region in which to obtain the V2 DNS client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new DNS  record set.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The time to live (TTL) of the record set.
     */
    public readonly ttl!: pulumi.Output<number>;
    /**
     * The type of record set. Examples: "A", "MX".
     * Changing this creates a new DNS  record set.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Map of additional options. Changing this creates a
     * new record set.
     */
    public readonly valueSpecs!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The ID of the zone in which to create the record set.
     * Changing this creates a new DNS  record set.
     */
    public readonly zoneId!: pulumi.Output<string>;

    /**
     * Create a RecordSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RecordSetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RecordSetArgs | RecordSetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RecordSetState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["records"] = state ? state.records : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["ttl"] = state ? state.ttl : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
            inputs["zoneId"] = state ? state.zoneId : undefined;
        } else {
            const args = argsOrState as RecordSetArgs | undefined;
            if ((!args || args.zoneId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'zoneId'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["records"] = args ? args.records : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["ttl"] = args ? args.ttl : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["zoneId"] = args ? args.zoneId : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(RecordSet.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RecordSet resources.
 */
export interface RecordSetState {
    /**
     * A description of the  record set.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the record set. Note the `.` at the end of the name.
     * Changing this creates a new DNS  record set.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An array of DNS records. _Note:_ if an IPv6 address
     * contains brackets (`[ ]`), the brackets will be stripped and the modified
     * address will be recorded in the state.
     */
    readonly records?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region in which to obtain the V2 DNS client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new DNS  record set.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The time to live (TTL) of the record set.
     */
    readonly ttl?: pulumi.Input<number>;
    /**
     * The type of record set. Examples: "A", "MX".
     * Changing this creates a new DNS  record set.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * Map of additional options. Changing this creates a
     * new record set.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
    /**
     * The ID of the zone in which to create the record set.
     * Changing this creates a new DNS  record set.
     */
    readonly zoneId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RecordSet resource.
 */
export interface RecordSetArgs {
    /**
     * A description of the  record set.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the record set. Note the `.` at the end of the name.
     * Changing this creates a new DNS  record set.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An array of DNS records. _Note:_ if an IPv6 address
     * contains brackets (`[ ]`), the brackets will be stripped and the modified
     * address will be recorded in the state.
     */
    readonly records?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The region in which to obtain the V2 DNS client.
     * If omitted, the `region` argument of the provider is used.
     * Changing this creates a new DNS  record set.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The time to live (TTL) of the record set.
     */
    readonly ttl?: pulumi.Input<number>;
    /**
     * The type of record set. Examples: "A", "MX".
     * Changing this creates a new DNS  record set.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * Map of additional options. Changing this creates a
     * new record set.
     */
    readonly valueSpecs?: pulumi.Input<{[key: string]: any}>;
    /**
     * The ID of the zone in which to create the record set.
     * Changing this creates a new DNS  record set.
     */
    readonly zoneId: pulumi.Input<string>;
}
