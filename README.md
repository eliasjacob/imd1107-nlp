# IMD1107 - Natural Language Processing

## [Dr. Elias Jacob de Menezes Neto](https://docente.ufrn.br/elias.jacob)

This repository contains the code and resources for the course. The course covers a broad spectrum of topics in Natural Language Processing (NLP) and Generative Models, including foundational concepts, advanced architectures, and practical applications.

## Course Topics
Please refer to the [Syllabus](Programa_IMD1107.pdf) for a detailed overview of the course topics and schedule.


## Installation

Follow these steps to set up the environment and dependencies:

1. **Download the Repository**:
    ```shell
    git clone https://github.com/eliasjacob/imd1107-nlp.git
    cd imd1107-nlp
    ```

2. **Run the Download Script**:
    ```shell
    bash download_datasets_and_binaries.sh
    ```

3. **Install Ollama**:
   Download and install Ollama from [here](https://ollama.com/download).

4. **Download LLama 3.1**:
    ```bash
    ollama pull llama3.1
    ```

5. **Install Dependencies**:
 - For GPU support:
    ```shell
    poetry install --sync -E cuda --with cuda
    poetry shell
    ```
    
- For CPU-only support:
    ```shell
    poetry install --sync -E cpu
    poetry shell
    ```

6. **Authenticate Weights & Biases**:
    ```bash
    wandb login
    ```
    
## Using VS Code Dev Containers

This repository is configured to work with Visual Studio Code Dev Containers, providing a consistent and isolated development environment. To use this feature:

1. Install [Visual Studio Code](https://code.visualstudio.com/) and the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

2. Clone this repository to your local machine (if you haven't already):

   ```shell
   git clone https://github.com/eliasjacob/imd1107-nlp.git
   ```

3. Open the cloned repository in VS Code.

4. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

5. VS Code will build the Docker container and set up the development environment. This may take a few minutes the first time.

6. Once the container is built, you'll have a fully configured environment with all the necessary dependencies installed.

Using Dev Containers ensures that all course participants have the same development environment, regardless of their local setup. It also makes it easier to manage dependencies and avoid conflicts with other projects.

## Getting Started

Once the environment is set up, you can start exploring the course materials, running code examples, and working on the practical exercises.

### Notes

- Some parts of the code may require a GPU for efficient execution. If you don't have access to a GPU, consider using Google Colab.

## Teaching Approach

The course will use a **top-down** teaching method, which is different from the traditional **bottom-up** approach. 

- **Top-Down Method**: We'll start with a high-level overview and practical application, then delve into the underlying details as needed. This approach helps maintain motivation and provides a clearer picture of how different components fit together.
- **Bottom-Up Method**: Typically involves learning individual components in isolation before combining them into more complex structures, which can sometimes lead to a fragmented understanding.

### Example: Learning Baseball
Harvard Professor David Perkins, in his book [Making Learning Whole](https://www.amazon.com/Making-Learning-Whole-Principles-Transform/dp/0470633719), compares learning to playing baseball. Kids don't start by memorizing all the rules and technical details; they begin by playing the game and gradually learn the intricacies. Similarly, in this course, you'll start with practical applications and slowly uncover the theoretical aspects.

> **Important**: Don't worry if you don't understand everything initially. Focus on what things do, not what they are. 

### Learning Methods
1. **Doing**: Engage in coding and building projects.
2. **Explaining**: Write about what you've learned or help others in the course.

You'll be encouraged to follow along with coding exercises and explain your learning to others. Summarizing key points as the course progresses will also be part of the learning process.

## Contributing

Contributions to the course repository are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:

    ```shell
    git checkout -b feature/YourFeature
    ```

3. Make your changes.
4. Commit your changes:

    ```shell
    git commit -m 'Add some feature'
    ```

5. Push to the branch:

    ```shell
    git push origin feature/YourFeature
    ```

6. Create a Pull Request.

## Contact

For any questions or feedback regarding the course materials or repository, you can [contact me](mailto:elias.jacob@ufrn.br).