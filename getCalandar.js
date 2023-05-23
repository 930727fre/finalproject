let ourevents = []

const path = "./jsons/";

async function getJSON(url)
{
    const response = await fetch(url).then(res => {
      if(!res.ok) {
        return res.text().then(text => { throw new Error(text) })
       }
      else {
       return res.json();
     }    
    })
    .catch(err => {
       alert("在讀取 json 時發生錯誤");
    });
    for(var i = 0; i < response.length; ++i){
        ourevents.push({id: i,title: response[i]["title"], start: response[i]["start"], end: response[i]["end"]});
    }
}

document.addEventListener('DOMContentLoaded', function() {
    getJSON(path + 'codeforces.json').then
    (data =>{
      getJSON(path + 'zerojudge.json').then
      (data =>{
        getJSON(path + 'leetcode.json').then
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
    })
    
});
