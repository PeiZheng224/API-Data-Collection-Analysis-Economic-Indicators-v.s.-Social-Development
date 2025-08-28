# HW3: Remote Data via APIs

This assignment introduces you to **web APIs** and **data collection** for computational social science research. You'll use Python to fetch data from a public API, process the JSON responses, and analyze the results to answer a research question.

---

## Getting Started

1. **Clone this repository** to your local machine
2. **Set up your environment** (see Setup section below)
3. **Choose one API scenario** and start coding

---

**Note:** Examples of API analyses can be found in the example_analyses folder.

## API Scenarios (Choose ONE)

Pick **one** scenario below and complete all requirements:

### Option 1: News Analysis with NewsAPI
**Research Question:** How does news coverage of climate change vary across different sources?

**Your Task:**
- Use the [NewsAPI](https://newsapi.org/) to collect articles about a topic you are interested in
- Fetch articles from at least 3 different news sources
- Compare headline sentiment, article length, and publication frequency
- Analyze patterns: Which sources cover climate change most/least? What are common themes?

### Option 2: Academic Research with Semantic Scholar
**Research Question:** What are the trending topics in computational social science research?

**Your Task:**
- Use the [OpenAlex](https://openalex.org/) API to search for papers
- Collect papers with keywords for a topic you are interested in
- Extract titles, authors, publication years, and citation counts
- Analyze trends: Which topics are growing? Who are the most cited authors?

### Option 3: Economic Data with World Bank API
**Research Question:** How do economic indicators relate to social development?

**Your Task:**
- Use the [World Bank Data API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) (no key required!)
- Collect data on GDP, education, and internet usage for 10+ countries
- Compare economic vs. social indicators over time (2010-2020)
- Analyze patterns: Do wealthier countries have better social indicators?

### Option 4: Reddit Social Analysis with PRAW
**Research Question:** How do different communities discuss the same topic?

**Your Task:**
- Use the [Reddit API via PRAW](https://praw.readthedocs.io/) to collect posts
- Search for the same keyword (e.g., "artificial intelligence") in 3+ different subreddits
- Compare post titles, scores, comment counts, and discussion tone
- Analyze differences: How do tech vs. general vs. academic communities discuss AI?

### Option 5: Choose Your Own API!
**Research Question:** Formulate a research question related to your group project and find a relevant API.

**Your Task:**
- Retrieve at least 1000 entries
- Engage in exploratory analysis of the data

---

## Required Deliverables

Your repository must contain:

### 1. Python Script (`data_collector.py`)
- Functions to fetch data from your chosen API
- Proper error handling for API requests
- Data cleaning and processing functions
- Clear documentation and comments

### 2. Analysis Notebook (`analysis.ipynb`)
- Data exploration and visualization
- Answer your research question with evidence
- At least 2 charts/graphs showing your findings
- Written interpretation of results (markdown cells)

### 3. Data Files
- `raw_data.json` - Raw API responses (first 50-100 records)
- `processed_data.csv` - Cleaned data ready for analysis
- Include a small sample even if you collect more data

### 4. Documentation (`README.md`)
- Replace this file with your project documentation
- Research question and methodology
- API usage summary (endpoints used, data collected)
- Key findings and limitations
- Instructions for running your code

### 5. Requirements and Setup
- `requirements.txt` - List of Python packages needed
- `.env.template` - Template showing required environment variables (without real keys!)
- `.gitignore` - Ensure API keys are not committed

---

## Technical Requirements

### API Usage
- Make at least **50 API requests** to collect meaningful data
- Handle rate limiting appropriately (add delays between requests)
- Include error handling for network issues, missing data, etc.
- Save raw responses to avoid re-downloading during development

### Data Processing  
- Parse JSON responses into structured data
- Clean and standardize the data (handle missing values, normalize formats)
- Create at least one derived variable (e.g., sentiment score, word count, category)
- Export final dataset as CSV for analysis

### Analysis
- Load and explore your processed data
- Create at least 2 visualizations (charts, graphs, plots)
- Answer your research question with quantitative evidence
- Discuss limitations and potential biases in your data

---

## API Key Setup

Most APIs require free registration. **NEVER commit API keys to GitHub!**

### Setup Steps:
1. **Register for your chosen API** and get a free key
2. **Edit `.env` file** in this repo:
   ```bash
   # .env - Replace with real keys
   NEWSAPI_KEY=your_actual_key_here
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_secret
   ```
3. **In your code, load environment variables:**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()  # Load .env file
   api_key = os.getenv('NEWSAPI_KEY')
   if not api_key:
       print("Please set NEWSAPI_KEY in your .env file")
       exit()
   ```

**Important:** The .env file is already in .gitignore, so your real API keys won't be committed to GitHub.

---

## Running Python Script

After editing your `data_collector.py` script, run it on the command line:
```bash
python data_collector.py
```

## Example Analysis Structure

Your `analysis.ipynb` should follow this general structure:

1. **Introduction** - Research question and motivation
2. **Data Collection** - How you gathered the data
3. **Data Exploration** - Basic statistics and patterns
4. **Visualizations** - Charts answering your research question
5. **Findings** - What did you discover?
6. **Limitations** - What are the caveats and biases?

---

## Grading Rubric (20 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **API Integration** | 6 pts | Successfully fetches data, handles errors, respects rate limits |
| **Data Processing** | 4 pts | Cleans data appropriately, creates meaningful derived variables |
| **Analysis & Visualization** | 6 pts | Clear charts, answers research question with evidence |
| **Code Quality** | 2 pts | Well-documented, organized, follows best practices |
| **Documentation** | 2 pts | Clear README, explains methodology and findings |

---

## Tips for Success

**API Best Practices:**
- **Test with small requests first** before collecting lots of data
- **Save raw data immediately** - APIs can change or become unavailable
- **Add delays** between requests (e.g., `time.sleep(1)`) to avoid rate limiting
- **Check status codes** and handle errors gracefully

**Data Processing:**
- **Explore the JSON structure** before writing processing code
- **Handle missing data** - not all API responses have complete information
- **Create helper functions** for repetitive data cleaning tasks

**Analysis:**
- **Start with basic statistics** - counts, averages, distributions
- **Make simple plots first** - bar charts, line graphs, histograms
- **Tell a story** with your data - what's interesting or surprising?

---

## Resources

### API Documentation:
- [NewsAPI Docs](https://newsapi.org/docs)
- [Semantic Scholar API](https://www.semanticscholar.org/product/api)
- [World Bank API Guide](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392)
- [PRAW Documentation](https://praw.readthedocs.io/)

### Python Libraries:
- `requests` - Making HTTP requests
- `json` - Parsing JSON data  
- `pandas` - Data manipulation
- `matplotlib/seaborn` - Data visualization
- `time` - Adding delays between requests
- `python-dotenv` - Loading environment variables securely

---

## FAQ

**Q: Can I use a different API not listed?**  
A: Ask first! It needs to be free, publicly available, and relevant to social science.

**Q: How many requests should I make?**  
A: At least 50, but quality matters more than quantity. Collect enough for meaningful analysis.

**Q: What if I hit rate limits?**  
A: Add delays (`time.sleep()`) between requests and respect the API's rules.

**Q: Can I use the same API as someone else?**  
A: Yes, but you must ask different research questions and do your own analysis.

**Q: What if my API key stops working?**  
A: Most free APIs have daily limits. Plan ahead and don't wait until the last day!

---

## Submission

Your final repository should contain all files listed in "Required Deliverables." We'll grade based on what's in your GitHub repository at the deadline.

**Checklist before submitting:**
- ✅ All code runs without errors
- ✅ API keys are NOT committed (check `.gitignore`)
- ✅ Data files are included and properly formatted
- ✅ Fuctioning data_collector.py script is included
- ✅ Analysis notebook has clear explanations and visualizations
- ✅ README explains your research question and findings

---

**Questions?** Ask in bCourses discussion or come to office hours!