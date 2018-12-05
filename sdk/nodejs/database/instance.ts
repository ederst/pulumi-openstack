// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V1 DB instance resource within OpenStack.
 */
export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /**
     * Configuration ID to be attached to the instance. Database instance
     * will be rebooted when configuration is detached.
     */
    public readonly configurationId: pulumi.Output<string | undefined>;
    /**
     * An array of database name, charset and collate. The database
     * object structure is documented below.
     */
    public readonly databases: pulumi.Output<{ charset?: string, collate?: string, name: string }[] | undefined>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates a new instance.
     */
    public readonly datastore: pulumi.Output<{ type: string, version: string }>;
    /**
     * The flavor ID of the desired flavor for the instance.
     * Changing this creates new instance.
     */
    public readonly flavorId: pulumi.Output<string>;
    /**
     * A unique name for the resource.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * An array of one or more networks to attach to the
     * instance. The network object structure is documented below. Changing this
     * creates a new instance.
     */
    public readonly networks: pulumi.Output<{ fixedIpV4?: string, fixedIpV6?: string, port?: string, uuid?: string }[] | undefined>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    public readonly region: pulumi.Output<string>;
    /**
     * Specifies the volume size in GB. Changing this creates new instance.
     */
    public readonly size: pulumi.Output<number>;
    /**
     * An array of username, password, host and databases. The user
     * object structure is documented below.
     */
    public readonly users: pulumi.Output<{ databases?: string[], host?: string, name: string, password?: string }[] | undefined>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: InstanceState = argsOrState as InstanceState | undefined;
            inputs["configurationId"] = state ? state.configurationId : undefined;
            inputs["databases"] = state ? state.databases : undefined;
            inputs["datastore"] = state ? state.datastore : undefined;
            inputs["flavorId"] = state ? state.flavorId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networks"] = state ? state.networks : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            if (!args || args.datastore === undefined) {
                throw new Error("Missing required property 'datastore'");
            }
            if (!args || args.region === undefined) {
                throw new Error("Missing required property 'region'");
            }
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            inputs["configurationId"] = args ? args.configurationId : undefined;
            inputs["databases"] = args ? args.databases : undefined;
            inputs["datastore"] = args ? args.datastore : undefined;
            inputs["flavorId"] = args ? args.flavorId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networks"] = args ? args.networks : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["users"] = args ? args.users : undefined;
        }
        super("openstack:database/instance:Instance", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * Configuration ID to be attached to the instance. Database instance
     * will be rebooted when configuration is detached.
     */
    readonly configurationId?: pulumi.Input<string>;
    /**
     * An array of database name, charset and collate. The database
     * object structure is documented below.
     */
    readonly databases?: pulumi.Input<pulumi.Input<{ charset?: pulumi.Input<string>, collate?: pulumi.Input<string>, name: pulumi.Input<string> }>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates a new instance.
     */
    readonly datastore?: pulumi.Input<{ type: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * The flavor ID of the desired flavor for the instance.
     * Changing this creates new instance.
     */
    readonly flavorId?: pulumi.Input<string>;
    /**
     * A unique name for the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An array of one or more networks to attach to the
     * instance. The network object structure is documented below. Changing this
     * creates a new instance.
     */
    readonly networks?: pulumi.Input<pulumi.Input<{ fixedIpV4?: pulumi.Input<string>, fixedIpV6?: pulumi.Input<string>, port?: pulumi.Input<string>, uuid?: pulumi.Input<string> }>[]>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * Specifies the volume size in GB. Changing this creates new instance.
     */
    readonly size?: pulumi.Input<number>;
    /**
     * An array of username, password, host and databases. The user
     * object structure is documented below.
     */
    readonly users?: pulumi.Input<pulumi.Input<{ databases?: pulumi.Input<pulumi.Input<string>[]>, host?: pulumi.Input<string>, name: pulumi.Input<string>, password?: pulumi.Input<string> }>[]>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * Configuration ID to be attached to the instance. Database instance
     * will be rebooted when configuration is detached.
     */
    readonly configurationId?: pulumi.Input<string>;
    /**
     * An array of database name, charset and collate. The database
     * object structure is documented below.
     */
    readonly databases?: pulumi.Input<pulumi.Input<{ charset?: pulumi.Input<string>, collate?: pulumi.Input<string>, name: pulumi.Input<string> }>[]>;
    /**
     * An array of database engine type and version. The datastore
     * object structure is documented below. Changing this creates a new instance.
     */
    readonly datastore: pulumi.Input<{ type: pulumi.Input<string>, version: pulumi.Input<string> }>;
    /**
     * The flavor ID of the desired flavor for the instance.
     * Changing this creates new instance.
     */
    readonly flavorId?: pulumi.Input<string>;
    /**
     * A unique name for the resource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * An array of one or more networks to attach to the
     * instance. The network object structure is documented below. Changing this
     * creates a new instance.
     */
    readonly networks?: pulumi.Input<pulumi.Input<{ fixedIpV4?: pulumi.Input<string>, fixedIpV6?: pulumi.Input<string>, port?: pulumi.Input<string>, uuid?: pulumi.Input<string> }>[]>;
    /**
     * The region in which to create the db instance. Changing this
     * creates a new instance.
     */
    readonly region: pulumi.Input<string>;
    /**
     * Specifies the volume size in GB. Changing this creates new instance.
     */
    readonly size: pulumi.Input<number>;
    /**
     * An array of username, password, host and databases. The user
     * object structure is documented below.
     */
    readonly users?: pulumi.Input<pulumi.Input<{ databases?: pulumi.Input<pulumi.Input<string>[]>, host?: pulumi.Input<string>, name: pulumi.Input<string>, password?: pulumi.Input<string> }>[]>;
}
