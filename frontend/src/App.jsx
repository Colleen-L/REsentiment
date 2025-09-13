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
      <h1>Company Rebranding Sentiment Analysis</h1>
      <input
        type = "text"
        placeholder = "company name"
        value = {company}
        onChange={(e) => setCompany(e.target.value)}
      />

      <button onClick={handleAnalysis} disabled = {loading || !company}>
        {loading ? "Analyzing..." : "Analyze Sentiment"}
      </button>
     

      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>Result for: {result.company}</h2>
          <p>Sentiment: {result.sentiment.label}</p>
          <p>Score: {result.sentiment.score.toFixed(2)}</p>
        </div>
      )}
    </>
  )
}

export default App;
