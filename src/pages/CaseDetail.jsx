import { useEffect, useState } from "react";
import api from "../api";


export default function CaseDetail({ id }) {
const [data, setData] = useState(null);


useEffect(() => {
api.get(`/cases/${id}`).then(res => setData(res.data));
}, [id]);


if (!data) return null;


return (
<div>
<h2>{data.invoice_number}</h2>
<p>Status: {data.status}</p>
<p>{data.last_follow_up_notes}</p>
</div>
);
}