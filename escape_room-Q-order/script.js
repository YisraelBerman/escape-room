const events = [
    { id: 1, name: 'Event 1', date: '2021-01-01' },
    { id: 2, name: 'Event 2', date: '2021-03-15' },
    { id: 3, name: 'Event 3', date: '2021-05-22' },
    { id: 4, name: 'Event 4', date: '2021-07-30' },
    { id: 5, name: 'Event 5', date: '2021-09-10' },
    { id: 6, name: 'Event 6', date: '2021-11-25' },
    { id: 7, name: 'Event 7', date: '2022-02-14' },
    { id: 8, name: 'Event 8', date: '2022-04-01' },
    { id: 9, name: 'Event 9', date: '2022-06-20' },
    { id: 10, name: 'Event 10', date: '2022-08-05' }
];

let shuffledEvents = [...events].sort(() => Math.random() - 0.5);

const eventsList = document.getElementById('eventsList');

shuffledEvents.forEach(event => {
    const li = document.createElement('li');
    li.textContent = event.name;
    li.setAttribute('data-id', event.id);
    eventsList.appendChild(li);
});

const submitButton = document.getElementById('submitOrder');
const result = document.getElementById('result');
const popup = document.getElementById('popup');
const closePopup = document.getElementById('closePopup');

// Initialize SortableJS on the eventsList element
new Sortable(eventsList, {
    animation: 150,
});

submitButton.addEventListener('click', () => {
    const orderedEvents = Array.from(eventsList.children).map(li => parseInt(li.getAttribute('data-id')));
    const correctOrder = events.map(event => event.id);
    
    if (JSON.stringify(orderedEvents) === JSON.stringify(correctOrder)) {
        popup.style.display = 'block';
        result.style.display = 'none'; // Hide the result message
    } else {
        const correctPositions = orderedEvents.map((id, index) => id === correctOrder[index] ? '✔️' : '❌');
        result.textContent = `Try again! Here's what you got: ${correctPositions.join(' ')}`;
        result.style.color = 'black'; // Explicitly set the text color
        result.style.display = 'inline-block'; // Show the result message
    }
});

closePopup.addEventListener('click', () => {
    popup.style.display = 'none';
});
