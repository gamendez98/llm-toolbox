from copy import deepcopy

from tool_sandbox.common.execution_context import ExecutionContext
import json
from tool_sandbox.common.tool_discovery import ToolBackend
from tool_sandbox.scenarios import named_scenarios


#%%
scenarios = named_scenarios(ToolBackend.DEFAULT)

#%%

exec_context_path = "data/agent_gpt-4o-2024-05-13_user_gpt-4o-2024-05-13_09_17_2025_17_26_14/trajectories/wifi_off/execution_context.json"

with open(exec_context_path, "r") as f:
    execution_context_dict = json.load(f)


#%%

execution_context = ExecutionContext.from_dict(execution_context_dict)

#%%

wifi_off = scenarios["wifi_off"]

#%%

evaluation = wifi_off.evaluation.evaluate(
    execution_context=execution_context,
    max_turn_count=wifi_off.max_messages
)

print(evaluation.similarity)

#%%

execution_context_clonet = deepcopy(execution_context)

#%%

execution_context_clonet._dbs['SANDBOX'] = execution_context_clonet._dbs['SANDBOX'][:-4]

#%%

evaluation_clonet = wifi_off.evaluation.evaluate(
    execution_context=execution_context_clonet,
    max_turn_count=wifi_off.max_messages
)

#%%

print(evaluation_clonet.similarity)
