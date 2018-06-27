import * as pulumi from "@pulumi/pulumi";
/**
 * Use this data source to get the ID of an available OpenStack security group.
 */
export declare function getSecGroup(args?: GetSecGroupArgs): Promise<GetSecGroupResult>;
/**
 * A collection of arguments for invoking getSecGroup.
 */
export interface GetSecGroupArgs {
    /**
     * The name of the security group.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Neutron client.
     * A Neutron client is needed to retrieve security groups ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The ID of the security group.
     */
    readonly secgroupId?: pulumi.Input<string>;
    /**
     * The owner of the security group.
     */
    readonly tenantId?: pulumi.Input<string>;
}
/**
 * A collection of values returned by getSecGroup.
 */
export interface GetSecGroupResult {
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    readonly tenantId: string;
}