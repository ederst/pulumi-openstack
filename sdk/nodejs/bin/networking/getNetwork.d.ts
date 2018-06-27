import * as pulumi from "@pulumi/pulumi";
/**
 * Use this data source to get the ID of an available OpenStack network.
 */
export declare function getNetwork(args?: GetNetworkArgs): Promise<GetNetworkResult>;
/**
 * A collection of arguments for invoking getNetwork.
 */
export interface GetNetworkArgs {
    /**
     * The CIDR of a subnet within the network.
     */
    readonly matchingSubnetCidr?: pulumi.Input<string>;
    /**
     * The name of the network.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the network.
     */
    readonly networkId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 Neutron client.
     * A Neutron client is needed to retrieve networks ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The status of the network.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The owner of the network.
     */
    readonly tenantId?: pulumi.Input<string>;
}
/**
 * A collection of values returned by getNetwork.
 */
export interface GetNetworkResult {
    /**
     * (Optional) The administrative state of the network.
     */
    readonly adminStateUp: string;
    /**
     * (Optional) The availability zone candidates for the network.
     */
    readonly availabilityZoneHints: string[];
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    /**
     * (Optional)  Specifies whether the network resource can be accessed
     * by any tenant or not.
     */
    readonly shared: string;
}