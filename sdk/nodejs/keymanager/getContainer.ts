// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an available Barbican container.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const example = openstack.keymanager.getContainer({
 *     name: "myContainer",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/keymanager_container_v1.html.markdown.
 */
export function getContainer(args?: GetContainerArgs, opts?: pulumi.InvokeOptions): Promise<GetContainerResult> & GetContainerResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetContainerResult> = pulumi.runtime.invoke("openstack:keymanager/getContainer:getContainer", {
        "name": args.name,
        "region": args.region,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getContainer.
 */
export interface GetContainerArgs {
    /**
     * The Container name.
     */
    readonly name?: string;
    /**
     * The region in which to obtain the V1 KeyManager client.
     * A KeyManager client is needed to fetch a container. If omitted, the `region`
     * argument of the provider is used.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getContainer.
 */
export interface GetContainerResult {
    /**
     * The list of the container consumers. The structure is described
     * below.
     */
    readonly consumers: outputs.keymanager.GetContainerConsumer[];
    /**
     * The container reference / where to find the container.
     */
    readonly containerRef: string;
    /**
     * The date the container was created.
     */
    readonly createdAt: string;
    /**
     * The creator of the container.
     */
    readonly creatorId: string;
    /**
     * The name of the consumer.
     */
    readonly name?: string;
    /**
     * See Argument Reference above.
     */
    readonly region?: string;
    /**
     * A set of dictionaries containing references to secrets. The
     * structure is described below.
     */
    readonly secretRefs: outputs.keymanager.GetContainerSecretRef[];
    /**
     * The status of the container.
     */
    readonly status: string;
    /**
     * The container type.
     */
    readonly type: string;
    /**
     * The date the container was last updated.
     */
    readonly updatedAt: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}