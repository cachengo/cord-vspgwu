# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
from django.db.models import Q, F
from synchronizers.new_base.modelaccessor import *
from synchronizers.new_base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

class SyncVSPGWUTenant(SyncInstanceUsingAnsible):
    observes = VSPGWUTenant
    template_name = "vspgwutenant_playbook.yaml"
    service_key_name = "/opt/xos/configurations/mcord/mcord_private_key"

    def __init__(self, *args, **kwargs):
        super(SyncVSPGWUTenant, self).__init__(*args, **kwargs)

    def get_extra_attributes(self, o):

        scenario = self.get_scenario()

        if scenario == 'ng4t_with_sdncontroller':
            return self.get_values_for_ng4t_w_sdncontroller()
        elif scenario == 'ng4t_without_sdncontroller':
            return self.get_values_for_ng4t_wo_sdncontroller()
        elif scenario == 'spirent_with_sdncontroller':
            return self.get_values_for_spirent_w_sdncontroller()
        elif scenario == 'spirent_without_sdncontroller':
            return self.get_values_for_spirent_wo_sdncontroller()
        else:
            return self.get_extra_attributes_for_manual()

    # fields for manual case
    def get_extra_attributes_for_manual(self):
        fields = {}
        fields['scenario'] = self.get_scenario()
        # for interface.cfg file
        fields['zmq_sub_ip'] = "manual"
        fields['zmq_pub_ip'] = "manual"
        fields['dp_comm_ip'] = "manual"
        fields['cp_comm_ip'] = "manual"
        fields['fpc_ip'] = "manual"
        fields['cp_nb_server_ip'] = "manual"

        # for dp_config.cfg file
        fields['s1u_ip'] = "manual"
        fields['sgi_ip'] = "manual"

        return fields

    def get_values_for_ng4t_w_sdncontroller(self):
        fields = {}
        fields['scenario'] = "ng4t_with_sdncontroller"
        # for interface.cfg file
        fields['zmq_sub_ip'] = self.get_ip_address('sbi_network', SDNControllerServiceInstance, 'zmq_sub_ip')
        fields['zmq_pub_ip'] = self.get_ip_address('sbi_network', SDNControllerServiceInstance, 'zmq_pub_ip')
        fields['dp_comm_ip'] = self.get_ip_address('sbi_network', VSPGWUTenant, 'dp_comm_ip')
        fields['cp_comm_ip'] = self.get_ip_address('nbi_network', VSPGWCTenant, 'cp_comm_ip')
        fields['fpc_ip'] = self.get_ip_address('nbi_network', SDNControllerServiceInstance, 'fpc_ip')
        fields['cp_nb_server_ip'] = self.get_ip_address('nbi_network', VSPGWCTenant, 'cp_nb_server_ip')

        # for dp_config.cfg file
        fields['s1u_ip'] = self.get_ip_address('s1u_network', VSPGWUTenant, 's1u_ip')
        fields['sgi_ip'] = self.get_ip_address('sgi_network', VSPGWUTenant, 'sgi_ip')

        return fields

    def get_values_for_ng4t_wo_sdncontroller(self):
        fields = {}
        fields['scenario'] = "ng4t_without_sdncontroller"
        # for interface.cfg file
        fields['zmq_sub_ip'] = "127.0.0.1"
        fields['zmq_pub_ip'] = "127.0.0.1"
        fields['dp_comm_ip'] = self.get_ip_address('spgw_network', VSPGWUTenant, 'dp_comm_ip')
        fields['cp_comm_ip'] = self.get_ip_address('spgw_network', VSPGWCTenant, 'cp_comm_ip')
        fields['fpc_ip'] = "127.0.0.1"
        fields['cp_nb_server_ip'] = "127.0.0.1"

        # for cp_config.cfg file
        fields['s1u_ip'] = self.get_ip_address('s1u_network', VSPGWUTenant, 's1u_ip')
        fields['sgi_ip'] = self.get_ip_address('sgi_network', VSPGWUTenant, 'sgi_ip')

        return fields

    def get_values_for_spirent_w_sdncontroller(self):
        fields = {}
        fields['scenario'] = "ng4t_with_sdncontroller"
        # for interface.cfg file
        fields['zmq_sub_ip'] = self.get_ip_address('sbi_network', SDNControllerServiceInstance, 'zmq_sub_ip')
        fields['zmq_pub_ip'] = self.get_ip_address('sbi_network', SDNControllerServiceInstance, 'zmq_pub_ip')
        fields['dp_comm_ip'] = self.get_ip_address('sbi_network', VSPGWUTenant, 'dp_comm_ip')
        fields['cp_comm_ip'] = self.get_ip_address('nbi_network', VSPGWCTenant, 'cp_comm_ip')
        fields['fpc_ip'] = self.get_ip_address('nbi_network', SDNControllerServiceInstance, 'fpc_ip')
        fields['cp_nb_server_ip'] = self.get_ip_address('nbi_network', VSPGWCTenant, 'cp_nb_server_ip')

        # for dp_config.cfg file
        fields['s1u_ip'] = self.get_ip_address('s1u_network', VSPGWUTenant, 's1u_ip')
        fields['sgi_ip'] = self.get_ip_address('sgi_network', VSPGWUTenant, 'sgi_ip')

        return fields

    def get_values_for_spirent_wo_sdncontroller(self):
        fields = {}
        fields['scenario'] = "ng4t_without_sdncontroller"
        # for interface.cfg file
        fields['zmq_sub_ip'] = "127.0.0.1"
        fields['zmq_pub_ip'] = "127.0.0.1"
        fields['dp_comm_ip'] = self.get_ip_address('spgw_network', VSPGWUTenant, 'dp_comm_ip')
        fields['cp_comm_ip'] = self.get_ip_address('spgw_network', VSPGWCTenant, 'cp_comm_ip')
        fields['fpc_ip'] = "127.0.0.1"
        fields['cp_nb_server_ip'] = "127.0.0.1"

        # for cp_config.cfg file
        fields['s1u_ip'] = self.get_ip_address('s1u_network', VSPGWUTenant, 's1u_ip')
        fields['sgi_ip'] = self.get_ip_address('sgi_network', VSPGWUTenant, 'sgi_ip')

        return fields

    def has_venb(self):
        # try get vMME instance
        try:
            instance_id = self.get_instance_id(VENBServiceInstance)
        except Exception:
            self.log.debug('VENBServiceInstance not found')
            return False

        return True

    def has_vmme(self):
        # try get vMME instance
        try:
            instance_id = self.get_instance_id(VMMETenant)
        except Exception:
            self.log.debug('VMMETenant not found')
            return False

        return True

    def has_sdncontroller(self):
        # try get vMME instance
        try:
            instance_id = self.get_instance_id(SDNControllerServiceInstance)
        except Exception:
            self.log.debug('SDNControllerServiceInstance not found')
            return False

        return True

    def has_vspgwu(self):
        # try get vMME instance
        try:
            instance_id = self.get_instance_id(VSPGWUTenant)
        except Exception:
            self.log.debug('VSPGWU not found')
            return False

        return True

    def has_internetemulator(self):
        # try get vMME instance
        try:
            instance_id = self.get_instance_id(InternetEmulatorServiceInstance)
        except Exception:
            self.log.debug('InternetEmulator instance not found')
            return False

        return True

    # Which scenario does it use among Spirent or NG4T?
    def get_scenario(self):
        # try get vENB instance: one of both Spirent and NG4T
        venb_flag = self.has_venb()
        vmme_flag = self.has_vmme()
        sdncontroller_flag = self.has_sdncontroller()
        vspgwu_flag = self.has_vspgwu()
        internetemulator_flag = self.has_internetemulator()

        if vmme_flag and venb_flag and sdncontroller_flag and vspgwu_flag and internetemulator_flag:
            return 'ng4t_with_sdncontroller'

        if vmme_flag and venb_flag and (not sdncontroller_flag) and vspgwu_flag and internetemulator_flag:
            return 'ng4t_without_sdncontroller'

        if (not vmme_flag) and venb_flag and sdncontroller_flag and vspgwu_flag and (not internetemulator_flag):
            return 'spirent_with_sdncontroller'

        if (not vmme_flag) and venb_flag and (not sdncontroller_flag) and vspgwu_flag and (
        not internetemulator_flag):
            return 'spirent_without_sdncontroller'

        return 'manual'

    def get_ip_address(self, network_name, service_instance, parameter):

        try:
            net_id = self.get_network_id(network_name)
            ins_id = self.get_instance_id(service_instance)
            ip_address = Port.objects.get(network_id=net_id, instance_id=ins_id).ip
        except Exception:
            self.log.error("Failed to fetch parameter", parameter = parameter, network_name = network_name)
            self.defer_sync("Waiting for parameters to become available")

        return ip_address

    # To get each network id
    def get_network_id(self, network_name):
        return Network.objects.get(name=network_name).id

    # To get service_instance (assumption: there is a single instance for each service)
    def get_instance_id(self, serviceinstance):
        instances = serviceinstance.objects.all()
        instance_id = instances[0].instance_id
        return instance_id
