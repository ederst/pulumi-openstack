// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";

export namespace blockstorage {
    export interface VolumeAttachment {
        device?: pulumi.Input<string>;
        id?: pulumi.Input<string>;
        instanceId?: pulumi.Input<string>;
    }

    export interface VolumeV1Attachment {
        device?: pulumi.Input<string>;
        id?: pulumi.Input<string>;
        instanceId?: pulumi.Input<string>;
    }

    export interface VolumeV2Attachment {
        device?: pulumi.Input<string>;
        id?: pulumi.Input<string>;
        instanceId?: pulumi.Input<string>;
    }
}

export namespace compute {
    export interface InstanceBlockDevice {
        bootIndex?: pulumi.Input<number>;
        deleteOnTermination?: pulumi.Input<boolean>;
        destinationType?: pulumi.Input<string>;
        deviceType?: pulumi.Input<string>;
        diskBus?: pulumi.Input<string>;
        guestFormat?: pulumi.Input<string>;
        sourceType: pulumi.Input<string>;
        uuid?: pulumi.Input<string>;
        volumeSize?: pulumi.Input<number>;
    }

    export interface InstanceNetwork {
        accessNetwork?: pulumi.Input<boolean>;
        fixedIpV4?: pulumi.Input<string>;
        fixedIpV6?: pulumi.Input<string>;
        mac?: pulumi.Input<string>;
        /**
         * A unique name for the resource.
         */
        name?: pulumi.Input<string>;
        port?: pulumi.Input<string>;
        uuid?: pulumi.Input<string>;
    }

    export interface InstancePersonality {
        content: pulumi.Input<string>;
        file: pulumi.Input<string>;
    }

    export interface InstanceSchedulerHint {
        additionalProperties?: pulumi.Input<{[key: string]: any}>;
        buildNearHostIp?: pulumi.Input<string>;
        differentHosts?: pulumi.Input<pulumi.Input<string>[]>;
        group?: pulumi.Input<string>;
        queries?: pulumi.Input<pulumi.Input<string>[]>;
        sameHosts?: pulumi.Input<pulumi.Input<string>[]>;
        targetCell?: pulumi.Input<string>;
    }

    export interface InstanceVendorOptions {
        ignoreResizeConfirmation?: pulumi.Input<boolean>;
    }

    export interface SecGroupRule {
        cidr?: pulumi.Input<string>;
        fromGroupId?: pulumi.Input<string>;
        fromPort: pulumi.Input<number>;
        id?: pulumi.Input<string>;
        ipProtocol: pulumi.Input<string>;
        self?: pulumi.Input<boolean>;
        toPort: pulumi.Input<number>;
    }
}

export namespace database {
    export interface ConfigurationConfiguration {
        /**
         * A unique name for the resource.
         */
        name: pulumi.Input<string>;
        value: pulumi.Input<string>;
    }

    export interface ConfigurationDatastore {
        type: pulumi.Input<string>;
        version: pulumi.Input<string>;
    }

    export interface InstanceDatabase {
        charset?: pulumi.Input<string>;
        collate?: pulumi.Input<string>;
        /**
         * A unique name for the resource.
         */
        name: pulumi.Input<string>;
    }

    export interface InstanceDatastore {
        type: pulumi.Input<string>;
        version: pulumi.Input<string>;
    }

    export interface InstanceNetwork {
        fixedIpV4?: pulumi.Input<string>;
        fixedIpV6?: pulumi.Input<string>;
        port?: pulumi.Input<string>;
        uuid?: pulumi.Input<string>;
    }

    export interface InstanceUser {
        databases?: pulumi.Input<pulumi.Input<string>[]>;
        host?: pulumi.Input<string>;
        /**
         * A unique name for the resource.
         */
        name: pulumi.Input<string>;
        password?: pulumi.Input<string>;
    }
}

export namespace identity {
    export interface UserMultiFactorAuthRule {
        rules: pulumi.Input<pulumi.Input<string>[]>;
    }
}

