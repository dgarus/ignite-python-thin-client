# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class IgniteDataTypeProps:
    """
    Add `type_name` and `type_id` properties for all classes and objects
    of Ignite type hierarchy.
    """
    @property
    def type_name(self) -> str:
        """ Binary object type name. """
        return getattr(self, '_type_name', None)

    @property
    def type_id(self) -> int:
        """ Binary object type ID. """
        from pyignite.utils import entity_id

        return getattr(
            self,
            '_type_id',
            entity_id(getattr(self, '_type_name', None))
        )


class IgniteDataTypeMeta(type, IgniteDataTypeProps):
    """
    Class variant of Ignate data type properties.
    """
    pass


class IgniteDataType(metaclass=IgniteDataTypeMeta):
    """
    This is a base class for all Ignite data types, a.k.a. parser/constructor
    classes, both object and payload varieties.
    """
    pass
