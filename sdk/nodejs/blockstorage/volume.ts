// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a V3 volume resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volume1 = new openstack.blockstorage.Volume("volume1", {
 *     description: "first test volume",
 *     region: "RegionOne",
 *     size: 3,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v3.html.markdown.
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState, opts?: pulumi.CustomResourceOptions): Volume {
        return new Volume(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:blockstorage/volume:Volume';

    /**
     * Returns true if the given object is an instance of Volume.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Volume {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Volume.__pulumiType;
    }

    /**
     * If a volume is attached to an instance, this attribute will
     * display the Attachment ID, Instance ID, and the Device as the Instance
     * sees it.
     */
    public /*out*/ readonly attachments!: pulumi.Output<{ device: string, id: string, instanceId: string }[]>;
    /**
     * The availability zone for the volume.
     * Changing this creates a new volume.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * The consistency group to place the volume
     * in.
     */
    public readonly consistencyGroupId!: pulumi.Output<string | undefined>;
    /**
     * A description of the volume. Changing this updates
     * the volume's description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * When this option is set it allows extending
     * attached volumes. Note: updating size of an attached volume requires Cinder
     * support for version 3.42 and a compatible storage driver.
     */
    public readonly enableOnlineResize!: pulumi.Output<boolean | undefined>;
    /**
     * The image ID from which to create the volume.
     * Changing this creates a new volume.
     */
    public readonly imageId!: pulumi.Output<string | undefined>;
    /**
     * Metadata key/value pairs to associate with the volume.
     * Changing this updates the existing volume metadata.
     */
    public readonly metadata!: pulumi.Output<{[key: string]: any}>;
    /**
     * Allow the volume to be attached to more than one Compute instance.
     */
    public readonly multiattach!: pulumi.Output<boolean | undefined>;
    /**
     * A unique name for the volume. Changing this updates the
     * volume's name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The region in which to create the volume. If
     * omitted, the `region` argument of the provider is used. Changing this
     * creates a new volume.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The size of the volume to create (in gigabytes).
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * The snapshot ID from which to create the volume.
     * Changing this creates a new volume.
     */
    public readonly snapshotId!: pulumi.Output<string | undefined>;
    /**
     * The volume ID to replicate with.
     */
    public readonly sourceReplica!: pulumi.Output<string | undefined>;
    /**
     * The volume ID from which to create the volume.
     * Changing this creates a new volume.
     */
    public readonly sourceVolId!: pulumi.Output<string | undefined>;
    /**
     * The type of volume to create.
     * Changing this creates a new volume.
     */
    public readonly volumeType!: pulumi.Output<string>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeArgs | VolumeState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VolumeState | undefined;
            inputs["attachments"] = state ? state.attachments : undefined;
            inputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            inputs["consistencyGroupId"] = state ? state.consistencyGroupId : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enableOnlineResize"] = state ? state.enableOnlineResize : undefined;
            inputs["imageId"] = state ? state.imageId : undefined;
            inputs["metadata"] = state ? state.metadata : undefined;
            inputs["multiattach"] = state ? state.multiattach : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["snapshotId"] = state ? state.snapshotId : undefined;
            inputs["sourceReplica"] = state ? state.sourceReplica : undefined;
            inputs["sourceVolId"] = state ? state.sourceVolId : undefined;
            inputs["volumeType"] = state ? state.volumeType : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            inputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            inputs["consistencyGroupId"] = args ? args.consistencyGroupId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enableOnlineResize"] = args ? args.enableOnlineResize : undefined;
            inputs["imageId"] = args ? args.imageId : undefined;
            inputs["metadata"] = args ? args.metadata : undefined;
            inputs["multiattach"] = args ? args.multiattach : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["snapshotId"] = args ? args.snapshotId : undefined;
            inputs["sourceReplica"] = args ? args.sourceReplica : undefined;
            inputs["sourceVolId"] = args ? args.sourceVolId : undefined;
            inputs["volumeType"] = args ? args.volumeType : undefined;
            inputs["attachments"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Volume.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    /**
     * If a volume is attached to an instance, this attribute will
     * display the Attachment ID, Instance ID, and the Device as the Instance
     * sees it.
     */
    readonly attachments?: pulumi.Input<pulumi.Input<{ device?: pulumi.Input<string>, id?: pulumi.Input<string>, instanceId?: pulumi.Input<string> }>[]>;
    /**
     * The availability zone for the volume.
     * Changing this creates a new volume.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * The consistency group to place the volume
     * in.
     */
    readonly consistencyGroupId?: pulumi.Input<string>;
    /**
     * A description of the volume. Changing this updates
     * the volume's description.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * When this option is set it allows extending
     * attached volumes. Note: updating size of an attached volume requires Cinder
     * support for version 3.42 and a compatible storage driver.
     */
    readonly enableOnlineResize?: pulumi.Input<boolean>;
    /**
     * The image ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly imageId?: pulumi.Input<string>;
    /**
     * Metadata key/value pairs to associate with the volume.
     * Changing this updates the existing volume metadata.
     */
    readonly metadata?: pulumi.Input<{[key: string]: any}>;
    /**
     * Allow the volume to be attached to more than one Compute instance.
     */
    readonly multiattach?: pulumi.Input<boolean>;
    /**
     * A unique name for the volume. Changing this updates the
     * volume's name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to create the volume. If
     * omitted, the `region` argument of the provider is used. Changing this
     * creates a new volume.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The size of the volume to create (in gigabytes).
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The snapshot ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly snapshotId?: pulumi.Input<string>;
    /**
     * The volume ID to replicate with.
     */
    readonly sourceReplica?: pulumi.Input<string>;
    /**
     * The volume ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly sourceVolId?: pulumi.Input<string>;
    /**
     * The type of volume to create.
     * Changing this creates a new volume.
     */
    readonly volumeType?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    /**
     * The availability zone for the volume.
     * Changing this creates a new volume.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * The consistency group to place the volume
     * in.
     */
    readonly consistencyGroupId?: pulumi.Input<string>;
    /**
     * A description of the volume. Changing this updates
     * the volume's description.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * When this option is set it allows extending
     * attached volumes. Note: updating size of an attached volume requires Cinder
     * support for version 3.42 and a compatible storage driver.
     */
    readonly enableOnlineResize?: pulumi.Input<boolean>;
    /**
     * The image ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly imageId?: pulumi.Input<string>;
    /**
     * Metadata key/value pairs to associate with the volume.
     * Changing this updates the existing volume metadata.
     */
    readonly metadata?: pulumi.Input<{[key: string]: any}>;
    /**
     * Allow the volume to be attached to more than one Compute instance.
     */
    readonly multiattach?: pulumi.Input<boolean>;
    /**
     * A unique name for the volume. Changing this updates the
     * volume's name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to create the volume. If
     * omitted, the `region` argument of the provider is used. Changing this
     * creates a new volume.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The size of the volume to create (in gigabytes).
     */
    readonly size: pulumi.Input<number>;
    /**
     * The snapshot ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly snapshotId?: pulumi.Input<string>;
    /**
     * The volume ID to replicate with.
     */
    readonly sourceReplica?: pulumi.Input<string>;
    /**
     * The volume ID from which to create the volume.
     * Changing this creates a new volume.
     */
    readonly sourceVolId?: pulumi.Input<string>;
    /**
     * The type of volume to create.
     * Changing this creates a new volume.
     */
    readonly volumeType?: pulumi.Input<string>;
}
