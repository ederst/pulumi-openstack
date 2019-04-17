// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of an available OpenStack flavor.
func LookupFlavor(ctx *pulumi.Context, args *GetFlavorArgs) (*GetFlavorResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["disk"] = args.Disk
		inputs["flavorId"] = args.FlavorId
		inputs["minDisk"] = args.MinDisk
		inputs["minRam"] = args.MinRam
		inputs["name"] = args.Name
		inputs["ram"] = args.Ram
		inputs["region"] = args.Region
		inputs["rxTxFactor"] = args.RxTxFactor
		inputs["swap"] = args.Swap
		inputs["vcpus"] = args.Vcpus
	}
	outputs, err := ctx.Invoke("openstack:compute/getFlavor:getFlavor", inputs)
	if err != nil {
		return nil, err
	}
	return &GetFlavorResult{
		Disk: outputs["disk"],
		ExtraSpecs: outputs["extraSpecs"],
		FlavorId: outputs["flavorId"],
		IsPublic: outputs["isPublic"],
		MinDisk: outputs["minDisk"],
		MinRam: outputs["minRam"],
		Name: outputs["name"],
		Ram: outputs["ram"],
		Region: outputs["region"],
		RxTxFactor: outputs["rxTxFactor"],
		Swap: outputs["swap"],
		Vcpus: outputs["vcpus"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getFlavor.
type GetFlavorArgs struct {
	// The exact amount of disk (in gigabytes).
	Disk interface{}
	// The ID of the flavor. Conflicts with the `name`,
	// `min_ram` and `min_disk`
	FlavorId interface{}
	// The minimum amount of disk (in gigabytes). Conflicts
	// with the `flavor_id`.
	MinDisk interface{}
	// The minimum amount of RAM (in megabytes). Conflicts
	// with the `flavor_id`.
	MinRam interface{}
	// The name of the flavor. Conflicts with the `flavor_id`.
	Name interface{}
	// The exact amount of RAM (in megabytes).
	Ram interface{}
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	Region interface{}
	// The `rx_tx_factor` of the flavor.
	RxTxFactor interface{}
	// The amount of swap (in gigabytes).
	Swap interface{}
	// The amount of VCPUs.
	Vcpus interface{}
}

// A collection of values returned by getFlavor.
type GetFlavorResult struct {
	Disk interface{}
	// Key/Value pairs of metadata for the flavor.
	ExtraSpecs interface{}
	FlavorId interface{}
	// Whether the flavor is public or private.
	IsPublic interface{}
	MinDisk interface{}
	MinRam interface{}
	Name interface{}
	Ram interface{}
	Region interface{}
	RxTxFactor interface{}
	Swap interface{}
	Vcpus interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
