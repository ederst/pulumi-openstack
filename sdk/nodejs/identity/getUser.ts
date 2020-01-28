// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get the ID of an OpenStack user.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const user1 = openstack.identity.getUser({
 *     name: "user1",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_user_v3.html.markdown.
 */
export function getUser(args?: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("openstack:identity/getUser:getUser", {
        "domainId": args.domainId,
        "enabled": args.enabled,
        "idpId": args.idpId,
        "name": args.name,
        "passwordExpiresAt": args.passwordExpiresAt,
        "protocolId": args.protocolId,
        "region": args.region,
        "uniqueId": args.uniqueId,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The domain this user belongs to.
     */
    readonly domainId?: string;
    /**
     * Whether the user is enabled or disabled. Valid
     * values are `true` and `false`.
     */
    readonly enabled?: boolean;
    /**
     * The identity provider ID of the user.
     */
    readonly idpId?: string;
    /**
     * The name of the user.
     */
    readonly name?: string;
    /**
     * Query for expired passwords. See the [OpenStack API docs](https://developer.openstack.org/api-ref/identity/v3/#list-users) for more information on the query format.
     */
    readonly passwordExpiresAt?: string;
    /**
     * The protocol ID of the user.
     */
    readonly protocolId?: string;
    readonly region?: string;
    /**
     * The unique ID of the user.
     */
    readonly uniqueId?: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * See Argument Reference above.
     */
    readonly defaultProjectId: string;
    /**
     * A description of the user.
     */
    readonly description: string;
    /**
     * See Argument Reference above.
     */
    readonly domainId: string;
    /**
     * See Argument Reference above.
     */
    readonly enabled?: boolean;
    /**
     * See Argument Reference above.
     */
    readonly idpId?: string;
    /**
     * See Argument Reference above.
     */
    readonly name?: string;
    /**
     * See Argument Reference above.
     */
    readonly passwordExpiresAt?: string;
    /**
     * See Argument Reference above.
     */
    readonly protocolId?: string;
    /**
     * The region the user is located in.
     */
    readonly region: string;
    /**
     * See Argument Reference above.
     */
    readonly uniqueId?: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
