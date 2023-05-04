let ourevents = []
async function getJSON(url)
{
    const response = await fetch(url);
    const json = await response.json();
    console.log(json)
    for(var i = 0; i < json.length; ++i)
        ourevents.push({title: json[i]['name'], startTime: json[i]['startTime']});
}

getJSON('./z.json');


document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      initialView: 'dayGridMonth',
      //高度設為自動
      height: '100%',
      locale: 'zh-tw',
      navLinks: true,
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek'
      },
      events: ourevents
    //   events: [
    //     {
    //         title: 'Codeforces Round (Div. 1)',
    //         startTime: '1683547500'
    //     },
    //     {
    //         title: 'test',
    //         start: '2023-05-08',
    //         end: '2023-05-08'
    //     }
    // ]
    });
    calendar.render();
  });
