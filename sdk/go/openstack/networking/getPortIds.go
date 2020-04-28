// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get a list of Openstack Port IDs matching the
// specified criteria.
func GetPortIds(ctx *pulumi.Context, args *GetPortIdsArgs, opts ...pulumi.InvokeOption) (*GetPortIdsResult, error) {
	var rv GetPortIdsResult
	err := ctx.Invoke("openstack:networking/getPortIds:getPortIds", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPortIds.
type GetPortIdsArgs struct {
	// The administrative state of the port.
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// Human-readable description of the port.
	Description *string `pulumi:"description"`
	// The ID of the device the port belongs to.
	DeviceId *string `pulumi:"deviceId"`
	// The device owner of the port.
	DeviceOwner *string `pulumi:"deviceOwner"`
	DnsName     *string `pulumi:"dnsName"`
	// The port IP address filter.
	FixedIp *string `pulumi:"fixedIp"`
	// The MAC address of the port.
	MacAddress *string `pulumi:"macAddress"`
	// The name of the port.
	Name *string `pulumi:"name"`
	// The ID of the network the port belongs to.
	NetworkId *string `pulumi:"networkId"`
	// The owner of the port.
	ProjectId *string `pulumi:"projectId"`
	// The region in which to obtain the V2 Neutron client.
	// A Neutron client is needed to retrieve port ids. If omitted, the
	// `region` argument of the provider is used.
	Region *string `pulumi:"region"`
	// The list of port security group IDs to filter.
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	// Order the results in either `asc` or `desc`.
	// Defaults to none.
	SortDirection *string `pulumi:"sortDirection"`
	// Sort ports based on a certain key. Defaults to none.
	SortKey *string `pulumi:"sortKey"`
	// The status of the port.
	Status *string `pulumi:"status"`
	// The list of port tags to filter.
	Tags     []string `pulumi:"tags"`
	TenantId *string  `pulumi:"tenantId"`
}

// A collection of values returned by getPortIds.
type GetPortIdsResult struct {
	AdminStateUp *bool   `pulumi:"adminStateUp"`
	Description  *string `pulumi:"description"`
	DeviceId     *string `pulumi:"deviceId"`
	DeviceOwner  *string `pulumi:"deviceOwner"`
	DnsName      *string `pulumi:"dnsName"`
	FixedIp      *string `pulumi:"fixedIp"`
	// The provider-assigned unique ID for this managed resource.
	Id               string   `pulumi:"id"`
	Ids              []string `pulumi:"ids"`
	MacAddress       *string  `pulumi:"macAddress"`
	Name             *string  `pulumi:"name"`
	NetworkId        *string  `pulumi:"networkId"`
	ProjectId        *string  `pulumi:"projectId"`
	Region           *string  `pulumi:"region"`
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	SortDirection    *string  `pulumi:"sortDirection"`
	SortKey          *string  `pulumi:"sortKey"`
	Status           *string  `pulumi:"status"`
	Tags             []string `pulumi:"tags"`
	TenantId         *string  `pulumi:"tenantId"`
}
