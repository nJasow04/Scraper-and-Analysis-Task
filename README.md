# Scraper-and-Analysis-Task

## Project Spec.
Task 1: Data Collection:
Build a scraper to collect reviews, blogs, or conversations for different applications — pick two.
Review: Collect reviews from 100 applications on SideQuest VR.
Forum: Collect all posts from Meta's community forums.
Reddit: Pick two S&P topics (e.g., Android S&P, VR S&P, Machine Learning S&P).
Discord/Telegram: Join 100 channels (preferably about the same topic) and scrape conversation records.
Write documentation describing the logic of your code, the challenges you encountered, and how you solved them.
Deliverable: Scraper code, scraped data, and documentation.

Task 2: Data Analysis:
Analyze the data you collected and identify interesting S&P-related information. Write a report on the data you found (e.g., keywords, reasoning, and why these are important for the topic).
You can perform manual analysis, automation scripts, models or use NLP tools to analyze the data. Please document the reason you chose the tool and why you think it's suitable for this task.
Deliverable: Analysis tool, Analysis report.

Task 3: Report:
Write a report (around 1000 words) summarizing the entire process of completing this task. You can reuse the materials you have for the previous tasks. Please address the following points:
Motivation: What was the motivation for conducting this analysis?
Method: What method did you use? What challenges did you encounter, and how did you design your solution to overcome them?
Analysis: What did you learn from the results? Why is this important, and what can the audience learn from your findings?
Discussion: What are the limitations of your approach? How could you build better tools or use other techniques to address unresolved problems in your task?
References: Any works that you think are relevant or you have used in completing your tasks.

## This Repository
This repository performs the first task of the Project Spec. Running `python sidequest_scraper.py` will scrape the reviews of 100+ apps on the Sidequest Applications page and store the results in sidequest_reviews (dot) csv. Running `python meta-forums.py` will scrape posts from all 8 pages of Meta's Community forums and store them in forums_post (dot) csv.

## Purpose
This was part of a starter task for a cybersecurity lab that I am joining
