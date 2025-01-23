#!/usr/bin/env python
import sys
import warnings
import requests
import os
from youtube.crew import Youtube

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    Youtube().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Youtube().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Youtube().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Youtube().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
# Complete the get_video_details method
def get_video_details(self, video_id):
    """Fetch video details using YouTube API."""
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={video_id}&key={os.getenv('YOUTUBE_API_KEY')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            item = data['items'][0]
            return {
                'video_id': video_id,
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'channel_title': item['snippet']['channelTitle'],
                'published_at': item['snippet']['publishedAt'],
                'view_count': item['statistics'].get('viewCount', '0'),
                'like_count': item['statistics'].get('likeCount', '0'),
            }
    return None

# Integrate the scraped data into CrewAI's RAG
def integrate_to_rag(self, video_data):
    """Integrate scraped video data into RAG."""
    # Assuming CrewAI RAG tool has a method for adding knowledge
    knowledge_base = self.crew().knowledge
    for video in video_data:
        knowledge_base.add_entry(
            content=video['description'],
            metadata={
                'title': video['title'],
                'channel': video['channel_title'],
                'views': video['view_count'],
                'likes': video['like_count'],
                'published': video['published_at']
            }
        )
    return "Scraped video data integrated into RAG."

# Chat with the videos
def chat_about_videos(self, query):
    """Chat with the RAG-enhanced knowledge base about the videos."""
    crew_instance = self.crew()
    response = crew_instance.chat(query=query)
    return response

