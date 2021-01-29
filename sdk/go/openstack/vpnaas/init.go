// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vpnaas

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "openstack:vpnaas/endpointGroup:EndpointGroup":
		r, err = NewEndpointGroup(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:vpnaas/ikePolicy:IkePolicy":
		r, err = NewIkePolicy(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:vpnaas/ipSecPolicy:IpSecPolicy":
		r, err = NewIpSecPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:vpnaas/service:Service":
		r, err = NewService(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:vpnaas/siteConnection:SiteConnection":
		r, err = NewSiteConnection(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := openstack.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"openstack",
		"vpnaas/endpointGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"vpnaas/ikePolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"vpnaas/ipSecPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"vpnaas/service",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"vpnaas/siteConnection",
		&module{version},
	)
}