export namespace keymanager {
    export interface ContainerV1Consumer {
        /**
         * Human-readable name for the Container. Does not have
         * to be unique.
         */
        name?: pulumi.Input<string>;
        /**
         * The consumer URL.
         */
        url?: pulumi.Input<string>;
    }

    export interface ContainerV1SecretRef {
        /**
         * Human-readable name for the Container. Does not have
         * to be unique.
         */
        name?: pulumi.Input<string>;
        secretRef: pulumi.Input<string>;
    }
}

export namespace loadbalancer {
    export interface PoolPersistence {
        /**
         * The name of the cookie if persistence mode is set
         * appropriately. Required if `type = APP_COOKIE`.
         */
        cookieName?: pulumi.Input<string>;
        /**
         * The type of persistence mode. The current specification
         * supports SOURCE_IP, HTTP_COOKIE, and APP_COOKIE.
         */
        type: pulumi.Input<string>;
    }
}

export namespace networking {
    export interface NetworkSegment {
        networkType?: pulumi.Input<string>;
        physicalNetwork?: pulumi.Input<string>;
        segmentationId?: pulumi.Input<number>;
    }

    export interface PortAllowedAddressPair {
        ipAddress: pulumi.Input<string>;
        /**
         * Specify a specific MAC address for the port. Changing
         * this creates a new port.
         */
        macAddress?: pulumi.Input<string>;
    }

    export interface PortBinding {
        hostId?: pulumi.Input<string>;
        profile?: pulumi.Input<string>;
        vifDetails?: pulumi.Input<{[key: string]: any}>;
        vifType?: pulumi.Input<string>;
        vnicType?: pulumi.Input<string>;
    }

    export interface PortExtraDhcpOption {
        ipVersion?: pulumi.Input<number>;
        /**
         * A unique name for the port. Changing this
         * updates the `name` of an existing port.
         */
        name: pulumi.Input<string>;
        value: pulumi.Input<string>;
    }

    export interface PortFixedIp {
        ipAddress?: pulumi.Input<string>;
        subnetId: pulumi.Input<string>;
    }

    export interface RouterExternalFixedIp {
        ipAddress?: pulumi.Input<string>;
        subnetId?: pulumi.Input<string>;
    }

    export interface RouterVendorOptions {
        setRouterGatewayAfterCreate?: pulumi.Input<boolean>;
    }

    export interface SubnetAllocationPool {
        end: pulumi.Input<string>;
        start: pulumi.Input<string>;
    }

    export interface SubnetAllocationPoolsCollection {
        end: pulumi.Input<string>;
        start: pulumi.Input<string>;
    }

    export interface SubnetHostRoute {
        destinationCidr: pulumi.Input<string>;
        nextHop: pulumi.Input<string>;
    }

    export interface TrunkSubPort {
        /**
         * The ID of the port to be used as the parent port of the
         * trunk. This is the port that should be used as the compute instance network
         * port. Changing this creates a new trunk.
         */
        portId: pulumi.Input<string>;
        segmentationId: pulumi.Input<number>;
        segmentationType: pulumi.Input<string>;
    }
}

export namespace objectstorage {
    export interface ContainerVersioning {
        location: pulumi.Input<string>;
        type: pulumi.Input<string>;
    }
}

export namespace sharedfilesystem {
    export interface ShareExportLocation {
        path?: pulumi.Input<string>;
        preferred?: pulumi.Input<string>;
    }
}

export namespace vpnaas {
    export interface IkePolicyLifetime {
        units?: pulumi.Input<string>;
        value?: pulumi.Input<number>;
    }

    export interface IpSecPolicyLifetime {
        units?: pulumi.Input<string>;
        value?: pulumi.Input<number>;
    }

    export interface SiteConnectionDpd {
        action?: pulumi.Input<string>;
        interval?: pulumi.Input<number>;
        timeout?: pulumi.Input<number>;
    }
}
