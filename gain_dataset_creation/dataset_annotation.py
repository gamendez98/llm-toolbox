import json
import os
from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

from tool_sandbox.common.execution_context import ExecutionContext, DatabaseNamespace
from tool_sandbox.common.scenario import Scenario
from tool_sandbox.common.tool_discovery import ToolBackend
from tool_sandbox.scenarios import named_scenarios


def get_step_milestone_similarity(execution_context: ExecutionContext, scenario: Scenario) -> list[float]:
    execution_context_clone = deepcopy(execution_context)
    execution_sandbox_length = len(execution_context._dbs['SANDBOX'])
    milestone_similarities = list([0] * execution_sandbox_length)
    for i in range(execution_sandbox_length, 0, -1):
        execution_context_clone._dbs['SANDBOX'] = execution_context_clone._dbs['SANDBOX'][:i]
        try:
            evaluation_clonet = scenario.evaluation.evaluate(
                execution_context=execution_context_clone,
                max_turn_count=scenario.max_messages
            )
            milestone_similarities[i - 1] = evaluation_clonet.similarity
        except:
            print(f"Error in milestone similarity calculation for step {i}")

    return milestone_similarities

def greatest_monotonic_change(values: list[float]) -> float:
    greatest_change = 0
    incrementing = None
    base = values[0]
    for i in range(1, len(values)):
        change = values[i] - base
        incrementing = change > 0 if incrementing is None and change!=0 else incrementing
        if incrementing is None:
            pass
        if incrementing:
            if change >= greatest_change:
                greatest_change = change
            else:
                return greatest_change
        else:
            if change <= greatest_change:
                greatest_change = change
            else:
                return greatest_change
    return greatest_change

def get_milestone_gains(milestone_similarities: list[float]) -> list[float]:
    gains = []
    for i in range(1,len(milestone_similarities)):
        gains.append(greatest_monotonic_change(milestone_similarities[i-1:]))
    return gains


def find_files_by_name(root_path: str, target_name: str):
    """
    Recursively yields paths of files in `root_path` (and subdirectories)
    that have the given `target_name`.
    """
    for entry in os.scandir(root_path):
        if entry.is_file() and entry.name == target_name:
            yield entry.path
        elif entry.is_dir():
            yield from find_files_by_name(entry.path, target_name)

def create_annotated_dataset(existing_dataset_path: str):
    expected_name = 'execution_context.json'
    scenarios = named_scenarios(ToolBackend.DEFAULT)
    for execution_context_file in tqdm(find_files_by_name(existing_dataset_path, expected_name), total=len(scenarios)):
        execution_context_file = Path(execution_context_file)
        destiny_file = execution_context_file.parent / 'annotated_execution_context.json'
        if destiny_file.exists():
            print(f"File {destiny_file} already exists. Skipping.")
            continue
        with open(execution_context_file, "r") as f:
            execution_context_dict = json.load(f)
        execution_context = ExecutionContext.from_dict(execution_context_dict)
        scenario_name = execution_context_file.parent.name
        scenario = scenarios[scenario_name]
        milestone_similarities = get_step_milestone_similarity(execution_context, scenario)
        milestone_gains = get_milestone_gains(milestone_similarities)
        sandbox = execution_context_dict['_dbs']['SANDBOX']
        milestone_gains = [None] + milestone_gains
        for i in range(len(sandbox)):
            sandbox[i]['milestone_gain'] = milestone_gains[i]
            sandbox[i]['milestone_similarity'] = milestone_similarities[i]
        with open(execution_context_file.parent / 'annotated_execution_context.json', "w") as f:
            json.dump(execution_context_dict, f, indent=4)


if __name__ == '__main__':
    existing_dataset_path = 'data/full_scenarios'
    create_annotated_dataset(existing_dataset_path)