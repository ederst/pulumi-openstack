// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package loadbalancer

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
	case "openstack:loadbalancer/l7PolicyV2:L7PolicyV2":
		r, err = NewL7PolicyV2(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/l7RuleV2:L7RuleV2":
		r, err = NewL7RuleV2(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/listener:Listener":
		r, err = NewListener(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/loadBalancer:LoadBalancer":
		r, err = NewLoadBalancer(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/member:Member":
		r, err = NewMember(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/memberV1:MemberV1":
		r, err = NewMemberV1(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/members:Members":
		r, err = NewMembers(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/monitor:Monitor":
		r, err = NewMonitor(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/monitorV1:MonitorV1":
		r, err = NewMonitorV1(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/pool:Pool":
		r, err = NewPool(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/poolV1:PoolV1":
		r, err = NewPoolV1(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/quota:Quota":
		r, err = NewQuota(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:loadbalancer/vip:Vip":
		r, err = NewVip(ctx, name, nil, pulumi.URN_(urn))
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
		"loadbalancer/l7PolicyV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/l7RuleV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/listener",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/loadBalancer",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/member",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/memberV1",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/members",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/monitor",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/monitorV1",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/pool",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/poolV1",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/quota",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"loadbalancer/vip",
		&module{version},
	)
}
