const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', () => { resvTab.classList.remove('open'); });


// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []

const selectedDate = {
    year: null,
    month: null,
    day: null,
};


const dateFunc = () => {
    const dates = document.querySelectorAll('.date');
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    dates.forEach((i) => {
        i.addEventListener('click', () => {
            if (i.classList.contains('other') || i.classList.contains('selected')) {
                dates.forEach((ig) => { ig.classList.remove('selected'); });
                i.classList.remove('selected');
                selectedDate.year = null;
                selectedDate.month = null;
                selectedDate.day = null;
                selDate.length = 0;
            } else if (selDate.length > 0) {
                dates.forEach((ig) => { ig.classList.remove('selected'); });
                selDate.length = 0;
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                selectedDate.year = year.innerHTML;
                selectedDate.month = month.innerHTML;
                selectedDate.day = i.querySelector('.date-itm').innerText.trim(); // 'date-itm' 클래스를 가진 div 요소의 텍스트 값을 가져옴
                resvTab.classList.add('open');

                const selectedYear = selectedDate.year;
                const selectedMonth = selectedDate.month;
                const selectedDay = selectedDate.day;

                console.log(`선택한 날짜: ${selectedYear}-${selectedMonth}-${selectedDay}`);
            } else {
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                selectedDate.year = year.innerHTML;
                selectedDate.month = month.innerHTML;
                selectedDate.day = i.querySelector('.date-itm').innerText.trim(); // 'date-itm' 클래스를 가진 div 요소의 텍스트 값을 가져옴
                resvTab.classList.add('open');

                const selectedYear = selectedDate.year;
                const selectedMonth = selectedDate.month;
                const selectedDay = selectedDate.day;

                console.log(`선택한 날짜: ${selectedYear}-${selectedMonth}-${selectedDay}`);
            }
        });
    });
};

// JavaScript에서 Ajax 요청 보내기
// $.ajax({
//    url: '/logs/write/${selectedYear}${selectedMonth}${selectedDay}',
//    method: 'POST',
//    data: {
//        year: selectedDate.year,
//        month: selectedDate.month,
//        day: selectedDate.day,
//        selected_date: `${selectedYear}${selectedMonth}${selectedDay}`
//
//    },
//    success: function (data) {
//        window.location.href = url; // 현재 창에서 URL 열기
//
//    },
//    error: function (error) {
//        alert('서버와의 통신 중 문제가 발생했습니다. 나중에 다시 시도해주세요.');
//    }
//});



// 초기화 함수 
const reset = () => {
    selDate.length = 0;
    dateFunc();
}

// 로드시 Nav 버튼들 이벤트 등록 및 초기화
window.onload = () => {
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf => {
        if (inf.classList.contains('go-prev')) {
            inf.addEventListener('click', () => { prevMonth(); reset(); });
        } else if (inf.classList.contains('go-today')) {
            inf.addEventListener('click', () => { goToday(); reset(); });
        } else if (inf.classList.contains('go-next')) {
            inf.addEventListener('click', () => { nextMonth(); reset(); });
        }
    });
    reset();
}
