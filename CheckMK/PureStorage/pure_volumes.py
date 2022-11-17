# 2021 created by Sven Rueß, sritd.de
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based

from .agent_based_api.v1 import (
	register,
	Service,
	Result,
	State,
	Metric,
	render,
)
							 
def parse_pure_volumes(string_table):
	section = {}
	for row in string_table:
		(item, size, total, volumes, data_reduction, total_reduction, shared_space, thin_provisioning, snapshots)  = row

		try:
			size = int(float(size))
		except ValueError:
			size = 0
		try:
			total = int(float(total))
		except ValueError:
			total = 0	
		try:
			volumes = int(float(volumes))
		except ValueError:
			volumes = 0  
		try:
			shared_space = int(float(shared_space))
		except ValueError:
			shared_space = 0
		try:
			thin_provisioning = int(float(thin_provisioning))
		except ValueError:
			thin_provisioning = 0
		try:
			snapshots = int(float(snapshots))
		except ValueError:
			snapshots = 0
		try:
			data_reduction = int(float(data_reduction))
		except ValueError:
			data_reduction = 0
		try:
			total_reduction = int(float(total_reduction))
		except ValueError:
			total_reduction = 0
				

		section[item] = {
			'size': size,
			'total': total,
			'volumes': volumes,
			'data_reduction': data_reduction,
			'total_reduction': total_reduction,
			'shared_space': shared_space,
			'thin_provisioning': thin_provisioning,
			'snapshots': snapshots,
		}
	return section

register.agent_section(
	name="pure_volumes",
	parse_function=parse_pure_volumes,
)

def discovery_pure_volumes(section):
	for item in section.keys():
		yield Service(item=item)

def check_pure_volumes(item, section):
	failed = []

	if item not in section.keys():
		yield Result(
			state=State.UNKNOWN,
			summary=f"Item {item} not found",
		)
		
	data = section[item]

#max = size
#used = total
#free = pervolume_free= (int(sizedata) - int(totaldata))

	size_available = f"{int(data['size'])}"
	size_used = f"{int(data['total'])}"
	volumes_data = f"{int(data['volumes'])}"
	snapshot_data = f"{int(data['snapshots'])}"
	thin_provisioning_data = f"{int(data['thin_provisioning'])}"
	fs_used_percent= (int(size_used) / int(size_available))
	fs_free= (int(size_available) - int(size_used))
	fs_percentage_used = f"{fs_used_percent:.0%}"
	
	size_available_bytes = int(size_used)
	size_free_bytes = int(fs_free)
	size_used_bytes = int(data['total'])
	#size_snapshot_bytes = int(snapshotdata)
	#size_thin_provisioning_bytes = int(thin_provisioningdata)
	
	
	if section[item]['snapshots'] == 'empty':
		yield Result(
			state=State.CRIT,
			summary=f"CRIT, size: {render.bytes(data['size'])}, used: {render.bytes(data['total'])}, free: {render.bytes(fs_free)}, percent in use: {fs_percentage_used}",
			details=f"Data Reduction: {data['data_reduction']} to 1, Total reduction: {(data['total_reduction'])} to 1, Shared Space: {render.bytes(data['shared_space'])}, Thin Provisioned: {data['thin_provisioning']}, Snapshots: {render.bytes(data['snapshots'])}, Used after deduplication: {render.bytes(data['volumes'])}",
		)
	else:
		yield Result(
			state=State.OK,
			summary=f"OK, size: {render.bytes(data['size'])}, used: {render.bytes(data['total'])}, free: {render.bytes(fs_free)}, percent in use: {fs_percentage_used}",
			details=f"Data Reduction: {data['data_reduction']} to 1, Total reduction: {(data['total_reduction'])} to 1, Shared Space: {render.bytes(data['shared_space'])}, Thin Provisioned: {data['thin_provisioning']}, Snapshots: {render.bytes(data['snapshots'])}, Used after deduplication: {render.bytes(data['volumes'])}",
		)
		yield Metric("fs_size", value=int(size_available), boundaries=(0, 100))
		yield Metric("fs_used", value=int(size_used), boundaries=(0, 100))
		yield Metric("fs_free", value=int(size_free_bytes), boundaries=(0, 100))
		yield Metric("fs_used_percent", value=int(fs_used_percent), boundaries=(0, 100))
		#yield Metric("snapshots", value=size_snapshot_bytes)
		#yield Metric("thin_provisioning", value=size_thin_provisioning_bytes)

register.check_plugin(
	name="pure_volumes",
	sections=['pure_volumes'],	
	service_name="volume %s",
	discovery_function=discovery_pure_volumes,
	check_function=check_pure_volumes,
)