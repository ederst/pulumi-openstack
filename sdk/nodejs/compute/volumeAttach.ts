// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Attaches a Block Storage Volume to an Instance using the OpenStack
 * Compute (Nova) v2 API.
 * 
 * ## Example Usage
 * 
 * ### Basic attachment of a single volume to a single instance
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volume1 = new openstack.blockstorage.VolumeV2("volume1", {
 *     size: 1,
 * });
 * const instance1 = new openstack.compute.Instance("instance1", {
 *     securityGroups: ["default"],
 * });
 * const va1 = new openstack.compute.VolumeAttach("va1", {
 *     instanceId: instance1.id,
 *     volumeId: volume1.id,
 * });
 * ```
 * 
 * ### Attaching multiple volumes to a single instance
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volumes: openstack.blockstorage.VolumeV2[] = [];
 * for (let i = 0; i < 2; i++) {
 *     volumes.push(new openstack.blockstorage.VolumeV2(`volumes-${i}`, {
 *         size: 1,
 *     }));
 * }
 * const instance1 = new openstack.compute.Instance("instance1", {
 *     securityGroups: ["default"],
 * });
 * const attachments: openstack.compute.VolumeAttach[] = [];
 * for (let i = 0; i < 2; i++) {
 *     attachments.push(new openstack.compute.VolumeAttach(`attachments-${i}`, {
 *         instanceId: instance1.id,
 *         volumeId: pulumi.all(volumes.map(v => v.id)).apply(id => id.map(v => v)[i]),
 *     }));
 * }
 * 
 * export const volumeDevices = attachments.map(v => v.device);
 * ```
 * 
 * Note that the above example will not guarantee that the volumes are attached in
 * a deterministic manner. The volumes will be attached in a seemingly random
 * order.
 * 
 * If you want to ensure that the volumes are attached in a given order, create
 * explicit dependencies between the volumes, such as:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volumes: openstack.blockstorage.VolumeV2[] = [];
 * for (let i = 0; i < 2; i++) {
 *     volumes.push(new openstack.blockstorage.VolumeV2(`volumes-${i}`, {
 *         size: 1,
 *     }));
 * }
 * const instance1 = new openstack.compute.Instance("instance1", {
 *     securityGroups: ["default"],
 * });
 * const attach1 = new openstack.compute.VolumeAttach("attach1", {
 *     instanceId: instance1.id,
 *     volumeId: volumes[0].id,
 * });
 * const attach2 = new openstack.compute.VolumeAttach("attach2", {
 *     instanceId: instance1.id,
 *     volumeId: volumes[1].id,
 * }, {dependsOn: [attach1]});
 * 
 * export const volumeDevices = openstack_compute_volume_attach_v2_attachments.map(v => v.device);
 * ```
 * 
 * ### Using Multiattach-enabled volumes
 * 
 * Multiattach Volumes are dependent upon your OpenStack cloud and not all
 * clouds support multiattach.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const volume1 = new openstack.blockstorage.Volume("volume1", {
 *     multiattach: true,
 *     size: 1,
 * });
 * const instance1 = new openstack.compute.Instance("instance1", {
 *     securityGroups: ["default"],
 * });
 * const instance2 = new openstack.compute.Instance("instance2", {
 *     securityGroups: ["default"],
 * });
 * const va1 = new openstack.compute.VolumeAttach("va1", {
 *     instanceId: instance1.id,
 *     multiattach: true,
 *     volumeId: openstack_blockstorage_volume_v2_volume_1.id,
 * });
 * const va2 = new openstack.compute.VolumeAttach("va2", {
 *     instanceId: instance2.id,
 *     multiattach: true,
 *     volumeId: openstack_blockstorage_volume_v2_volume_1.id,
 * }, {dependsOn: [va1]});
 * ```
 * 
 * It is recommended to use `dependsOn` for the attach resources
 * to enforce the volume attachments to happen one at a time.
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_volume_attach_v2.html.markdown.
 */
export class VolumeAttach extends pulumi.CustomResource {
    /**
     * Get an existing VolumeAttach resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeAttachState, opts?: pulumi.CustomResourceOptions): VolumeAttach {
        return new VolumeAttach(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:compute/volumeAttach:VolumeAttach';

    /**
     * Returns true if the given object is an instance of VolumeAttach.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VolumeAttach {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VolumeAttach.__pulumiType;
    }

    /**
     * See Argument Reference above. _NOTE_: The correctness of this
     * information is dependent upon the hypervisor in use. In some cases, this
     * should not be used as an authoritative piece of information.
     */
    public readonly device!: pulumi.Output<string>;
    /**
     * The ID of the Instance to attach the Volume to.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * Enable attachment of multiattach-capable volumes.
     */
    public readonly multiattach!: pulumi.Output<boolean | undefined>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a volume attachment. If omitted, the
     * `region` argument of the provider is used. Changing this creates a
     * new volume attachment.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The ID of the Volume to attach to an Instance.
     */
    public readonly volumeId!: pulumi.Output<string>;

    /**
     * Create a VolumeAttach resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeAttachArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeAttachArgs | VolumeAttachState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VolumeAttachState | undefined;
            inputs["device"] = state ? state.device : undefined;
            inputs["instanceId"] = state ? state.instanceId : undefined;
            inputs["multiattach"] = state ? state.multiattach : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["volumeId"] = state ? state.volumeId : undefined;
        } else {
            const args = argsOrState as VolumeAttachArgs | undefined;
            if (!args || args.instanceId === undefined) {
                throw new Error("Missing required property 'instanceId'");
            }
            if (!args || args.volumeId === undefined) {
                throw new Error("Missing required property 'volumeId'");
            }
            inputs["device"] = args ? args.device : undefined;
            inputs["instanceId"] = args ? args.instanceId : undefined;
            inputs["multiattach"] = args ? args.multiattach : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["volumeId"] = args ? args.volumeId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(VolumeAttach.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VolumeAttach resources.
 */
export interface VolumeAttachState {
    /**
     * See Argument Reference above. _NOTE_: The correctness of this
     * information is dependent upon the hypervisor in use. In some cases, this
     * should not be used as an authoritative piece of information.
     */
    readonly device?: pulumi.Input<string>;
    /**
     * The ID of the Instance to attach the Volume to.
     */
    readonly instanceId?: pulumi.Input<string>;
    /**
     * Enable attachment of multiattach-capable volumes.
     */
    readonly multiattach?: pulumi.Input<boolean>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a volume attachment. If omitted, the
     * `region` argument of the provider is used. Changing this creates a
     * new volume attachment.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The ID of the Volume to attach to an Instance.
     */
    readonly volumeId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VolumeAttach resource.
 */
export interface VolumeAttachArgs {
    /**
     * See Argument Reference above. _NOTE_: The correctness of this
     * information is dependent upon the hypervisor in use. In some cases, this
     * should not be used as an authoritative piece of information.
     */
    readonly device?: pulumi.Input<string>;
    /**
     * The ID of the Instance to attach the Volume to.
     */
    readonly instanceId: pulumi.Input<string>;
    /**
     * Enable attachment of multiattach-capable volumes.
     */
    readonly multiattach?: pulumi.Input<boolean>;
    /**
     * The region in which to obtain the V2 Compute client.
     * A Compute client is needed to create a volume attachment. If omitted, the
     * `region` argument of the provider is used. Changing this creates a
     * new volume attachment.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The ID of the Volume to attach to an Instance.
     */
    readonly volumeId: pulumi.Input<string>;
}
