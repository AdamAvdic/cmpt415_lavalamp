# Data Lava Lamp
**Project Overview**

This project is part of my CMPT 415 Special Research Project, where I developed a web application aimed at making Large Language Model (LLM) data more accessible and user-friendly. The application, hosted via Railway, fetches datasets from Hugging Face and displays them in an interactive, engaging way using a "Lava Lamp" visualization.

The goal is to create a platform where users unfamiliar with LLM data can explore it intuitively. Each bubble in the Lava Lamp contains a snippet of information related to LLM training data. By clicking on a bubble, users can view the data snippet, access its source, and see relevant metadata, such as the date it was fetched.

## Demo
![Demogif](https://github.com/user-attachments/assets/2c4704dc-393c-4a62-958a-1f46c60f8f94)

## Live Demo

Check out the live application: [DataLavaLamp](https://cmpt415lavalamp-production.up.railway.app/)

## Features

- **Interactive Visualization**: A dynamic Lava Lamp-style interface with floating bubbles, each representing a snippet of LLM data.
- **Data Exploration**: Clickable bubbles allow users to:
  - Read the data snippet.
  - Access the original data source.
  - View additional metadata, such as the fetch date.
- **User-Friendly Design**: Simplified interface tailored for non-technical audiences.
- **Railway Hosting**: Deployed using Railway for scalability and accessibility.

## Technology Stack

- **Backend**: Django (Python) for managing application logic and database connections.
- **Frontend**: HTML, CSS, and JavaScript for the interactive Lava Lamp visualization.
- **Database**: Postgres during development, with Railway-hosted SQL for deployment.
- **Hosting**: Railway for seamless deployment and hosting.

## Future Goals

1. **Real-Time Updates**:
   - Automate the fetching and display of new data from Hugging Face or other data repositories.
   
2. **Advanced Filtering**:
   - Introduce filtering options to explore data by categories, tags, or metadata.
