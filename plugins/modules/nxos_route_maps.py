#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for nxos_route_maps
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: nxos_route_maps
short_description: Route Maps resource module.
description:
- This module manages route maps configuration on devices running Cisco NX-OS.
version_added: 2.2.0
notes:
- Tested against NX-OS 9.3.6.
- This module works with connection C(network_cli) and C(httpapi).
author: Nilashish Chakraborty (@NilashishC)
mutually_exclusive: [["running_config", "config"]]
required_by:
  varA: 'varB'
  varC: ['varD', 'varE']
required_together:
  - - file_path
    - file_hash
required_if:
  - ["state", "merged", ["config",]]
  - ["state", "replaced", ["config",]]
  - ["state", "overridden", ["config",]]
  - ["state", "rendered", ["config",]]
  - ["state", "parsed", ["running_config",]]
supports_check_mode: True
options:
  file_path:
    description: Test
    type: str
  file_hash:
    description: Test
    type: str
  varA:
    description: Test
    type: str
  varB:
    description: Test
    type: str
  varC:
    description: Test
    type: str
  varD:
    description: Test
    type: str
  varE:
    description: Test
    type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the NX-OS device
      by executing the command B(show running-config | section '^route-map').
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A list of route-map configuration.
    type: list
    elements: dict
    suboptions:
      route_map:
        description: Route-map name.
        type: str
      entries:
        description: List of entries (identified by sequence number) for this route-map.
        type: list
        elements: dict
        mutually_exclusive: [["sequence", "action"]]
        suboptions:
          sequence:
            description: Sequence to insert to/delete from existing route-map entry.
            type: int
          action:
            description: Route map denies or permits set operations.
            type: str
            choices: ["deny", "permit"]
  state:
    description:
    - The state the configuration should be left in.
    - With state I(replaced), for the listed route-maps,
      sequences that are in running-config but not in the task are negated.
    - With state I(overridden), all route-maps that are in running-config but
      not in the task are negated.
    - Please refer to examples for more details.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.route_maps.route_maps import (
    Route_maps,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    convert_doc_to_ansible_module_kwargs,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    argspec = convert_doc_to_ansible_module_kwargs(DOCUMENTATION)
    module = AnsibleModule(**argspec)
    result = Route_maps(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
