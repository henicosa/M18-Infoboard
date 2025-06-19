async function fetchCalendar(calendar_name) {
    try {
        const response = await fetch(calendar_name + '.ics');
        const icalData = await response.text();
        return icalData;
    } catch (error) {
        console.error('Error fetching calendar:', error);
        return null;
    }
}

function getTodayEvents(events, calendar_name, calendar_url) {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);

    // Expand recurring events
    const expandedEvents = events.flatMap(event => {
        if (event.isRecurring()) {
            const iterator = event.iterator();
            const occurrences = [];
            let next;
            while ((next = iterator.next())) {
                const occDate = next.toJSDate();
                if (occDate >= tomorrow) break;
                if (occDate >= today && occDate < tomorrow) {
                    const occurrence = event.getOccurrenceDetails(next);
                    occurrences.push({
                        summary: event.summary,
                        startDate: occurrence.startDate,
                        endDate: occurrence.endDate,
                        calendar_name: calendar_name,
                        calendar_url: calendar_url,
                        uid: event.uid
                    });
                }
            }
            return occurrences;
        } else {
            const startDate = event.startDate.toJSDate();
            if (startDate >= today && startDate < tomorrow) {
                return [{
                    summary: event.summary,
                    startDate: event.startDate,
                    endDate: event.endDate,
                    calendar_name: calendar_name,
                    calendar_url: calendar_url,
                    uid: event.uid
                }];
            } else {
                return [];
            }
        }
    });

    return expandedEvents;
}


