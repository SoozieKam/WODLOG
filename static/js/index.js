document.addEventListener("DOMContentLoaded", function () {

    const toggleButtons = document.querySelectorAll(".toggle-button");
    let currentOpenDiv = null;

    toggleButtons.forEach(button => {
        button.addEventListener("click", function () {
            const targetId = this.getAttribute("data-target");
            const targetDiv = document.getElementById(targetId);


            if (targetDiv !== currentOpenDiv) {
                if (currentOpenDiv) {
                    currentOpenDiv.style.display = "none";
                }
                currentOpenDiv = targetDiv;
            }


            if (targetDiv.style.display === "none") {
                targetDiv.style.display = "block";
            } else {
                targetDiv.style.display = "none";
            }
        });
    });
});



// include, exclude datalist multiple 자동완성 (, 기준으로 구분)
document.addEventListener("DOMContentLoaded", function () {
    const separator = ',';

    const inputs = document.getElementsByTagName("input");
    for (const input of inputs) {
        if (!input.multiple) {
            continue;
        }

        if (input.list instanceof HTMLDataListElement) {
            const optionsValues = Array.from(input.list.options).map(function (opt) {
                return opt.value;
            });
            let valueCount = input.value.split(separator).length;

            input.addEventListener("input", function () {
                const currentValueCount = input.value.split(separator).length;

                if (valueCount !== currentValueCount) {
                    const lsIndex = input.value.lastIndexOf(separator);
                    const str = lsIndex !== -1 ? input.value.substr(0, lsIndex) + separator : "";
                    filldatalist(input, optionsValues, str);
                    valueCount = currentValueCount;
                }
            });
        }
    }

    function filldatalist(input, optionValues, optionPrefix) {
        const list = input.list;
        if (list && optionValues.length > 0) {
            list.innerHTML = "";

            const usedOptions = optionPrefix.split(separator).map(function (value) {
                return value.trim();
            });

            for (const optionsValue of optionValues) {
                if (usedOptions.indexOf(optionsValue) < 0) {
                    const option = document.createElement("option");
                    option.value = optionPrefix + optionsValue;
                    list.append(option);
                }
            }
        }
    }
});

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