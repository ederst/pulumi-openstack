// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages memberships status for the shared OpenStack Glance V2 Image within the
 * destination project, which has a member proposal.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 *
 * const rancheros = pulumi.output(openstack.images.getImage({
 *     memberStatus: "all",
 *     name: "RancherOS",
 *     visibility: "shared",
 * }, { async: true }));
 * const rancherosMember = new openstack.images.ImageAccessAccept("rancherosMember", {
 *     imageId: rancheros.id,
 *     status: "accepted",
 * });
 * ```
 */
export class ImageAccessAccept extends pulumi.CustomResource {
    /**
     * Get an existing ImageAccessAccept resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ImageAccessAcceptState, opts?: pulumi.CustomResourceOptions): ImageAccessAccept {
        return new ImageAccessAccept(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:images/imageAccessAccept:ImageAccessAccept';

    /**
     * Returns true if the given object is an instance of ImageAccessAccept.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ImageAccessAccept {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ImageAccessAccept.__pulumiType;
    }

    /**
     * The date the image membership was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The proposed image ID.
     */
    public readonly imageId!: pulumi.Output<string>;
    /**
     * The member ID, e.g. the target project ID. Optional
     * for admin accounts. Defaults to the current scope project ID.
     */
    public readonly memberId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Glance client.
     * A Glance client is needed to manage Image memberships. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * membership.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The membership schema.
     */
    public /*out*/ readonly schema!: pulumi.Output<string>;
    /**
     * The membership proposal status. Can either be
     * `accepted`, `rejected` or `pending`.
     */
    public readonly status!: pulumi.Output<string>;
    /**
     * The date the image membership was last updated.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a ImageAccessAccept resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ImageAccessAcceptArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ImageAccessAcceptArgs | ImageAccessAcceptState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ImageAccessAcceptState | undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["imageId"] = state ? state.imageId : undefined;
            inputs["memberId"] = state ? state.memberId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["schema"] = state ? state.schema : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as ImageAccessAcceptArgs | undefined;
            if (!args || args.imageId === undefined) {
                throw new Error("Missing required property 'imageId'");
            }
            if (!args || args.status === undefined) {
                throw new Error("Missing required property 'status'");
            }
            inputs["imageId"] = args ? args.imageId : undefined;
            inputs["memberId"] = args ? args.memberId : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["status"] = args ? args.status : undefined;
            inputs["createdAt"] = undefined /*out*/;
            inputs["schema"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ImageAccessAccept.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ImageAccessAccept resources.
 */
export interface ImageAccessAcceptState {
    /**
     * The date the image membership was created.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The proposed image ID.
     */
    readonly imageId?: pulumi.Input<string>;
    /**
     * The member ID, e.g. the target project ID. Optional
     * for admin accounts. Defaults to the current scope project ID.
     */
    readonly memberId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Glance client.
     * A Glance client is needed to manage Image memberships. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * membership.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The membership schema.
     */
    readonly schema?: pulumi.Input<string>;
    /**
     * The membership proposal status. Can either be
     * `accepted`, `rejected` or `pending`.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The date the image membership was last updated.
     */
    readonly updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ImageAccessAccept resource.
 */
export interface ImageAccessAcceptArgs {
    /**
     * The proposed image ID.
     */
    readonly imageId: pulumi.Input<string>;
    /**
     * The member ID, e.g. the target project ID. Optional
     * for admin accounts. Defaults to the current scope project ID.
     */
    readonly memberId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Glance client.
     * A Glance client is needed to manage Image memberships. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * membership.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The membership proposal status. Can either be
     * `accepted`, `rejected` or `pending`.
     */
    readonly status: pulumi.Input<string>;
}
