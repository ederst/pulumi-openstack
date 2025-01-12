// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package firewall

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get firewall policy information of an available OpenStack firewall policy.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/firewall"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "tf_test_policy"
// 		_, err := firewall.LookupPolicy(ctx, &firewall.LookupPolicyArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupPolicy(ctx *pulumi.Context, args *LookupPolicyArgs, opts ...pulumi.InvokeOption) (*LookupPolicyResult, error) {
	var rv LookupPolicyResult
	err := ctx.Invoke("openstack:firewall/getPolicy:getPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPolicy.
type LookupPolicyArgs struct {
	// The name of the firewall policy.
	Name *string `pulumi:"name"`
	// The ID of the firewall policy.
	PolicyId *string `pulumi:"policyId"`
	// The region in which to obtain the V2 Neutron client.
	// A Neutron client is needed to retrieve firewall policy ids. If omitted, the
	// `region` argument of the provider is used.
	Region *string `pulumi:"region"`
	// The owner of the firewall policy.
	TenantId *string `pulumi:"tenantId"`
}

// A collection of values returned by getPolicy.
type LookupPolicyResult struct {
	// The audit status of the firewall policy.
	Audited bool `pulumi:"audited"`
	// The description of the firewall policy.
	Description string `pulumi:"description"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// See Argument Reference above.
	Name *string `pulumi:"name"`
	// See Argument Reference above.
	PolicyId *string `pulumi:"policyId"`
	// See Argument Reference above.
	Region string `pulumi:"region"`
	// The array of one or more firewall rules that comprise the policy.
	Rules []string `pulumi:"rules"`
	// The sharing status of the firewall policy.
	Shared bool `pulumi:"shared"`
	// See Argument Reference above.
	TenantId string `pulumi:"tenantId"`
}
