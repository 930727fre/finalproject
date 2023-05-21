let ourevents = []
async function getJSON(url)
{
    const response = await fetch(url);
    const json = await response.json();
    console.log(json)
    for(var i = 0; i < json.length; ++i)
        ourevents.push({id: i,title: json[i]["title"], start: json[i]["start"], end: json[i]["end"]});
    ourevents.push({title: "Codeforces Round (Div. 1)", start: "2023-05-09T03:15:10", end: "2023-05-09T03:15:10"});
}

document.addEventListener('DOMContentLoaded', function() {
    getJSON('./z.json').then
    (data =>{
      getJSON('./ze.json').then
      (data =>{
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: 'dayGridMonth',
          //高度設置
          height:'100%',
          locale: 'zh-tw',
          navLinks: true,
          //dayMaxEvents: true,
          headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek'
          },
          
          events: ourevents,
          
          //讓月曆中的時間不要被文字切到
          //arg儲存了這個event的資訊
          eventContent: function(arg) {
            return {
              html: '<div class="event-content">' +
                    '<div class="event-time">' + formatTime(arg.event.start) + '</div>' +
                    '<div class="event-title">' + arg.event.title + '</div>' +
                    '</div>'
            };
          },
          //解決title超出格子的問題
          eventDidMount: function(info) {
            //info.el: 代表事件的 DOM 元素，並儲存於eventElement
            //eventTitle儲存現在事件的title
            var eventElement = info.el;
            var eventTitle = info.event.title;
            //如果事件的title長度超過了月曆每一格的大小，我就給予他一個新個div分類，並在css對他做改變(換行)
            if (eventElement.offsetWidth < eventElement.scrollWidth) {
              eventElement.querySelector('.event-title').classList.add('event-title-overflow');
            }
          }
        });
        function formatTime(date) {
          //24小時制
          //抓取時間，讓分鐘保持2位數
          return date.getHours() + ':' + ('0' + date.getMinutes()).slice(-2);
        }
        

        console.log(ourevents);
        calendar.render();
      })
    })
    
});
