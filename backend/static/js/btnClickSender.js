const btns = document.querySelectorAll('.btn');

function sendEventInfo(event) {

    fetch("/api/events", {
        method: "POST",
        body: JSON.stringify({
            element_id: event.target.id,
            event_type: event.type,
            timestamp: Date.now()
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then((response) => response.json())
    .then((json) => console.log(json.uuid));
}

btns.forEach((item) => {
    item.addEventListener('click', sendEventInfo);
    item.addEventListener('dblclick', sendEventInfo);
})
