COT_EXAMPLE = [
  {
    "Instruction": "Generate components to explain the Definition of AI. The contents is noun phrase",
    "response": 
      """
      Let's work this out in a step by step way to be sure we have the right answer.
      Are follow up questions needed here: Yes.
      Follow up: What is Definition of AI?
      Intermediate answer: Artificial intelligence (AI) makes it possible for machines to learn from experience, adjust to new inputs and perform human-like tasks.
      Follow up: What summarized contents are above Intermediate answer?
      Intermediate answer: Contents are "Machines to learn from experience", and "Performing human-like tasks"
      So the final answer is: Contents are ["Machines to learn from experience", "Performing human-like tasks"]
      """
  },
  {
    "Instruction": "Generate components to explain the meaning of Social Media. The contents is noun phrase",
    "response": 
      """
      Let's work this out in a step by step way to be sure we have the right answer.
      Are follow up questions needed here: Yes.
      Follow up: What is Definition of Social Media?
      Intermediate answer: Social media refers to digital platforms that enable users to create, share, and interact with content and other users across the internet.
      Follow up: What summarized contents are above Intermediate answer?
      Intermediate answer: Contents are "Digital Platforms", and "Enabling users to create, share, and interact with content and other users"
      So the final answer is: Contents are ["Digital Platforms", "Enabling users to create, share, and interact with content and other users"]
      """
  },
  {
    "Instruction": "아래 형식을 참고해 인공지능의 정의를 설명하는 구성요소를 출력해줘. 이때 내용은 한글로 된 명사구야.",
    "response": 
      """
      Let's work this out in a step by step way to be sure we have the right answer.
      Are follow up questions needed here: Yes.
      Follow up: 인공지능의 정의는 무엇일까?
      Intermediate answer: 인공지능은 컴퓨터에서 음성 및 작성된 언어를 보고 이해하고 번역하고 데이터를 분석하고 추천하는 기능을 포함하여 다양한 고급 기능을 수행할 수 있는 일련의 기술을 뜻한다.
      Follow up: 인공지능의 정의를 요약하자.
      Intermediate answer: 요약한 내용은 "사람의 지능을 모방한 기술", "데이터를 보고 이해, 번역, 분석, 추천할 수 있는 기계".
      So the final answer is: 내용은 ["사람의 지능을 모방한 기술", "데이터를 보고 이해, 번역, 분석, 추천할 수 있는 기계"]
      """
  },
  {
    "Instruction": "아래 형식을 참고해 운동의 종류를 설명하는 구성요소를 출력해줘. 이때 내용은 한글로 된 명사구야.",
    "response": 
      """
      Let's work this out in a step by step way to be sure we have the right answer.
      Are follow up questions needed here: Yes.
      Follow up: 운동의 종류에는 무엇이 있을까?
      Intermediate answer: 운동의 종류는 크게 유산소 운동과 무산소 운동으로 나뉜다.
      Follow up: 유산소 운동에는 무엇이 있을까?
      Intermediate answer: 유산소 운동은 대표적으로 "걷기", "자전거", "수영", "등산" 등이 있다.
      Follow up: 무산소 운동에는 무엇이 있을까?
      Intermediate answer: 무산소 운동은 대표적으로 "웨이트 트레이닝", "팔굽혀 펴기", "윗몸 일으키기" 등이 있다.
      So the final answer is: 내용은 ["유산소 운동", "걷기", "자전거", "수영", "등산", "무산소 운동", "웨이트 트레이닝", "팔굽혀 펴기", "윗몸 일으키기"]
      """
  },
]

  # {
  #   "Instruction": "Generate a table of contents: The table contains specific topics of the AI.",
  #   "response": 
  #     """
  #     Let's work this out in a step by step way to be sure we have the right answer.
  #     Are follow up questions needed here: Yes.
  #     Follow up: Which category does AI belong to?
  #     Intermediate answer: The category of Artificial intelligence (AI) is "technology".
  #     Follow up: What typical subtopics relative to "technology"?
  #     Intermediate answer: Subtopics are "The type of technology", "The impact of technology", and "Ethics in technology" etc.
  #     So the final answer is: Subtopics are ["The type of AI", "The impact of AI", "Ethics in AI", ...]
  #     """
  # },
  # {
  #   "Instruction": "Generate a table of contents: The table contains specific topics of the Social Media.",
  #   "response": 
  #     """
  #     Let's work this out in a step by step way to be sure we have the right answer.
  #     Are follow up questions needed here: Yes.
  #     Follow up: Which category does Social Media belong to?
  #     Intermediate answer: The category of Social Media is "Digital Communication".
  #     Follow up: What typical subtopics relative to "Digital Communication"?
  #     Intermediate answer: Subtopics are "The type of technology", "The impact of technology", and "Ethics in technology" etc.
  #     So the final answer is: Subtopics are ["The type of AI", "The impact of AI", "Ethics in AI", ...]
  #     """
  # }

  # {
  #   "Instruction": "Generate contents to explain the Negative Impact of Social Media",
  #   "response": 
  #     """
  #     Let's work this out in a step by step way to be sure we have the right answer.
  #     Are follow up questions needed here: Yes.
  #     Follow up: What is Social Media?
  #     Intermediate answer: Social media refers to digital platforms that enable users to create, share, and interact with content and other users across the internet.
  #     Follow up: Who use Social Media?
  #     Intermediate answer: People from all over the world
  #     Follow up: What is the negative influence of Social Media on people?
  #     Intermediate answer: People cannot distinguish fake news or information in Social Media. Social Media cannot protect user's Privacy, and can be vulnerable to Security.
  #     Follow up: What keywords are above Intermediate answer?
  #     Intermediate answer: Impacts are "fake news", "Privacy and Security", and "Information Dissemination" etc.
  #     So the final answer is: Impacts are ["fake news", "Privacy and Security", "Information Dissemination"]
  #     """
  # },
  # {
  #   "Instruction": "Generate a table of contents of the Social Media Impact",
  #   "response": 
  #     """
  #     Let's work this out in a step by step way to be sure we have the right answer.
  #     Are follow up questions needed here: Yes.
  #     Follow up: What are some aspects of the impact?
  #     Intermediate answer: Positive impact, Negative impact
  #     Follow up: What fields are affected by Social Media?
  #     Intermediate answer: Individuals' lives, Society, Businesses, Governments etc.
  #     So the final answer is: contents are ["The Positive impact of Social Media on Individuals' lives", "The Negative impact of Social Media on Individuals' lives", ..., The Negative impact of Social Media on Governments]
  #     """
  # },
