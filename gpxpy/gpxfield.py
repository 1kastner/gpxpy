# -*- coding: utf-8 -*-

# Copyright 2014 Tomo Krajina
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

from . import utils as mod_utils

class GPXFieldHandler:
    """
    Used for to (de)serialize fields with simple field<->xml_tag mapping.
    """
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag

    def from_xml(self, parser, node):
        __node = parser.get_first_child(node, self.tag)
        return parser.get_node_data(__node)

    def to_xml(self, value):
        return mod_utils.to_xml(self.tag, content=value)

def init_gpx_fields(instance):
    for gpx_field in instance.__gpx_fields__:
        setattr(instance, gpx_field.name, None)

def gpx_fields_to_xml(instance, xml):
    for gpx_field in instance.__gpx_fields__:
        value = getattr(instance, gpx_field.name)
        xml += gpx_field.to_xml(value)
    return xml

def gpx_fields_from_xml(instance, parser, node):
    for gpx_field in instance.__gpx_fields__:
        value = gpx_field.from_xml(parser, node)
        setattr(instance, gpx_field.name, value)
