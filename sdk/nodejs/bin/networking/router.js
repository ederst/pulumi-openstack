"use strict";
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***
Object.defineProperty(exports, "__esModule", { value: true });
const pulumi = require("@pulumi/pulumi");
/**
 * Manages a V2 router resource within OpenStack.
 */
class Router extends pulumi.CustomResource {
    /**
     * Get an existing Router resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name, id, state) {
        return new Router(name, state, { id });
    }
    constructor(name, argsOrState, opts) {
        let inputs = {};
        if (opts && opts.id) {
            const state = argsOrState;
            inputs["adminStateUp"] = state ? state.adminStateUp : undefined;
            inputs["availabilityZoneHints"] = state ? state.availabilityZoneHints : undefined;
            inputs["distributed"] = state ? state.distributed : undefined;
            inputs["enableSnat"] = state ? state.enableSnat : undefined;
            inputs["externalFixedIps"] = state ? state.externalFixedIps : undefined;
            inputs["externalGateway"] = state ? state.externalGateway : undefined;
            inputs["externalNetworkId"] = state ? state.externalNetworkId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
            inputs["valueSpecs"] = state ? state.valueSpecs : undefined;
            inputs["vendorOptions"] = state ? state.vendorOptions : undefined;
        }
        else {
            const args = argsOrState;
            inputs["adminStateUp"] = args ? args.adminStateUp : undefined;
            inputs["availabilityZoneHints"] = args ? args.availabilityZoneHints : undefined;
            inputs["distributed"] = args ? args.distributed : undefined;
            inputs["enableSnat"] = args ? args.enableSnat : undefined;
            inputs["externalFixedIps"] = args ? args.externalFixedIps : undefined;
            inputs["externalGateway"] = args ? args.externalGateway : undefined;
            inputs["externalNetworkId"] = args ? args.externalNetworkId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
            inputs["valueSpecs"] = args ? args.valueSpecs : undefined;
            inputs["vendorOptions"] = args ? args.vendorOptions : undefined;
        }
        super("openstack:networking/router:Router", name, inputs, opts);
    }
}
exports.Router = Router;
//# sourceMappingURL=router.js.map