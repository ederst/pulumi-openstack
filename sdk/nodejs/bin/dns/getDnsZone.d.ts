import * as pulumi from "@pulumi/pulumi";
/**
 * Use this data source to get the ID of an available OpenStack DNS zone.
 */
export declare function getDnsZone(args?: GetDnsZoneArgs): Promise<GetDnsZoneResult>;
/**
 * A collection of arguments for invoking getDnsZone.
 */
export interface GetDnsZoneArgs {
    readonly attributes?: pulumi.Input<{
        [key: string]: any;
    }>;
    readonly createdAt?: pulumi.Input<string>;
    /**
     * A description of the zone.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The email contact for the zone record.
     */
    readonly email?: pulumi.Input<string>;
    readonly masters?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the zone.
     */
    readonly name?: pulumi.Input<string>;
    readonly poolId?: pulumi.Input<string>;
    readonly projectId?: pulumi.Input<string>;
    /**
     * The region in which to obtain the V2 DNS client.
     * A DNS client is needed to retrieve zone ids. If omitted, the
     * `region` argument of the provider is used.
     */
    readonly region?: pulumi.Input<string>;
    readonly serial?: pulumi.Input<number>;
    /**
     * The zone's status.
     */
    readonly status?: pulumi.Input<string>;
    readonly transferredAt?: pulumi.Input<string>;
    /**
     * The time to live (TTL) of the zone.
     */
    readonly ttl?: pulumi.Input<number>;
    /**
     * The type of the zone. Can either be `PRIMARY` or `SECONDARY`.
     */
    readonly type?: pulumi.Input<string>;
    readonly updatedAt?: pulumi.Input<string>;
    readonly version?: pulumi.Input<number>;
}
/**
 * A collection of values returned by getDnsZone.
 */
export interface GetDnsZoneResult {
    /**
     * Attributes of the DNS Service scheduler.
     */
    readonly attributes: {
        [key: string]: any;
    };
    /**
     * The time the zone was created.
     */
    readonly createdAt: string;
    /**
     * An array of master DNS servers. When `type` is  `SECONDARY`.
     */
    readonly masters: string[];
    /**
     * The ID of the pool hosting the zone.
     */
    readonly poolId: string;
    /**
     * The project ID that owns the zone.
     */
    readonly projectId: string;
    /**
     * See Argument Reference above.
     */
    readonly region: string;
    /**
     * The serial number of the zone.
     */
    readonly serial: number;
    /**
     * The time the zone was transferred.
     */
    readonly transferredAt: string;
    /**
     * The time the zone was last updated.
     */
    readonly updatedAt: string;
    /**
     * The version of the zone.
     */
    readonly version: number;
}