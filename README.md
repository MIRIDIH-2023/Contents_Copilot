# Contents Generator with GPT-model

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white")

### Setup `python` environment
```
conda create -n PE python=3.11.4
```
### Install other dependencies
```
pip install -r requirements.txt
```
> Install chromadb for Wikipedia
> If you meet error, check this out: 
  <https://github.com/chroma-core/chroma/issues/189#issuecomment-1454418844>

## Repository Structure
``` bash
.
│  .env                     # OPENAI_API_KEY=<Your own API key>
│  .gitignore
│  README.md
│  requirements.txt
│
├─core
│  │  FewShotCoT.py
│  │  JF_PT.py
│  │  __init__.py
│  │
│  ├─common
│  │  │  utils.py
│  │
│  ├─few_shot_example
│  │  │  examples.py
│  │  │  __init__.py
│
├─demo
│     few_shot.py
│     ReAct_Doc.py
│     scenario.py
│     scenario2.py
│
└─generation
      fewShot_format_en.json
      scenario2_format_en.json
      scenario_format.json
      scenario_format_en.json
