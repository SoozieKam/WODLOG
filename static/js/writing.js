
const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', function () {
    // 테이블 내용 초기화
    const tableBody = document.querySelector("#logTable tbody");
    tableBody.innerHTML = "";

    const logDetail = document.querySelector("#logDetail")
    logDetail.innerHTML = ""



    // 선택한 날짜 정보 초기화
    document.getElementById("year").textContent = "";
    document.getElementById("month").textContent = "";
    document.getElementById("date").textContent = "";

    // 로컬 스토리지에서 선택한 날짜 정보 삭제
    localStorage.removeItem("selected_date");

    resvTab.classList.remove('open');
});

// const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
function convertLinebreaksToBr(text) {
    // return text.replace(/\r?\n/g, "<br>");
    return text.split("\n").map(line => `<p>${line}</p>`).join("");

}

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
                                writeBtn.style.display = 'none'; // 버튼을 숨깁니다.

                                const row = document.createElement("tr");
                                const cell1 = document.createElement("td");
                                cell1.textContent = '제목';
                                const cell2 = document.createElement("td");
                                cell2.textContent = log.title;

                                const row2 = document.createElement("tr")
                                const cell3 = document.createElement("td");
                                cell3.textContent = '오늘의 컨디션';
                                const cell4 = document.createElement("td");
                                cell4.textContent = log.today_condition;

                                const row3 = document.createElement("tr")
                                const cell5 = document.createElement("td");
                                cell5.textContent = '웜업';
                                const cell6 = document.createElement("td");
                                cell6.innerHTML = convertLinebreaksToBr(log.warmup);

                                const row4 = document.createElement("tr")
                                const cell7 = document.createElement("td");
                                cell7.textContent = '컨디셔닝';
                                const cell8 = document.createElement("td");

                                cell8.innerHTML = convertLinebreaksToBr(log.conditioning)


                                const row5 = document.createElement("tr")
                                const cell9 = document.createElement("td");
                                cell9.textContent = '아픈 곳';
                                const cell10 = document.createElement("td");
                                cell10.textContent = log.illness_range + ' 만큼 ' + log.illness + ' 이/가 아파요';

                                const row6 = document.createElement("tr")
                                const cell11 = document.createElement("td");
                                cell11.textContent = '스트렝스';
                                const cell12 = document.createElement("td");
                                cell12.innerHTML = convertLinebreaksToBr(log.strength);

                                const row7 = document.createElement("tr")
                                const cell13 = document.createElement("td");
                                cell13.textContent = '역도';
                                const cell14 = document.createElement("td");
                                cell14.innerHTML = convertLinebreaksToBr(log.weightlifting);



                                row.appendChild(cell1);
                                row.appendChild(cell2);

                                row2.appendChild(cell3)
                                row2.appendChild(cell4)

                                row5.appendChild(cell9)
                                row5.appendChild(cell10)

                                row3.appendChild(cell5)
                                row3.appendChild(cell6)

                                row4.appendChild(cell7)
                                row4.appendChild(cell8)

                                row6.appendChild(cell11)
                                row6.appendChild(cell12)

                                row7.appendChild(cell13)
                                row7.appendChild(cell14)

                                tableBody.appendChild(row);
                                tableBody.appendChild(row2);
                                tableBody.appendChild(row5);
                                tableBody.appendChild(row3);
                                tableBody.appendChild(row4);
                                tableBody.appendChild(row6);
                                tableBody.appendChild(row7);



                            }
                            else {
                                writeBtn.style.display = 'block'; // 버튼을 숨깁니다.

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

                        const another = JSON.parse(data.another)
                        console.log(another)


                        for (let i = 0; i < another.length; i++) {
                            const log2 = another[i].fields;
                            if (log2.new_date === selected_date) {
                                const writeBtn = document.getElementById('writeBtn');
                                if (writeBtn) {
                                    writeBtn.style.display = 'none'; // 버튼을 숨깁니다.
                                }
                                if (log2.image) {
                                    const imageUrl = `/media/` + log2.image; // JSON 데이터에서 이미지 URL 추출
                                    const imageElement = document.createElement("img");
                                    imageElement.src = imageUrl;
                                    logDetail.appendChild(imageElement);


                                    imageElement.onload = function () {
                                        // 이미지가 로드된 후에 실행됩니다.
                                        imageElement.style.width = '50%';
                                        imageElement.style.height = 'auto';

                                    };
                                }

                                if (log2.video) {
                                    const videoUrl = `/media/` + log2.video; // JSON 데이터에서 비디오 URL 추출
                                    const videoElement = document.createElement("video");
                                    videoElement.src = videoUrl;
                                    logDetail.appendChild(videoElement);

                                    videoElement.onload = function () {
                                        // 이미지가 로드된 후에 실행됩니다.
                                        videoElement.style.width = '20%';
                                        videoElement.style.height = 'auto';

                                    };
                                }


                                const row = document.createElement("tr");
                                const cell1 = document.createElement("td");
                                cell1.textContent = '제목';
                                const cell2 = document.createElement("td");
                                cell2.textContent = log2.title;

                                const row2 = document.createElement("tr")
                                const cell3 = document.createElement("td");
                                cell3.textContent = '오늘의 컨디션';
                                const cell4 = document.createElement("td");
                                cell4.textContent = log2.today_condition;

                                const row3 = document.createElement("tr")
                                const cell5 = document.createElement("td");
                                cell5.textContent = '웜업';
                                const cell6 = document.createElement("td");
                                cell6.innerHTML = convertLinebreaksToBr(log2.warmup);

                                const row4 = document.createElement("tr")
                                const cell7 = document.createElement("td");
                                cell7.textContent = '컨디셔닝';
                                const cell8 = document.createElement("td");

                                cell8.innerHTML = convertLinebreaksToBr(log2.conditioning)


                                const row5 = document.createElement("tr")
                                const cell9 = document.createElement("td");
                                cell9.textContent = '아픈 곳';
                                const cell10 = document.createElement("td");
                                cell10.textContent = log2.illness_range + ' 만큼 ' + log2.illness + ' 이/가 아파요';

                                const row6 = document.createElement("tr")
                                const cell11 = document.createElement("td");
                                cell11.textContent = '스트렝스';
                                const cell12 = document.createElement("td");
                                cell12.innerHTML = convertLinebreaksToBr(log2.strength);

                                const row7 = document.createElement("tr")
                                const cell13 = document.createElement("td");
                                cell13.textContent = '역도';
                                const cell14 = document.createElement("td");
                                cell14.innerHTML = convertLinebreaksToBr(log2.weightlifting);

                                console.log(log2.wod)


                                row.appendChild(cell1);
                                row.appendChild(cell2);

                                row2.appendChild(cell3)
                                row2.appendChild(cell4)

                                row5.appendChild(cell9)
                                row5.appendChild(cell10)

                                row3.appendChild(cell5)
                                row3.appendChild(cell6)

                                row4.appendChild(cell7)
                                row4.appendChild(cell8)

                                row6.appendChild(cell11)
                                row6.appendChild(cell12)

                                row7.appendChild(cell13)
                                row7.appendChild(cell14)

                                tableBody.appendChild(row);
                                tableBody.appendChild(row2);
                                tableBody.appendChild(row5);
                                tableBody.appendChild(row3);
                                tableBody.appendChild(row4);
                                tableBody.appendChild(row6);
                                tableBody.appendChild(row7);
                                break;



                            }
                        }
                        // another.forEach(function (log2) {

                        //});
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