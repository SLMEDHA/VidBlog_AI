from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


## content researcher
blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos" 
    ),
    tools=[yt_tool],
    allow_delegation=True
)

##  writer 
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "engaging narratives that captivate and educate."
    ),
    tools=[yt_tool],
    allow_delegation=False
)