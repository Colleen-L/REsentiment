import { useState } from 'react'
import './App.css'

function App() {
  const [company, setCompany] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleAnalysis() {
    setLoading(true);
    setResult(null);

    const response = await fetch("http://localhost:8000/analysis", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ company_name: company }),
    })

    const data = await response.json();
    console.log(data);
    setResult(data);
    setLoading(false);
  }

  return (
    <>
      <div className="container">
        <div className="headercontainer">
          <h1 className="title">Company Rebranding Sentiment Analysis</h1>
          <div className="intro">
            <hr></hr>
            <p>Type the name of a company below, and results will appear at the bottom with the overall sentiment of the specified company's rebranding efforts.
            </p>
            <p><b>Tools used:</b></p>
            <p>This website utilizes a FastAPI backend and a React frontend.</p>
            <li>Google Search API... for finding relevant websites and articles</li>
            <li>BeautifulSoup... for HTML parsing</li>
            <li>VADER... for sentiment analysis</li>
            <hr></hr>
          </div>
          <input
            type = "text"
            placeholder = "Enter company name: "
            value = {company}
            onChange={(e) => setCompany(e.target.value)}
          />
          <br></br>
          <button onClick={handleAnalysis} disabled = {loading || !company}>
            {loading ? "Analyzing..." : "Analyze Sentiment"}
          </button>
        </div>
      
        <div className="resultscontainer">
          <h1 className="resultsLabel">RESULTS: </h1>
          {result && (
            <div style={{ marginTop: 20 }}>
              <h2>{result.company}</h2>
              <p>Overall Sentiment: <b>{result.sentiment.label}</b></p>
              <p>Score: <b>{result.sentiment.score.toFixed(2)}</b></p>
              <br></br>
              <h3>Headlines:</h3>
              <ul>
                {result.headlines.map((item, index) => (
                  <li key={index}>
                    <a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a> — <strong>{item.sentiment.label}</strong> ({item.sentiment.score.toFixed(2)})
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </>
  )
}

export default App;
