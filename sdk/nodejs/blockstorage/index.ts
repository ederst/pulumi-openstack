// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./getAvailabilityZonesV3";
export * from "./getSnapshotV2";
export * from "./getSnapshotV3";
export * from "./getVolumeV2";
export * from "./getVolumeV3";
export * from "./quoteSetV2";
export * from "./quoteSetV3";
export * from "./volume";
export * from "./volumeAttach";
export * from "./volumeAttachV2";
export * from "./volumeV1";
export * from "./volumeV2";

// Import resources to register:
import { QuoteSetV2 } from "./quoteSetV2";
import { QuoteSetV3 } from "./quoteSetV3";
import { Volume } from "./volume";
import { VolumeAttach } from "./volumeAttach";
import { VolumeAttachV2 } from "./volumeAttachV2";
import { VolumeV1 } from "./volumeV1";
import { VolumeV2 } from "./volumeV2";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "openstack:blockstorage/quoteSetV2:QuoteSetV2":
                return new QuoteSetV2(name, <any>undefined, { urn })
            case "openstack:blockstorage/quoteSetV3:QuoteSetV3":
                return new QuoteSetV3(name, <any>undefined, { urn })
            case "openstack:blockstorage/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            case "openstack:blockstorage/volumeAttach:VolumeAttach":
                return new VolumeAttach(name, <any>undefined, { urn })
            case "openstack:blockstorage/volumeAttachV2:VolumeAttachV2":
                return new VolumeAttachV2(name, <any>undefined, { urn })
            case "openstack:blockstorage/volumeV1:VolumeV1":
                return new VolumeV1(name, <any>undefined, { urn })
            case "openstack:blockstorage/volumeV2:VolumeV2":
                return new VolumeV2(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("openstack", "blockstorage/quoteSetV2", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/quoteSetV3", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/volume", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/volumeAttach", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/volumeAttachV2", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/volumeV1", _module)
pulumi.runtime.registerResourceModule("openstack", "blockstorage/volumeV2", _module)
