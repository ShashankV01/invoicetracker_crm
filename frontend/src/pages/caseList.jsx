import { useEffect, useState } from "react";
import api from "../api";


export default function CaseList() {
const [cases, setCases] = useState([]);


useEffect(() => {
api.get("/cases").then(res => setCases(res.data));
}, []);

return (
<table>
<thead>
<tr>
<th>Invoice</th><th>Amount</th><th>Due Date</th><th>Status</th>
</tr>
</thead>
<tbody>
{cases.map(c => (
<tr key={c.id}>
<td>{c.invoice_number}</td>
<td>{c.invoice_amount}</td>
<td>{c.due_date}</td>
<td>{c.status}</td>
</tr>
))}
</tbody>
</table>
);
}