from tool_sandbox.common.tool_discovery import ToolBackend
from tool_sandbox.scenarios import named_scenarios


#%%
scenarios = named_scenarios(ToolBackend.DEFAULT)
#%%
(print(scenarios.keys()))
#%%
gs = scenarios["get_cellular"]
#%%
type(gs)

#%%
from tool_sandbox.cli.utils import run_scenario

