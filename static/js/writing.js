
const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', function () {
    // 테이블 내용 초기화
    const tableBody = document.querySelector("#logTable tbody");
    tableBody.innerHTML = "";

    // 선택한 날짜 정보 초기화
    document.getElementById("year").textContent = "";
    document.getElementById("month").textContent = "";
    document.getElementById("date").textContent = "";

    // 로컬 스토리지에서 선택한 날짜 정보 삭제
    localStorage.removeItem("selected_date");

    resvTab.classList.remove('open');
});

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
            // 이전에 선택된 날짜의 로그 테이블 초기화
            const tableBody = document.querySelector("#logTable tbody");
            tableBody.innerHTML = "";

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
                if (selectedDate.day.length === 1) {
                    selectedDate.day = '0' + selectedDate.day
                }
                if (selectedDate.month.length === 1) {
                    selectedDate.month = '0' + selectedDate.month
                }
                resvTab.classList.add('open');
                console.log(selDate)
                const selected_date = `${selectedDate.year}${selectedDate.month}${selectedDate.day}`

                document.getElementById("year").textContent = selectedDate.year;
                document.getElementById("month").textContent = selectedDate.month;
                document.getElementById("date").textContent = selectedDate.day;


                // // JavaScript에서 Ajax 요청 보내기
                $.ajax({
                    url: 'write/',
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
                localStorage.setItem("selected_date", JSON.stringify(selected_date));

                console.log(`선택한 날짜: ${selectedDate.year}-${selectedDate.month}-${selectedDate.day}`);


                // 해당 날짜 일지 불러오기 
                $.ajax({
                    url: "/logs/get-logs/", // 요청할 URL
                    method: "GET",     // GET 요청
                    dataType: "json",  // JSON 데이터 형식으로 응답을 기대합니다.
                    success: function (data) {
                        // 서버에서 받아온 JSON 데이터는 'data' 변수에 들어옵니다.
                        console.log(data);

                        // JSON 파싱 (JSON 문자열을 객체로 파싱!!)
                        // const logs = data.logs;
                        // console.log(logs)
                        const logs = JSON.parse(data.logs);
                        console.log(logs)

                        // logs 배열 순회하며 title과 date 출력
                        for (let i = 0; i < logs.length; i++) {
                            const log = logs[i];
                            console.log("Log Title:", log["title"], "Date: ", log["new_date"]);
                        }


                        logs.forEach(function (log) {
                            if (log.new_date === selected_date) {
                                const row = document.createElement("tr");
                                const cell1 = document.createElement("td");
                                cell1.textContent = log.title;
                                const cell2 = document.createElement("td");
                                cell2.textContent = log.conditioning;

                                row.appendChild(cell1);
                                row.appendChild(cell2);

                                tableBody.appendChild(row);
                            }
                        });
                    }
                });

            } else {
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                selectedDate.year = year.innerHTML;
                selectedDate.month = month.innerHTML;
                selectedDate.day = i.querySelector('.date-itm').innerText.trim();
                if (selectedDate.day.length === 1) {
                    selectedDate.day = '0' + selectedDate.day
                }
                if (selectedDate.month.length === 1) {
                    selectedDate.month = '0' + selectedDate.month
                }

                resvTab.classList.add('open');

                const selected_date = `${selectedDate.year}${selectedDate.month}${selectedDate.day}`

                document.getElementById("year").textContent = selectedDate.year;
                document.getElementById("month").textContent = selectedDate.month;
                document.getElementById("date").textContent = selectedDate.day;
                // document.getElementById("selected_date").innerHTML = selected_date



                // JavaScript에서 Ajax 요청 보내기
                $.ajax({
                    url: 'write/',
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

                localStorage.setItem("selected_date", JSON.stringify(selected_date));

                console.log(selected_date);

                // 해당 날짜 일지 불러오기 
                $.ajax({
                    url: "/logs/get-logs/", // 요청할 URL
                    method: "GET",     // GET 요청
                    dataType: "json",  // JSON 데이터 형식으로 응답을 기대합니다.
                    success: function (data) {
                        // 서버에서 받아온 JSON 데이터는 'data' 변수에 들어옵니다.
                        console.log(data);

                        // JSON 파싱 (JSON 문자열을 객체로 파싱!!)
                        // const logs = data.logs;
                        // console.log(logs)
                        const logs = JSON.parse(data.logs);
                        console.log(logs)

                        // logs 배열 순회하며 title과 date 출력
                        for (let i = 0; i < logs.length; i++) {
                            const log = logs[i];
                            console.log("Log Title:", log["title"], "Date: ", log["new_date"]);
                        }


                        logs.forEach(function (log) {
                            if (log.new_date === selected_date) {
                                console.log("date 일치!" + selected_date)
                                const row = document.createElement("tr");
                                const cell1 = document.createElement("td");
                                cell1.textContent = log.title;
                                const cell2 = document.createElement("td");
                                cell2.textContent = log.conditioning;
                                const cell3 = document.createElement("td");
                                cell3.textContent = log.illness + log.illness_range

                                row.appendChild(cell1);
                                row.appendChild(cell2);
                                row.appendChild(cell3);


                                tableBody.appendChild(row);
                            }
                        });
                    }
                });









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