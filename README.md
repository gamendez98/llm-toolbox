# llm-toolbox


env ANTHROPIC_API_KEY=<YOUR_ANTHROPIC_API_KEY> OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> tool_sandbox --user GPT_4_o_2024_05_13 --agent Claude_3_Haiku --scenario wifi_off

## Call tool sa

```
usage: __init__.py [-h]
                   [--agent {Hermes,Gorilla,MistralOpenAIServer,GPT_3_5_0125,GPT_4_0125,GPT_4_o_2024_05_13,Uniandes_GPT_4_o_2024_05_13,Claude_3_Opus,Claude_3_Sonnet,Claude_3_Haiku,Gemini_1_0,Gemini_1_5,Gemini_1_5_Flash,Cli,Cohere_Command_R,Cohere_Command_R_Plus,Unhelpful}]
                   [--user {GPT_3_5_0125,GPT_4_0125,GPT_4_o_2024_05_13,Uniandes_GPT_4_o_2024_05_13,Cli}]
                   [--preferred_tool_backend {DEFAULT}]
                   [-t | -s [SCENARIOS ...]] [-p PARALLEL] [-o OUTPUT_DIR]

Run all scenarios in the tool sandbox.

optional arguments:
  -h, --help            show this help message and exit
  --agent {Hermes,Gorilla,MistralOpenAIServer,GPT_3_5_0125,GPT_4_0125,GPT_4_o_2024_05_13,Uniandes_GPT_4_o_2024_05_13,Claude_3_Opus,Claude_3_Sonnet,Claude_3_Haiku,Gemini_1_0,Gemini_1_5,Gemini_1_5_Flash,Cli,Cohere_Command_R,Cohere_Command_R_Plus,Unhelpful}
                        Agent type.
  --user {GPT_3_5_0125,GPT_4_0125,GPT_4_o_2024_05_13,Uniandes_GPT_4_o_2024_05_13,Cli}
                        User type.
  --preferred_tool_backend {DEFAULT}
                        Preferred tool backend to use.
  -t, --test_mode       Only run a few scenarios rather than the full suite.
  -s [SCENARIOS ...], --scenarios [SCENARIOS ...]
                        Name of scenarios to run.
  -p PARALLEL, --parallel PARALLEL
                        Max number of processes for running scenarios in
                        parallel.
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        Output base directory.
```