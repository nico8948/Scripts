#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Mattias Schlenker <ms@mattiasschlenker.de> for tribe29 GmbH
# License: GNU General Public License v2
#local/share/check_mk/web/plugins/metrics/
# Reference for details:
# https://docs.checkmk.com/latest/en/devel_check_plugins.html
#
# Here we define the metrics for the graph of our "Hello World!" Plugin
# Colors:
#
#                   red
#  magenta                       orange
#            11 12 13 14 15 16
#         46                   21
#         45                   22
#   blue  44                   23  yellow
#         43                   24
#         42                   25
#         41                   26
#            36 35 34 33 32 31
#     cyan                       yellow-green
#                  green
#
# Special colors:
# 51  gray
# 52  brown 1
# 53  brown 2
# "color" : "23/a" (basic color yellow)
# "color" : "23/b" (nuance of color yellow)
# Import everything of relevance
#metric_info["size"] = {
#	# Set a title, use _() to allow translations
#	"title": _("Filesystem_size"),
#	# Set the unit: Percentage has clear borders
#	"unit": "bytes",
#	# Choose a color that isn't red/yellow/green 
#	"color": "35/a",
#}

from cmk.gui.i18n import _

from cmk.gui.plugins.metrics import (
	check_metrics,
	metric_info,
	graph_info,
)

from cmk.gui.plugins.metrics.translation import (
	df_translation
)

check_metrics["check_mk-pure_volumes"] = df_translation
#metric_info["pfs_size"] = {
#	# Set a title, use _() to allow translations
#	"title": _("Filesystem size"),
#	# Set the unit: Percentage has clear borders
#	"unit": "bytes",
#	# Choose a color that isn't red/yellow/green 
#	"color": "35/a",
#}

#metric_info["pfs_used"] = {
#	# Set a title, use _() to allow translations
#	"title": _("Used filesystem space"),
#	# Set the unit: Percentage has clear borders
#	"unit": "bytes",
#	# Choose a color that isn't red/yellow/green 
#	"color": "15/a",
#}

#metric_info["pfs_free"] = {
#	# Set a title, use _() to allow translations
#	"title": _("Free space"),
#	# Set the unit: Percentage has clear borders
#	"unit": "bytes",
#	# Choose a color that isn't red/yellow/green 
#	"color": "15/a",
#}

#metric_info["pfs_used_percent"] = {
#	# Set a title, use _() to allow translations
#	"title": _("Used filesystem percent"),
#	# Set the unit: Percentage has clear borders
#	"unit": "bytes",
#	# Choose a color that isn't red/yellow/green 
#	"color": "15/a",
#}

metric_info["volumes"] = {
	# Set a title, use _() to allow translations
	"title": _("Volume Total"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "15/a",
}

metric_info["data_reduction"] = {
	# Set a title, use _() to allow translations
	"title": _("Data reduction"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "11/a",
}
metric_info["total_reduction"] = {
	# Set a title, use _() to allow translations
	"title": _("Total reduction"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "16/b",
}

metric_info["shared_space"] = {
	# Set a title, use _() to allow translations
	"title": _("Shared space"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "41/a",
}
metric_info["thin_provisioning"] = {
	# Set a title, use _() to allow translations
	"title": _("Thin provisioning"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "36/a",
}
metric_info["snapshots"] = {
	# Set a title, use _() to allow translations
	"title": _("Snapshot space used"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "23/a",
}


metric_info["reads_per_sec"] = {
	# Set a title, use _() to allow translations
	"title": _("reads_per_sec"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "36/a",
}
metric_info["writes_per_sec"] = {
	# Set a title, use _() to allow translations
	"title": _("writes_per_sec"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "23/a",
}
metric_info["output_per_sec"] = {
	# Set a title, use _() to allow translations
	"title": _("output_per_sec"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "36/a",
}
metric_info["input_per_sec"] = {
	# "title": _("input_per_sec"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "23/a",
}
metric_info["usec_per_read_op"] = {
	# Set a title, use _() to allow translations
	"title": _("usec_per_read_op"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "36/a",
}
metric_info["usec_per_write_op"] = {
	# Set a title, use _() to allow translations
	"title": _("usec_per_write_op"),
	# Set the unit: Percentage has clear borders
	"unit": "bytes",
	# Choose a color that isn't red/yellow/green 
	"color": "23/a",
}



#graph_info["volumes_combined"] = {
#	"metrics": [
#		("fs_size", "line"),
#		("used", "line"),
#		("fs_free", "line"),
#	],
#}

#graph_info["pfs_size"] = {
#	"metrics": [
#		("pfs_size", "line"),
#	],
#}

#graph_info["fs_used"] = {
#	"metrics": [
#		("pfs_used", "line"),
#	],
#}

#graph_info["fs_free"] = {
#	"metrics": [
#		("pfs_free", "line"),
#	],
#}

#graph_info["fs_used_percent"] = {
#	"metrics": [
#		("pfs_used_percent", "line"),
#	],
#}

graph_info["data_reduction"] = {
	"metrics": [
		("data_reduction", "line"),
	],
}

graph_info["total_reduction"] = {
	"metrics": [
	],
}

graph_info["shared_space"] = {
	"metrics": [
		("shared_space", "line"),
	],
}

graph_info["thin_provisioning"] = {
	"metrics": [
		("thin_provisioning", "line"),
	],
}

graph_info["snapshots"] = {
	"metrics": [
		("snapshots", "line"),
	],
}

graph_info["reads_per_sec"] = {
	"metrics": [
		("reads_per_sec", "line"),
	],
}

graph_info["writes_per_sec"] = {
	"metrics": [
		("writes_per_sec", "line"),
	],
}

graph_info["output_per_sec"] = {
	"metrics": [
		("output_per_sec", "line"),
	],
}

graph_info["input_per_sec"] = {
	"metrics": [
		("input_per_sec", "line"),
	],
}

graph_info["usec_per_read_op"] = {
	"metrics": [
		("usec_per_read_op", "line"),
	],
}

graph_info["usec_per_write_op"] = {
	"metrics": [
		("usec_per_write_op", "line"),
	],
}