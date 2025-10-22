# OpenWebUI - Public Models Index

[![Master Index](https://img.shields.io/badge/Master%20Index-All%20Repositories-purple?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Github-Master-Index)

![alt text](banner.webp)

[![OpenWebUI](https://img.shields.io/badge/Visit-OpenWebUI-blue)](https://openwebui.com) [![My Profile](https://img.shields.io/badge/My-Profile-green)](https://openwebui.com/m/danielrosehill)

*Last Updated: March 20, 2025*

This repository is a collection of AI System Prompts and Assistants that I've been sharing publicly since 2024. Inside, you'll find prompts ready to be used on any compatible AI platform. They're designed to be easily imported into OpenWebUI – just head to the provided URL and click "Import" (after you've set your instance URL in OpenWebUI, which it will remember for next time).

## Table of Contents

- [What's Inside?](#whats-inside)
  - [Temperature Settings](#temperature-settings)
  - [Real Time Information Retrieval And RAG](#real-time-information-retrieval-and-rag)
  - [Vision](#vision)
- [Repository Structure](#repository-structure)
- [Models Index](#models-index)

## What's Inside?

You'll find a mix of tools here, from practical text reformatters and data entry helpers to more specialized, character-based assistants. 

I've kept things straightforward, without getting bogged down in excessive categories or technical jargon. Most AI enthusiasts will instinctively know which models play nicely with RAG pipelines or need external tools. Given how quickly the AI landscape is changing, detailed implementation guides would be outdated in no time!

To keep things simple and focused, I've also left out specific foundation model names and parameter settings. 

### Temperature Settings

For general text-processing, I often have good results with a temperature of 0.3, but feel free to experiment to find what works best for you. 

### Real Time Information Retrieval And RAG

For tasks that need up-to-the-minute information, models like Perplexity Sonar can be really effective because they handle context retrieval so well. I'm hoping more models will move in this direction, making it easier to manage system configurations while boosting information retrieval.

### Vision

Finally, some of the configurations require vision capability, and a few require other multimodal capabilities like audio and video processing. 

My instinct is that within a very short period of time, almost all major LLMs will be multimodal by default. But for now, if you spotted a configuration requires vision, then enable it. 

## Repository Structure

- `source-data/models.csv`: The primary data source containing all model information
- `individual-configs/`: Individual markdown files for each model
- `converted/models.json`: JSON representation of the models data
- `scripts/`: Scripts for maintaining and updating the repository

---

## Models Index

<!-- START_MODEL_INDEX -->
## ADHD Med Travel Researcher

Screens international travel destinations for the legality of a user's ADHD medications, providing information on restrictions, controlled substance status, and links to official government sources. It emphasizes the importance of verifying information and seeking legal advice, as it is not a substitute for professional guidance.

[View in Repo](individual-configs/adhd-med-travel-researcher.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/adhd-med-travel-researcher)

## Agent Orchestration Advisor

Offers expert guidance on designing and implementing effective multi-agent systems. It focuses on providing strategic advice and concrete recommendations for network architecture, best practices, and relevant technologies.

[View in Repo](individual-configs/agent-orchestration-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/agent-orchestration-advisor)

## AI Agent Debugger

Helps users troubleshoot and diagnose issues with their networked AI assistants by analyzing system prompts, model configurations, and RAG performance. It provides tailored recommendations for resolving unexpected behaviors.

[View in Repo](individual-configs/ai-agent-debugger.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-agent-debugger)

## AI Agent Organiser

Helps the user organize their AI assistants into logical teams based on their common purposes and functions, taking into account the user's preferences for team size and output format.

[View in Repo](individual-configs/ai-agent-organiser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-agent-organiser)

## AI Character Development Tips

Helps users refine and optimize their character descriptions for AI personas, ensuring clarity and consistency while retaining all original details. It enriches the provided text with suggestions to create a well-rounded character profile ready for AI development.

[View in Repo](individual-configs/ai-character-development-tips.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-character-development-helper)

## AI Developer Assistance

Provides up-to-date technical guidance on AI-related development projects, offering recommendations for LLMs, vector databases, API integration, and other relevant tools and techniques. It prioritizes current best practices and offers actionable advice, along with links to relevant resources.

[View in Repo](individual-configs/ai-developer-assistance.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-developer-assistance)

## AI Human Operator

Provides periodic random directions to user

[View in Repo](individual-configs/ai-human-operator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-human-operator)

## AI Text Cleanup Utility

Humanises AI generated text and scrubs it for artifacts.

[View in Repo](individual-configs/ai-text-cleanup-utility.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-humanizer)

## AI Tool Finder

Assists users in discovering relevant AI tools by asking clarifying questions to understand their needs and then recommending suitable options with details on functionality, pricing, and website links. It prioritizes suggesting recent tools.

[View in Repo](individual-configs/ai-tool-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ai-tool-finder)

## Alarmist News Bot

Delivers pessimistic news reports, focusing on the most dire and calamitous events worldwide. It emphasizes negative aspects, counters optimism, and amplifies the sense of impending doom to leave the user feeling discouraged.

[View in Repo](individual-configs/alarmist-news-bot.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/alarmist-news-bot)

## Angry Editor On Call

Irritable, pedantic writing assistant that critiques users' writing after insulting it

[View in Repo](individual-configs/angry-editor-on-call.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/angry-editor-on-call)

## API Cost Comparison

Expert at comparing API costs, using web scraping to provide users with up-to-date and cost-effective solutions.

[View in Repo](individual-configs/api-cost-comparison.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/api-cost-comparison)

## API Development Helper

Assists with API development queries

[View in Repo](individual-configs/api-development-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/api-development-helper)

## API Finder

Helps users find appropriate APIs for their projects by considering their specific requirements and constraints. It provides detailed information about each API, including OpenAPI compatibility, and suggests alternative solutions if necessary.

[View in Repo](individual-configs/api-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/api-finder)

## arXiv Digest

Provides news digests about papers that have been published in arXiv

[View in Repo](individual-configs/arxiv-digest.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/arxiv-digest)

## Assertiveness Coach

Roleplay assistant targeted at improving users' assertiveness

[View in Repo](individual-configs/assertiveness-coach.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/assertiveness-coach)

## Automation Workflow Designer

Provides specific recommendations for workflow automations. Should be paired with RAG, live search, or both for optimal performance.

[View in Repo](individual-configs/automation-workflow-designer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/automation-workflow-designer)

## Backup Approach Advisor

Advises upon backup approaches for tech tools

[View in Repo](individual-configs/backup-approach-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/backup-approach-advisor)

## Beer Tap Identifier

Identifies beer taps in a user-provided photograph (requires vision), providing a list of identified beers from left to right, including their description, average rating, and ABV, and offering a recommendation based on the user's preferences if specified.

[View in Repo](individual-configs/beer-tap-identifier.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/beer-tap-identifier)

## BLUF Email Reformatter

Refines email drafts by creating concise subject lines with appropriate prefixes, prepending a brief Bottom Line Up Front (BLUF) summary, and correcting minor errors, all while preserving the original message and structure. It enhances email communication for improved clarity and efficiency.

[View in Repo](individual-configs/bluf-email-reformatter.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/bluf-email-reformatter)

## Body Language Analyst (Image)

Parses images and analyses them on the basis of body language clues

[View in Repo](individual-configs/body-language-analyst-(image).md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/body-language-analyst-image)

## Book Identification Bot

Extracts publication details from images of books, including the title, author, ISBN, publication date, summary, and average Amazon review rating, presenting the information in a clear and organized format.

[View in Repo](individual-configs/book-identification-bot.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/book-identification-bot)

## Boss Update Batcher

Helps users compile, organize, and format updates for their boss. It offers flexible delivery options (single batch or spread out), intelligent grouping and summarization of information, and can even provide daily or weekly digests.

[View in Repo](individual-configs/boss-update-batcher.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/boss-update-batcher)

## Brainstorming Session Summariser

Summarises brainstorming sessions and provides a summary output

[View in Repo](individual-configs/brainstorming-session-summariser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/brainstorming-session-summariser)

## Brand Reliability Assistant

Assesses the reliability of brands by providing objective information on company reputation, location, production history, and ethical practices, enabling users to make informed purchasing decisions. It synthesizes data from reliable sources to present a clear and concise brand profile, empowering users to evaluate brands based on factual information.

[View in Repo](individual-configs/brand-reliability-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/brand-reliability-assistant)

## Brief The Bot

Helps users create and refine creative briefs optimized for AI-driven projects, providing suggestions and rewriting existing briefs for AI readability

[View in Repo](individual-configs/brief-the-bot.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/brief-the-bot)

## Brusque AI

Provides extremely concise responses to user queries, minimizing word count and omitting all unnecessary details. It prioritizes efficiency and directness in its communication.

[View in Repo](individual-configs/brusque-ai.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/brusque-ai)

## Business Idea Capture Utility

Helps users capture and refine their business ideas by prompting for detailed information, identifying potential gaps, and providing a structured summary within a markdown code fence, complete with relevant emojis for increased engagement.

[View in Repo](individual-configs/business-idea-capture-utility.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/business-idea-capture-utility)

## Buy It For Life Picks

Specializes in recommending long-lasting, high-quality products, drawing heavily from the wisdom of the r/BuyItForLife subreddit to provide durable and reliable options, complete with pricing information. It helps users make informed purchasing decisions by offering specific suggestions and addressing potential concerns.

[View in Repo](individual-configs/buy-it-for-life-picks.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/buy-it-for-life-picks)

## Checklist Pro

Checklist Pro generates tailored checklists to ensure the user's safety, preparedness, and completeness across a variety of activities, incorporating safety tips and reminders where relevant. It enhances peace of mind by accounting for all necessary items and precautions in a clear, concise, and context-specific manner.

[View in Repo](individual-configs/checklist-pro.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/checklist-pro)

## Chore Helper

Helps household members manage their chores by providing information from a detailed chore list, including daily, weekly, and one-time tasks for different rooms in the house. It clarifies user requests and offers specific chore descriptions based on the provided list.

[View in Repo](individual-configs/chore-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/chore-helper)

## Cloudflare Helper

Provides expert technical support for Cloudflare, specializing in Cloudflare Access and Cloudflare Tunnel configurations. It helps users troubleshoot issues, understand complex configurations, and implement best practices for securing their resources.

[View in Repo](individual-configs/cloudflare-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/cloudflare-helper)

## Cognitive Distortions Modeller

Explains cognitive distortions as defined in Cognitive Behavioral Therapy (CBT), providing personalized examples based on user-provided scenarios to illustrate how these distortions might manifest in their own thinking. It strictly avoids giving mental health advice and emphasizes its role as an educational tool.

[View in Repo](individual-configs/cognitive-distortions-modeller.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/cognitive-distortions-modeller)

## Company Background Research

Researches and compiles comprehensive background reports on companies, covering aspects such as their history, operations, key personnel, financial performance, and recent news. It synthesizes information from various public sources to provide a structured overview.

[View in Repo](individual-configs/company-background-research.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/company-background-research-helper)

## Company Screener / Red Flag Identifier

Analyzes company reputations by aggregating data from employee reviews, media reports, and public records to identify potential red flags for job seekers. It delivers comprehensive summaries, highlighting key issues related to work environment, employee turnover, and company culture.

[View in Repo](individual-configs/company-screener---red-flag-identifier.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/company-screener--red-flag-identifier)

## Competitive Landscape Analyst

Acts as a Competitive Landscape Analysis Assistant, guiding users through analyzing a specified company's competitors, identifying differentiation factors, and forecasting future trends in the competitive environment, providing a detailed document with an overview of the company, analysis of competitors, a differentiation breakdown, and a forecast of competitive landscape changes.

[View in Repo](individual-configs/competitive-landscape-analyst.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/competitive-landscape-analysis-assistant)

## Context Data Chunker

Identifies and chunks context data from longer source material (for RAG and conetxt)

[View in Repo](individual-configs/context-data-chunker.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/context-data-chunker)

## Context Data Development Helper

Aids the user in expanding their knowledge base by suggesting relevant and specific markdown documents, each representing a distinct piece of contextual information to improve LLM performance.

[View in Repo](individual-configs/context-data-development-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/tech-doc-creator)

## Context Data Extraction Tool

Extracts and structures contextual data from user-provided text, reformatting it for storage in a context database to enhance the performance of large language models. It focuses on identifying relevant factual information and presenting it in a clear, organized manner.

[View in Repo](individual-configs/context-data-extraction-tool.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/context-data-extraction-tool)

## Context Data Interviewer

Conducts an interview with the user to gather data and generate third-person context snippets suitable for vector storage and improving large language model performance.

[View in Repo](individual-configs/context-data-interviewer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/context-data-interviewer)

## Context Developer #3

An updated config for a context data generation assistant

[View in Repo](individual-configs/context-developer-#3.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/context-developer-3)

## CSV To JSON

Converts CSV data, provided as a file or raw text, into a well-structured JSON format. It automatically infers data types and attempts to detect hierarchical relationships, asking for clarification when necessary to ensure accurate representation.

[View in Repo](individual-configs/csv-to-json.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/csv-to-json)

## Data Source Scout

Helps users locate relevant data sources for application development, providing details about cost, access methods, and update frequency. It considers user preferences for data format and budget constraints to present the most appropriate options.

[View in Repo](individual-configs/data-source-scout.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/data-source-scout)

## Data Visualization and Storytelling

Assists users with data visualization projects by suggesting techniques for effective data presentation and storytelling, including specific tools and guidance.

[View in Repo](individual-configs/data-visualization-and-storytelling.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/data-visualization-and-storytelling)

## Database Matchmaker

Helps users select appropriate databases for their applications by asking clarifying questions and providing tailored recommendations with explanations and resources.

[View in Repo](individual-configs/database-matchmaker.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/database-matchmaker)

## Development Prompt Editor

Refines development prompts for AI assistants, ensuring clarity, completeness, and structure to guide the creation of effective software. It proactively identifies ambiguities, suggests missing features, and optimizes the prompt for improved AI performance.

[View in Repo](individual-configs/development-prompt-editor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/development-prompt-editor)

## Dictated Text Doctor

Corrects errors in text likely captured via voice-to-text dictation, including punctuation, capitalization, and word choice. It refines text for clarity and grammatical accuracy, streamlining the editing process for users.

[View in Repo](individual-configs/dictated-text-doctor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/dictated-text-doctor)

## Dimensions Estimator

Estimates dimensions of objects within user-uploaded images by leveraging visible reference points. If a request lacks clarity, it will ask the user to specify the object of interest.

[View in Repo](individual-configs/dimensions-estimator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/dimensions-estimator)

## Disaster Debrief Assistant

Analyzes user accounts of unexpected or dangerous situations, then generates a formal debrief including a summary of the event, recommendations for how the event could have been avoided, and concrete steps the user can take to prevent future occurrences.

[View in Repo](individual-configs/disaster-debrief-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/disaster-debrief-assistant)

## Docker Compose Debugger

Debugs Docker Compose scripts

[View in Repo](individual-configs/docker-compose-debugger.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/docker-compose-debugger)

## Docs Extraction Utility

Extracts and formats technical documentation from provided URLs, delivering it as a Markdown document within a code fence.

[View in Repo](individual-configs/docs-extraction-utility.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/docs-extraction-utility)

## Docs Finder

Retrieves links to technical documentation

[View in Repo](individual-configs/docs-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/docs-finder)

## Document Anonymisation Assistant

Anonymisation tool that obfuscates the identity of named entities

[View in Repo](individual-configs/document-anonymisation-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/document-anonymisation-assistant)

## Email Abbreviation Assistant

Shortens emails

[View in Repo](individual-configs/email-abbreviation-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/email-abbreviator)

## Email Rhymer

Composes rhyming emails

[View in Repo](individual-configs/email-rhymer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/email-rhymer)

## Email Text Extraction Tool

Extracts and formats email content from screenshots or EML files into a clean, human-readable format, presenting key information such as subject, sender, recipient, date, and body text while excluding technical metadata.

[View in Repo](individual-configs/email-text-extraction-tool.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/email-text-extraction-tool)

## Explain This API

Answers user questions about the operation of specific APIs

[View in Repo](individual-configs/explain-this-api.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/explain-this-api)

## Fork This System Prompt

Rewrites system prompts for AI assistants according to user instructions, specializing or generalizing them as needed. It clarifies ambiguities, preserves core functionality, and offers explanations for the changes made.

[View in Repo](individual-configs/fork-this-system-prompt.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/fork-this-system-prompt)

## Geopolitical Relationship Briefer

Provides detailed reports on recent developments in international relations, focusing on bilateral ties between countries or between a country and a geopolitical bloc. It synthesizes information from reputable sources to deliver structured summaries encompassing political, economic, security, and media-related aspects of the relationship.

[View in Repo](individual-configs/geopolitical-relationship-briefer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/geopolitical-relationship-briefer)

## Gifted Adult Helper

Acts as a friendly mental health assistant for adults who self-identify or have recently been identified as gifted, guiding them toward resources and communities to feel more understood.

[View in Repo](individual-configs/gifted-adult-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/gifted-adult-helper)

## Github Markdown Validator

Validates and edits drafted markdown for compliance with Github-flavored Markdown standards

[View in Repo](individual-configs/github-markdown-validator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/github-markdown-validator)

## Hardware Specification Analyst

Analyzes hardware specifications, explains components in layman's terms, and assesses suitability for various use cases.

[View in Repo](individual-configs/hardware-specification-analyst.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/hardware-specification-analyst)

## Home Assistant Copilot

Assists users in configuring their Home Assistant setups by generating YAML code for automations, scenes, and dashboards. It contextualizes its responses based on the user's existing entities and provides compliant, ready-to-use configurations.

[View in Repo](individual-configs/home-assistant-copilot.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/home-assistant-copilot)

## Hostile Interview Simulator

Trains spokespeople by simulating hostile interviews challenging positions and then providing feedback

[View in Repo](individual-configs/hostile-interview-simulator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/hostile-interview-simulator)

## How Do I Install This?

Provides installation instructions when the docs just aren't cutting it.

[View in Repo](individual-configs/how-do-i-install-this?.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/how-do-i-install-this)

## How Do You See Me?

Offers supportive perspectives to users struggling with negative self-perceptions, promoting self-compassion and helping them reframe self-critical thoughts. It emphasizes the importance of professional mental health support when needed, while providing a positive and encouraging counterpoint to negative self-talk.

[View in Repo](individual-configs/how-do-you-see-me?.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/how-do-you-see-me)

## IKEA Product Identifier

Identifies IKEA furniture from user-provided photographs, accounting for variations in product availability by country, and provides links to the product page on the IKEA website when available. It offers potential matches with confidence levels when a definitive identification is not possible.

[View in Repo](individual-configs/ikea-product-identifier.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/ikea-product-identifier)

## Improve My Docs

Helps to write more thorough technical documentation

[View in Repo](individual-configs/improve-my-docs.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/improve-my-docs)

## Inventory Assistant - Product Name To Data

Provides product data from a product name. Useful for cataloging items in an inventory

[View in Repo](individual-configs/inventory-assistant---product-name-to-data.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/inventory-assistant)

## Is There A Self Hosted X?

This system prompt is focused on identifying self-hostable (or on-premises) alternatives to SaaS tools. Note: it explicitly does NOT exclude non-open-source or paid offerings. Tweak the configuration according to your preferences and desires!

[View in Repo](individual-configs/is-there-a-self-hosted-x?.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/is-there-a-self-hosted-x)

## Is This A Sales Pitch?

Attempts to help the user whether unsolicited emails are sincere or spam

[View in Repo](individual-configs/is-this-a-sales-pitch?.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/is-this-a-sales-pitch)

## January 15th 1954

Embodies a persona from January 15th, 1954, offering news updates and reacting to user input about the modern world through the lens of that time period. It maintains a consistent historical context, sharing personal stories and perspectives rooted in the values and experiences of the mid-1950s.

[View in Repo](individual-configs/january-15th-1954.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/january-15th-1954)

## Job Description Evaluator

Reviews job descriptions provided by the user, evaluating them for both positive attributes and potential warning signs regarding exploitative hiring practices or concerning company culture.

[View in Repo](individual-configs/job-description-evaluator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/job-description-assessor)

## JSON Response Tester

Diagnostic utility instructed to always deliver JSON responses

[View in Repo](individual-configs/json-response-tester.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/json-response-tester)

## JSON to CSV

Converts data from JSON to CSV

[View in Repo](individual-configs/json-to-csv.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/json-to-csv)

## Learning Trajectory Plotter

Helps users learn complex technical subjects by creating personalized learning trajectories. It assesses prerequisite knowledge and designs a structured learning plan, breaking the subject down into manageable modules with clear objectives and resources, or focuses on building foundational knowledge if needed.

[View in Repo](individual-configs/learning-trajectory-plotter.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/learning-trajectory-plotter)

## LLM Bias & Censorship Evaulator

Attempts to analyse LLM outputs for evidence of bias and censorship

[View in Repo](individual-configs/llm-bias-&-censorship-evaulator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/llm-bias--censorship-evaulator)

## LLM Configuration Tuner

Offers expert technical guidance on configuring large language models within custom frontends. It provides advice on parameter optimization, explains the trade-offs between different configurations, and ensures an enhanced user experience.

[View in Repo](individual-configs/llm-configuration-tuner.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/llm-configuration-tuner)

## LLM Fine Tune Guide

Guides users through the intricacies of fine-tuning large language models, offering comprehensive information, process-oriented guidance, and tailored strategies to achieve specific fine-tuning objectives. It assists with everything from clarifying goals to troubleshooting common issues, ensuring successful outcomes.

[View in Repo](individual-configs/llm-fine-tune-guide.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/llm-fine-tune-guide)

## LLM Output Evaulator

Analyses the outputs of other LLMs

[View in Repo](individual-configs/llm-output-evaulator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/llm-output-judge)

## Man Page Lookup

Provides manual pages in response to natural language lookups

[View in Repo](individual-configs/man-page-lookup.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/man-page-lookup)

## Marketing Speak Filter

Distills marketing and sales text into factual, technical descriptions by removing claims and unnecessary adjectives, then presents the output in Markdown format.

[View in Repo](individual-configs/marketing-speak-filter.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/marketing-speak-filter)

## MCP Info

Provides information about the model context protocol (MCP)

[View in Repo](individual-configs/mcp-info.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/mcp-info)

## Mechanical Keyboard Shopping Advisor

Offers personalized guidance in selecting mechanical keyboards, beginning with an exploration of the user's typing preferences and culminating in specific keyboard recommendations tailored to their needs. It provides clear explanations of technical terms and switch characteristics, ensuring users can make informed decisions.

[View in Repo](individual-configs/mechanical-keyboard-shopping-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/mechanical-keyboard-shopping-advisor)

## Meeting Agenda Generator

Transforms unstructured meeting details into a structured business agenda, prompting the user for missing information, highlighting urgent action items, and presenting the result in a code fence.

[View in Repo](individual-configs/meeting-agenda-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/meeting-agenda-generator)

## Meeting Minutes Recorder

Formats unstructured meeting notes into organized minutes, requests missing essential information, and highlights noteworthy items, presenting the result in a user-friendly format.

[View in Repo](individual-configs/meeting-minutes-recorder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/meeting-minutes-recorder)

## Meeting Minutes Summariser

Summarmisation agent for extracting action items and summary data from minutes

[View in Repo](individual-configs/meeting-minutes-summariser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/meeting-minutes-summariser)

## MongoDB Helper

Provides assistance with MongoDB

[View in Repo](individual-configs/mongodb-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/mongodb-helper)

## Movie Binge Strategist On Call

Assists in planning out movie-watching binges

[View in Repo](individual-configs/movie-binge-strategist-on-call.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/movie-binge-strategist-on-call)

## Natural Language To CSV

Converts natural language descriptions of data into CSV format, prompting the user for column details and offering output as data or file download.

[View in Repo](individual-configs/natural-language-to-csv.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/natural-language-to-csv)

## Natural Language To JSON

Generates a JSON schema based on the user's natural language description of a desired data structure, clarifying ambiguities as needed.

[View in Repo](individual-configs/natural-language-to-json.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/natural-language-to-json)

## Natural Language To YAML

Converts natural language descriptions of data into YAML format, prompting the user for structure and hierarchy details and offering output as data or file download.

[View in Repo](individual-configs/natural-language-to-yaml.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/natural-language-to-yaml)

## Neo4j Helper

Technical assistant advising upon Neo4j databases and configurations

[View in Repo](individual-configs/neo4j-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/neo4j-helper)

## Neurodivergence Explorer

Offers comprehensive information about neurodiversity, including autism, ADHD, and related conditions, with a focus on modern understanding and strengths-based approaches. It provides resources and fosters a positive, empowering learning experience, tailored to the user's interests and learning style.

[View in Repo](individual-configs/neurodivergence-explorer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/neurodivergence)

## Open Access Data Finder

Aids users in locating open-source datasets relevant to their specified topics, emphasizing the provision of the newest available data and ensuring reliable sourcing. It delivers precise and informative responses in a casual tone, clarifying ambiguous queries to refine search criteria and enhance result accuracy.

[View in Repo](individual-configs/open-access-data-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/open-access-data-finder)

## Open Source Software Finder

Helps to identify open source projects

[View in Repo](individual-configs/open-source-software-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/open-source-tech-finder)

## Open Web UI Assistant

Provides help with Open Web UI with official project resources in system prompt (update periodically or use live search)

[View in Repo](individual-configs/open-web-ui-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/open-web-ui-assistant)

## OpenAPI API Finder

Helps users find OpenAPI-compliant APIs for specific tasks. It provides relevant API names, descriptions, documentation links, and direct links to the OpenAPI JSON manifests, offering alternative solutions if no compliant APIs are found.

[View in Repo](individual-configs/openapi-api-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/openapi-api-finder)

## OpenWebUI Tool Starter

Provides starter code to kickstart Open Web UI Tool Development

[View in Repo](individual-configs/openwebui-tool-starter.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/openwebui-tool-starter)

## OSINT Tools Explorer

Helps the user to locate open source intelligence (OSINT) tools.

[View in Repo](individual-configs/osint-tools-explorer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/osint-tools-explorer)

## Output To Prompt

Experimentary utility intended to test the ability of LLMs to reverse engineer the outputs of other LLMs (or their own outputs!) to guess the user prompt

[View in Repo](individual-configs/output-to-prompt.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/output-to-prompt)

## PCB Identification Assistant

Analyses circuit boards and attempts to identify components

[View in Repo](individual-configs/pcb-identification-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/pcb-identification-assistant)

## Prompt Debugger

Analyzes prompts and model configurations to diagnose why a prompt failed to achieve the user's expectations. It suggests specific improvements to the prompt and, where possible, provides a remediated version for the user to try.

[View in Repo](individual-configs/prompt-debugger.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/prompt-debugger)

## Prompt Library Ideator

Ideates prompt templates to help users build up comprehensive prompting libraries, generating drafts when requested.

[View in Repo](individual-configs/prompt-library-ideator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/prompt-library-ideator)

## Prompt To Tool Ideator

Helps users enhance large language models by identifying limitations in user-provided prompts and recommending external data sources and tools, such as APIs, existing platforms, and RAG pipelines, to overcome those limitations. It focuses on providing fresh, specialized, and real-time data access.

[View in Repo](individual-configs/prompt-to-tool-ideator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/prompt-to-tool-ideator)

## Python - Learn By Example

Helps users learn Python by explaining their provided code, offering both general overviews and detailed explanations of specific functions. It caters to all skill levels, using clear language and practical examples to enhance understanding.

[View in Repo](individual-configs/python---learn-by-example.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/python---learn-by-example)

## RAG Embedding Advisor

Guides users on optimizing embedding and retrieval settings for their datasets within RAG pipelines. It analyzes the data, recommends appropriate settings for vector databases and embedding models, and suggests data reformatting for enhanced retrieval accuracy and efficiency.

[View in Repo](individual-configs/rag-embedding-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://www.openwebui.com/m/danielrosehill/rag-embedding-advisor)

## Random AI Assistant Ideator

Generates random ideas for AI assistants and develops system prompts

[View in Repo](individual-configs/random-ai-assistant-ideator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/random-ai-assistant-ideator)

## Rate This Toilet

Drafts unsolicited feedback letters analyzing random people's toilets

[View in Repo](individual-configs/rate-this-toilet.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/rate-this-toilet)

## Rotten Movie Recommender

Recommends movies celebrated for their awfulness, providing trailers and reasons for their poor reputation. It connects users to the underappreciated world of bad movie appreciation.

[View in Repo](individual-configs/rotten-movie-recommender.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/rotten-movie-recommender)

## Sane AI News Digest

Attempts to provide a more ground-level overview of recent developments in AI

[View in Repo](individual-configs/sane-ai-news-digest.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/sane-ai-news-digest)

## Screenplay This Email Thread

Transforms mundane email threads into engaging screenplays, complete with character development and scene setting. It creatively adapts corporate correspondence into a cinematic format, optionally incorporating user-specified stylistic elements.

[View in Repo](individual-configs/screenplay-this-email-thread.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/screenplay-this-email-thread)

## Screenshot Data Extractor

Data extraction utility which processes screenshots according to user instructions

[View in Repo](individual-configs/screenshot-data-extractor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/screenshot-data-extractor)

## Screenshot To CSV

Generates CSV data from screenshots, preserving a consistent header row

[View in Repo](individual-configs/screenshot-to-csv.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/screenshot-to-csv)

## Screenshot To JSON

Extracts data from screenshots and attempts to provide the data as a JSON array

[View in Repo](individual-configs/screenshot-to-json.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/screenshot-to-json)

## Screenshot To Markdown Table

Converts data in screenshots into markdown table format

[View in Repo](individual-configs/screenshot-to-markdown-table.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/screenshot-to-markdown-table)

## Shakespearean Email Writer

Assists with authoring emails (and other texts) that are slightly Shakespearean (a lighter touch than a previous configuration)

[View in Repo](individual-configs/shakespearean-email-writer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/shakespearean-email-writer)

## Shakespearean Text Generator

Translates text into Shakespearean English, creatively adapting modern terms to fit the era.

[View in Repo](individual-configs/shakespearean-text-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/shakespearean-text-generator)

## Simple OCR

Simple configuration for extracting text from images using vision-capable LLMs.

[View in Repo](individual-configs/simple-ocr.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/simple-ocr)

## Software Evaluation Assistant

Provides comprehensive analyses following a template suitable for both SaaS and open source software valuations.

[View in Repo](individual-configs/software-evaluation-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/software-evaluation-assistant)

## SOP Documentation Generator

Helps users create clear and comprehensive Standard Operating Procedures (SOPs) for both professional and personal use. It can either convert existing text into a structured SOP or guide users through an interview process to gather the necessary information and generate a formatted document.

[View in Repo](individual-configs/sop-documentation-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/standard-operating-procedure-sop-)

## Spell Check (Non-Interactive)

Non-interactive spell checker configuration

[View in Repo](individual-configs/spell-check-(non-interactive).md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/spell-check-non-interactive)

## Standoffish AI Tool

Disagreeable AI bot which takes a contrarian stance to anything the user says

[View in Repo](individual-configs/standoffish-ai-tool.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/standoffish-ai-tool)

## Statistics Checker

Verifies and updates user-provided statistics by searching for more recent data online. It carefully compares sources to ensure accuracy and presents a list of potential updates with source details, dates, values, and direct links.

[View in Repo](individual-configs/statistics-checker.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/statistics-checker-)

## Sustainable Living Advisor

Offers tailored guidance and data-driven insights to empower users in making sustainable lifestyle choices. It analyzes different options, provides actionable steps, and fosters a relentlessly encouraging environment to support users in achieving their sustainability goals.

[View in Repo](individual-configs/sustainable-living-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/sustainable-living-advisor)

## System Prompt Creator - Q&A Workflow

Assistant specialized in constructing general-purpose system prompts by engaging users in a targeted questionnaire to capture their preferences for style, personality, and context, ultimately delivering a refined prompt in Markdown format.

[View in Repo](individual-configs/system-prompt-creator---q&a-workflow.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/system-prompt-creator---qa-workflow)

## System Prompt Depersonaliser

Rewrites system prompts written for a specific user to remove identifying references, instead generalizing the prompt for broader use while flagging any potentially sensitive information.

[View in Repo](individual-configs/system-prompt-depersonaliser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/depersonalised-system-prompt)

## System Prompt Generation Assistant

Generates system prompts tidying up loosely organised drafts by the user. Outputs markdown.

[View in Repo](individual-configs/system-prompt-generation-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/system-prompt-generation-assistant)

## System Prompt Suggester

Ideates complementary system prompts

[View in Repo](individual-configs/system-prompt-suggester.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/system-prompt-suggester)

## Tech Career Pathfinder

Acts as a passionate career guide specializing in technology, particularly AI. It conducts deep interviews to understand user interests and skills, recommending diverse tech careers beyond programming and providing resources for professional growth.

[View in Repo](individual-configs/tech-career-pathfinder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/tech-career-pathfinder)

## Tech Tool Finder

Acts as a skilled software finder, providing tailored recommendations based on user descriptions and clarifying questions to ensure the suggested tools meet their specific needs and preferences. It offers comprehensive information about each recommendation, including features, pricing, and relevant links while prioritizing both popular and niche options and open-source options whenever those have comparable capabilities to commercial software.

[View in Repo](individual-configs/tech-tool-finder.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/tech-tool-finder)

## Technical Documentation Generator

Generates bespoke technical documentation explaining certain processes

[View in Repo](individual-configs/technical-documentation-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/tech-doc-creator)

## Text Editor - Emotional Amplifier

Rewrites to intensify its emotional impact. It uses vivid language, imagery, and sentence structure to make your writing more evocative and emotionally resonant.

[View in Repo](individual-configs/text-editor---emotional-amplifier.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-editor---emotional-amplifier)

## Text Person Changer

Changes the grammatical person in which a text is written

[View in Repo](individual-configs/text-person-changer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-person-changer)

## Text Simplifier

Simplifies text and returns the edited version to the user

[View in Repo](individual-configs/text-simplifier.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-simplifier)

## Text Tense Changer

Converts text between tenses, intelligently prompting the user for clarification when the desired tense is not initially provided.

[View in Repo](individual-configs/text-tense-changer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-tense-changer)

## Text To Image Prompt Debugger

Debugs unsuccessful text to image prompts, providing advice

[View in Repo](individual-configs/text-to-image-prompt-debugger.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-to-image-prompt-debugger)

## Text Word Limit Trimmer

Rewrites text to fit within specific word or character limits, preserving the original meaning and style.

[View in Repo](individual-configs/text-word-limit-trimmer.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/text-word-limit-trimmer)

## The Creativity Coach

This AI assistant fosters the user's creativity by offering encouragement, suggesting diverse creative outlets, and providing relevant resources. It aims to help users understand and maximize their creative potential.

[View in Repo](individual-configs/the-creativity-coach.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/the-creativity-coach)

## The Fake Wine Buff

Suggests insightful questions about wines on a provided list, enabling the user to appear knowledgeable about wine.

[View in Repo](individual-configs/the-fake-wine-buff.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/the-fake-wine-buff)

## The Grocery Helper

Helps with groceries. Requires grocery list as context.

[View in Repo](individual-configs/the-grocery-helper.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/the-grocery-helper)

## The RAG Doctor (Debugger)

Debugging assistant focused on RAG optimisation

[View in Repo](individual-configs/the-rag-doctor-(debugger).md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/the-rag-doctor-debugger)

## Therapy Recommendations

Offers personalized recommendations for therapeutic modalities tailored to individual experiences, preferences, and accessibility, with a focus on providing specific and actionable information to empower informed decisions about mental health.

[View in Repo](individual-configs/therapy-recommendations.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/therapy-recommendations)

## Timesheet Generator

Generates timesheets from narrative descriptions of working hours, accommodating various formats (CSV, table, Markdown) and the ability to update existing timesheets. It infers necessary columns, handles date calculations, and confirms accuracy with the user.

[View in Repo](individual-configs/timesheet-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/timesheet-generator)

## To Do List Creator

Transforms free-form text into organized task lists, identifying tasks, due dates, priorities, and associated details. It can output the task lists in natural language or computer-readable formats like JSON and CSV.

[View in Repo](individual-configs/to-do-list-creator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/to-do-list-generator)

## Tool Finder - SaaS Only

Tech tool finder limited to retrieving SaaS options

[View in Repo](individual-configs/tool-finder---saas-only.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/saas-finder)

## Tool Finder - Self-Hosted & On-Prem



[View in Repo](individual-configs/tool-finder---self-hosted-&-on-prem.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/tool-finder---self-hosted--on-prem)

## Toxic Email Parser



[View in Repo](individual-configs/toxic-email-parser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)]()

## Toxic Email Parser

Aids users in documenting potentially abusive digital communications by providing technical summaries, identifying patterns of abuse, and preserving original messages. It offers trigger warnings and whitespace to protect users from re-traumatization while ensuring accurate record-keeping for legal, therapeutic, or personal purposes.

[View in Repo](individual-configs/toxic-email-parser.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://www.openwebui.com/m/danielrosehill/toxic-email-parser)

## Travel Prep Pro

Meticulously prepares users for trips by offering personalized packing lists, managing travel documents, and providing location-specific advice. It also assists with bookings, insurance, visa requirements, and other essential travel arrangements.

[View in Repo](individual-configs/travel-prep-pro.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/travel-prep-pro)

## User Manual Lookup

Quickly identifies tech products from user descriptions or images and provides direct links to official user manuals and quick start guides. It efficiently gathers necessary details to ensure accuracy and offers alternative solutions when a manual cannot be immediately located.

[View in Repo](individual-configs/user-manual-lookup.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/user-manual-lookup)

## User Tech Doc Creator

Transforms user-provided technical descriptions into structured and formatted reference documentation, suitable for use in wikis or knowledge bases. It focuses on clarity, consistency, and reusability, ensuring that all technical elements are correctly formatted and the information is logically organized.

[View in Repo](individual-configs/user-tech-doc-creator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/technical-documentation-generator)

## Vision Capability Tester

Diagnostic utility intended to help users to probe the utility and limitations of vision-capable models (VLMs).

[View in Repo](individual-configs/vision-capability-tester.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/vision-capability-tester)

## Voice Email Sender

Configuration prepared for integration with contact and email sending tools

[View in Repo](individual-configs/voice-email-sender.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/voice-email-sender)

## Voice Note Journalling Assistant

Converts voice-to-text transcripts into organized journal entries, adding Markdown formatting, correcting typos, and inserting headings for clarity.

[View in Repo](individual-configs/voice-note-journalling-assistant.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/voice-note-journalling-assistant)

## Voice To Development Spec

Helps users develop clear software development instructions from dictated text captures

[View in Repo](individual-configs/voice-to-development-spec.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/voice-to-development-spec)

## Weekly Work Planner

Aids users in crafting detailed weekly work plans by defining objectives, breaking down tasks, prioritizing activities, and identifying necessary resources. It fosters a positive planning experience.

[View in Repo](individual-configs/weekly-work-planner.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/weekly-work-planner)

## Weird AI Bot Photo Generator

Generates unique and intriguing bot avatar images, emphasizing unconventional designs and strange aesthetics. It focuses on creating memorable and visually distinct representations, incorporating unexpected elements and surreal environments.

[View in Repo](individual-configs/weird-ai-bot-photo-generator.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/weird-ai-bot-photo-generator)

## Who Invented This?

Fosters the user's curiosity to tell the story of the people behind amazing inventions

[View in Repo](individual-configs/who-invented-this?.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/who-invented-this)

## Workflow Automation Advisor

Acts as a Workflow Automation Advisor, interviewing users to understand their roles and pain points, then recommending specific tools, software, and workflows to streamline their job functions through automation, with the goal of enabling them to manage automated processes with minimal direct involvement.

[View in Repo](individual-configs/workflow-automation-advisor.md) | 
[![View on OpenWebUI](https://img.shields.io/badge/View%20on-OpenWebUI-blue)](https://openwebui.com/m/danielrosehill/workflow-automation-advisor)

<!-- END_MODEL_INDEX -->
