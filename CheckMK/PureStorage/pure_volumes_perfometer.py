#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Mattias Schlenker <ms@mattiasschlenker.de> for tribe29 GmbH
# License: GNU General Public License v2
#
# Reference for details:
# https://docs.checkmk.com/latest/en/devel_check_plugins.html
#
# Configuration for a simple perf-o-meter that displays percentage

from cmk.gui.plugins.metrics import perfometer_info


# Just create the most simple perf-o-meter displaying only one linear value.
# We use the variable "hellolevel" as reference. Since output ranges from 0
# to 100 we just use the full range.

#perfometer_info.append({
#	"type": "linear",
#	"segments": ["pfs_size"],
#	"pfs_size": 100.0,
#})

#perfometer_info.append({
#	"type": "linear",
#	"segments": ["pfs_used"],
#	"pfs_used": 100.0,
#})

#perfometer_info.append({
#	"type": "linear",
#	"segments": ["pfs_free"],
#	"pfs_free": 100.0,
#})

#perfometer_info.append({
#	"type": "linear",
#	"segments": ["pfs_used_percent"],
#	"pfs_used_percent": 100.0,
#})

perfometer_info.append({
	"type": "linear",
	"segments": ["volumes"],
	"volumes": 100.0,
})


perfometer_info.append({
	"type": "linear",
	"segments": ["data_reduction"],
	"data_reduction": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["total_reduction"],
	"total_reduction": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["shared_space"],
	"shared_space": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["thin_provisioning"],
	"thin_provisioning": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["snapshots"],
	"snapshots": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["reads_per_sec"],
	"reads_per_sec": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["writes_per_sec"],
	"writes_per_sec": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["output_per_sec"],
	"output_per_sec": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["input_per_sec"],
	"input_per_sec": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["usec_per_read_op"],
	"usec_per_read_op": 100.0,
})

perfometer_info.append({
	"type": "linear",
	"segments": ["usec_per_write_op"],
	"usec_per_write_op": 100.0,
})