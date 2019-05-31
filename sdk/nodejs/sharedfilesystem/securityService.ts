// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to configure a security service.
 * 
 * A security service stores configuration information for clients for
 * authentication and authorization (AuthN/AuthZ). For example, a share server
 * will be the client for an existing service such as LDAP, Kerberos, or
 * Microsoft Active Directory.
 * 
 * Minimum supported Manila microversion is 2.7.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as openstack from "@pulumi/openstack";
 * 
 * const securityservice1 = new openstack.sharedfilesystem.SecurityService("securityservice_1", {
 *     description: "created by terraform",
 *     dnsIp: "192.168.199.10",
 *     domain: "example.com",
 *     ou: "CN=Computers,DC=example,DC=com",
 *     password: "s8cret",
 *     server: "192.168.199.10",
 *     type: "active_directory",
 *     user: "joinDomainUser",
 * });
 * ```
 */
export class SecurityService extends pulumi.CustomResource {
    /**
     * Get an existing SecurityService resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityServiceState, opts?: pulumi.CustomResourceOptions): SecurityService {
        return new SecurityService(name, <any>state, { ...opts, id: id });
    }

    /**
     * The human-readable description for the security service.
     * Changing this updates the description of the existing security service.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The security service DNS IP address that is used inside the
     * tenant network.
     */
    public readonly dnsIp!: pulumi.Output<string | undefined>;
    /**
     * The security service domain.
     */
    public readonly domain!: pulumi.Output<string | undefined>;
    /**
     * The name of the security service. Changing this updates the name
     * of the existing security service.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The security service ou. An organizational unit can be added to
     * specify where the share ends up. New in Manila microversion 2.44.
     */
    public readonly ou!: pulumi.Output<string | undefined>;
    /**
     * The user password, if you specify a user.
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * The owner of the Security Service.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a security service. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security service.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The security service host name or IP address.
     */
    public readonly server!: pulumi.Output<string | undefined>;
    /**
     * The security service type - can either be active\_directory,
     * kerberos or ldap.  Changing this updates the existing security service.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * The security service user or group name that is used by the
     * tenant.
     */
    public readonly user!: pulumi.Output<string | undefined>;

    /**
     * Create a SecurityService resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SecurityServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SecurityServiceArgs | SecurityServiceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SecurityServiceState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsIp"] = state ? state.dnsIp : undefined;
            inputs["domain"] = state ? state.domain : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["ou"] = state ? state.ou : undefined;
            inputs["password"] = state ? state.password : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["server"] = state ? state.server : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as SecurityServiceArgs | undefined;
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["dnsIp"] = args ? args.dnsIp : undefined;
            inputs["domain"] = args ? args.domain : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["ou"] = args ? args.ou : undefined;
            inputs["password"] = args ? args.password : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["server"] = args ? args.server : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["user"] = args ? args.user : undefined;
            inputs["projectId"] = undefined /*out*/;
        }
        super("openstack:sharedfilesystem/securityService:SecurityService", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SecurityService resources.
 */
export interface SecurityServiceState {
    /**
     * The human-readable description for the security service.
     * Changing this updates the description of the existing security service.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The security service DNS IP address that is used inside the
     * tenant network.
     */
    readonly dnsIp?: pulumi.Input<string>;
    /**
     * The security service domain.
     */
    readonly domain?: pulumi.Input<string>;
    /**
     * The name of the security service. Changing this updates the name
     * of the existing security service.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The security service ou. An organizational unit can be added to
     * specify where the share ends up. New in Manila microversion 2.44.
     */
    readonly ou?: pulumi.Input<string>;
    /**
     * The user password, if you specify a user.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The owner of the Security Service.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a security service. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security service.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The security service host name or IP address.
     */
    readonly server?: pulumi.Input<string>;
    /**
     * The security service type - can either be active\_directory,
     * kerberos or ldap.  Changing this updates the existing security service.
     */
    readonly type?: pulumi.Input<string>;
    /**
     * The security service user or group name that is used by the
     * tenant.
     */
    readonly user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SecurityService resource.
 */
export interface SecurityServiceArgs {
    /**
     * The human-readable description for the security service.
     * Changing this updates the description of the existing security service.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The security service DNS IP address that is used inside the
     * tenant network.
     */
    readonly dnsIp?: pulumi.Input<string>;
    /**
     * The security service domain.
     */
    readonly domain?: pulumi.Input<string>;
    /**
     * The name of the security service. Changing this updates the name
     * of the existing security service.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The security service ou. An organizational unit can be added to
     * specify where the share ends up. New in Manila microversion 2.44.
     */
    readonly ou?: pulumi.Input<string>;
    /**
     * The user password, if you specify a user.
     */
    readonly password?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Shared File System client.
     * A Shared File System client is needed to create a security service. If omitted, the
     * `region` argument of the provider is used. Changing this creates a new
     * security service.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The security service host name or IP address.
     */
    readonly server?: pulumi.Input<string>;
    /**
     * The security service type - can either be active\_directory,
     * kerberos or ldap.  Changing this updates the existing security service.
     */
    readonly type: pulumi.Input<string>;
    /**
     * The security service user or group name that is used by the
     * tenant.
     */
    readonly user?: pulumi.Input<string>;
}
