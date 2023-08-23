import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from core.JF_PT import JF_PT_Prompt
import json

JF_PT_prompt = JF_PT_Prompt(
    model_name="text-davinci-003",
    creative_temperature=0.7,
    informatic_temperature=0.1
)

# Create Table of Contents
main_topic = input("What is topic do you want to generate?: ")
while True:
    out = JF_PT_prompt.getContentsOfTable(query=main_topic)
    print("Entered Topic:", out.main_topic)
    print("Recommended subtopics")
    for t in out.sub_topic:
        print(t)
        
    ask_edit = input("Edit subtopics or Regenerate or Accept?, Press E(edit) or G(Regenerate) or A(accept)\n")
    if ask_edit.lower() == 'g' : 
      ans = input("Do you want to change Topic?\n(y/n): ")
      if ans.lower() == 'y':
        changed_topic = input("What is topic do you want to generate?: ")
        main_topic = changed_topic
      continue
    elif ask_edit.lower() == 'e':
      print("If you complete, press C")
      ans = input("Table of Contents:\n")
      
      sub_topics = []
      while ans.upper() != 'C':
        if ans != "" : sub_topics.append(ans)
        ans = input()
        
    out.sub_topic = sub_topics
    break

# create json format: Table of Contents
reference = [out.source]
result = {"Generation": []}
table_contents = [out.main_topic]
table_contents.extend(out.sub_topic)
result["Generation"].append({
    "table_of_contents": table_contents
})

# Create Contents of each subtopics
for i, topic in enumerate(out.sub_topic):
  while True:
    out = JF_PT_prompt.getContents(query=topic)
    print(f"{i+1}. Subtopic : {out.topic}")
    print("Generated contents")
    for c in out.contents:
        print(c)
        
    ask_edit = input("Edit contents or Regenerate or Accept?, Press E(edit) or G(Regenerate) or A(accept)\n")
    if ask_edit.lower() == 'g' : 
      continue
    elif ask_edit.lower() == 'e':
      print("If you complete, press C")
      ans = input("Contents:\n")
      
      contents = []
      while ans.upper() != 'C':
        if ans != "" : contents.append(ans)
        ans = input()
        
    out.contents = contents
    
    result["Generation"].append({
        "topic": out.topic,
        "keywords": out.keywords,
        "contents": out.contents,
    })
    reference.append(out.source)
    break
  
# write json result
file_path = "../generation/scenario2_format_en.json"

with open(file_path, 'w', encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent='\t')