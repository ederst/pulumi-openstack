"use strict";
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***
Object.defineProperty(exports, "__esModule", { value: true });
const pulumi = require("@pulumi/pulumi");
/**
 * Creates a routing entry on a OpenStack V2 subnet.
 */
class SubnetRoute extends pulumi.CustomResource {
    /**
     * Get an existing SubnetRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name, id, state) {
        return new SubnetRoute(name, state, { id });
    }
    constructor(name, argsOrState, opts) {
        let inputs = {};
        if (opts && opts.id) {
            const state = argsOrState;
            inputs["destinationCidr"] = state ? state.destinationCidr : undefined;
            inputs["nextHop"] = state ? state.nextHop : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
        }
        else {
            const args = argsOrState;
            if (!args || args.destinationCidr === undefined) {
                throw new Error("Missing required property 'destinationCidr'");
            }
            if (!args || args.nextHop === undefined) {
                throw new Error("Missing required property 'nextHop'");
            }
            if (!args || args.subnetId === undefined) {
                throw new Error("Missing required property 'subnetId'");
            }
            inputs["destinationCidr"] = args ? args.destinationCidr : undefined;
            inputs["nextHop"] = args ? args.nextHop : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
        }
        super("openstack:networking/subnetRoute:SubnetRoute", name, inputs, opts);
    }
}
exports.SubnetRoute = SubnetRoute;
//# sourceMappingURL=subnetRoute.js.map