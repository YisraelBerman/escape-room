const events = [
    { id: 1, name: 'מעיין חרוד - מלחמת גדעון', date: '2021-01-01' },
    { id: 2, name: 'עין אפק -מלחמת ישראל בפלישתים', date: '2021-03-15' },
    { id: 3, name: 'עין גדי -דוד בורח משאול', date: '2021-05-22' },
    { id: 4, name: 'מעיין השילוח - בניית נקבת חזקיהו', date: '2021-07-30' },
    { id: 5, name: 'מעיין הכפר פקיעין - רשב"י בורח מהרומאים', date: '2021-09-10' },
    { id: 6, name: 'מעיין חרוד - הקרב בין הממלוכים למונגולים', date: '2021-11-25' },
    { id: 7, name: 'עין אלרועי - בניית רכבת העמק', date: '2022-02-14' },
    { id: 8, name: 'עיו השופט  ומעיין צבי - מבצע חומה ומגדל', date: '2022-04-01' },
    { id: 9, name: 'עין צובה - מבצע דני', date: '2022-06-20' },
    { id: 10, name: 'אילת - דגל הדיו', date: '2022-08-05' }
];

const groups = [
    { name: 'נחל', color: 'אדום' },
    { name: 'אגם', color: 'כחול' },
    { name: 'באר', color: 'ירוק' },
    { name: 'בור', color: 'צהוב' },
    { name: 'ים', color: 'סגול' },
    { name: 'מעין', color: 'כתום' },
    { name: 'גב', color: 'ורוד' },
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
        showPopup(); // Call a new function to show the popup with group selection
        result.style.display = 'none'; // Hide the result message
    } else {
        const correctPositions = orderedEvents.map((id, index) => id === correctOrder[index] ? '✔️' : '❌');
        result.textContent = `Try again! Here's what you got: ${correctPositions.join(' ')}`;
        result.style.color = 'black'; // Explicitly set the text color
        result.style.display = 'inline-block'; // Show the result message
    }
});

function showPopup() {
    popup.style.display = 'block';

    const selectGroup = document.getElementById('selectGroup');
    selectGroup.innerHTML = `<option value="" disabled selected>שם הקבוצה:</option>` +
        groups.map(group => `<option value="${group.name}">${group.name}</option>`).join('');

    selectGroup.addEventListener('change', function() {
        const selectedGroup = groups.find(group => group.name === this.value);
        showColorPopup(selectedGroup.color);  // Show the new popup with the color
    });
}

function showColorPopup(color) {
    popup.style.display = 'none'; // Close the initial popup
    const colorPopup = document.createElement('div');
    colorPopup.classList.add('popup');
    colorPopup.innerHTML = `
        <div class="popup-content">
            <p>הצבע שלכם הוא  ${color}</p>
            <button id="closeColorPopup">Close</button>
        </div>
    `;
    document.body.appendChild(colorPopup);
    colorPopup.style.display = 'block';

    document.getElementById('closeColorPopup').addEventListener('click', () => {
        colorPopup.style.display = 'none';
    });
}
