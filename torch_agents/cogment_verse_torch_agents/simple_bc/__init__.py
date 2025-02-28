# Copyright 2021 AI Redefined Inc. <dev+cogment@ai-r.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cogment_verse_torch_agents.simple_bc.tutorial_1 import SimpleBCAgentAdapterTutorialStep1
from cogment_verse_torch_agents.simple_bc.tutorial_2 import SimpleBCAgentAdapterTutorialStep2
from cogment_verse_torch_agents.simple_bc.tutorial_3 import SimpleBCAgentAdapterTutorialStep3
from cogment_verse_torch_agents.simple_bc.tutorial_4 import SimpleBCAgentAdapterTutorialStep4
from cogment_verse_torch_agents.simple_bc.dqn_agent import DQNAgent
from cogment_verse_torch_agents.simple_bc.td3_agent import TD3Agent
# from cogment_verse_torch_agents.simple_bc.td3_agent2 import TD3Agent2

# SimpleBCAgentAdapter = SimpleBCAgentAdapterTutorialStep4
# SimpleBCAgentAdapter = DQNAgent
SimpleBCAgentAdapter = TD3Agent
# SimpleBCAgentAdapter = TD3Agent2
