import { useState } from "react";
import api from "../api";


export default function CaseCreate() {
const [form, setForm] = useState({});


const submit = () => {
api.post("/cases", form).then(() => alert("Case created"));
};


return (
<div>
<input placeholder="Client ID" onChange={e => setForm({...form, client_id: e.target.value})} />
<input placeholder="Invoice Number" onChange={e => setForm({...form, invoice_number: e.target.value})} />
<button onClick={submit}>Create</button>
</div>
);
}