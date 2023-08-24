import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./views/homeView.jsx";
import Detail from "./views/detailView.jsx";
import Error from "./views/errorView.jsx";
import Login from "./../src/components/Login.jsx";
import { Navbar } from "./components/Navbar.jsx";
import "./App.css";

function App() {

  return (
    <BrowserRouter basepath="/">
      <Navbar/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/detail/:resource/:id" element={<Detail />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<Error />} />
        </Routes>
    </BrowserRouter>
  )
}

export default App;
