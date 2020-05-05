module github.com/pulumi/pulumi-openstack/provider/v2

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.11.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.3.0
	github.com/pulumi/pulumi/sdk/v2 v2.1.1-0.20200501142137-f36a8b4ca0ce
	github.com/terraform-providers/terraform-provider-openstack v1.28.0
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
