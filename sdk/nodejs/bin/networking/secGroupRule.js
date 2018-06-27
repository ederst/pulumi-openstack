"use strict";
// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***
Object.defineProperty(exports, "__esModule", { value: true });
const pulumi = require("@pulumi/pulumi");
/**
 * Manages a V2 neutron security group rule resource within OpenStack.
 * Unlike Nova security groups, neutron separates the group from the rules
 * and also allows an admin to target a specific tenant_id.
 */
class SecGroupRule extends pulumi.CustomResource {
    /**
     * Get an existing SecGroupRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    static get(name, id, state) {
        return new SecGroupRule(name, state, { id });
    }
    constructor(name, argsOrState, opts) {
        let inputs = {};
        if (opts && opts.id) {
            const state = argsOrState;
            inputs["direction"] = state ? state.direction : undefined;
            inputs["ethertype"] = state ? state.ethertype : undefined;
            inputs["portRangeMax"] = state ? state.portRangeMax : undefined;
            inputs["portRangeMin"] = state ? state.portRangeMin : undefined;
            inputs["protocol"] = state ? state.protocol : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["remoteGroupId"] = state ? state.remoteGroupId : undefined;
            inputs["remoteIpPrefix"] = state ? state.remoteIpPrefix : undefined;
            inputs["securityGroupId"] = state ? state.securityGroupId : undefined;
            inputs["tenantId"] = state ? state.tenantId : undefined;
        }
        else {
            const args = argsOrState;
            if (!args || args.direction === undefined) {
                throw new Error("Missing required property 'direction'");
            }
            if (!args || args.ethertype === undefined) {
                throw new Error("Missing required property 'ethertype'");
            }
            if (!args || args.securityGroupId === undefined) {
                throw new Error("Missing required property 'securityGroupId'");
            }
            inputs["direction"] = args ? args.direction : undefined;
            inputs["ethertype"] = args ? args.ethertype : undefined;
            inputs["portRangeMax"] = args ? args.portRangeMax : undefined;
            inputs["portRangeMin"] = args ? args.portRangeMin : undefined;
            inputs["protocol"] = args ? args.protocol : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["remoteGroupId"] = args ? args.remoteGroupId : undefined;
            inputs["remoteIpPrefix"] = args ? args.remoteIpPrefix : undefined;
            inputs["securityGroupId"] = args ? args.securityGroupId : undefined;
            inputs["tenantId"] = args ? args.tenantId : undefined;
        }
        super("openstack:networking/secGroupRule:SecGroupRule", name, inputs, opts);
    }
}
exports.SecGroupRule = SecGroupRule;
//# sourceMappingURL=secGroupRule.js.map