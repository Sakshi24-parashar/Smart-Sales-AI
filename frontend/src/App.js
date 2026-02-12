import "./App.css";
import { useState } from "react";

function App() {
  const [form, setForm] = useState({
    cost: "",
    price: "",
    sold: "",
    discount: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const predict = async () => {
    const res = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        cost: Number(form.cost),
        price: Number(form.price),
        sold: Number(form.sold),
        discount: Number(form.discount)
      })
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1>📊 Smart Sales Predictor</h1>

        <input name="cost" placeholder="Cost Price" onChange={handleChange} />
        <input name="price" placeholder="Selling Price" onChange={handleChange} />
        <input name="sold" placeholder="Units Sold" onChange={handleChange} />
        <input name="discount" placeholder="Discount %" onChange={handleChange} />

        <button onClick={predict}>Predict</button>

        {result && (
          <div className="result">
            <h3>Profit: ₹{result.profit}</h3>
            <h3>{result.trend}</h3>
            <h3>Advice: {result.recommendation}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
