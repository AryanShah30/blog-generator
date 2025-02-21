# Blog Generator with Llama

## Overview

This project is a web application built using Streamlit that generates blog posts based on user input. It utilizes the Llama language model from the `langchain-community` library to create blog content tailored to specific job profiles and word counts.

## Features

- Input a blog topic and specify the desired word count
- Choose a writing style for the blog from predefined options (e.g., Researchers, Data Scientist, Common People)
- Generate and display blog content dynamically

## Requirements

To run this application, you need Python installed along with the following packages:

- sentence-transformers
- uvicorn
- ctransformers
- langchain
- python-box
- streamlit
- langchain-community

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository:

```bash
git clone 
cd 
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Usage

1. Enter the blog topic in the input field
2. Specify the number of words for the blog post
3. Select the desired writing style from the dropdown menu
4. Click the "Generate" button to create the blog post

## Acknowledgments

- Streamlit for the web framework
- Langchain for language model integration
- Ollama for providing the Llama model

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries, suggestions, or feedback, please reach out to: [AryanShah30](https://github.com/AryanShah30)
