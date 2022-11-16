# 2021 created by Sven Rueß, sritd.de
#/omd/sites/BIS/local/lib/python3/cmk/base/plugins/agent_based

from .agent_based_api.v1 import (
	register,
	Service,
	Result,
	State,
	Metric,
)

def parse_pure_volumes_performance(string_table):
	section = {}
	for row in string_table:
		(item, reads_per_sec, writes_per_sec, output_per_sec, input_per_sec, usec_per_read_op, usec_per_write_op)  = row

		try:
			reads_per_sec = int(float(reads_per_sec))
		except ValueError:
			reads_per_sec = 0
		try:
			writes_per_sec = int(float(writes_per_sec))
		except ValueError:
			writes_per_sec = 0

		section[item] = {
			'reads_per_sec': reads_per_sec,
			'writes_per_sec': writes_per_sec,
			'output_per_sec': output_per_sec,
			'input_per_sec': input_per_sec,
			'usec_per_read_op': usec_per_read_op,
			'usec_per_write_op': usec_per_write_op 
		}
	return section

register.agent_section(
	name="pure_volumes_performance",
	parse_function=parse_pure_volumes_performance,
)

def render_size(value):
	units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
	unit_index = 0

	while value > 1000 and unit_index < 4:
		value /= 1024
		unit_index += 1
	return "{:.2f} {}".format(value, units[unit_index])\

def discovery_pure_volumes_performance(section):
	for item in section.keys():
		yield Service(item=item)

def check_pure_volumes_performance(item, section):
	failed = []

	if item not in section.keys():
		yield Result(
			state=State.UNKNOWN,
			summary=f"Item {item} not found",
		)
		
	data = section[item]
	
	if section[item]['snapshots'] == 'empty':
		yield Result(
			state=State.CRIT,
			perfdata = f"reads_per_sec: {render_size(data['reads_per_sec'])}, writes_per_sec: {render_size(data['writes_per_sec'])}, output_per_sec: {data['output_per_sec']}, input_per_sec: {data['input_per_sec']}, usec_per_read_op: {data['usec_per_read_op']}, usec_per_write_op: {data['usec_per_write_op']}"
		)
	else:
		yield Result(
			state=State.OK,
			perfdata = f"reads_per_sec: {render_size(data['reads_per_sec'])}, writes_per_sec: {render_size(data['writes_per_sec'])}, output_per_sec: {data['output_per_sec']}, input_per_sec: {data['input_per_sec']}, usec_per_read_op: {data['usec_per_read_op']}, usec_per_write_op: {data['usec_per_write_op']}"
		)

register.check_plugin(
	name="pure_volumes_performance",
	sections=['pure_volumes_performance'],	
	service_name="perf_data %s",
	discovery_function=discovery_pure_volumes_performance,
	check_function=check_pure_volumes_performance,
)