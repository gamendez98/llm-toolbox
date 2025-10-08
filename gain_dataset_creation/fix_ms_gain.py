import json

from gain_dataset_creation.dataset_annotation import find_files_by_name, get_milestone_gains


def main():
    for file_path in find_files_by_name("data", "annotated_execution_context.json"):
        with open(file_path, "r") as f:
            execution_context_dict = json.load(f)
        sandbox = execution_context_dict['_dbs']['SANDBOX']
        ms_similarities = [entry['milestone_similarity'] for entry in sandbox]
        ms_gains = get_milestone_gains(ms_similarities)
        ms_gains = [None] + ms_gains
        for i in range(len(sandbox)):
            sandbox[i]['milestone_gain'] = ms_gains[i]
        with open(file_path, "w") as f:
            json.dump(execution_context_dict, f, indent=4)


if __name__ == "__main__":
    main()