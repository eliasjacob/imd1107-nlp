# IMD1107 - Processamento de Linguagem Natural
## [Dr. Elias Jacob de Menezes Neto](https://docente.ufrn.br/elias.jacob)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)

## Overview

This repository contains the code, resources, and Jupyter notebooks used in the **IMD1107 - Processamento de Linguagem Natural** course.  

The course provides an introduction to the basic concepts and applications of Natural Language Processing (NLP). Emphasis is given to both supervised and unsupervised learning techniques, challenges in processing annotated corpora (especially in Portuguese), and practical applications using state-of-the-art tools and frameworks.

## Table of Contents

- [Overview](#overview)
- [Course Objectives](#course-objectives)
- [Ementa (Syllabus Summary)](#ementa-syllabus-summary)
- [Methodology](#methodology)
- [Evaluation](#evaluation)
- [Course Schedule Overview](#course-schedule-overview)
- [Installation](#installation)
  - [Repository and Dataset Setup](#repository-and-dataset-setup)
  - [Installing Dependencies](#installing-dependencies)
- [Using VS Code Dev Containers](#using-vs-code-dev-containers)
- [Jupyter Notebooks](#jupyter-notebooks)
- [Further Reading and References](#further-reading-and-references)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Contact](#contact)

## Course Objectives

- **Introduce basic concepts and applications of NLP:** Gain an understanding of how natural language can be processed and analyzed.
- **Explore machine learning techniques:** Learn both supervised and unsupervised methods applied to NLP tasks.
- **Practical experience:** Work hands-on with Python code and Jupyter notebooks for solving real-world NLP problems.
- **Familiarization with tools and frameworks:** Get acquainted with modern NLP libraries and annotation tools.

## Syllabus Summary

- **Overview of NLP Challenges:** Discussion on the main difficulties in processing and understanding human language.
- **Annotated Corpora:** Study of language corpora in English and Portuguese, including preprocessing and annotation tools.
- **NLP System Modules:** Exploration of different levels of text processing:
  - Preprocessing and tokenization
  - Syntactic/dependency parsing
  - Semantic and pragmatic analysis, including discourse and coreference resolution
- **Word Representations:** Vector space models and word embeddings.
- **Machine Learning for NLP:** Techniques ranging from classical algorithms to modern deep learning approaches.
- **Practical Applications:** From text classification and sentiment analysis to topic modeling and generative models.

## Teaching Approach

The course employs a **top-down** teaching method, differing from the traditional **bottom-up** approach.

- **Top-Down Method:** We begin with a high-level overview and practical applications, then delve into the details when needed. This helps maintain motivation and offers a clear view of how different components integrate.
- **Bottom-Up Method:** In contrast, this approach involves learning individual components in isolation, which can lead to a fragmented understanding.
- **Collaborative Learning:** In addition to individual assessments, there will be group projects (Bring Your Own Data) that require explanation and discussion of the introduced concepts.

### Example: Learning Baseball
Harvard Professor David Perkins, in his book [Making Learning Whole](https://www.amazon.com/Making-Learning-Whole-Principles-Transform/dp/0470633719), compares learning to playing baseball. Children start by playing the game and gradually learn the rules. Similarly, you will begin with practical applications and gradually uncover the underlying theories.
> **Important:** Initially, focus on what things do rather than all the details about how they work.

## Evaluation

The learning evaluation in this course is **dynamic** and covers the following:
- **Individual Assessments:** Participation, in-class discussions, and a written exam (especially for the third unit).
- **Group Projects:** Two group projects where students work with their own datasets to apply NLP techniques.
- **Attendance:** Minimum 75% presence is required, along with partial averages as defined in the course guidelines.
- The final grade is the arithmetic mean of the scores obtained in the three units.

## Course Schedule Overview

- **Part 1:**
  - Introduction to ML basics and NLP fundamentals.
  - Exploration of text representations and system components.
  - First group project: "Bring your own data" (project presentation).
  
- **Part 2:**
  - NLP applications with machine learning.
  - Topics include text classification, sentiment analysis, and token classification.
  - Second group project: Implementation and project presentation.
  
- **Part 3:**
  - Deep learning for NLP, transfer learning, and advanced architectures (e.g., recurrent networks, transformers).
  - Intelligent agents and NLP pipelines.
  - Written exam as the individual evaluation for this unit.

_For detailed dates and activities, refer to the course [syllabus](Programa_IMD1107.pdf)._

## Installation

Ensure you have a compatible system (Linux, macOS, or Windows 10+ with WSL recommended) and Python 3.12 or higher.

### Repository and Dataset Setup

1. **Clone the Repository:**

    ```shell
    git clone https://github.com/eliasjacob/imd1107-nlp.git
    cd imd1107-nlp
    ```

2. **Run the Download Script:**

    This script downloads necessary datasets and binaries needed for the course:

    ```shell
    bash download_datasets_and_binaries.sh
    ```

3. **Install Ollama:**

    Download and install Ollama from [here](https://ollama.com/download).

4. **Download LLama 3.1:**

    ```shell
    ollama pull llama3.1
    ```

### Installing Dependencies

- **For GPU Support:**

    ```shell
    poetry install --sync -E cuda --with cuda
    poetry self add poetry-plugin-shell
    poetry shell
    ```

- **For CPU-only Support:**

    ```shell
    poetry install --sync -E cpu
    poetry self add poetry-plugin-shell
    poetry shell
    ```

5. **Authenticate Weights & Biases (Optional):**

    If using Weights & Biases for experiment tracking:

    ```shell
    wandb login
    ```

## Using VS Code Dev Containers

To ensure a consistent environment:

1. **Install [Visual Studio Code](https://code.visualstudio.com/)** and the **[Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)**.
2. Open the repository in VS Code.
3. Click **"Reopen in Container"** when prompted or use the command palette and run **"Remote-Containers: Reopen in Container"**.
4. Wait for the Docker container to build the environment automatically.

## Jupyter Notebooks

The course makes extensive use of Jupyter notebooks for hands-on coding sessions and practical exercises. 

## Contributing

Contributions to the course repository are welcome! To contribute:

1. **Fork the Repository.**
2. Create a new branch:

    ```shell
    git checkout -b feature/YourFeature
    ```

3. Make your changes.
4. Commit your changes:

    ```shell
    git commit -m 'Add feature or update content'
    ```

5. Push to your branch:

    ```shell
    git push origin feature/YourFeature
    ```

6. Submit a Pull Request.

## License

This course and its materials are a resource made possible by the investment of Brazilian taxpayers in public education. Your access to this educational opportunity is a direct result of their collective contribution.

As you learn and benefit from this course, please remember the broader community that supports institutions like our Federal University. I encourage you to honor this opportunity by using your education to contribute positively to society and to share your knowledge openly whenever possible.

This course is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details. Let's pay it forward by sharing what we learn!


## Contact

For any questions or feedback regarding the course materials or repository, please [contact me](mailto:elias.jacob@ufrn.br).

If you wish to provide anonymous feedback, use the [Google Forms feedback link](https://jacob.al/feedbacks).