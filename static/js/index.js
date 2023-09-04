// document.addEventListener("DOMContentLoaded", function () {
//     const separator = ',';

//     const inputs = document.getElementsByTagName("input");
//     for (const input of inputs) {
//         if (!input.multiple) {
//             continue;
//         }

//         if (input.list instanceof HTMLDataListElement) {
//             const optionsValues = Array.from(input.list.options).map(function (opt) {
//                 return opt.value;
//             });
//             let valueCount = input.value.split(separator).length;

//             input.addEventListener("input", function () {
//                 const currentValueCount = input.value.split(separator).length;

//                 if (valueCount !== currentValueCount) {
//                     valueCount = currentValueCount; // Update valueCount

//                     const lsIndex = input.value.lastIndexOf(separator);
//                     const str = lsIndex !== -1 ? input.value.substr(0, lsIndex) + separator : "";

//                     // Clear and then refill the datalist
//                     filldatalist(input, optionsValues, str);
//                 }
//             });
//         }
//     }

//     function filldatalist(input, optionValues, optionPrefix) {
//         const list = input.list;
//         if (list && optionValues.length > 0) {
//             list.innerHTML = "";

//             const usedOptions = optionPrefix.split(separator).map(function (value) {
//                 return value.trim();
//             });

//             for (const optionsValue of optionValues) {
//                 if (usedOptions.indexOf(optionsValue) < 0) {
//                     const separateOptions = optionsValue.split(',').map(function (value) {
//                         return value.trim();
//                     });

//                     for (const separateOption of separateOptions) {
//                         const option = document.createElement("option");
//                         option.value = optionPrefix + separateOption.toLowerCase(); // Convert to lowercase if needed
//                         list.append(option);

//                         console.log(usedOptions)
//                         console.log(separateOptions) // 예: ['Wall walk']
//                         console.log(optionPrefix) // 예: bike, Burpee
//                         console.log(separateOption) // 예: Wall walk
//                         console.log(option)
//                     }
//                 }
//             }
//         }
//     }
// });


// // 카테고리별 필터링 
document.addEventListener("DOMContentLoaded", function () {
    const toggleButtons = document.querySelectorAll(".toggle-button");
    const wodItems = document.querySelectorAll(".wod-item");

    // 페이지가 로드될 때, 모든 wod-item을 보이게 설정
    wodItems.forEach(item => {
        item.style.display = "block";
    });

    toggleButtons.forEach(button => {
        button.addEventListener("click", function () {
            const targetCategory = this.getAttribute("data-category");


            // 모든 wod-item을 숨김
            wodItems.forEach(item => {
                item.style.display = "none";
            });

            // 선택한 카테고리에 해당하는 wod-item만 보이도록 설정
            wodItems.forEach(item => {
                const category = item.getAttribute("data-category");
                if (category === targetCategory) {
                    item.style.display = "block";
                }
            });
        });
    });
});

// document.addEventListener("DOMContentLoaded", function () {

//     const toggleButtons = document.querySelectorAll(".toggle-button");
//     const wodItems = document.querySelector(".wod-item");

//     let currentOpenDiv = null;


//     toggleButtons.forEach(button => {
//         button.addEventListener("click", function () {
//             const targetId = this.getAttribute("data-target");
//             const targetDiv = document.getElementById(targetId);


//             if (targetDiv !== currentOpenDiv) {
//                 if (currentOpenDiv) {
//                     currentOpenDiv.style.display = "none";
//                 }
//                 currentOpenDiv = targetDiv;
//             }


//             if (targetDiv.style.display === "none") {
//                 targetDiv.style.display = "block";
//             } else {
//                 targetDiv.style.display = "none";
//             }
//         });
//     });
// });


// include, exclude datalist multiple 자동완성 (, 기준으로 구분)
document.addEventListener("DOMContentLoaded", function () {
    const separator = ',';

    const inputs = document.querySelectorAll("input"); // Change the selector to match your HTML structure
    inputs.forEach(input => {
        if (input.multiple) {
            const datalist = document.getElementById(input.getAttribute("list"));
            const optionsValues = Array.from(datalist.options).map(opt => opt.value);

            input.addEventListener("input", () => {
                const values = input.value.split(separator).map(value => value.trim());

                // Clear the datalist options
                datalist.innerHTML = "";

                // Add options for each value
                values.forEach(value => {
                    if (!optionsValues.includes(value)) {
                        const option = document.createElement("option");
                        option.value = value;
                        datalist.appendChild(option);

                        console.log(option)

                    }
                });


            });
        }
    });
});

// include, exclude datalist multiple 자동완성 (, 기준으로 구분)

// document.addEventListener("DOMContentLoaded", function () {
//     const separator = ',';

