import React from "react";
import Header from "./Components/Header/Header";
import "./app.css";
import Catalog from "./Components/Catalog/Catalog";

function App() {
  return (
    <div className="App">
      <Header />
      <Catalog />
    </div>
  );
}

export default App;
