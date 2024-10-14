## Tools
Tools are interfaces that an agent, chain, or LLM can use to interact with the world. They combine a few things:
1. The name of the tool
2. A description of what the tool is
3. JSON schema of what the inputs to the tool are
4. The function to call
5. Whether the result of a tool should be returned directly to the user


GPT 4-0 i trained till December 2023 Data . 

Tools:
1. ARXIV - Research Paper
2. WIKI - New Context
3. Documnets Q&A

Tools requires Agents.


## Agents
The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning engine to determine which actions to take and in which order.