//     const inputs = document.getElementsByTagName("input");
//     for (const input of inputs) {
//         if (!input.multiple) {
//             continue;
//         }

//         if (input.list instanceof HTMLDataListElement) {
//             const optionsValues = Array.from(input.list.options).map(function (opt) {
//                 return opt.value;
//             });
//             let valueCount = input.value.split(separator).length;
//             console.log(valueCount)

//             input.addEventListener("input", function () {
//                 const currentValueCount = input.value.split(separator).length;

//                 if (valueCount !== currentValueCount) {
//                     valueCount = currentValueCount; // Update valueCount

//                     const lsIndex = input.value.lastIndexOf(separator);
//                     const str = lsIndex !== -1 ? input.value.substr(0, lsIndex) + separator : "";

//                     // Clear and then refill the datalist
//                     filldatalist(input, optionsValues, str);
//                 }
//             });
//         }
//     }

//     function filldatalist(input, optionValues, optionPrefix) {
//         const list = input.list;
//         if (list && optionValues.length > 0) {
//             list.innerHTML = "";

//             const usedOptions = optionPrefix.split(separator).map(function (value) {
//                 return value.trim();
//             });

//             for (const optionsValue of optionValues) {
//                 if (usedOptions.indexOf(optionsValue) < 0) {
//                     const separateOptions = optionsValue.split(',').map(function (value) {
//                         return value.trim();
//                     });

//                     for (const separateOption of separateOptions) {
//                         const option = document.createElement("option");
//                         option.value = optionPrefix + separateOption;
//                         list.append(option);

//                         console.log(usedOptions) // 예: ['Bike', 'Burpee', '']
//                         console.log(separateOptions) // 예: ['Wall walk']
//                         console.log(optionPrefix) // 예: bike, Burpee
//                         console.log(separateOption) // 예: Wall walk
//                         console.log(option) // 예: <option value="bike,Box jump,Wall walk"></option>

//                     }
//                 }
//             }
//         }
//     }
// });
// 이까지 기존




// document.addEventListener("DOMContentLoaded", function () {
//     const separator = ',';

//     const inputs = document.getElementsByTagName("input");
//     for (const input of inputs) {
//         if (!input.multiple) {
//             continue;
//         }

//         if (input.list instanceof HTMLDataListElement) {
//             const optionsValues = Array.from(input.list.options).map(function (opt) {
//                 return opt.value;
//             });
//             let valueCount = input.value.split(separator).length;

//             input.addEventListener("input", function () {
//                 const currentValueCount = input.value.split(separator).length;

//                 if (valueCount !== currentValueCount) {
//                     const lsIndex = input.value.lastIndexOf(separator);
//                     const str = lsIndex !== -1 ? input.value.substr(0, lsIndex) + separator : "";
//                     filldatalist(input, optionsValues, str);
//                     valueCount = currentValueCount;
//                 }
//             });
//         }
//     }

//     function filldatalist(input, optionValues, optionPrefix) {
//         const list = input.list;
//         if (list && optionValues.length > 0) {
//             list.innerHTML = "";

//             const usedOptions = optionPrefix.split(separator).map(function (value) {
//                 return value.trim();
//             });

//             console.log(usedOptions)

//             for (const optionsValue of optionValues) {
//                 if (usedOptions.indexOf(optionsValue) < 0) {

//                     for (const separateOption of separateoption) {
//                         const option = document.createElement("option");
//                         option.value = separateOption;
//                         list.append(option);
//                     }

                    // const option = document.createElement("option");
                    // option.value = optionPrefix + optionsValue;
                    // const separateoption = option[0].split(',').map(value => value.trim());

                    // list.append(separateoption);

//                }
//            }
//        }
//    }
// });

// const forrepsbtn = document.getElementById('forrepsbtn');
// const infoDiv = document.getElementById('infoDiv');

// forrepsbtn.addEventListener('click', () => {
//     if (infoDiv.style.display === 'none') {
//         infoDiv.style.display = 'block';
//     } else {
//         infoDiv.style.display = 'none';
//     }
// });

// const emombtn = document.getElementById('emombtn');
// const infoDiv2 = document.getElementById('infoDiv2');

// emombtn.addEventListener('click', () => {
//     if (infoDiv2.style.display === 'none') {
//         infoDiv2.style.display = 'block';
//     } else {
//         infoDiv2.style.display = 'none';
//     }
// });

// const amrapbtn = document.getElementById('amrapbtn');
// const infoDiv3 = document.getElementById('infoDiv3');

// amrapbtn.addEventListener('click', () => {
//    if (infoDiv3.style.display === 'none') {
//        infoDiv3.style.display = 'block';
//    } else {
//        infoDiv3.style.display = 'none';
//    }
//});