// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package loadbalancer

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 L7 Rule resource within OpenStack.
type L7RuleV2 struct {
	pulumi.CustomResourceState

	// The administrative state of the L7 Rule.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp pulumi.BoolPtrOutput `pulumi:"adminStateUp"`
	// The comparison type for the L7 rule - can either be
	// CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
	CompareType pulumi.StringOutput `pulumi:"compareType"`
	// When true the logic of the rule is inverted. For example, with invert
	// true, equal to would become not equal to. Default is false.
	Invert pulumi.BoolPtrOutput `pulumi:"invert"`
	// The key to use for the comparison. For example, the name of the cookie to
	// evaluate. Valid when `type` is set to COOKIE or HEADER.
	Key pulumi.StringPtrOutput `pulumi:"key"`
	// The ID of the L7 Policy to query. Changing this creates a new
	// L7 Rule.
	L7policyId pulumi.StringOutput `pulumi:"l7policyId"`
	// The ID of the Listener owning this resource.
	ListenerId pulumi.StringOutput `pulumi:"listenerId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an . If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// L7 Rule.
	Region pulumi.StringOutput `pulumi:"region"`
	// Required for admins. The UUID of the tenant who owns
	// the L7 Rule.  Only administrative users can specify a tenant UUID
	// other than their own. Changing this creates a new L7 Rule.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
	// The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
	// HOST\_NAME or PATH.
	Type pulumi.StringOutput `pulumi:"type"`
	// The value to use for the comparison. For example, the file type to
	// compare.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewL7RuleV2 registers a new resource with the given unique name, arguments, and options.
func NewL7RuleV2(ctx *pulumi.Context,
	name string, args *L7RuleV2Args, opts ...pulumi.ResourceOption) (*L7RuleV2, error) {
	if args == nil || args.CompareType == nil {
		return nil, errors.New("missing required argument 'CompareType'")
	}
	if args == nil || args.L7policyId == nil {
		return nil, errors.New("missing required argument 'L7policyId'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	if args == nil {
		args = &L7RuleV2Args{}
	}
	var resource L7RuleV2
	err := ctx.RegisterResource("openstack:loadbalancer/l7RuleV2:L7RuleV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetL7RuleV2 gets an existing L7RuleV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetL7RuleV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *L7RuleV2State, opts ...pulumi.ResourceOption) (*L7RuleV2, error) {
	var resource L7RuleV2
	err := ctx.ReadResource("openstack:loadbalancer/l7RuleV2:L7RuleV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering L7RuleV2 resources.
type l7ruleV2State struct {
	// The administrative state of the L7 Rule.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// The comparison type for the L7 rule - can either be
	// CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
	CompareType *string `pulumi:"compareType"`
	// When true the logic of the rule is inverted. For example, with invert
	// true, equal to would become not equal to. Default is false.
	Invert *bool `pulumi:"invert"`
	// The key to use for the comparison. For example, the name of the cookie to
	// evaluate. Valid when `type` is set to COOKIE or HEADER.
	Key *string `pulumi:"key"`
	// The ID of the L7 Policy to query. Changing this creates a new
	// L7 Rule.
	L7policyId *string `pulumi:"l7policyId"`
	// The ID of the Listener owning this resource.
	ListenerId *string `pulumi:"listenerId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an . If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// L7 Rule.
	Region *string `pulumi:"region"`
	// Required for admins. The UUID of the tenant who owns
	// the L7 Rule.  Only administrative users can specify a tenant UUID
	// other than their own. Changing this creates a new L7 Rule.
	TenantId *string `pulumi:"tenantId"`
	// The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
	// HOST\_NAME or PATH.
	Type *string `pulumi:"type"`
	// The value to use for the comparison. For example, the file type to
	// compare.
	Value *string `pulumi:"value"`
}

type L7RuleV2State struct {
	// The administrative state of the L7 Rule.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp pulumi.BoolPtrInput
	// The comparison type for the L7 rule - can either be
	// CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
	CompareType pulumi.StringPtrInput
	// When true the logic of the rule is inverted. For example, with invert
	// true, equal to would become not equal to. Default is false.
	Invert pulumi.BoolPtrInput
	// The key to use for the comparison. For example, the name of the cookie to
	// evaluate. Valid when `type` is set to COOKIE or HEADER.
	Key pulumi.StringPtrInput
	// The ID of the L7 Policy to query. Changing this creates a new
	// L7 Rule.
	L7policyId pulumi.StringPtrInput
	// The ID of the Listener owning this resource.
	ListenerId pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an . If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// L7 Rule.
	Region pulumi.StringPtrInput
	// Required for admins. The UUID of the tenant who owns
	// the L7 Rule.  Only administrative users can specify a tenant UUID
	// other than their own. Changing this creates a new L7 Rule.
	TenantId pulumi.StringPtrInput
	// The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
	// HOST\_NAME or PATH.
	Type pulumi.StringPtrInput
	// The value to use for the comparison. For example, the file type to
	// compare.
	Value pulumi.StringPtrInput
}

func (L7RuleV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*l7ruleV2State)(nil)).Elem()
}

type l7ruleV2Args struct {
	// The administrative state of the L7 Rule.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// The comparison type for the L7 rule - can either be
	// CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
	CompareType string `pulumi:"compareType"`
	// When true the logic of the rule is inverted. For example, with invert
	// true, equal to would become not equal to. Default is false.
	Invert *bool `pulumi:"invert"`
	// The key to use for the comparison. For example, the name of the cookie to
	// evaluate. Valid when `type` is set to COOKIE or HEADER.
	Key *string `pulumi:"key"`
	// The ID of the L7 Policy to query. Changing this creates a new
	// L7 Rule.
	L7policyId string `pulumi:"l7policyId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an . If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// L7 Rule.
	Region *string `pulumi:"region"`
	// Required for admins. The UUID of the tenant who owns
	// the L7 Rule.  Only administrative users can specify a tenant UUID
	// other than their own. Changing this creates a new L7 Rule.
	TenantId *string `pulumi:"tenantId"`
	// The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
	// HOST\_NAME or PATH.
	Type string `pulumi:"type"`
	// The value to use for the comparison. For example, the file type to
	// compare.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a L7RuleV2 resource.
type L7RuleV2Args struct {
	// The administrative state of the L7 Rule.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp pulumi.BoolPtrInput
	// The comparison type for the L7 rule - can either be
	// CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
	CompareType pulumi.StringInput
	// When true the logic of the rule is inverted. For example, with invert
	// true, equal to would become not equal to. Default is false.
	Invert pulumi.BoolPtrInput
	// The key to use for the comparison. For example, the name of the cookie to
	// evaluate. Valid when `type` is set to COOKIE or HEADER.
	Key pulumi.StringPtrInput
	// The ID of the L7 Policy to query. Changing this creates a new
	// L7 Rule.
	L7policyId pulumi.StringInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an . If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// L7 Rule.
	Region pulumi.StringPtrInput
	// Required for admins. The UUID of the tenant who owns
	// the L7 Rule.  Only administrative users can specify a tenant UUID
	// other than their own. Changing this creates a new L7 Rule.
	TenantId pulumi.StringPtrInput
	// The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
	// HOST\_NAME or PATH.
	Type pulumi.StringInput
	// The value to use for the comparison. For example, the file type to
	// compare.
	Value pulumi.StringInput
}

func (L7RuleV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*l7ruleV2Args)(nil)).Elem()
}