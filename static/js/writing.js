const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', () => { resvTab.classList.remove('open'); });

// const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;


// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []

const selectedDate = {
    year: null,
    month: null,
    day: null,
};

let url = ''; // URL 변수를 미리 정의

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
                selectedDate.day = i.querySelector('.date-itm').innerText.trim();
                resvTab.classList.add('open');
                console.log(selDate)

                // JavaScript에서 Ajax 요청 보내기
                $.ajax({
                    url: '/logs/write/',
                    method: 'GET',
                    data: {
                        year: selectedDate.year,
                        month: selectedDate.month,
                        day: selectedDate.day,
                        selected_date: `${selectedDate.year}${selectedDate.month}${selectedDate.day}`
                    },
                    success: function (data) {
                    },
                    error: function (error) {
                        alert('서버와의 통신 중 문제가 발생했습니다. 나중에 다시 시도해주세요.');
                    }
                });

                console.log(`선택한 날짜: ${selectedDate.year}-${selectedDate.month}-${selectedDate.day}`);
            } else {
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                selectedDate.year = year.innerHTML;
                selectedDate.month = month.innerHTML;
                selectedDate.day = i.querySelector('.date-itm').innerText.trim();
                resvTab.classList.add('open');
                console.log(selDate)

                // JavaScript에서 Ajax 요청 보내기
                $.ajax({
                    url: '/logs/write/',
                    method: 'GET',
                    data: {
                        year: selectedDate.year,
                        month: selectedDate.month,
                        day: selectedDate.day,
                        selected_date: `${selectedDate.year}${selectedDate.month}${selectedDate.day}`
                    },
                    success: function (data) {

                    },
                    error: function (error) {
                        alert('서버와의 통신 중 문제가 발생했습니다. 나중에 다시 시도해주세요.');
                    }
                });

                const selected_date = `${selectedDate.year}${selectedDate.month}${selectedDate.day}`
                // window.location.href = `write.html?data=${encodeURIComponent(selected_date)}`;


                console.log(`선택한 날짜: ${selectedDate.year}-${selectedDate.month}-${selectedDate.day}`);
            }
        });
    });
};

// JavaScript에서 Ajax 요청 보내기
// $.ajax({
//    url: '/logs/write/',
//    method: 'POST',
//    data: {
//        year: selectedDate.year,
//        month: selectedDate.month,
//        day: selectedDate.day,
//        selected_date: `${selectedDate.year}${selectedDate.month}${selectedDate.day}`
//    },
//    success: function (data) {
//        window.location.href = url; // 현재 창에서 URL 열기
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