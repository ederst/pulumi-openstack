// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Manages a V1 DB configuration resource within OpenStack.
 *
 * ## Example Usage
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
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState, opts?: pulumi.CustomResourceOptions): Configuration {
        return new Configuration(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:database/configuration:Configuration';

    /**
     * Returns true if the given object is an instance of Configuration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Configuration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Configuration.__pulumiType;
    }

    /**
     * An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
     */
    public readonly configurations!: pulumi.Output<outputs.database.ConfigurationConfiguration[] | undefined>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    public readonly datastore!: pulumi.Output<outputs.database.ConfigurationDatastore>;
    /**
     * Description of the resource.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Configuration parameter name. Changing this creates a new resource.
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
            if ((!args || args.datastore === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'datastore'");
            }
            if ((!args || args.description === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'description'");
            }
            inputs["configurations"] = args ? args.configurations : undefined;
            inputs["datastore"] = args ? args.datastore : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Configuration.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Configuration resources.
 */
export interface ConfigurationState {
    /**
     * An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
     */
    readonly configurations?: pulumi.Input<pulumi.Input<inputs.database.ConfigurationConfiguration>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    readonly datastore?: pulumi.Input<inputs.database.ConfigurationDatastore>;
    /**
     * Description of the resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Configuration parameter name. Changing this creates a new resource.
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
    readonly configurations?: pulumi.Input<pulumi.Input<inputs.database.ConfigurationConfiguration>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates resource.
     */
    readonly datastore: pulumi.Input<inputs.database.ConfigurationDatastore>;
    /**
     * Description of the resource.
     */
    readonly description: pulumi.Input<string>;
    /**
     * Configuration parameter name. Changing this creates a new resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    readonly region?: pulumi.Input<string>;
}
