import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import CaseList from "./pages/CaseList";
import CaseCreate from "./pages/CaseCreate";
import CaseDetail from "./pages/CaseDetail";

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: "10px", background: "#eee" }}>
        <Link to="/" style={{ marginRight: "15px" }}>Cases</Link>
        <Link to="/create">Create Case</Link>
      </nav>

      <Routes>
        <Route path="/" element={<CaseList />} />
        <Route path="/create" element={<CaseCreate />} />
        <Route path="/cases/:id" element={<CaseDetail />} />
      </Routes>
    </BrowserRouter>
  );
}
