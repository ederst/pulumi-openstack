// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V1 DB configuration resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ### Configuration
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const test = new openstack.database.Configuration("test", {
 *     configurations: [{
 *         name: "max_connections",
 *         value: "200",
 *     }],
 *     datastore: {
 *         type: "mysql",
 *         version: "mysql-5.7",
 *     },
 *     description: "description",
 * });
 * ```
 */
export class Configuration extends pulumi.CustomResource {
    /**
     * Get an existing Configuration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState, opts?: pulumi.CustomResourceOptions): Configuration {
        return new Configuration(name, <any>state, { ...opts, id: id });
    }

    /**
     * An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
     */
    public readonly configurations!: pulumi.Output<{ name: string, value: string }[] | undefined>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    public readonly datastore!: pulumi.Output<{ type: string, version: string }>;
    /**
     * Description of the resource.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * A unique name for the resource.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a Configuration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfigurationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConfigurationArgs | ConfigurationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ConfigurationState | undefined;
            inputs["configurations"] = state ? state.configurations : undefined;
            inputs["datastore"] = state ? state.datastore : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as ConfigurationArgs | undefined;
            if (!args || args.datastore === undefined) {
                throw new Error("Missing required property 'datastore'");
            }
            if (!args || args.description === undefined) {
                throw new Error("Missing required property 'description'");
            }
            inputs["configurations"] = args ? args.configurations : undefined;
            inputs["datastore"] = args ? args.datastore : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
        }
        super("openstack:database/configuration:Configuration", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Configuration resources.
 */
export interface ConfigurationState {
    /**
     * An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
     */
    readonly configurations?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, value: pulumi.Input<string> }>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    readonly datastore?: pulumi.Input<{ type: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * Description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A unique name for the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Configuration resource.
 */
export interface ConfigurationArgs {
    /**
     * An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
     */
    readonly configurations?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, value: pulumi.Input<string> }>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    readonly datastore: pulumi.Input<{ type: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * Description of the resource.
     */
    readonly description: pulumi.Input<string>;
    /**
     * A unique name for the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    readonly region?: pulumi.Input<string>;
}
