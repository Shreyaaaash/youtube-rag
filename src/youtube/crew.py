from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import requests
import os

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Youtube():
	"""Youtube crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def search_youtube_task(self) -> Task:
		return Task(
			config=self.tasks_config['search_youtube_task'],
		)

	@task
	def scrape_videos_task(self) -> Task:
		return Task(
			config=self.tasks_config['scrape_videos_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Youtube crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

	def search_youtube(self, topic):
		"""Search YouTube for the given topic and return video IDs."""
		url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={topic}&key={os.getenv('YOUTUBE_API_KEY')}&maxResults=20"
		response = requests.get(url)
		videos = response.json().get('items', [])
		return [video['id']['videoId'] for video in videos if 'videoId' in video['id']]

	def scrape_videos(self, video_ids):
		"""Scrape video details and content."""
		video_data = []
		for video_id in video_ids:
			video_data.append(self.get_video_details(video_id))
		return video_data

	def get_video_details(self, video_id):
		"""Fetch video details using YouTube API."""
		# Implement the logic to get video details
		pass

