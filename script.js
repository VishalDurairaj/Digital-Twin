function toggleDevice(id, currentStatus) {
    fetch("/toggle", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({id: id, status: currentStatus})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById(`status-${data.id}`).innerText = data.status;
    });
}
