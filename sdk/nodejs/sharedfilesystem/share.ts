// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to configure a share.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const network1 = new openstack.networking.Network("network_1", {
 *     adminStateUp: true,
 * });
 * const subnet1 = new openstack.networking.Subnet("subnet_1", {
 *     cidr: "192.168.199.0/24",
 *     ipVersion: 4,
 *     networkId: network1.id,
 * });
 * const sharenetwork1 = new openstack.sharedfilesystem.ShareNetwork("sharenetwork_1", {
 *     description: "test share network with security services",
 *     neutronNetId: network1.id,
 *     neutronSubnetId: subnet1.id,
 * });
 * const share1 = new openstack.sharedfilesystem.Share("share_1", {
 *     description: "test share description",
 *     shareNetworkId: sharenetwork1.id,
 *     shareProto: "NFS",
 *     size: 1,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_share_v2.html.markdown.
 */
export class Share extends pulumi.CustomResource {
    /**
     * Get an existing Share resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState, opts?: pulumi.CustomResourceOptions): Share {
        return new Share(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:sharedfilesystem/share:Share';

    /**
     * Returns true if the given object is an instance of Share.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Share {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Share.__pulumiType;
    }

    /**
     * The map of metadata, assigned on the share, which has been
     * explicitly and implicitly added.
     */
    public /*out*/ readonly allMetadata!: pulumi.Output<{[key: string]: any}>;
    /**
     * The share availability zone. Changing this creates a
     * new share.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * The human-readable description for the share.
     * Changing this updates the description of the existing share.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * A list of export locations. For example, when a share server
     * has more than one network interface, it can have multiple export locations.
     */
    public /*out*/ readonly exportLocations!: pulumi.Output<{ path: string, preferred: string }[]>;
    /**
     * Indicates whether a share has replicas or not.
     */
    public /*out*/ readonly hasReplicas!: pulumi.Output<boolean>;
    /**
     * The share host name.
     */
    public /*out*/ readonly host!: pulumi.Output<string>;
    /**
     * The level of visibility for the share. Set to true to make
     * share public. Set to false to make it private. Default value is false. Changing this
     * updates the existing share.
     */
    public readonly isPublic!: pulumi.Output<boolean | undefined>;
    /**
     * One or more metadata key and value pairs as a dictionary of
     * strings.
     */
    public readonly metadata!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The name of the share. Changing this updates the name
     * of the existing share.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The owner of the Share.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share. Changing this
     * creates a new share.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The share replication type.
     */
    public /*out*/ readonly replicationType!: pulumi.Output<string>;
    /**
     * The UUID of a share network where the share server exists
     * or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
     * the share_network_id value from the snapshot is used. Changing this creates a new share.
     */
    public readonly shareNetworkId!: pulumi.Output<string>;
    /**
     * The share protocol - can either be NFS, CIFS,
     * CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
     */
    public readonly shareProto!: pulumi.Output<string>;
    /**
     * The UUID of the share server.
     */
    public /*out*/ readonly shareServerId!: pulumi.Output<string>;
    /**
     * The share type name. If you omit this parameter, the default
     * share type is used.
     */
    public readonly shareType!: pulumi.Output<string>;
    /**
     * The share size, in GBs. The requested share size cannot be greater
     * than the allowed GB quota. Changing this resizes the existing share.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * The UUID of the share's base snapshot. Changing this creates
     * a new share.
     */
    public readonly snapshotId!: pulumi.Output<string | undefined>;

    /**
     * Create a Share resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareArgs | ShareState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ShareState | undefined;
            inputs["allMetadata"] = state ? state.allMetadata : undefined;
            inputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["exportLocations"] = state ? state.exportLocations : undefined;
            inputs["hasReplicas"] = state ? state.hasReplicas : undefined;
            inputs["host"] = state ? state.host : undefined;
            inputs["isPublic"] = state ? state.isPublic : undefined;
            inputs["metadata"] = state ? state.metadata : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["replicationType"] = state ? state.replicationType : undefined;
            inputs["shareNetworkId"] = state ? state.shareNetworkId : undefined;
            inputs["shareProto"] = state ? state.shareProto : undefined;
            inputs["shareServerId"] = state ? state.shareServerId : undefined;
            inputs["shareType"] = state ? state.shareType : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["snapshotId"] = state ? state.snapshotId : undefined;
        } else {
            const args = argsOrState as ShareArgs | undefined;
            if (!args || args.shareProto === undefined) {
                throw new Error("Missing required property 'shareProto'");
            }
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            inputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["isPublic"] = args ? args.isPublic : undefined;
            inputs["metadata"] = args ? args.metadata : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["shareNetworkId"] = args ? args.shareNetworkId : undefined;
            inputs["shareProto"] = args ? args.shareProto : undefined;
            inputs["shareType"] = args ? args.shareType : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["snapshotId"] = args ? args.snapshotId : undefined;
            inputs["allMetadata"] = undefined /*out*/;
            inputs["exportLocations"] = undefined /*out*/;
            inputs["hasReplicas"] = undefined /*out*/;
            inputs["host"] = undefined /*out*/;
            inputs["projectId"] = undefined /*out*/;
            inputs["replicationType"] = undefined /*out*/;
            inputs["shareServerId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Share.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Share resources.
 */
export interface ShareState {
    /**
     * The map of metadata, assigned on the share, which has been
     * explicitly and implicitly added.
     */
    readonly allMetadata?: pulumi.Input<{[key: string]: any}>;
    /**
     * The share availability zone. Changing this creates a
     * new share.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * The human-readable description for the share.
     * Changing this updates the description of the existing share.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * A list of export locations. For example, when a share server
     * has more than one network interface, it can have multiple export locations.
     */
    readonly exportLocations?: pulumi.Input<pulumi.Input<{ path?: pulumi.Input<string>, preferred?: pulumi.Input<string> }>[]>;
    /**
     * Indicates whether a share has replicas or not.
     */
    readonly hasReplicas?: pulumi.Input<boolean>;
    /**
     * The share host name.
     */
    readonly host?: pulumi.Input<string>;
    /**
     * The level of visibility for the share. Set to true to make
     * share public. Set to false to make it private. Default value is false. Changing this
     * updates the existing share.
     */
    readonly isPublic?: pulumi.Input<boolean>;
    /**
     * One or more metadata key and value pairs as a dictionary of
     * strings.
     */
    readonly metadata?: pulumi.Input<{[key: string]: any}>;
    /**
     * The name of the share. Changing this updates the name
     * of the existing share.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The owner of the Share.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share. Changing this
     * creates a new share.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The share replication type.
     */
    readonly replicationType?: pulumi.Input<string>;
    /**
     * The UUID of a share network where the share server exists
     * or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
     * the share_network_id value from the snapshot is used. Changing this creates a new share.
     */
    readonly shareNetworkId?: pulumi.Input<string>;
    /**
     * The share protocol - can either be NFS, CIFS,
     * CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
     */
    readonly shareProto?: pulumi.Input<string>;
    /**
     * The UUID of the share server.
     */
    readonly shareServerId?: pulumi.Input<string>;
    /**
     * The share type name. If you omit this parameter, the default
     * share type is used.
     */
    readonly shareType?: pulumi.Input<string>;
    /**
     * The share size, in GBs. The requested share size cannot be greater
     * than the allowed GB quota. Changing this resizes the existing share.
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The UUID of the share's base snapshot. Changing this creates
     * a new share.
     */
    readonly snapshotId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Share resource.
 */
export interface ShareArgs {
    /**
     * The share availability zone. Changing this creates a
     * new share.
     */
    readonly availabilityZone?: pulumi.Input<string>;
    /**
     * The human-readable description for the share.
     * Changing this updates the description of the existing share.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The level of visibility for the share. Set to true to make
     * share public. Set to false to make it private. Default value is false. Changing this
     * updates the existing share.
     */
    readonly isPublic?: pulumi.Input<boolean>;
    /**
     * One or more metadata key and value pairs as a dictionary of
     * strings.
     */
    readonly metadata?: pulumi.Input<{[key: string]: any}>;
    /**
     * The name of the share. Changing this updates the name
     * of the existing share.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a share. Changing this
     * creates a new share.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The UUID of a share network where the share server exists
     * or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
     * the share_network_id value from the snapshot is used. Changing this creates a new share.
     */
    readonly shareNetworkId?: pulumi.Input<string>;
    /**
     * The share protocol - can either be NFS, CIFS,
     * CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
     */
    readonly shareProto: pulumi.Input<string>;
    /**
     * The share type name. If you omit this parameter, the default
     * share type is used.
     */
    readonly shareType?: pulumi.Input<string>;
    /**
     * The share size, in GBs. The requested share size cannot be greater
     * than the allowed GB quota. Changing this resizes the existing share.
     */
    readonly size: pulumi.Input<number>;
    /**
     * The UUID of the share's base snapshot. Changing this creates
     * a new share.
     */
    readonly snapshotId?: pulumi.Input<string>;
}
