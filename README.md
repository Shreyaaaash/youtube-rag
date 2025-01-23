# 🎥 YouTube RAG Project

Welcome to the YouTube RAG (Retrieval-Augmented Generation) project! This project leverages the power of AI to search, scrape, and analyze YouTube videos related to AI LLMs (Large Language Models). 

## 🚀 Overview

This project is designed to:
- **Search YouTube** for the latest videos about AI LLMs.
- **Scrape video content** to gather detailed information.
- **Generate reports** based on the scraped data.

The system is built using **Crew AI**, which allows for the orchestration of agents and tasks to perform complex operations seamlessly.

## 📚 Dependencies

This project utilizes the following libraries and APIs:
- **Crew AI**: A framework for building and managing AI agents and tasks.
- **Requests**: For making HTTP requests to the YouTube API.
- **OS**: For environment variable management.
- **YouTube API**: To fetch video details and search for videos.
- **Groq API**: For model integration.

## 🧠 Model Used

- **Llama 3.1**: A powerful language model used for processing and generating text.
  ---
## 🌟 Features

1. **Search YouTube**: The system can search upto 20 latest videos about AI LLMs and return a list of video IDs.
2. **Scrape Video Content**: It scrapes detailed information from the identified videos, including titles, descriptions, and timestamps.
3. **Generate Reports**: The project can generate structured reports based on the scraped data.

## 📄 Example Output

### Search Results
### 1. **Video Search Results** 🎥
The crew successfully identified and retrieved a selection of the most recent and relevant videos related to AI LLMs. This included:
- A diverse range of topics covering advancements, applications, and ethical considerations of AI LLMs. 🌐
- A total of **20 video IDs** collected, showcasing the latest insights from various content creators. 📈

### 2. **Scraped Video Content** 📋
The scraping task yielded structured data from the identified videos, which included:
- **Titles** and **Descriptions**: Captured key insights and summaries of each video. ✍️
- **Channel Information**: Identified the creators behind the content, providing context on their expertise. 👤
- **Engagement Metrics**: Gathered data on view counts and like counts, offering a glimpse into the popularity and reception of the videos. 👍

### 3. **Research Insights** 🔍
The research task compiled a list of the most relevant information about AI LLMs, resulting in:
- **10 Bullet Points** summarizing cutting-edge developments and trends in the field. 📝
- Insights into practical applications and future directions for AI LLMs, aiding in informed decision-making and reporting. 🚀

### 4. **Generated Reports** 📄
The reporting task synthesized the gathered data into a comprehensive report, which included:
- A structured format with main topics and detailed sections for each area of interest. 📊
- Clear and concise presentation of findings, making it easy for stakeholders to understand the implications of the research. 📚

## 🔧 Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Shreyaaaash/youtube-rag.git
cd youtube-rag
pip install -r requirements.txt
```



**Add your `YOUTUBE_API_KEY`,`GROQ_API_KEY`/`OPENAI_API_KEY` into the `.env` file**



## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```


## 📦 Environment Variables

Make sure to set up your environment variables in a `.env` file:

## Results
![image](https://github.com/user-attachments/assets/5645b0af-6001-4af8-a8d5-2ea42036d532)

![image](https://github.com/user-attachments/assets/070db8cf-5a00-47d4-86de-81d7d2791699)




## Understanding Your Crew

The youtube Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
