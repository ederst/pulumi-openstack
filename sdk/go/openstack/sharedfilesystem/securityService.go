// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sharedfilesystem

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this resource to configure a security service.
//
// A security service stores configuration information for clients for
// authentication and authorization (AuthN/AuthZ). For example, a share server
// will be the client for an existing service such as LDAP, Kerberos, or
// Microsoft Active Directory.
//
// Minimum supported Manila microversion is 2.7.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/sharedfilesystem"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sharedfilesystem.NewSecurityService(ctx, "securityservice1", &sharedfilesystem.SecurityServiceArgs{
// 			Description: pulumi.String("created by terraform"),
// 			DnsIp:       pulumi.String("192.168.199.10"),
// 			Domain:      pulumi.String("example.com"),
// 			Ou:          pulumi.String("CN=Computers,DC=example,DC=com"),
// 			Password:    pulumi.String("s8cret"),
// 			Server:      pulumi.String("192.168.199.10"),
// 			Type:        pulumi.String("active_directory"),
// 			User:        pulumi.String("joinDomainUser"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// This resource can be imported by specifying the ID of the security service
//
// ```sh
//  $ pulumi import openstack:sharedfilesystem/securityService:SecurityService securityservice_1 <id>
// ```
type SecurityService struct {
	pulumi.CustomResourceState

	// The human-readable description for the security service.
	// Changing this updates the description of the existing security service.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The security service DNS IP address that is used inside the
	// tenant network.
	DnsIp pulumi.StringPtrOutput `pulumi:"dnsIp"`
	// The security service domain.
	Domain pulumi.StringPtrOutput `pulumi:"domain"`
	// The name of the security service. Changing this updates the name
	// of the existing security service.
	Name pulumi.StringOutput `pulumi:"name"`
	// The security service ou. An organizational unit can be added to
	// specify where the share ends up. New in Manila microversion 2.44.
	Ou pulumi.StringPtrOutput `pulumi:"ou"`
	// The user password, if you specify a user.
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// The owner of the Security Service.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a security service. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security service.
	Region pulumi.StringOutput `pulumi:"region"`
	// The security service host name or IP address.
	Server pulumi.StringPtrOutput `pulumi:"server"`
	// The security service type - can either be active\_directory,
	// kerberos or ldap.  Changing this updates the existing security service.
	Type pulumi.StringOutput `pulumi:"type"`
	// The security service user or group name that is used by the
	// tenant.
	User pulumi.StringPtrOutput `pulumi:"user"`
}

// NewSecurityService registers a new resource with the given unique name, arguments, and options.
func NewSecurityService(ctx *pulumi.Context,
	name string, args *SecurityServiceArgs, opts ...pulumi.ResourceOption) (*SecurityService, error) {
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &SecurityServiceArgs{}
	}
	var resource SecurityService
	err := ctx.RegisterResource("openstack:sharedfilesystem/securityService:SecurityService", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecurityService gets an existing SecurityService resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecurityServiceState, opts ...pulumi.ResourceOption) (*SecurityService, error) {
	var resource SecurityService
	err := ctx.ReadResource("openstack:sharedfilesystem/securityService:SecurityService", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecurityService resources.
type securityServiceState struct {
	// The human-readable description for the security service.
	// Changing this updates the description of the existing security service.
	Description *string `pulumi:"description"`
	// The security service DNS IP address that is used inside the
	// tenant network.
	DnsIp *string `pulumi:"dnsIp"`
	// The security service domain.
	Domain *string `pulumi:"domain"`
	// The name of the security service. Changing this updates the name
	// of the existing security service.
	Name *string `pulumi:"name"`
	// The security service ou. An organizational unit can be added to
	// specify where the share ends up. New in Manila microversion 2.44.
	Ou *string `pulumi:"ou"`
	// The user password, if you specify a user.
	Password *string `pulumi:"password"`
	// The owner of the Security Service.
	ProjectId *string `pulumi:"projectId"`
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a security service. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security service.
	Region *string `pulumi:"region"`
	// The security service host name or IP address.
	Server *string `pulumi:"server"`
	// The security service type - can either be active\_directory,
	// kerberos or ldap.  Changing this updates the existing security service.
	Type *string `pulumi:"type"`
	// The security service user or group name that is used by the
	// tenant.
	User *string `pulumi:"user"`
}

type SecurityServiceState struct {
	// The human-readable description for the security service.
	// Changing this updates the description of the existing security service.
	Description pulumi.StringPtrInput
	// The security service DNS IP address that is used inside the
	// tenant network.
	DnsIp pulumi.StringPtrInput
	// The security service domain.
	Domain pulumi.StringPtrInput
	// The name of the security service. Changing this updates the name
	// of the existing security service.
	Name pulumi.StringPtrInput
	// The security service ou. An organizational unit can be added to
	// specify where the share ends up. New in Manila microversion 2.44.
	Ou pulumi.StringPtrInput
	// The user password, if you specify a user.
	Password pulumi.StringPtrInput
	// The owner of the Security Service.
	ProjectId pulumi.StringPtrInput
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a security service. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security service.
	Region pulumi.StringPtrInput
	// The security service host name or IP address.
	Server pulumi.StringPtrInput
	// The security service type - can either be active\_directory,
	// kerberos or ldap.  Changing this updates the existing security service.
	Type pulumi.StringPtrInput
	// The security service user or group name that is used by the
	// tenant.
	User pulumi.StringPtrInput
}

func (SecurityServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*securityServiceState)(nil)).Elem()
}

