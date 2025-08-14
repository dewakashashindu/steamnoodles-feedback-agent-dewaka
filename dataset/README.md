# SteamNoodles Feedback Agent – Dewaka Shashindu Abeywikrama

## Project Overview

This project implements a multi-agent system for analyzing restaurant customer feedback and visualizing sentiment trends. It consists of two agents:

### Agent 1 – Auto Response Generator

- Detects sentiment (positive/negative/neutral) using a local Hugging Face model.
- Generates polite automated responses to customer feedback.

### Agent 2 – Sentiment Trend Visualizer

- Reads stored feedback from CSV.
- Plots sentiment trends over time using Matplotlib.

## Setup Instructions

1. **Clone the repository**:

```
git clone https://github.com/YOUR-USERNAME/steamnoodles-feedback-agent-dewaka.git
cd steamnoodles-feedback-agent-dewaka
```

2. **Create and activate a virtual environment**:

```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:

```
pip install -r requirements.txt
```

## Running the Agents

### Agent 1 – Feedback Response Generator

```
python agent1_response_generator.py
```

- Enter feedback manually or use the sample CSV.
- Generates polite automated responses based on sentiment.

### Agent 2 – Sentiment Trend Visualizer

```
python agent2_visualizer.py
```

- Reads feedback CSV.
- Outputs sentiment trend plots in the `plots/` folder.

## Project Structure

```
steamnoodles-feedback-agent-dewaka/
│
├─ agent1_response_generator.py    # Agent 1 code
├─ agent2_visualizer.py            # Agent 2 code
├─ sample_feedback.csv             # Example CSV data
├─ requirements.txt                # Python dependencies
├─ README.md
└─ plots/                          # Generated sentiment plots
```

## Author

- **Name**: Dewaka Shashindu Abeywikrama
- **University**: [Your University Name]
- **Year**: [Your Year]

## Summary of Approach

- **Agent 1**: Uses a local Hugging Face sentiment model to classify feedback and generate polite replies.
- **Agent 2**: Reads feedback history and visualizes sentiment trends over time using Matplotlib.
- Both agents can run independently or as a multi-agent system using LangChain.

## Additional Notes

- Ensure your virtual environment is activated before running scripts.
- Replace `YOUR-USERNAME` in the clone URL with your GitHub username.
- You can replace the sample CSV with your own dataset if needed.
- Optional: Include screenshots or a demo video in the repository for better demonstration.

## Submission Instructions

- Upload all files and folders to a public GitHub repository titled: `steamnoodles-feedback-agent-[your-name]`
- Submit the GitHub repository link via the Google Form before August 15, 2025 – 11:59 PM.

## Example Outputs (Optional)

- Sample Sentiment Trend Plot: `plots/sample_plot.png`
- Example Agent 1 Output:

```
Feedback: "The noodles were too salty."
Response: "Thank you for your feedback! We will take note of your comment and improve our recipe."
```

