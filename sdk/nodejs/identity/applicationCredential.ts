// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a V3 Application Credential resource within OpenStack Keystone.
 * 
 * > **Note:** All arguments including the application credential name and secret
 * will be stored in the raw state as plain-text. [Read more about sensitive data
 * in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 * > **Note:** An Application Credential is created within the authenticated user
 * project scope and is not visible by an admin or other accounts.
 * The Application Credential visibility is similar to
 * `openstack.compute.Keypair`.
 * 
 * ## Example Usage
 * 
 * ### Predefined secret
 * 
 * Application credential below will have only one `swiftoperator` role.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const swift = new openstack.identity.ApplicationCredential("swift", {
 *     description: "Swift technical application credential",
 *     expiresAt: "2019-02-13T12:12:12Z",
 *     roles: ["swiftoperator"],
 *     secret: "supersecret",
 * });
 * ```
 * 
 * ### Unrestricted with autogenerated secret and unlimited TTL
 * 
 * Application credential below will inherit all the current user's roles.
 * 
 * !> **WARNING:** Restrictions on these Identity operations are deliberately
 * imposed as a safeguard to prevent a compromised application credential from
 * regenerating itself. Disabling this restriction poses an inherent added risk.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const unrestricted = new openstack.identity.ApplicationCredential("unrestricted", {
 *     description: "Unrestricted application credential",
 *     unrestricted: true,
 * });
 * 
 * export const applicationCredentialSecret = unrestricted.secret;
 * ```
 * 
 * ### Application credential with access rules
 * 
 * > **Note:** Application Credential access rules are supported only in Keystone
 * starting from [Train](https://releases.openstack.org/train/highlights.html#keystone-identity-service) release.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const monitoring = new openstack.identity.ApplicationCredential("monitoring", {
 *     accessRules: [
 *         {
 *             method: "GET",
 *             path: "/v2.0/metrics",
 *             service: "monitoring",
 *         },
 *         {
 *             method: "PUT",
 *             path: "/v2.0/metrics",
 *             service: "monitoring",
 *         },
 *     ],
 *     expiresAt: "2019-02-13T12:12:12Z",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown.
 */
export class ApplicationCredential extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationCredential resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationCredentialState, opts?: pulumi.CustomResourceOptions): ApplicationCredential {
        return new ApplicationCredential(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'openstack:identity/applicationCredential:ApplicationCredential';

    /**
     * Returns true if the given object is an instance of ApplicationCredential.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationCredential {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationCredential.__pulumiType;
    }

    /**
     * A collection of one or more access rules, which
     * this application credential allows to follow. The structure is described
     * below. Changing this creates a new application credential.
     */
    public readonly accessRules!: pulumi.Output<outputs.identity.ApplicationCredentialAccessRule[] | undefined>;
    /**
     * A description of the application credential.
     * Changing this creates a new application credential.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The expiration time of the application credential
     * in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
     * an application credential will never expire. Changing this creates a new
     * application credential.
     */
    public readonly expiresAt!: pulumi.Output<string | undefined>;
    /**
     * A name of the application credential. Changing this
     * creates a new application credential.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project the application credential was created
     * for and that authentication requests using this application credential will
     * be scoped to.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V3 Keystone client.
     * If omitted, the `region` argument of the provider is used. Changing this
     * creates a new application credential.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * A collection of one or more role names, which this
     * application credential has to be associated with its project. If omitted,
     * all the current user's roles within the scoped project will be inherited by
     * a new application credential. Changing this creates a new application
     * credential.
     */
    public readonly roles!: pulumi.Output<string[]>;
    /**
     * The secret for the application credential. If omitted,
     * it will be generated by the server. Changing this creates a new application
     * credential.
     */
    public readonly secret!: pulumi.Output<string>;
    /**
     * A flag indicating whether the application
     * credential may be used for creation or destruction of other application
     * credentials or trusts. Changing this creates a new application credential.
     */
    public readonly unrestricted!: pulumi.Output<boolean | undefined>;

    /**
     * Create a ApplicationCredential resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationCredentialArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationCredentialArgs | ApplicationCredentialState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ApplicationCredentialState | undefined;
            inputs["accessRules"] = state ? state.accessRules : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["expiresAt"] = state ? state.expiresAt : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["secret"] = state ? state.secret : undefined;
            inputs["unrestricted"] = state ? state.unrestricted : undefined;
        } else {
            const args = argsOrState as ApplicationCredentialArgs | undefined;
            inputs["accessRules"] = args ? args.accessRules : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["expiresAt"] = args ? args.expiresAt : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["secret"] = args ? args.secret : undefined;
            inputs["unrestricted"] = args ? args.unrestricted : undefined;
            inputs["projectId"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ApplicationCredential.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationCredential resources.
 */
export interface ApplicationCredentialState {
    /**
     * A collection of one or more access rules, which
     * this application credential allows to follow. The structure is described
     * below. Changing this creates a new application credential.
     */
    readonly accessRules?: pulumi.Input<pulumi.Input<inputs.identity.ApplicationCredentialAccessRule>[]>;
    /**
     * A description of the application credential.
     * Changing this creates a new application credential.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The expiration time of the application credential
     * in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
     * an application credential will never expire. Changing this creates a new
     * application credential.
     */
    readonly expiresAt?: pulumi.Input<string>;
    /**
     * A name of the application credential. Changing this
     * creates a new application credential.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project the application credential was created
     * for and that authentication requests using this application credential will
     * be scoped to.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V3 Keystone client.
     * If omitted, the `region` argument of the provider is used. Changing this
     * creates a new application credential.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A collection of one or more role names, which this
     * application credential has to be associated with its project. If omitted,
     * all the current user's roles within the scoped project will be inherited by
     * a new application credential. Changing this creates a new application
     * credential.
     */
    readonly roles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The secret for the application credential. If omitted,
     * it will be generated by the server. Changing this creates a new application
     * credential.
     */
    readonly secret?: pulumi.Input<string>;
    /**
     * A flag indicating whether the application
     * credential may be used for creation or destruction of other application
     * credentials or trusts. Changing this creates a new application credential.
     */
    readonly unrestricted?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a ApplicationCredential resource.
 */
export interface ApplicationCredentialArgs {
    /**
     * A collection of one or more access rules, which
     * this application credential allows to follow. The structure is described
     * below. Changing this creates a new application credential.
     */
    readonly accessRules?: pulumi.Input<pulumi.Input<inputs.identity.ApplicationCredentialAccessRule>[]>;
    /**
     * A description of the application credential.
     * Changing this creates a new application credential.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The expiration time of the application credential
     * in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
     * an application credential will never expire. Changing this creates a new
     * application credential.
     */
    readonly expiresAt?: pulumi.Input<string>;
    /**
     * A name of the application credential. Changing this
     * creates a new application credential.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V3 Keystone client.
     * If omitted, the `region` argument of the provider is used. Changing this
     * creates a new application credential.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A collection of one or more role names, which this
     * application credential has to be associated with its project. If omitted,
     * all the current user's roles within the scoped project will be inherited by
     * a new application credential. Changing this creates a new application
     * credential.
     */
    readonly roles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The secret for the application credential. If omitted,
     * it will be generated by the server. Changing this creates a new application
     * credential.
     */
    readonly secret?: pulumi.Input<string>;
    /**
     * A flag indicating whether the application
     * credential may be used for creation or destruction of other application
     * credentials or trusts. Changing this creates a new application credential.
     */
    readonly unrestricted?: pulumi.Input<boolean>;
}
