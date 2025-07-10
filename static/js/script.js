document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.save-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const row = e.target.closest('tr');
            const id = row.dataset.id;
            const cells = row.querySelectorAll('td');
            const data = {
                id: id,
                name: cells[0].innerText.trim(),
                subject: cells[1].innerText.trim(),
                marks: parseInt(cells[2].innerText.trim())
            };

            const response = await fetch('/update_student', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            if (result.status === 'success') {
                alert('Updated successfully');
            }
        });
    });
});
