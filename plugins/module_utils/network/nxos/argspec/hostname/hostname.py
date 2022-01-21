# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the nxos_hostname module
"""


class HostnameArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_hostname module
    """

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {"type": "dict", "options": {"hostname": {"type": "str"}}},
        "state": {
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
