// 계산기 상태 변수
let display = document.getElementById('display');
let firstNumber = null;
let operation = null;
let newNumber = true;

// 숫자 추가
function appendNumber(num) {
    if (newNumber) {
        display.textContent = num;
        newNumber = false;
    } else {
        if (display.textContent === '0') {
            display.textContent = num;
        } else {
            display.textContent += num;
        }
    }
}

// 소수점 추가
function appendDecimal() {
    if (newNumber) {
        display.textContent = '0.';
        newNumber = false;
    } else if (!display.textContent.includes('.')) {
        display.textContent += '.';
    }
}

// 연산자 설정
function setOperation(op) {
    if (display.textContent !== 'Error') {
        firstNumber = parseFloat(display.textContent);
        operation = op;
        newNumber = true;
    }
}

// 계산 실행
function calculate() {
    if (firstNumber !== null && operation !== null) {
        const secondNumber = parseFloat(display.textContent);
        let result;

        try {
            switch (operation) {
                case '+':
                    result = firstNumber + secondNumber;
                    break;
                case '-':
                    result = firstNumber - secondNumber;
                    break;
                case '*':
                    result = firstNumber * secondNumber;
                    break;
                case '/':
                    if (secondNumber === 0) {
                        display.textContent = 'Error';
                        firstNumber = null;
                        operation = null;
                        newNumber = true;
                        return;
                    }
                    result = firstNumber / secondNumber;
                    break;
            }

            // 결과가 정수면 정수로 표시
            if (Number.isInteger(result)) {
                display.textContent = result;
            } else {
                display.textContent = result.toFixed(8).replace(/\.?0+$/, '');
            }

            firstNumber = null;
            operation = null;
            newNumber = true;
        } catch (error) {
            display.textContent = 'Error';
            firstNumber = null;
            operation = null;
            newNumber = true;
        }
    }
}

// 초기화
function clearDisplay() {
    display.textContent = '0';
    firstNumber = null;
    operation = null;
    newNumber = true;
}

// 키보드 입력 지원
document.addEventListener('keydown', function (event) {
    const key = event.key;

    // 숫자 키
    if (key >= '0' && key <= '9') {
        appendNumber(key);
    }
    // 소수점
    else if (key === '.') {
        appendDecimal();
    }
    // 연산자
    else if (key === '+' || key === '-' || key === '*' || key === '/') {
        setOperation(key);
    }
    // Enter 또는 =
    else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    }
    // Escape 또는 C
    else if (key === 'Escape' || key === 'c' || key === 'C') {
        clearDisplay();
    }
    // Backspace
    else if (key === 'Backspace') {
        if (display.textContent.length > 1) {
            display.textContent = display.textContent.slice(0, -1);
        } else {
            display.textContent = '0';
        }
    }
});