type securityServiceArgs struct {
	// The human-readable description for the security service.
	// Changing this updates the description of the existing security service.
	Description *string `pulumi:"description"`
	// The security service DNS IP address that is used inside the
	// tenant network.
	DnsIp *string `pulumi:"dnsIp"`
	// The security service domain.
	Domain *string `pulumi:"domain"`
	// The name of the security service. Changing this updates the name
	// of the existing security service.
	Name *string `pulumi:"name"`
	// The security service ou. An organizational unit can be added to
	// specify where the share ends up. New in Manila microversion 2.44.
	Ou *string `pulumi:"ou"`
	// The user password, if you specify a user.
	Password *string `pulumi:"password"`
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a security service. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security service.
	Region *string `pulumi:"region"`
	// The security service host name or IP address.
	Server *string `pulumi:"server"`
	// The security service type - can either be active\_directory,
	// kerberos or ldap.  Changing this updates the existing security service.
	Type string `pulumi:"type"`
	// The security service user or group name that is used by the
	// tenant.
	User *string `pulumi:"user"`
}

// The set of arguments for constructing a SecurityService resource.
type SecurityServiceArgs struct {
	// The human-readable description for the security service.
	// Changing this updates the description of the existing security service.
	Description pulumi.StringPtrInput
	// The security service DNS IP address that is used inside the
	// tenant network.
	DnsIp pulumi.StringPtrInput
	// The security service domain.
	Domain pulumi.StringPtrInput
	// The name of the security service. Changing this updates the name
	// of the existing security service.
	Name pulumi.StringPtrInput
	// The security service ou. An organizational unit can be added to
	// specify where the share ends up. New in Manila microversion 2.44.
	Ou pulumi.StringPtrInput
	// The user password, if you specify a user.
	Password pulumi.StringPtrInput
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a security service. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security service.
	Region pulumi.StringPtrInput
	// The security service host name or IP address.
	Server pulumi.StringPtrInput
	// The security service type - can either be active\_directory,
	// kerberos or ldap.  Changing this updates the existing security service.
	Type pulumi.StringInput
	// The security service user or group name that is used by the
	// tenant.
	User pulumi.StringPtrInput
}

func (SecurityServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*securityServiceArgs)(nil)).Elem()
}

type SecurityServiceInput interface {
	pulumi.Input

	ToSecurityServiceOutput() SecurityServiceOutput
	ToSecurityServiceOutputWithContext(ctx context.Context) SecurityServiceOutput
}

func (SecurityService) ElementType() reflect.Type {
	return reflect.TypeOf((*SecurityService)(nil)).Elem()
}

func (i SecurityService) ToSecurityServiceOutput() SecurityServiceOutput {
	return i.ToSecurityServiceOutputWithContext(context.Background())
}

func (i SecurityService) ToSecurityServiceOutputWithContext(ctx context.Context) SecurityServiceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecurityServiceOutput)
}

type SecurityServiceOutput struct {
	*pulumi.OutputState
}

func (SecurityServiceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecurityServiceOutput)(nil)).Elem()
}

func (o SecurityServiceOutput) ToSecurityServiceOutput() SecurityServiceOutput {
	return o
}

func (o SecurityServiceOutput) ToSecurityServiceOutputWithContext(ctx context.Context) SecurityServiceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SecurityServiceOutput{})
}
