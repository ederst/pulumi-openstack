// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package identity

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get the ID of an OpenStack user.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/identity"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "user_1"
// 		_, err := identity.LookupUser(ctx, &identity.LookupUserArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupUser(ctx *pulumi.Context, args *LookupUserArgs, opts ...pulumi.InvokeOption) (*LookupUserResult, error) {
	var rv LookupUserResult
	err := ctx.Invoke("openstack:identity/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type LookupUserArgs struct {
	// The domain this user belongs to.
	DomainId *string `pulumi:"domainId"`
	// Whether the user is enabled or disabled. Valid
	// values are `true` and `false`.
	Enabled *bool `pulumi:"enabled"`
	// The identity provider ID of the user.
	IdpId *string `pulumi:"idpId"`
	// The name of the user.
	Name *string `pulumi:"name"`
	// Query for expired passwords. See the [OpenStack API docs](https://developer.openstack.org/api-ref/identity/v3/#list-users) for more information on the query format.
	PasswordExpiresAt *string `pulumi:"passwordExpiresAt"`
	// The protocol ID of the user.
	ProtocolId *string `pulumi:"protocolId"`
	// The region the user is located in.
	Region *string `pulumi:"region"`
	// The unique ID of the user.
	UniqueId *string `pulumi:"uniqueId"`
}

// A collection of values returned by getUser.
type LookupUserResult struct {
	// See Argument Reference above.
	DefaultProjectId string `pulumi:"defaultProjectId"`
	// A description of the user.
	Description string `pulumi:"description"`
	// See Argument Reference above.
	DomainId string `pulumi:"domainId"`
	// See Argument Reference above.
	Enabled *bool `pulumi:"enabled"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// See Argument Reference above.
	IdpId *string `pulumi:"idpId"`
	// See Argument Reference above.
	Name *string `pulumi:"name"`
	// See Argument Reference above.
	PasswordExpiresAt *string `pulumi:"passwordExpiresAt"`
	// See Argument Reference above.
	ProtocolId *string `pulumi:"protocolId"`
	// The region the user is located in.
	Region string `pulumi:"region"`
	// See Argument Reference above.
	UniqueId *string `pulumi:"uniqueId"`
}
