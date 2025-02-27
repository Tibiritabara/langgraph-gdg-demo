# From Zero to Hero: AI Agents and Multi-Agents

This repository contains code examples and tutorials demonstrating how to build AI agents and multi-agent systems using LangChain and LangGraph.

## About

This material was presented at the Google Developers Group (GDG) Berlin event on February 27th, 2025. The presentation titled "From Zero to Hero: AI Agents and Multi-Agents" focused on demonstrating practical applications of LangChain and LangGraph for building AI agents.

## Presentation

The presentation slides are available in the [docs folder](./docs/GDG.pdf). This presentation covers:

- Introduction to AI agents
- Single-agent vs multi-agent architectures
- Practical implementation examples using LangChain and LangGraph

## Project Setup

This project uses [UV](https://github.com/astral-sh/uv) for fast, reliable Python package management.

### Prerequisites

- Python 3.8 or higher
- UV package manager

### Installing UV

To install UV, run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installing Dependencies

To install project dependencies using UV:

```bash
uv sync
```

## Repository Structure

The repository is organized as follows:

- **docs/** - Contains the presentation materials
  - [GDG.pdf](./docs/GDG.pdf) - Presentation slides from the GDG Berlin event
- **notebooks/** - Contains Jupyter notebooks with code examples
  - [single-agent.ipynb](./notebooks/single-agent.ipynb) - Examples of single-agent implementations using LangChain
  - [multi-agent.ipynb](./notebooks/multi-agent.ipynb) - Examples of multi-agent systems using LangGraph
- **src/** - Contains source code for the project
  - **main.py** - Entry point for the application
  - **services/** - Service-related code
    - **gql/** - GraphQL service implementations including clients for GitHub API
  - **tools/** - Tool implementations
    - **github.py** - GitHub-related tools
    - **types.py** - Type definitions
  - **queries/** - GraphQL query definitions
    - **GitHub.graphql** - GraphQL queries for GitHub API

## Getting Started

After installing the dependencies, you can run the Jupyter notebooks to explore the examples:

```bash
jupyter notebook notebooks/
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
