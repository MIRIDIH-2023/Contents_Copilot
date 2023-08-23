import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from core.JF_PT import JF_PT_Prompt
import json

# ==============================================
# Scenario
# 1. User enter a topic
# 2. Suggest some specific subtopics related to user's query
# 3. User select subtopics and ask again to the AI service
# 4. generate contents
# ==============================================

JF_PT_prompt = JF_PT_Prompt(
    model_name="text-davinci-003",
    creative_temperature=0.7,
    informatic_temperature=0.1
)

# Scenario 1. User enter a topic
main_topic = input("What is topic do you want to generate?: ")
while True:
    # Scenario 2. Suggest some specific subtopics related to user's query
    out = JF_PT_prompt.getContentsOfTable(query=main_topic)
    print("Entered Topic:", out.main_topic)
    print("Recommended subtopics")
    for t in out.sub_topic:
        print(t)

    # Scenario 3. User select subtopics
    ask_edit = input("Edit subtopics or Generate?, Press E(edit) or G(generate)\n")
    if ask_edit.lower() == 'e' :
        print("If you complete, press G(generate)")
        ans = input(f"Main Topic ({out.main_topic}): ")
        if ans != "": 
            main_topic = ans
            print("Regenerate")
            continue
        sub_topics = []
        while ans.upper() != 'G':
            if ans != "" : sub_topics.append(ans)
            ans = input()
            
        out.sub_topic = sub_topics
        break
    else :
      break

print("====== Let's Generate!! ======")
# Scenario 3. ask again to the AI service
reference = [out.source]
result = {"Generation": []}
table_contents = [out.main_topic]
table_contents.extend(out.sub_topic)
result["Generation"].append({
    "table_of_contents": table_contents
})

for topic in out.sub_topic:
    out = JF_PT_prompt.getContents(query=topic)
    result["Generation"].append({
        "topic": out.topic,
        "keywords": out.keywords,
        "contents": out.contents,
    })
    reference.append(out.source)
    
result["Generation"].append({
    "reference": reference
})

# 4. generate contents
file_path = "../generation/scenario_format_en.json"

with open(file_path, 'w', encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent='\t')