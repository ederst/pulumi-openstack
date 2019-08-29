// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a V1 Barbican container resource within OpenStack.
 * 
 * ## Example Usage
 * 
 * The container with the TLS certificates, which can be used by the loadbalancer HTTPS listener.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const subnet1 = openstack.networking.getSubnet({
 *     name: "my-subnet",
 * });
 * const certificate1 = new openstack.keymanager.SecretV1("certificate1", {
 *     payload: fs.readFileSync("cert.pem", "utf-8"),
 *     payloadContentType: "text/plain",
 *     secretType: "certificate",
 * });
 * const intermediate1 = new openstack.keymanager.SecretV1("intermediate1", {
 *     payload: fs.readFileSync("intermediate-ca.pem", "utf-8"),
 *     payloadContentType: "text/plain",
 *     secretType: "certificate",
 * });
 * const privateKey1 = new openstack.keymanager.SecretV1("privateKey1", {
 *     payload: fs.readFileSync("cert-key.pem", "utf-8"),
 *     payloadContentType: "text/plain",
 *     secretType: "private",
 * });
 * const tls1 = new openstack.keymanager.ContainerV1("tls1", {
 *     secretRefs: [
 *         {
 *             name: "certificate",
 *             secretRef: certificate1.secretRef,
 *         },
 *         {
 *             name: "privateKey",
 *             secretRef: privateKey1.secretRef,
 *         },
 *         {
 *             name: "intermediates",
 *             secretRef: intermediate1.secretRef,
 *         },
 *     ],
 *     type: "certificate",
 * });
 * const lb1 = new openstack.loadbalancer.LoadBalancer("lb1", {
 *     vipSubnetId: subnet1.id,
 * });
 * const listener1 = new openstack.loadbalancer.Listener("listener1", {
 *     defaultTlsContainerRef: tls1.containerRef,
 *     loadbalancerId: lb1.id,
 *     protocol: "TERMINATED_HTTPS",
 *     protocolPort: 443,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown.
 */
export class ContainerV1 extends pulumi.CustomResource {
    /**
     * Get an existing ContainerV1 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerV1State, opts?: pulumi.CustomResourceOptions): ContainerV1 {
        return new ContainerV1(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:keymanager/containerV1:ContainerV1';

    /**
     * Returns true if the given object is an instance of ContainerV1.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContainerV1 {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContainerV1.__pulumiType;
    }

    /**
     * The list of the container consumers. The structure is described below.
     */
    public /*out*/ readonly consumers!: pulumi.Output<outputs.keymanager.ContainerV1Consumer[]>;
    /**
     * The container reference / where to find the container.
     */
    public /*out*/ readonly containerRef!: pulumi.Output<string>;
    /**
     * The date the container was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The creator of the container.
     */
    public /*out*/ readonly creatorId!: pulumi.Output<string>;
    /**
     * Human-readable name for the Container. Does not have
     * to be unique.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V1 KeyManager client.
     * A KeyManager client is needed to create a container. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * V1 container.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * A set of dictionaries containing references to secrets. The structure is described
     * below.
     */
    public readonly secretRefs!: pulumi.Output<outputs.keymanager.ContainerV1SecretRef[] | undefined>;
    /**
     * The status of the container.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The date the container was last updated.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a ContainerV1 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContainerV1Args, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ContainerV1Args | ContainerV1State, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ContainerV1State | undefined;
            inputs["consumers"] = state ? state.consumers : undefined;
            inputs["containerRef"] = state ? state.containerRef : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["creatorId"] = state ? state.creatorId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["secretRefs"] = state ? state.secretRefs : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as ContainerV1Args | undefined;
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["secretRefs"] = args ? args.secretRefs : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["consumers"] = undefined /*out*/;
            inputs["containerRef"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["creatorId"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["updatedAt"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ContainerV1.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ContainerV1 resources.
 */
export interface ContainerV1State {
    /**
     * The list of the container consumers. The structure is described below.
     */
    readonly consumers?: pulumi.Input<pulumi.Input<inputs.keymanager.ContainerV1Consumer>[]>;
    /**
     * The container reference / where to find the container.
     */
    readonly containerRef?: pulumi.Input<string>;
    /**
     * The date the container was created.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * The creator of the container.
     */
    readonly creatorId?: pulumi.Input<string>;
    /**
     * Human-readable name for the Container. Does not have
     * to be unique.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V1 KeyManager client.
     * A KeyManager client is needed to create a container. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * V1 container.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of dictionaries containing references to secrets. The structure is described
     * below.
     */
    readonly secretRefs?: pulumi.Input<pulumi.Input<inputs.keymanager.ContainerV1SecretRef>[]>;
    /**
     * The status of the container.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The date the container was last updated.
     */
    readonly updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ContainerV1 resource.
 */
export interface ContainerV1Args {
    /**
     * Human-readable name for the Container. Does not have
     * to be unique.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V1 KeyManager client.
     * A KeyManager client is needed to create a container. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * V1 container.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A set of dictionaries containing references to secrets. The structure is described
     * below.
     */
    readonly secretRefs?: pulumi.Input<pulumi.Input<inputs.keymanager.ContainerV1SecretRef>[]>;
    /**
     * Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
     */
    readonly type: pulumi.Input<string>;
}
