# AI Travel Assistant – Core AI Logic

## Overview
This repository showcases core AI logic inspired by a real-world travel assistant project. The focus is on building a more intelligent and context-aware chatbot for travel recommendations.

## Key Features

### 1. Manual Travel Filtering
- Designed and improved manual filtering logic
- Allows users to customize travel preferences
- Integrated with backend data models

### 2. Seasonal Awareness
- Implemented a season detection module
- Enhances travel suggestions based on time of year

### 3. Context-Aware Chatbot (Simulation)
- Designed logic for handling multi-turn conversations
- Maintains conversation state
- Improves response relevance using previous inputs

### 4. Image Integration
- Integrated travel-related images using Unsplash API
- Enhances user experience with dynamic visuals

### 5. Prompt Engineering
- Structured prompts for better AI responses
- Improved intent detection and output clarity

### 6. AI Behavior Control
- Designed system prompts to enforce business rules
- Restricted responses to UAE-based destinations
- Implemented fallback handling for invalid requests

### 7. External API Integration
- Integrated Unsplash API for dynamic travel images
- Implemented fallback mechanism for reliability

### 8. Database & System Design
- Designed relational database models using SQLAlchemy
- Implemented complex relationships between travel entities
- Structured AI responses into database-friendly formats

### 9. AI Prompt Engineering & Response Structuring
- Designed structured prompts to generate consistent JSON outputs
- Enforced strict rules to reduce hallucination
- Implemented post-processing to clean and validate AI responses

### 10. Context-Aware Chatbot System
- Implemented multi-turn conversation support with context tracking
- Designed intent classification (plan / general / irrelevant)
- Built an AI service layer for handling responses and memory
- Optimized conversation history for better performance

## Project Structure
```
detect_season.py        # Season detection logic
chatbot_simulation.py   # Multi-turn conversation handling (simulation)
manual_filter.py        # Travel filtering logic (simplified)
image_fetcher.py        # Fetch images from Unsplash API (simulation)
prompts.txt             # Example structured prompts
```

## Tech Stack
- Python
- FastAPI (conceptual)
- OpenAI API (conceptual)
- Git & GitHub

## Note
This repository is a simplified and non-confidential version of a real project. It is intended to demonstrate core AI concepts and implementation skills.

## Author
Sepideh – AI Developer
