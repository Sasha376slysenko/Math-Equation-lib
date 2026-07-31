document.addEventListener('DOMContentLoaded', function(){
    document.addEventListener('submit',   async function(event){
        event.preventDefault();

        switch (event.target.id){
            case 'myForm':
                onClick();
                setTimeout(() =>{
                    adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
                }, 100);
                break;
            case 'usr-1':
                feedBackText = document.getElementById('feedBack-input');
                dictTransferDataSER = {text: feedBackText.value};
                await sendFeedBackSQL(dictTransferDataSER);
                feedBackText.value = '';
                modalWindow.style.display = 'none';
                break;
            case 'usr-2':
                username = document.getElementById('username');
                password = document.getElementById('password');
                dictTransferDataSER = {username: username.value, password: password.value};
                await sendReadSQL(dictTransferDataSER);

                if (dictFeedBackTexts['status']){
                    styleInput(username, password);
                    removeElement('btnDeveloperSql');
                    removeElement();
                    documentDeveloper();
                    modalWindowDeveloper.style.display = 'none';
                }else{
                    styleInput(username, password, false);
                }
                break;
        }
    });

    document.addEventListener('click', async function(event) {
        if(event.target.closest('#EndTheGameSlider')){
            removeSlider();
            removeElement();
            updateVariable();
            flagGameDescription = true;
            flagGlobalButton = true;
            endGame();
            adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
        }
        if(event.target.closest('#MenuSlider')){
            removeSlider();
            updateVariable();
            updateBackgroundImage();
            flagGlobalButton = true;
            flagGameDescription = false;
            onClick();
            adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
        }
        switch (event.target.id) {
            case 'ButtonPreviousSlide':
                counterTutorial--;
                NextSlideTutorial();
                break;
            case 'ButtonNextSlide':
                counterTutorial++;
                NextSlideTutorial();
                break;
            case 'ButtonStart':
                updateBackgroundImage();
                onClick();
                adaptationUpdate().then(()=>{console.log('Adaption was successful!');});
                break;
            case 'ButtonGoBack':
                updateVariable();
                flagGameDescription = true;
                flagGlobalButton = true;
                onClick();
                break;
            case 'Initial-1':
                sliders();
                updateBackgroundImage();
                flagButtonInitialOne = true;
                maxTime = 360;
                await startGame();
                dialogBox(true);
                startTimer();
                adaptationUpdate().then(()=>{console.log('Adaption was successful!');});
                break;
            case 'Initial-2':
                sliders();
                updateBackgroundImage(true);
                flagButtonInitialTwo = true;
                maxTime = 360;
                await startGame();
                startTimer();
                dialogBox(true);
                adaptationUpdate().then(()=>{console.log('Adaption was successful!');});
                break;
            case 'Advanced':
                sliders();
                updateBackgroundImage(true);
                flagButtonAdvanced = true;
                maxTime = 360;
                await startGame();
                dialogBox(true);
                startTimer();
                adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
                break;
            case 'ButtonStartTheGame':
                sliders();
                updateBackgroundImage();
                updateVariable(false);
                await startGame();
                updateDigits();
                startTimer();
                dialogBox(true);
                adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
                break;
            case 'ButtonEndTheGame':
                removeElement();
                updateVariable();
                flagGameDescription = true;
                flagGlobalButton = true;
                endGame();
                adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
                break;
            case 'ButtonMenu':
                updateVariable();
                updateBackgroundImage();
                flagGlobalButton = true;
                flagGameDescription = false;
                onClick();
                adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
                break;
            case 'startGame':
                updateBackgroundImage();
                updateVariable();
                onClick();
                break;
            case 'ButtonInput':
                dataVerification(true);
                await checkInputDialogBox()

                if(dictOutputServerCheck && 'flag' in dictOutputServerCheck){
                    correctIncorrectEquation = dictOutputServerCheck.flag;
                }else{
                    console.warn("⚠️ Відповідь не містить 'flag':", dictOutputServerCheck);
                    correctIncorrectEquation = 'ERROR';
                }

                if (correctIncorrectEquation && correctIncorrectEquation !== 'ERROR'){
                    if (is_ukrainian){ warningEquation('Молодець'); }
                    else{ warningEquation('Well done'); }

                    // UPDATE USER
                    counter_eq_input++;
                    arrayInputEQ.push(InputEquation);
                    divContentLocallyInput.textContent = InputEquation;
                    divContentLocally.append(divContentLocallyInput.cloneNode(true));
                    counter.innerHTML = counter_eq_input + '/' + count_eq;

                    // UPDATE FRONTEND - SERVER VARIABLE
                    updateServerAndFrontend();

                    if (counter_eq_input >= count_eq){removeElement(); await windowEndDialogBox();}
                }else if(correctIncorrectEquation === 'ERROR'){
                    if (is_ukrainian){ warningEquation('Ви вели не правильне рівняння.'); }
                    else{ warningEquation('You used the wrong equation.'); }
                }else{
                    if (is_ukrainian){ warningEquation('Ви вже водили це рівняння.'); }
                    else{ warningEquation('You have already solved this equation.'); }

                    // UPDATE FRONTEND - SERVER VARIABLE
                    updateServerAndFrontend();
                }
                updateDigits();
                break;
            case 'ButtonNext':
                if (counter_eq_input !== 0){
                    stopTimer();
                    removeSlider();
                    removeElement();
                    await windowEndDialogBox();
                }else{
                    if (is_ukrainian){ warningEquation('Ви не вили жодного рівняння.'); }
                    else{ warningEquation('You haven\'t solved a single equation.'); }
                    updateDigits();
                }
                break;
            case "ButtonFeedBack":
                modalWindow.style.display = 'flex';
                break;
            case 'ButtonAnalysis':
                AnalysisUserInputEquation();
                break;
            case 'btnDeveloperSql':
                modalWindowDeveloper.style.display = 'flex';
                break;
            case 'closeBtn-1':
                modalWindow.style.display = 'none';
                break;
            case 'closeBtn-2':
                modalWindowDeveloper.style.display = 'none';
                break;
        }
    });
});

/*
 * +----------------------+
 * //---- 14.09.2025 ----//
 * | functional variables |
 * +--------------------- +
 */
//Boolean -> Flag User UI
let flagGlobalButton = true;
let flagGameDescription = true;
// Boolean -> Flag Button
let flagButtonInitialOne = false;
let flagButtonInitialTwo = false;
let flagButtonAdvanced = false;
// boolean -> Other
let isRunning = false;

// Number
let remainingTime = null;
let maxTime = null;
let minutes = null;
let seconds = null;
let counter = null;
let counterTime = null;
let intervalTime = null;
let digitDisplay = null;

// Global Container HTML (HTML ELEMENT)
const container = document.getElementById('CARD-container');

// Digits and Symbols (HTML ELEMENT)
const elDivEquationResult = document.createElement('div');
const elDivDigitsResult = document.createElement('div');
const elDivInitialOneSymbolsMath = document.createElement('div');
const elDivInitialTwoSymbolsMath = document.createElement('div');
const elDivAdvancedSymbolsMath = document.createElement('div');
const elDivInitialOneSymbolsMathEquals = document.createElement('div');
const elDivInitialTwoSymbolsMathEquals = document.createElement('div');
const elDivAdvancedSymbolsMathEquals = document.createElement('div');

// Slider (HTML ELEMENT)
const divSlider = document.createElement('div');
const divSliderContent = document.createElement('div');
const ulSlider = document.createElement('ul');
const liOneSlider = document.createElement('li');
const liTwoSlider = document.createElement('li');
const liThreeSlider = document.createElement('li');
const imgOneSlider = document.createElement('img');
const imgTwoSlider = document.createElement('img');
const imgThreeSlider = document.createElement('img');
const btnOneLiSlider = document.createElement('button');
const btnTwoLiSlider = document.createElement('button');
const btnThreeLiSlider = document.createElement('button');
const buttonSlider = document.createElement('button');
const buttonSliderImg = document.createElement('img');
const divContentLocally = document.createElement('div');
const divContentLocallyInput = document.createElement('div');

// CONTENT INPUT EQUATION DIV
divContentLocallyInput.classList.add('inp-content-locally');

// Other NULL
let marginTopGeneralLevel = null;
let counterSymbolsMat = null;
let widthEquationResult = null;
let widthDigitsResult = null
let variableDiv = {};
let variableH1 = {};
let counterItemDigits = 0;
let counterItemSymbol = 0;
let elDivEquationResultContentText;
let resultContentText = '';
let InputEquation = "";
let dictTransferDataSER = {};
let dictOutputServer = {};
let widthTabel = null;
let heightTabel = null;
let minLengthCheckInput = 0;
let correctIncorrectEquation = null;
let count_eq = 0;
let counter_eq_input = 0;
let dictOutputServerCheck = {};
let arrayInputEQ = [];
let ResultManyEquation = 0;
let ResultText = '';
let feedBackText = null;
let username = null;
let password = null;
let dictFeedBackTexts = {};

//tutorial
let counterTutorial = 0;
const tutorial = document.createElement('iframe');

// modal window (HTML ELEMENT)
const btnAppend = document.getElementById('btnAppend');
const modalWindow = document.getElementById('modal-feedback');
const modalWindowDeveloper = document.getElementById('modal-developer');

//tabel (HTML ELEMENT)
let dictTabel = {
    tabel: document.createElement('tabel'),
    tr_1: document.createElement('tr'),
    tr_2: document.createElement('tr'),
    th_1: document.createElement('th'),
    th_2: document.createElement('th'),
    td_1: document.createElement('td'),
    td_2: document.createElement('td'),
}

//Chart plugins
Chart.register(ChartDataLabels);

//LOUDER
const divPreloader = document.createElement('div');
const divLoader = document.createElement('div');
divPreloader.classList.add('preloader')
divPreloader.id = 'page-preloader';
divLoader.classList.add('loader');
divLoader.id = 'loader';


/*
 * +--------------------+
 * | Create Symbol Math |
 * +--------------------+
 */

// Dict symbol Math Initial One
let dictSymbolMathInitialOne = {};
let dictSymbolMathInitialOneEquals = {}

// Dict Symbol Math Initial Two
let dictSymbolMathInitialTwo = {};
let dictSymbolMathInitialTwoEquals = {};

// Dict Symbol Math Advanced
let dictSymbolMathAdvanced = {};
let dictSymbolMathAdvancedEquals = {};

dictSymbolMathInitialOneEquals['divAdd'] = document.createElement('div');
dictSymbolMathInitialOneEquals['divSub'] = document.createElement('div');
dictSymbolMathInitialOneEquals['divBracketLeft'] = document.createElement('div');
dictSymbolMathInitialOneEquals['divBracketRight'] = document.createElement('div');
dictSymbolMathInitialOneEquals['divEquals'] = document.createElement('div');

dictSymbolMathInitialTwoEquals['divMul'] = document.createElement('div');
dictSymbolMathInitialTwoEquals['divTruediv'] = document.createElement('div');
dictSymbolMathInitialTwoEquals['divBracketLeft'] = document.createElement('div');
dictSymbolMathInitialTwoEquals['divBracketRight'] = document.createElement('div');
dictSymbolMathInitialTwoEquals['divEquals'] = document.createElement('div');

dictSymbolMathAdvancedEquals['divAdd'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divSub'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divMul'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divTruediv'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divBracketLeft'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divBracketRight'] = document.createElement('div');
dictSymbolMathAdvancedEquals['divEquals'] = document.createElement('div');

const arrayH1InitialOne = [
    document.createElement('h1'), // Add -> 0
    document.createElement('h1'), // Sub -> 1
    document.createElement('h1'), // BracketLeft -> 2
    document.createElement('h1'), // BracketRight -> 3
    document.createElement('h1'), // Equals -> 4
];

const arrayH1InitialTwo = [
    document.createElement('h1'), // Mul -> 0
    document.createElement('h1'), // Div -> 1
    document.createElement('h1'), // BracketLeft -> 2
    document.createElement('h1'), // BracketRight -> 3
    document.createElement('h1'), // Equals -> 4
];

const arrayH1Advanced = [
    document.createElement('h1'), // Add -> 0
    document.createElement('h1'), // Sub -> 1
    document.createElement('h1'), // Mul -> 2
    document.createElement('h1'), // Div -> 3
    document.createElement('h1'), // BracketLeft -> 4
    document.createElement('h1'), // BracketRight -> 5
    document.createElement('h1'), // Equals -> 6
];

const arrayKeySymbolMathInitialOne = ['divAdd', 'divSub', 'divBracketLeft', 'divBracketRight', 'divEquals'];
const arrayKeySymbolMathInitialTwo = ['divMul', 'divTruediv', 'divBracketLeft', 'divBracketRight', 'divEquals'];
const arrayKeySymbolMathAdvanced = ['divAdd', 'divSub', 'divMul', 'divTruediv', 'divBracketLeft', 'divBracketRight', 'divEquals'];

const arrayH1SymbolInitialOne = ["+", "-", "(", ")", "="];
const arrayH1SymbolInitialTwo = ["*", "/", "(", ")", "="];
const arrayH1SymbolAdvanced = ["+", "-", "*", "/", "(", ")", "="];

/*
 * +--------------------------+
 * | array H1 providing Style |
 * +--------------------------+
 */
function styleArrayH1(ArrayH1){
    ArrayH1.forEach(elementH1 => {
        elementStyleDialogBox(elementH1);
    });
}

styleArrayH1(arrayH1InitialOne);
styleArrayH1(arrayH1InitialTwo);
styleArrayH1(arrayH1Advanced);

/*
 * +-------------------------------+
 * | dictSymbolMath append arrayH1 |
 * +-------------------------------+
 */
function appendDictSymbolMath(dict, arrayH1, arrayH1Symbol, arrayKeySymbolMath, length_elements){
    for(let i = 0; i < length_elements; i++){
        arrayH1[i].innerText = arrayH1Symbol[i];
        dict[arrayKeySymbolMath[i]].appendChild(arrayH1[i]);
    }
}

/*
 * +---------------------------------------------------------------+
 * | Create dict symbols Math (InitialOne, InitialOnTwo, Advanced) |
 * +---------------------------------------------------------------+
 */
function keySymbolMath(arrayKeySymbolMath, dictAppend, dictClone){
    arrayKeySymbolMath.forEach(key => {
        if(key !== 'divEquals'){
            counterItemSymbol++;
            dictAppend[key] = dictClone[key].cloneNode(true);
            dictAppend[key].id = 'ItemSymbol' + counterItemSymbol;
        }
    });
}

/*
 * +-------------------------+
 * |dicSymbolMath InitialOne |
 * +-------------------------+
 */
arrayKeySymbolMathInitialOne.forEach(key => {
    counterItemSymbol++;
    dictSymbolMathInitialOneEquals[key].draggable = true;
    dictSymbolMathInitialOneEquals[key].id = 'ItemSymbol' + counterItemSymbol;
    dictSymbolMathInitialOneEquals[key].classList.add('ItemSymbol');
});

appendDictSymbolMath(
    dictSymbolMathInitialOneEquals,
    arrayH1InitialOne,
    arrayH1SymbolInitialOne,
    arrayKeySymbolMathInitialOne,
    arrayKeySymbolMathInitialOne.length
)

keySymbolMath(
    arrayKeySymbolMathInitialOne,
    dictSymbolMathInitialOne,
    dictSymbolMathInitialOneEquals
);

/*
 * +-------------------------+
 * |dicSymbolMath InitialTwo |
 * +-------------------------+
 */
counterItemSymbol = 0;
arrayKeySymbolMathInitialTwo.forEach(key => {
    counterItemSymbol++;
    dictSymbolMathInitialTwoEquals[key].draggable = true;
    dictSymbolMathInitialTwoEquals[key].id = 'ItemSymbol' + counterItemSymbol;
    dictSymbolMathInitialTwoEquals[key].classList.add('ItemSymbol');
});

appendDictSymbolMath(
    dictSymbolMathInitialTwoEquals,
    arrayH1InitialTwo,
    arrayH1SymbolInitialTwo,
    arrayKeySymbolMathInitialTwo,
    arrayKeySymbolMathInitialTwo.length
)

keySymbolMath(
    arrayKeySymbolMathInitialTwo,
    dictSymbolMathInitialTwo,
    dictSymbolMathInitialTwoEquals
);

/*
 * +-----------------------+
 * |dicSymbolMath Advanced |
 * +-----------------------+
 */
counterItemSymbol = 0;
arrayKeySymbolMathAdvanced.forEach(key => {
    counterItemSymbol++;
    dictSymbolMathAdvancedEquals[key].draggable = true;
    dictSymbolMathAdvancedEquals[key].id = 'ItemSymbol' + counterItemSymbol;
    dictSymbolMathAdvancedEquals[key].classList.add('ItemSymbol');
});

appendDictSymbolMath(
    dictSymbolMathAdvancedEquals,
    arrayH1Advanced,
    arrayH1SymbolAdvanced,
    arrayKeySymbolMathAdvanced,
    arrayKeySymbolMathAdvanced.length
)

keySymbolMath(
    arrayKeySymbolMathAdvanced,
    dictSymbolMathAdvanced,
    dictSymbolMathAdvancedEquals
);

/*
 * +----------------------------------+
 * | Update Symbols Math on DialogBox |
 * +----------------------------------+
 */
function appendSymbolsMath(arrayKeySymbolMath, flag, valueHTML, dictSymbol, length_array=6){
    if(valueHTML){
        if (flag){
            valueHTML.innerHTML = '';
            arrayKeySymbolMath.forEach(key => {
                valueHTML.appendChild(dictSymbol[key].cloneNode(true));
            });
        }else{
            valueHTML.innerHTML = '';
            arrayKeySymbolMath.slice(0, length_array).forEach(key => {
                valueHTML.appendChild(dictSymbol[key].cloneNode(true));
            });
        }
    }else{
        console.error('ERROR valueHTML = ' + valueHTML);
    }
}

/*
 * +---------------------------------------------------------------+
 * //----------------------- 14.09.2025---------------------------//
 * | 1. Вирівнювання елементів на сторінці. (в колонку і в рядок) =|
 * | 2. Адаптація під мобільні пристрої. ==========================|
 * | 3. Оновлення адаптації при зміні екрана. =====================|
 * | 4. Стилізація кнопок. ========================================|
 * | 5. Рухомі елементи. ==========================================|
 * | 6. Стилізація рухомих елементів. =============================|
 * | 7. Видалення елементів DOM. ==================================|
 * | 8. Оновлення Фону DOM. =======================================|
 * +---------------------------------------------------------------+
 */
function updateVariable(marker=true){
    if (marker){
        flagButtonInitialOne = false;
        flagButtonInitialTwo = false;
        flagButtonAdvanced = false;
    }
    InputEquation = "";
    dictOutputServerCheck = {};
    dictTransferDataSER = {};
    dictOutputServer = {};
    arrayInputEQ = [];
    counter_eq_input = 0;
    count_eq = 0;
    setTimeout(() => {
        divContentLocally.innerHTML = '';
        divContentLocallyInput.innerHTML = '';
        dictTabel.td_1.innerHTML = '';
        dictTabel.td_2.innerHTML = '';
        dictTabel.tabel.innerHTML = '';
    }, 100);
}

function elementAlignment(element, elementPosition){
    if(elementPosition){
        element.style.position = 'static';
    }
    element.style.display = 'flex';
    element.style.flexDirection = 'column';
    element.style.alignItems = 'center';
}

function elementAlignmentRow(element, elementPosition){
    if(elementPosition){
        element.style.position = 'static';
    }
    element.style.display = 'flex';
    element.style.flexDirection = 'row';
    element.style.alignItems = 'center';
}

function styleInput(username_id, password_id, marker=true){
    username_id.value = '';
    password_id.value = '';

    if (marker){
        username_id.placeholder = 'username';
        username_id.style.border = '1px solid black';
        password_id.style.border = '1px solid black';

        username_id.addEventListener('focus', () => {username.style.outline = '';});
        password_id.addEventListener('focus', () => {password.style.outline = '';});
        username_id.addEventListener('blur', () => {username.style.outline = 'none';});
        password_id.addEventListener('blur', () => {password.style.outline = 'none';});
    }else{
        username_id.placeholder = 'Не вірне введення';
        username_id.style.border = '1px solid red';
        password_id.style.border = '1px solid red';

        username_id.addEventListener('focus', () => {username.style.outline = '2px solid red';});
        password_id.addEventListener('focus', () => {password.style.outline = '2px solid red';});
        username_id.addEventListener('blur', () => {username.style.outline = 'none';});
        password_id.addEventListener('blur', () => {password.style.outline = 'none';});
    }
}

function adaptationToMobileDevices(element, elementWidth, elementHeight, elementPadding, elementMargin, marker=true, elementId = ''){
    let screenWidth = window.innerWidth;
    if(element){
        switch (true) {
            case (screenWidth > 1200):
                element.style.width = elementWidth + "px";
                element.style.margin = elementMargin + "px";
                element.style.padding = (elementPadding - 3) + "px";
                element.style.height = elementHeight + "px";
                element.style.fontSize = "36px";
                element.style.borderRadius = "40px";

                if (elementId === 'header'){ element.style.fontSize = '23px'; }
                break;
            case (screenWidth > 768):
                element.style.width = (elementWidth * 0.9) + "px";
                element.style.margin = (elementMargin * 0.9) + "px";
                element.style.borderRadius = '40px';
                element.style.flexWrap = "wrap";

                if(elementId === 'ButtonEquationNotFound'){
                    element.style.height = (elementHeight * 0.9) + "px";
                    element.style.fontSize = "32px";
                }else if(elementId === 'tutorial'){
                    element.style.height = "405px"
                }else if (elementId === 'developer'){
                    element.style.width = "40%";
                    element.style.height = "50px";
                }else if (elementId === 'start'){
                    element.style.width = "60%";
                    element.style.height = "60px";
                }else if (elementId === 'equation'){
                    element.style.width = "65%";
                    element.style.height = "50px";
                    element.style.padding = "10px";
                }else if(elementId === 'levelSelection'){
                    element.style.width = "97%";
                    element.style.height = "55px";
                    element.style.padding = "13px";
                }else if(marker){
                    element.style.fontSize = "32px";
                    element.style.padding = (elementPadding * 0.9) + "px";
                    element.style.height = (elementHeight * 0.9) + "px";
                }else if(elementId === 'elDivEquationResult'){
                    element.style.height = 200 + "px";
                    element.style.width = (elementWidth * 0.9) + "px";
                }else{
                    element.style.height = "200px";
                }

                document.body.style.height = "auto";
                document.body.style.height = document.body.scrollHeight + "px"
                break;
            case (screenWidth > 480):
                element.style.width = "90%";
                element.style.borderRadius = '35px';
                element.style.margin = elementMargin + "px";
                element.style.flexWrap = "wrap";

                if(elementId === 'ButtonEquationNotFound'){
                    element.style.width = "40%";
                    element.style.height = "60px";
                }else if(elementId === 'tutorial'){
                    element.style.height = "405px"
                }else if (elementId === 'developer'){
                    element.style.width = "40%";
                    element.style.height = "45px";
                }else if (elementId === 'start'){
                    element.style.width = "60%";
                    element.style.height = "60px";
                }else if (elementId === 'equation'){
                    element.style.width = "65%";
                    element.style.height = "50px";
                    element.style.padding = "10px";
                }else if(elementId === 'levelSelection') {
                    element.style.width = "97%";
                    element.style.height = "55px";
                    element.style.padding = "13px";
                }else if(marker){
                    element.style.fontSize = "20px";
                    element.style.padding = "15px";
                    element.style.height = "57px";
                }else{
                    element.style.height = "200px";
                    document.body.style.height = "auto";
                    document.body.style.height = document.body.scrollHeight + "px"
                }
                break;
            case (screenWidth <= 480):
                element.style.width = "83%";
                element.style.fontSize = "20px";
                element.style.padding = "5px";
                element.style.borderRadius = "30px";
                element.style.margin = elementMargin + "px";
                element.style.flexWrap = "wrap";

                if (elementId === 'ButtonEquationNotFound') {
                    element.style.width = "40%";
                    element.style.height = "60px";
                }else if (elementId === 'tutorial'){
                    element.style.height = "405px"
                }else if (elementId === 'developer'){
                    element.style.width = "40%";
                    element.style.height = "40px";
                }else if (elementId === 'start'){
                    element.style.width = "60%";
                    element.style.height = "50px";
                    element.style.padding = "10px";
                }else if (elementId === 'equation'){
                    element.style.width = "65%";
                    element.style.height = "50px";
                    element.style.padding = "10px";
                }else if (elementId === 'levelSelection') {
                    element.style.width = "97%";
                    element.style.height = "55px";
                    element.style.padding = "13px";
                }else if(marker){
                    element.style.fontSize = "20px";
                    element.style.padding = "15px";
                    element.style.height = "57px";
                }else{
                    element.style.height = "150px";
                    document.body.style.height = "auto";
                    document.body.style.height = document.body.scrollHeight + "px"
                }
                break;
        }
    }else{
        console.error('ERROR valueHTML = ' + element);
    }
}

async function adaptationUpdate(){
    const elements = [
        { id: 'ButtonStart', width: 200, height: 55, padding: 10, margin: 10},
        { id: 'ButtonNextSlide', width: 200, height: 55, padding: 10, margin: 10},
        { id: 'ButtonPreviousSlide', width: 200, height: 55, padding: 10, margin: 10},
        { id: 'buttonMultiplayerEquationGame', width: 220, height: 70, padding: 12, margin: 10},
        { id: 'tutorial', width: 720, height: 405, padding: 5, margin: 10},
        { id: 'buttonOneEquationGame', width: 220, height: 90, padding: 5, margin: 10},
        { id: 'buttonManyEquationGame', width: 220, height: 90, padding: 10, margin: 10},
        { id: 'Initial-1', width: 320, height: 100, padding: 30, margin: 10},
        { id: 'Initial-2', width: 320, height: 100, padding: 25, margin: 10},
        { id: 'Advanced', width: 320, height: 100, padding: 30, margin: 10},
        { id: 'ButtonNext', width: 290, height: 75, padding: 15, margin: 12},
        { id: 'ButtonStartTheGame', width: 250, height: 60, padding: 8, margin: 10},
        { id: 'ButtonEndTheGame', width: 250, height: 60, padding: 8, margin: 10},
        { id: 'ButtonMenu', width: 250, height: 60, padding: 10, margin: 10},
        { id: 'startGame', width: 300, height: 60, padding: 15, margin: 10},
        { id: 'ButtonInput', width: 250, height: 75, padding: 15, margin: 10},
        { id: 'ButtonFeedBack', width: 180, height: 60, padding: 10, margin: 5},
        { id: 'ButtonAnalysis', width: 180, height: 60, padding: 10, margin: 5},
        { id: 'btnDeveloperSql', width: 220, height: 55, padding: 10, margin: 5},
        { id: 'elDivEquationResult', width: widthEquationResult, height: 85, padding: 10, margin: 10}
    ];

    for (const {id, width, height, padding, margin} of elements){
        const element = document.getElementById(id);
        if (element) {
            switch (id) {
                case 'tutorial':
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'tutorial');
                        setTimeout(resolve, 50);
                    });
                    break;
                case "elDivEquationResult":
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'elDivEquationResult');
                        setTimeout(resolve, 50);
                    });
                    break;
                case 'btnDeveloperSql':
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'developer');
                        setTimeout(resolve, 50);
                    });
                    break;
                case 'ButtonStart':
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'start');
                        setTimeout(resolve, 50);
                    });
                    break;
                case 'buttonOneEquationGame':
                case 'buttonManyEquationGame':
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'equation');
                        setTimeout(resolve, 50);
                    })
                    break;
                case 'BeginnerLevel':
                case 'WarmUpLevel':
                case 'MasterLevel':
                case 'ProLevel':
                case 'ExpertLevel':
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin, false, 'levelSelection');
                       setTimeout(resolve, 50);
                    });
                    break;
                default:
                    await new Promise(resolve => {
                        adaptationToMobileDevices(element, width, height, padding, margin);
                        setTimeout(resolve, 50);
                    });
                    break;
            }
            if(id === 'startGame'){
                element.style.marginTop = "350px";
            }
        }
    }
}

// RUN FUNCTION -> adaption Update()
window.addEventListener('resize', async function(){
    document.body.appendChild(divPreloader);
    divPreloader.appendChild(divLoader);

    await adaptationUpdate();
    await new Promise( resolve => {setTimeout(resolve, 100);});

    const preloader = document.getElementById('page-preloader');
    if(preloader){preloader.remove();}
});

function elementDraggable(elementsClass, elementIDFirst, elementIDSecond){
    const items = document.querySelectorAll('.' + elementsClass);
    const target = document.getElementById(elementIDFirst);
    const source = document.getElementById(elementIDSecond);

    // MOUSE
    items.forEach(item => {
        item.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData('text/plain', e.target.id);
            e.target.style.opacity = '0.5';
        });

        item.addEventListener('dragend', (e) => {
            e.target.style.opacity = '1';
        });

        [target, source].forEach((box) => {
            box.addEventListener('dragover', (e) => {
                e.preventDefault();
            });

            box.addEventListener('drop', (e) => {
                e.preventDefault();
                const id = e.dataTransfer.getData('text/plain');
                const targetElement = document.getElementById(id);
                if(targetElement){
                    box.appendChild(targetElement);
                }else{
                    console.error(`Елемент з Id = ${id} не знайдено!`);
                }
            });
        });
    });

    //TOUCH SCREEN
    items.forEach(item => {
        let activeItem = null;

        item.addEventListener('touchstart', (e) => {
            activeItem = e.target;
            activeItem.style.opacity = '0.5';

            const touch = e.touches[0];
            activeItem.style.position = "absolute";
            activeItem.style.zIndex = "1000";
            moveAt(touch.pageX, touch.pageY);

            function moveAt(pageX, pageY) {
                activeItem.style.left = pageX - activeItem.offsetWidth / 2 + "px";
                activeItem.style.top = pageY - activeItem.offsetHeight / 2 + "px";
            }

            document.addEventListener('touchmove', onTouchMove);
            function onTouchMove(event) {
                const touch = event.touches[0];
                moveAt(touch.pageX, touch.pageY);
            }

            document.addEventListener('touchend', function onTouchEnd(event) {
                activeItem.style.opacity = '1';
                activeItem.style.position = "static";
                activeItem.style.zIndex = "1";

                let touch = event.changedTouches[0];
                let dropped = false;

                [target, source].forEach((box) => {
                    const rect = box.getBoundingClientRect();
                    if (
                        touch.pageX >= rect.left &&
                        touch.pageX <= rect.right &&
                        touch.pageY >= rect.top &&
                        touch.pageY <= rect.bottom
                    ) {
                        box.appendChild(activeItem);
                        dropped = true;
                    }
                });

                document.removeEventListener('touchmove', onTouchMove);
                document.removeEventListener('touchend', onTouchEnd);
                activeItem = null;
            }, { once: true });

            e.preventDefault();
        });
    });
}

function elementStyleDialogBox(element){
    element.style.backgroundColor = '#66BAB0';
    element.style.margin = '4px';
    element.style.cursor = 'gap';
    element.style.width = '41px';
    element.style.textAlign = 'center';
    element.style.borderRadius = '20px';
    element.style.color = 'black';
    element.style.boxShadow = '2px 2px 2px 2px rgba(0, 0, 0, 0.5)';
}

function removeElement(elementFirst='', elementSecond='') {
    if(elementFirst || elementSecond){
        let elementFirstDOMElement = null;
        let elementSecondDOMElement = null;

        if (elementFirst) { elementFirstDOMElement = document.getElementById(elementFirst); }
        if (elementSecond) { elementSecondDOMElement = document.getElementById(elementSecond); }
        if(elementFirstDOMElement){ elementFirstDOMElement.remove(); }
        if(elementSecondDOMElement){ elementSecondDOMElement.remove(); }
    }else{
        container.innerHTML = '';
    }
}

function removeSlider(){
    const slider = document.getElementById('Slider');
    if(slider){slider.remove();}
}

function updateServerAndFrontend(){
    correctIncorrectEquation = null;
    dictOutputServerCheck = {};
}

function updateBackgroundImage(marker=false){
    document.body.style.backgroundSize = "cover";
    document.body.style.backgroundRepeat = "repeat-y";
    document.body.style.backgroundPosition = "top center";
    document.body.style.backgroundImage = "url('/static/img/backgroundImage.svg')";
    if (marker){
        document.body.style.height = '115vh';
    }
}

function btnEventContentLocally(elementButton, classElement, marker=false){
    if(!elementButton){
        console.error(`Not found element: ${classElement}`);
        return;
    }

    const element = document.querySelector('.' + classElement);
    if(!element){
        console.error(`Not found element: ${classElement}`);
        return;
    }

    if(!marker){
        function toggleMenu(event){
            event.preventDefault();
            event.stopPropagation();
        }
        
        elementButton.addEventListener('mouseenter', function(){
            element.style.display = 'block';
        });
        elementButton.addEventListener('mouseleave', function(event){
            if(!element.contains(event.relatedTarget)){
                element.style.display = 'none';
            }
        });
        element.addEventListener('mouseleave', function(event){
            if(!elementButton.contains(event.relatedTarget)){
                element.style.display = 'none';
            }
        });

        elementButton.addEventListener('click', toggleMenu);
        elementButton.addEventListener('touchstart', toggleMenu);
        elementButton.addEventListener('touchend', toggleMenu);
    }else{
        elementButton.addEventListener('pointerenter', function(){
            element.style.backgroundColor = '#3A85C6';
        })
        elementButton.addEventListener('pointerleave', function(){
            element.style.backgroundColor = 'white';
        });
    }
}


/*
 * +-------------------------------------------------+
 * //-------------------- 13.09.2025 ---------------//
 * | 1. Розрахунок відсотків "виграшу" і "програшу". |
 * | 2. Створення даних для відображення графічно. ==|
 * +-------------------------------------------------+
 */
function secondNumbersToPercentage(numberEquationComputer, numberEquationInputUser){
    const x = Math.round(numberEquationInputUser * 100 / numberEquationComputer);
    return [100 - x, x]
}

function exponentialScale(equationsInput, equationsComputer){
    let resultExp = [];

    function pushObjectInArray(number, type){
        let arrayObjectsAxis = [];

        for(let i = 0 ; i < number; i++){
            if(type === 'success'){
                if (i < 3){
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 2)));
                }else if (i < 6){
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 1.5)));
                }else{
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 1.2)));
                }
            }else if (type === 'failure'){
                if (i < 3){
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 1.8)));
                }else if (i < 6){
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 1.4)));
                }else{
                    arrayObjectsAxis.push(Math.round(Math.pow(i, 1.1)));
                }
            }
        }
        return arrayObjectsAxis;
    }

    const arrayObjectInputUser = pushObjectInArray(equationsInput, 'success');
    const arrayObjectComputer = pushObjectInArray(equationsComputer, 'failure');

    resultExp.push(arrayObjectInputUser);
    resultExp.push(arrayObjectComputer);
    return resultExp;
}

function bubbleScale(equationsInput, equationsComputer, coefficientRadius){
    let resultArray = [];

    function pushObjectInArray(number, type){
        let arrayObjectsAxis = [];

        for(let i = 0; i < number; i++){
            if (type === 'success'){
                const object = {
                    x: i + 1,
                    y: Math.floor((i * 2 * 120 - remainingTime) / 60),
                    r: Math.round(5 * coefficientRadius * (i + 1))
                }
                arrayObjectsAxis.push(object);
            }else{
                const object = {
                    x: i + 1,
                    y: Math.floor((i * 2 * 120 - maxTime) / 60),
                    r: Math.round(5 * coefficientRadius * (i + 1))
                }
                arrayObjectsAxis.push(object);
            }
        }
        return arrayObjectsAxis;
    }

    const arrayObjectInputUser = pushObjectInArray(equationsInput, 'success');
    const arrayObjectComputer = pushObjectInArray(equationsComputer, 'failure');

    resultArray.push(arrayObjectInputUser);
    resultArray.push(arrayObjectComputer);
    return resultArray;
}

/*
 * +--------------------------------------------------------+
 * //---------------------- 13.09.2025 --------------------//
 * | 1. Функції сортування даних сервера перед надсиланням. |
 * | 2. Функції надсилання й отримання даних. ==============|
 * +--------------------------------------------------------+
 */
function dataVerification(flagDataVerification){
    InputEquation = "";
    resultContentText = "";
    if(flagDataVerification){
        elDivEquationResultContentText = document.getElementById('elDivEquationResult');
        elDivEquationResultContentText = JSON.stringify(elDivEquationResultContentText.innerText);
        for(let i = 0; i < elDivEquationResultContentText.length; i++){
            if(elDivEquationResultContentText[i] !== "\\" && elDivEquationResultContentText[i] !== "n"){
                resultContentText += elDivEquationResultContentText[i];
            }
        }
        elDivEquationResult.innerHTML = '';
        InputEquation = resultContentText;
    }else{
        elDivEquationResult.innerHTML = '';
    }
}

async function addSubBr(){
    try{
        const response = await fetch('/add_sub_br', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            dictOutputServer = await response.json();
        }else{
            console.warn(`HTTP ERROR add_sub_br: ${response.statusText}`);
            return null;
        }

    }catch(error){
        console.error(`Fetch Error: ${error} `);
    }finally {
        console.log('Process Add_Sub_Br finished');
    }
}

async function mulDivBr(){
    try{
        const response = await fetch('/mul_div_br', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            dictOutputServer = await response.json();
        }else{
            console.warn(`HTTP ERROR add_sub_br: ${response.statusText}`);
            return null;
        }

    }catch(error){
        console.error(`Fetch Error: ${error} `);
    }finally {
        console.log('Process Add_Sub_Br finished');
    }
}

async function addSubMulDivBr(){
    try{
        const response = await fetch('/add_sub_mul_div_br', {
            method: 'GET',
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (response.ok) {
            dictOutputServer = await response.json();
        }else{
            console.warn(`HTTP ERROR add_sub_br: ${response.statusText}`);
            return null;
        }

    }catch(error){
        console.error(`Fetch Error: ${error} `);
    }finally {
        console.log('Process Add_Sub_Br finished');
    }
}

async function sendManyEquationCheck(equation){
    try{
        const response = await fetch('/equation_input_in_equations',{
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(equation)
        });

        if(response.ok){
            dictOutputServerCheck = await response.json();
        }else{
            console.warn('HTTP ERROR many equation check');
            return null;
        }
    }catch (error){
        console.error('Помилка: ' + error);
    }finally {
        console.log('success check many equation');
    }
}

async function sendFeedBackSQL(dictTextFeedBAck){
    try{
        const response = await fetch('/feedback_input', {
            method: 'POST',
            headers:{
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dictTextFeedBAck)
        });

        if(!response.ok){
            console.warn('HTTP ERROR FeedBack SQl');
            return null;
        }
    }catch(error){
        console.error('Помилка: '+ error);
    }finally {
        console.log('success write feed back sql');
    }
}

async function sendReadSQL(dictCheckPasswordANDUsername){
    try{
        const response = await fetch('/feedback_read', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(dictCheckPasswordANDUsername)
        });

        if(response.ok){
            dictFeedBackTexts = await response.json();
        }else{
            console.warn('HTTP ERROR READ FeedBack SQL');
            return null;
        }
    }catch (error){
        console.error('Помилка: ' + error);
    }finally {
        console.log('success read feed back sql');
    }
}


async function waitForIntervalToFinish(){
    return new Promise(resolve => {
        const intervalDigits = setInterval(async () => {
            if(Object.keys(dictOutputServer).length > 0){
                if (dictOutputServer['eq'].length > 2){
                    clearInterval(intervalDigits);
                    resolve();
                    return;
                }
            }

            if (isRunning){return}
            isRunning = true;

            if (flagButtonInitialOne){ await addSubBr(); }
            if (flagButtonInitialTwo){ await mulDivBr(); }
            if (flagButtonAdvanced){ await addSubMulDivBr(); }
            digitDisplay = dictOutputServer['digit'].toString();
            console.log('Digits Equation?: ' + digitDisplay);
            isRunning = false;
        }, 100);
    });
}


async function startGame() {
    InputEquation = "";
    dictTransferDataSER = {};

    const easyButton = document.getElementById('Initial-1');
    const mediumButton = document.getElementById('Initial-2');
    const hardButton = document.getElementById('Advanced');

    if (easyButton && mediumButton && hardButton) {
        easyButton.remove();
        mediumButton.remove();
        hardButton.remove();
    }else{
        removeElement();
    }

    await waitForIntervalToFinish();
    count_eq = dictOutputServer['eq'].length;

    counter = document.createElement('div')
    counter.classList.add('card-Counter');
    if (is_colorTheme){ counter.style.color = '#66BAB0'; }
    else{ counter.style.color = 'white'; }

    counter.innerHTML = '0/' + count_eq;
    container.style.top = '0px';
    container.appendChild(counter);
}


function endGame() {
    window.scrollTo(0, 0);
    document.body.style.overflow = 'hidden';
    document.body.style.backgroundRepeat = "no-repeat";
    document.body.style.backgroundImage = "url('/static/img/home.svg')"
    document.body.style.backgroundSize = "contain";
    document.body.style.backgroundPosition = "center 100px";

    const elDivGame = document.createElement('div');
    const elDivGameText = document.createElement('div');
    const myForm  = document.createElement('form');
    const elH1 = document.createElement('h1');
    const elP = document.createElement('p');
    const Button = document.createElement('button');
    const headerContainer = document.createElement('header');
    const headerContentDiv = document.createElement('div');
    const btnLanguageHeader = document.createElement('button');
    const imgLanguageHeader = document.createElement('img');
    const btnThemeHeader = document.createElement('button');
    const imgThemeHeader = document.createElement('img');
    const btnSoundHeader = document.createElement('button');
    const btnAbutUsHeader = document.createElement('button');
    const imgAbutUsHeader = document.createElement('img');
    let screenWidth = window.innerWidth;

    function prLanguageUI(){
        elP.id = 'p-game-content';
        if (is_ukrainian){
            elP.innerText = 'Тренуй пам’ять — рівняння за тебе не вирішить ніхто!';
        }else{
            elP.innerText = 'Train your memory — no one else can solve the equations for you!'
        }
    }

    elDivGame.classList.add('card-game');
    elDivGame.id = 'card-game';
    elDivGameText.classList.add('card-game-text');

    if (is_ukrainian){ elH1.innerText = 'Рівняння пам\'яті'; }
    else{ elH1.innerText = 'Memory equation'; }
    elH1.id = 'animated-h1';
    elDivGameText.appendChild(elH1);
    elDivGameText.appendChild(elP);
    elDivGame.appendChild(elDivGameText);

    elementAlignment(Button, false);
    Button.id = 'button_js'
    if (is_ukrainian){
        Button.innerText = 'Дізнатися більше';
    }else{
        Button.innerText = 'Learn more';
    }
    myForm.id = 'myForm'
    Button.style.fontSize = '24px';
    myForm.appendChild(Button);

    //START BTN CREATE GENERATE_LEVELS_FILES
    btnLanguageHeader.id = 'language';
    btnThemeHeader.id = 'color-theme';
    btnAbutUsHeader.id = 'info';
    btnSoundHeader.id = 'sound';
    //END BTN CREATE GENERATE_LEVELS_FILES

    //LANGUAGE
    imgLanguageHeader.src = '/static/img/language.png';
    imgLanguageHeader.width = 30;
    imgLanguageHeader.height = 30;
    btnLanguageHeader.appendChild(imgLanguageHeader);

    //COLOR-THEME
    if (is_colorTheme){ imgThemeHeader.src = '/static/img/night-mode.png'; }
    else{ imgThemeHeader.src = '/static/img/night-mode-light.png'; }
    imgThemeHeader.width = 30;
    imgThemeHeader.height = 30;
    btnThemeHeader.appendChild(imgThemeHeader);

    //ABOUT-US
    imgAbutUsHeader.src = '/static/img/info.png';
    imgAbutUsHeader.width = 30;
    imgAbutUsHeader.height = 30;
    btnAbutUsHeader.appendChild(imgAbutUsHeader);

    headerContainer.id = 'header';
    headerContainer.style.width = '100%';
    headerContainer.style.height = '80px';
    headerContainer.style.backgroundColor = 'white';
    headerContainer.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.1)';
    headerContainer.style.borderBottom = '1px solid #f0f0f0';

    if (is_colorTheme){ headerContainer.style.backgroundColor = 'white'; }
    else{  headerContainer.style.backgroundColor = '#243447'; }

    headerContentDiv.style.display = 'flex';
    headerContentDiv.style.width = '100%';
    headerContentDiv.style.height = '100%';
    headerContentDiv.style.flexDirection = 'row';
    headerContentDiv.style.alignItems = 'center';
    headerContentDiv.style.justifyContent = 'center';
    headerContentDiv.style.padding = '0 20px';
    headerContentDiv.style.gap = '20px';

    headerContentDiv.appendChild(btnLanguageHeader);
    headerContentDiv.appendChild(btnThemeHeader);
    headerContentDiv.appendChild(btnSoundHeader);
    headerContentDiv.appendChild(btnAbutUsHeader);
    headerContainer.appendChild(headerContentDiv);

    if(screenWidth >= 1200){
        prLanguageUI();
        container.style.dispaly = 'flex';
        container.style.alignItems = 'center';
        container.style.flexDirection = 'column';
        container.style.top = '100px';
    }else if(screenWidth >= 750){
        prLanguageUI();
        elH1.style.fontSize = '28px';
        elDivGame.style.marginTop = '80px';
        container.style.top = '80px';
        elementAlignment(elDivGame, true);
    }else if(screenWidth > 480){
        prLanguageUI();
        elH1.style.fontSize = '28px';
        elDivGame.style.marginTop = '50px';
        container.style.top = '25px';
        elementAlignment(elDivGame, true);
    }else{
        prLanguageUI();
        elH1.style.fontSize = '28px';
        elDivGame.style.marginTop = '25px';
        container.style.top = '5px';
        elementAlignment(elDivGame, true);
    }
    document.body.prepend(headerContainer);
    container.appendChild(elDivGame);
    container.appendChild(myForm);
    is_colorTheme = !is_colorTheme;
    is_ukrainian = !is_ukrainian;
    language_change();
    color_change();
}


function updateDigits(){
    variableDiv = {};
    variableH1 = {};
    InputEquation = "";
    counterItemDigits = 0;
    elDivDigitsResult.innerHTML = '';

    if(flagButtonInitialOne){
        while(elDivInitialOneSymbolsMath.firstChild){
            elDivInitialOneSymbolsMath.removeChild(elDivInitialOneSymbolsMath.firstChild);
        }
    }

    if (flagButtonInitialTwo){
        while(elDivInitialTwoSymbolsMath.firstChild){
            elDivInitialTwoSymbolsMath.removeChild(elDivInitialTwoSymbolsMath.firstChild);
        }
    }

    if(flagButtonAdvanced){
        while(elDivAdvancedSymbolsMath.firstChild){
            elDivAdvancedSymbolsMath.removeChild(elDivAdvancedSymbolsMath.firstChild);
        }
    }

    for(let i of digitDisplay){
        counterItemDigits++;
        variableDiv[i] = document.createElement('div');
        variableH1[i] = document.createElement('h1');

        variableDiv[i].draggable = true;
        variableDiv[i].id = 'ItemDigit' + counterItemDigits;
        variableDiv[i].classList.add('ItemDigit');

        variableH1[i].innerText = i;
        elementStyleDialogBox(variableH1[i]);
        variableDiv[i].appendChild(variableH1[i]);
        elDivDigitsResult.appendChild(variableDiv[i]);
    }
    elementDraggable(
        'ItemDigit',
        'elDivEquationResult',
        'elDivDigitsResult'
    );

    //symbols append start
    if(flagButtonInitialOne){
        appendSymbolsMath(
            arrayKeySymbolMathInitialOne,
            false,
            elDivInitialOneSymbolsMath,
            dictSymbolMathInitialOne,
            4
        );
        appendSymbolsMath(
            arrayKeySymbolMathInitialOne,
            true,
            elDivInitialOneSymbolsMathEquals, //Equals
            dictSymbolMathInitialOneEquals
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivInitialOneSymbolsMath'
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivInitialOneSymbolsMathEquals' //Equals
        );
    }

    if(flagButtonInitialTwo){
        appendSymbolsMath(
            arrayKeySymbolMathInitialTwo,
            false,
            elDivInitialTwoSymbolsMath,
            dictSymbolMathInitialTwo,
            4
        );
        appendSymbolsMath(
            arrayKeySymbolMathInitialTwo,
            true,
            elDivInitialTwoSymbolsMathEquals, //Equals
            dictSymbolMathInitialTwoEquals
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivInitialTwoSymbolsMath'
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivInitialTwoSymbolsMathEquals' //Equals
        );
    }

    if(flagButtonAdvanced){
        appendSymbolsMath(
            arrayKeySymbolMathAdvanced,
            false,
            elDivAdvancedSymbolsMath,
            dictSymbolMathAdvanced,
            6
        );
        appendSymbolsMath(
            arrayKeySymbolMathAdvanced,
            true,
            elDivAdvancedSymbolsMathEquals, //Equals
            dictSymbolMathAdvancedEquals
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivAdvancedSymbolsMath'
        );
        elementDraggable(
            'ItemSymbol',
            'elDivEquationResult',
            'elDivAdvancedSymbolsMathEquals' //Equals
        );
    }
    //symbols append end
}


function dialogBox(flagDialogBox) {
    if(flagButtonInitialOne){
        counterSymbolsMat = 1;
        widthEquationResult = '600';
        widthDigitsResult = '200px';
        marginTopGeneralLevel = '130px';
        widthTabel = '400px';
        heightTabel = '400px';
    }else if(flagButtonInitialTwo){
        counterSymbolsMat = 2;
        widthEquationResult = '700';
        widthDigitsResult = '300px';
        marginTopGeneralLevel = '140px';
        widthTabel = '600px';
        heightTabel = '400px';
    }else{
        counterSymbolsMat = 2;
        widthEquationResult = '700';
        widthDigitsResult = '300px';
        marginTopGeneralLevel = '140px';
        widthTabel = '600px';
        heightTabel = '400px';
    }
    elDivEquationResult.style.width = widthEquationResult + 'px';

    if(flagDialogBox){
        const basicDiv = document.createElement('div');
        const DivButtonGeneral = document.createElement('div');
        const ButtonInput = document.createElement('button');
        const ButtonNext = document.createElement('button');

        elementAlignment(basicDiv, true);
        basicDiv.style.marginTop = marginTopGeneralLevel;

        elementAlignmentRow(elDivEquationResult, false);
        elDivEquationResult.id = 'elDivEquationResult';
        elDivEquationResult.classList.add('elDivEquationResult');
        adaptationToMobileDevices(elDivEquationResult, widthEquationResult, '80', '10', '20')

        elementAlignmentRow(elDivDigitsResult, false);
        elDivDigitsResult.id = 'elDivDigitsResult';
        elDivDigitsResult.classList.add('elDivDigitsResult');

        elementAlignmentRow(DivButtonGeneral, false);
        DivButtonGeneral.style.margin = '20px';

        ButtonInput.id = 'ButtonInput'
        ButtonNext.id = 'ButtonNext';

        if (is_ukrainian) {
            ButtonInput.innerText = 'Підтвердити';
            ButtonNext.innerText = 'Далі';
        }else{
            ButtonInput.innerText = 'Confirm';
            ButtonNext.innerText = 'Next';
        }

        basicDiv.appendChild(elDivEquationResult);
        basicDiv.appendChild(elDivDigitsResult);

        //symbols append start
        if(flagButtonInitialOne){
            elementAlignmentRow(elDivInitialOneSymbolsMath, false);
            elementAlignmentRow(elDivInitialOneSymbolsMathEquals, false); //Equals

            elDivInitialOneSymbolsMath.id = 'elDivInitialOneSymbolsMath';
            elDivInitialOneSymbolsMathEquals.id = 'elDivInitialOneSymbolsMathEquals'; //Equals

            elDivInitialOneSymbolsMath.classList.add('elDivInitialOneSymbolsMath');
            elDivInitialOneSymbolsMathEquals.classList.add('elDivInitialOneSymbolsMathEquals'); //Equals

            appendSymbolsMath(
                arrayKeySymbolMathInitialOne,
                false,
                elDivInitialOneSymbolsMath,
                dictSymbolMathInitialOne,
                4
            );
            appendSymbolsMath(
                arrayKeySymbolMathInitialOne,
                true,
                elDivInitialOneSymbolsMathEquals, // Equals
                dictSymbolMathInitialOneEquals
            );
            basicDiv.appendChild(elDivInitialOneSymbolsMath);
            basicDiv.appendChild(elDivInitialOneSymbolsMathEquals); // Equals
        }

        if(flagButtonInitialTwo) {
            elementAlignmentRow(elDivInitialTwoSymbolsMath, false);
            elementAlignmentRow(elDivInitialTwoSymbolsMathEquals, false); //Equals

            elDivInitialTwoSymbolsMath.id = 'elDivInitialTwoSymbolsMath';
            elDivInitialTwoSymbolsMathEquals.id = 'elDivInitialTwoSymbolsMathEquals'; //Equals

            elDivInitialTwoSymbolsMath.classList.add('elDivInitialTwoSymbolsMath');
            elDivInitialTwoSymbolsMathEquals.classList.add('elDivInitialTwoSymbolsMathEquals'); //Equals

            appendSymbolsMath(
                arrayKeySymbolMathInitialTwo,
                false,
                elDivInitialTwoSymbolsMath,
                dictSymbolMathInitialTwo,
                4
            );
            appendSymbolsMath(
                arrayKeySymbolMathInitialTwo,
                true,elDivInitialTwoSymbolsMathEquals, //Equals
                dictSymbolMathInitialTwoEquals
            );
            basicDiv.appendChild(elDivInitialTwoSymbolsMath);
            basicDiv.appendChild(elDivInitialTwoSymbolsMathEquals); //Equals
        }

        if(flagButtonAdvanced) {
            elementAlignmentRow(elDivAdvancedSymbolsMath, false);
            elementAlignmentRow(elDivAdvancedSymbolsMathEquals, false); //Equals

            elDivAdvancedSymbolsMath.id = 'elDivAdvancedSymbolsMath';
            elDivAdvancedSymbolsMathEquals.id = 'elDivAdvancedSymbolsMathEquals'; //Equals

            elDivAdvancedSymbolsMath.classList.add('elDivAdvancedSymbolsMath');
            elDivAdvancedSymbolsMathEquals.classList.add('elDivAdvancedSymbolsMathEquals'); //Equals

            appendSymbolsMath(
                arrayKeySymbolMathAdvanced,
                false,
                elDivAdvancedSymbolsMath,
                dictSymbolMathAdvanced,
                6
            );
            appendSymbolsMath(
                arrayKeySymbolMathAdvanced,
                true,
                elDivAdvancedSymbolsMathEquals, //equals
                dictSymbolMathAdvancedEquals
            );
            basicDiv.appendChild(elDivAdvancedSymbolsMath);
            basicDiv.appendChild(elDivAdvancedSymbolsMathEquals); //Equals
        }
        //symbols append end

        DivButtonGeneral.appendChild(ButtonInput);
        DivButtonGeneral.appendChild(ButtonNext);
        basicDiv.appendChild(DivButtonGeneral);
        container.appendChild(basicDiv);
        updateDigits(); //ДУЖЕ ВАЖЛИВО (НЕ МІНЯТИ ПОРЯДОК ВИКЛИКІВ ФУНКЦІЇ) !!!!!
    }else{
        updateDigits();
    }
}


async function windowEndDialogBox(){
    const divFinish = document.createElement('div');
    const h1Finish = document.createElement('h1');
    const counterFinish = document.createElement('h1');
    const divResultImgAndText = document.createElement('div');
    const resultImg = document.createElement('img');
    const resultTextImg = document.createElement('span');
    const ButtonDivFinish = document.createElement('div');
    const ButtonMenu = document.createElement('button');
    const ButtonHomePage = document.createElement('button');
    const ButtonRepeat = document.createElement('button');
    const ButtonFeedBack = document.createElement('button');
    const ButtonAnalysis = document.createElement('button');
    const divFeedbackAnalysis = document.createElement('div');

    // Розрахунок відсотків користувача
    ResultManyEquation = (counter_eq_input / count_eq) * 100;


    function languageBtn(arrayLabels){
        ButtonMenu.id = 'ButtonMenu';
        ButtonHomePage.id = 'ButtonEndTheGame';
        ButtonRepeat.id = 'ButtonStartTheGame';
        ButtonFeedBack.id = 'ButtonFeedBack';
        ButtonAnalysis.id = 'ButtonAnalysis';
        ButtonMenu.innerText = arrayLabels[0];
        ButtonHomePage.innerText = arrayLabels[1];
        ButtonRepeat.innerText = arrayLabels[2];
        ButtonFeedBack.innerText = arrayLabels[3];
        ButtonAnalysis.innerText = arrayLabels[4];
    }


    function languageCorrectIncorrectEq(arrayLabels){
        if (ResultManyEquation === 100){correctIncorrectEquation = true; ResultText = 'Відмінно';}
        else if (90 < ResultManyEquation && ResultManyEquation < 100){ correctIncorrectEquation = true; ResultText = arrayLabels[0]; }
        else if (80 < ResultManyEquation && ResultManyEquation <= 90){ correctIncorrectEquation = true; ResultText = arrayLabels[1]; }
        else if (70 < ResultManyEquation && ResultManyEquation <= 80){ correctIncorrectEquation = true; ResultText = arrayLabels[2]; }
        else if (60 < ResultManyEquation && ResultManyEquation <= 70){ correctIncorrectEquation = true; ResultText = arrayLabels[3]; }
        else if (50 < ResultManyEquation && ResultManyEquation <= 60){ correctIncorrectEquation = true; ResultText = arrayLabels[4]; }
        else if (40 < ResultManyEquation && ResultManyEquation <= 50){ correctIncorrectEquation = true; ResultText = arrayLabels[5]; }
        else if (30 < ResultManyEquation && ResultManyEquation <= 40){ correctIncorrectEquation = false; ResultText = arrayLabels[6]; }
        else if (20 < ResultManyEquation && ResultManyEquation <= 30){ correctIncorrectEquation = false; ResultText = arrayLabels[7]; }
        else if (10 < ResultManyEquation && ResultManyEquation <= 20){ correctIncorrectEquation = false; ResultText = arrayLabels[8]; }
        else{correctIncorrectEquation = false; ResultText = arrayLabels[9]; }
    }


    if (is_ukrainian){
        languageCorrectIncorrectEq([
            'Відмінно',
            'Відмінно',
            'Відмінно',
            'Добре',
            'Добре',
            'Добре',
            'Погано',
            'Погано',
            'Жахливо',
            'Жахливо'
        ]);
    }else{
        languageCorrectIncorrectEq([
            'Excellent',
            'Excellent',
            'Excellent',
            'Good',
            'Good',
            'Good',
            'Bad',
            'Bad',
            'Terrible',
            'Terrible'
        ]);
    }

    elementAlignment(divFinish, true);
    elementAlignment(h1Finish, false);
    divFinish.style.marginTop = '200px';
    h1Finish.classList.add('fontStylesBold');
    h1Finish.style.color = 'rgb(29, 44, 21)';
    h1Finish.style.fontSize = '50px';
    h1Finish.style.margin = '10px';

    elementAlignment(counterFinish, false);
    if (is_colorTheme){ counterFinish.style.color = '#66BAB0'; }
    else{ counterFinish.style.color = 'white'; }
    counterFinish.style.fontSize = '50px';
    counterFinish.style.margin =  '20px';

    elementAlignmentRow(divResultImgAndText, false);
    divResultImgAndText.style.margin = '10px';
    if(correctIncorrectEquation) {
        if (is_ukrainian){ h1Finish.innerText = 'Ви виграли!'; }
        else{ h1Finish.innerText = 'You won!'; }

        const audioLevelUp = new Audio('/static/audio/level-up.mp3');
        audioLevelUp.volume = 0.8;
        audioLevelUp.play().then(() =>{console.log('Play audio level up.');});

        if (is_colorTheme){ resultImg.src = 'static/img/checkMark.png'; }
        else{ resultImg.src = 'static/img/checkMark-light.png'; }

        resultTextImg.innerText = ResultText;
        counterFinish.innerText = counter_eq_input + '/' + count_eq;

        //Confetti
        const start = () =>{
            setTimeout(function(){
                confetti.start();
            }, 1000);
        }
        const stop = () =>{
            setTimeout(function(){
                confetti.stop();
            }, 5000);
        }

        start();
        stop();
    }else{
        if (is_ukrainian){
            h1Finish.innerText = 'Ви програли!';
        }else{
            h1Finish.innerText = 'You lost!';
        }

        const audioGameOver = new Audio('/static/audio/gameOver.mp3');
        audioGameOver.volume = 0.8;
        audioGameOver.play().then(() =>{console.log('Play audio game over.');});
        resultImg.src = 'static/img/cross.png';
        resultTextImg.innerText = ResultText;
        counterFinish.innerText = counter_eq_input + '/' + count_eq;
    }

    resultImg.style.width = '90px';
    resultImg.style.height = '90px';
    resultTextImg.style.fontSize = '30px';

    if (is_colorTheme){
        h1Finish.style.color= 'rgb(29, 44, 21)';
        resultTextImg.style.color = 'rgb(29, 44, 21)';
    }else{
        h1Finish.style.color= 'white';
        resultTextImg.style.color = 'white';
    }

    elementAlignmentRow(ButtonDivFinish, false);
    elementAlignmentRow(divFeedbackAnalysis, false);
    ButtonDivFinish.style.margin = '20px';

    if (is_ukrainian){
        languageBtn(['Меню', 'Головна', 'Повторити', 'Відгук', 'Аналіз'])
    }else{
        languageBtn(['Menu', 'Home', 'Repeat', 'Review', 'Analysis'])
    }

    divFinish.appendChild(h1Finish);
    divFinish.appendChild(counterFinish);
    divResultImgAndText.appendChild(resultImg);
    divResultImgAndText.appendChild(resultTextImg);
    divFinish.appendChild(divResultImgAndText);
    ButtonDivFinish.appendChild(ButtonRepeat);
    ButtonDivFinish.appendChild(ButtonMenu);
    ButtonDivFinish.appendChild(ButtonHomePage);
    divFinish.appendChild(ButtonDivFinish);
    divFeedbackAnalysis.appendChild(ButtonFeedBack);
    divFeedbackAnalysis.appendChild(ButtonAnalysis);
    divFinish.appendChild(divFeedbackAnalysis);
    container.appendChild(divFinish);
}


function warningEquation(text){
    elDivEquationResult.innerText = text;
    elDivEquationResult.style.fontSize = '36px';
    setTimeout(() =>{
        elDivEquationResult.innerText = "";
    }, 2000);
}


async function checkInputDialogBox() {
    if(flagButtonInitialOne || flagButtonInitialTwo) {
        minLengthCheckInput = 7;
    }else{
        minLengthCheckInput = 9;
    }

    if(InputEquation.length === 2 || InputEquation.length === 1){
        if (is_ukrainian){ warningEquation("Ви нічого не ввели!"); }
        else{ warningEquation("You haven't entered anything!"); }
        updateDigits();
        return;
    }

    if(InputEquation.length >= minLengthCheckInput){
        let flag = false;
        for(let symbol of InputEquation){
            if(symbol === '=') {
                flag = true;
                break;
            }
        }
        await nextEquation();
    }else{
        updateDigits();

        if (is_ukrainian){ warningEquation("Не вірне ведення."); }
        else{ warningEquation("Incorrect handling."); }
    }
}


async function nextEquation(){
    stopTimer();
    document.body.appendChild(divPreloader);
    divPreloader.appendChild(divLoader);

    dictTransferDataSER = {
        input_equation: InputEquation
    }
    await sendManyEquationCheck(dictTransferDataSER);

    const interval = setInterval(() => {
        if(dictOutputServerCheck){
            clearInterval(interval);
            removeElement('loader', 'page-preloader');
        }
    }, 500);

    startTimer();
}


//FIXME слайдер оптимізувати його для телефонів!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
function sliders(){
    divSlider.id = 'Slider';
    divSlider.classList.add('slider');
    buttonSlider.classList.add('sliderBtn');
    divSliderContent.id = 'SliderContent';
    divSliderContent.classList.add('sliderContent');

    imgOneSlider.src = 'static/img/home-icon.svg';
    imgThreeSlider.src = 'static/img/single-player.svg';
    buttonSliderImg.src= 'static/img/slider.svg';

    imgOneSlider.classList.add('element-imgOneSlider');
    imgThreeSlider.classList.add('element-imgThreeSlider');
    buttonSliderImg.classList.add('element-buttonSliderImg');
    buttonSlider.appendChild(buttonSliderImg);

    btnOneLiSlider.classList.add('element-btnOneLiSlider');
    btnOneLiSlider.id = 'EndTheGameSlider';
    btnOneLiSlider.type = 'button';

    btnThreeLiSlider.classList.add('element-btnThreeLiSlider');
    btnThreeLiSlider.id = 'MenuSlider'
    btnThreeLiSlider.type = 'button';

    btnOneLiSlider.appendChild(imgOneSlider);
    btnThreeLiSlider.appendChild(imgThreeSlider);

    liOneSlider.appendChild(btnOneLiSlider);
    liThreeSlider.appendChild(btnThreeLiSlider);

    ulSlider.innerHTML = ''; // Обов'язково очищення списку!
    ulSlider.appendChild(liOneSlider);

    imgTwoSlider.src = 'static/img/new-idea.svg';
    imgTwoSlider.classList.add('element-imgTwoSlider');
    btnTwoLiSlider.classList.add('element-btnTwoLiSlider');
    btnTwoLiSlider.appendChild(imgTwoSlider);

    divContentLocally.classList.add('content-locally');
    btnTwoLiSlider.appendChild(divContentLocally);
    liTwoSlider.appendChild(btnTwoLiSlider);
    ulSlider.appendChild(liTwoSlider);
    ulSlider.appendChild(liThreeSlider);
    divSlider.appendChild(buttonSlider);
    divSliderContent.appendChild(ulSlider);
    divSlider.appendChild(divSliderContent);
    document.body.prepend(divSlider);

    btnEventContentLocally(buttonSlider, 'sliderContent');
    btnEventContentLocally(btnTwoLiSlider, 'content-locally');
    btnEventContentLocally(btnOneLiSlider, 'element-btnOneLiSlider', true);
    btnEventContentLocally(btnTwoLiSlider, 'element-btnTwoLiSlider', true);
    btnEventContentLocally(btnThreeLiSlider, 'element-btnThreeLiSlider', true);

}


function AnalysisUserInputEquation(){
    removeElement();
    document.body.style.overflowY = 'auto'


    function buttonLanguage(arrayLabels){
        ButtonMenu.id = 'ButtonMenu';
        ButtonHomePage.id = 'ButtonEndTheGame';
        ButtonFeedBack.id = 'ButtonFeedBack';
        ButtonRepeat.id = 'ButtonStartTheGame';
        ButtonMenu.innerText = arrayLabels[0];
        ButtonHomePage.innerText = arrayLabels[1];
        ButtonRepeat.innerText = arrayLabels[2];
        ButtonFeedBack.innerText = arrayLabels[3];
    }


    const divFinishAnalysis = document.createElement('div');
    const h1FinishAnalysis = document.createElement('h1');
    const divTabelWrapper = document.createElement('div');
    const ButtonGlobalFinish = document.createElement('div');
    const ButtonDivFinish = document.createElement('div');
    const ButtonMenu = document.createElement('button');
    const ButtonHomePage = document.createElement('button');
    const ButtonRepeat = document.createElement('button');
    const ButtonFeedBack = document.createElement('button');
    const ulContentTabel_1 = document.createElement('ul');
    const ulContentTabel_2 = document.createElement('ul');
    let bubbleDampingCoefficient;

    let labels;
    let label_success;
    let label_defeat;
    let text;
    let text_time;

    const canvasChart = document.createElement('canvas');
    const divWrapperChart = document.createElement('div');
    const divContainerChart = document.createElement('div');
    const divTitleChart = document.createElement('div');
    const h3TitleChart = document.createElement('h3');
    const divChartWrapper  = document.createElement('div');

    const canvasRadar = document.createElement('canvas');
    const divWrapperRadar = document.createElement('div');
    const divContainerRadar = document.createElement('div');
    const divTitleRadar = document.createElement('div');
    const h3TitleRadar = document.createElement('h3');
    const divRadarWrapper = document.createElement('div');

    const canvasBubble = document.createElement('canvas');
    const divWrapperBubble = document.createElement('div');
    const divContainerBubble = document.createElement('div');
    const divTitleBubble = document.createElement('div');
    const h3TitleBubble = document.createElement('h3');
    const divBubbleWrapper = document.createElement('div');

    if (is_ukrainian){
        dictTabel.th_1.innerText = 'Введенні\nрівняння';
        dictTabel.th_2.innerText = 'Рівняння які\nзнайшов\nкомпютер';
    }
    else{
        dictTabel.th_1.innerText = 'Introduction\nequations';
        dictTabel.th_2.innerText = 'Equations\nfound by\nthe computer';
    }

    dictTabel.tr_1.appendChild(dictTabel.th_1)
    dictTabel.tr_1.appendChild(dictTabel.th_2);
    ulContentTabel_1.innerHTML = '';
    ulContentTabel_2.innerHTML = '';

    arrayInputEQ.forEach(eq =>{
        const liContentTabel = document.createElement('li');
        liContentTabel.innerText = eq;
        ulContentTabel_1.appendChild(liContentTabel);
    });
    dictTabel.td_1.appendChild(ulContentTabel_1);

    dictOutputServer['eq'].forEach(eq =>{
        const liContentTabel = document.createElement('li');
        liContentTabel.innerText = eq;
        ulContentTabel_2.appendChild(liContentTabel);
    });
    dictTabel.td_2.appendChild(ulContentTabel_2);

    elementAlignmentRow(ButtonDivFinish, false);
    elementAlignment(ButtonFeedBack, false);

    if (is_ukrainian){
        buttonLanguage(['Меню', 'Головна', 'Повторити', 'Відгук']);
    }else{
        buttonLanguage(['Menu', 'Home', 'Repeat', 'Review']);
    }

    ButtonDivFinish.style.gap = '10px';
    ButtonGlobalFinish.classList.add('ButtonGlobalFinish');
    ButtonDivFinish.appendChild(ButtonMenu);
    ButtonDivFinish.appendChild(ButtonHomePage);
    ButtonDivFinish.appendChild(ButtonRepeat);
    ButtonGlobalFinish.appendChild(ButtonDivFinish);
    ButtonGlobalFinish.appendChild(ButtonFeedBack)

    dictTabel.tr_2.appendChild(dictTabel.td_1);
    dictTabel.tr_2.appendChild(dictTabel.td_2);
    dictTabel.tabel.appendChild(dictTabel.tr_1);
    dictTabel.tabel.appendChild(dictTabel.tr_2);
    divTabelWrapper.classList.add('wrapper');
    divTabelWrapper.style.paddingTop = '30px';
    divTabelWrapper.appendChild(dictTabel.tabel);

    canvasChart.id = 'myChart';
    divWrapperChart.classList.add('wrapper');
    divContainerChart.classList.add('container-chart');
    divTitleChart.classList.add('title-chart');
    divChartWrapper.classList.add('chart-wrapper');

    canvasRadar.id = 'myRadar';
    divWrapperRadar.classList.add('wrapper');
    divContainerRadar.classList.add('container-chart');
    divTitleRadar.classList.add('title-chart');

    canvasBubble.id = 'myBubble';
    divWrapperBubble.classList.add('wrapper');
    divContainerBubble.classList.add('container-chart');
    divTitleBubble.classList.add('title-chart');

    divRadarWrapper.style.width = '500px';
    divRadarWrapper.style.height = '600px';
    divBubbleWrapper.style.width = '600px';
    divBubbleWrapper.style.height = '350px';
    bubbleDampingCoefficient = 0.75;

    if (is_ukrainian){
        h1FinishAnalysis.innerText = 'Результат';
        h3TitleChart.innerText = 'Кругова діограма';
        h3TitleBubble.innerText = 'Кількість рівнянь в залежності від часу';
        h3TitleRadar.innerText = 'Область досягнень';
        labels = ['Рівняння які знайшов комп\'ютер', 'Введенні рівняння'];
        label_success = 'успіх';
        label_defeat = 'поразка';
        text = 'Рівняння';
        text_time = 'Час (хвилини : секунди)';
    }else{
        h1FinishAnalysis.innerText = 'Result';
        h3TitleChart.innerText = 'Circular diagram';
        h3TitleBubble.innerText = 'Number of equations depending on time';
        h3TitleRadar.innerText = 'Area of achievement';
        labels = ['Equations found by the computer', 'Entering equations'];
        label_success = 'success';
        label_defeat = 'defeat';
        text = 'Equation';
        text_time = 'Time (minutes : seconds)';
    }

    if (is_colorTheme){ h1FinishAnalysis.style.color = 'black'; }
    else{ h1FinishAnalysis.style.color= 'white'; }

    divTitleChart.appendChild(h3TitleChart);
    divContainerChart.appendChild(divTitleChart);
    divChartWrapper.appendChild(canvasChart);
    divContainerChart.appendChild(divChartWrapper);
    divWrapperChart.appendChild(divContainerChart);

    divTitleRadar.appendChild(h3TitleRadar);
    divContainerRadar.appendChild(divTitleRadar);
    divRadarWrapper.appendChild(canvasRadar);
    divContainerRadar.appendChild(divRadarWrapper);
    divWrapperRadar.appendChild(divContainerRadar);

    divTitleBubble.appendChild(h3TitleBubble);
    divContainerBubble.appendChild(divTitleBubble);
    divBubbleWrapper.appendChild(canvasBubble);
    divContainerBubble.appendChild(divBubbleWrapper);
    divWrapperBubble.appendChild(divContainerBubble);

    elementAlignment(divFinishAnalysis, false);
    divFinishAnalysis.style.gap = '20px';
    divFinishAnalysis.appendChild(h1FinishAnalysis);
    divFinishAnalysis.appendChild(divWrapperChart);
    divFinishAnalysis.appendChild(divWrapperRadar);
    divFinishAnalysis.appendChild(divWrapperBubble);
    divFinishAnalysis.appendChild(divTabelWrapper);
    divFinishAnalysis.appendChild(ButtonGlobalFinish);
    
    container.style.top = '20px';
    container.appendChild(divFinishAnalysis);

    let values = secondNumbersToPercentage(count_eq, counter_eq_input);
    let BackgroundColorHex = ['#fa0000','#0dbd0d'];
    let myChart = new Chart(document.getElementById('myChart'), {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: BackgroundColorHex,
            }]
        },
        options: {
            responsive: true,
            legend: {
                position: 'bottom',
            },
            plugins: {
                datalabels: {
                    color: "#fff",
                    anchor: "end",
                    align: 'start',
                    offset: -10,
                    borderWidth: 2,
                    borderColor: '#fff',
                    borderRadius: 25,
                    backgroundColor: (context) => {
                        return context.dataset.backgroundColor;
                    },
                    font :{
                        weight: 'bold',
                        size: '12',
                    },
                    formatter: (value) => {
                        return value + '%';
                    }
                }
            }
        },
        plugins: [ChartDataLabels]
    });

    const exponentialGraphScale = exponentialScale(counter_eq_input, count_eq);
    let myRadar = new Chart(document.getElementById('myRadar'), {
        type: 'radar',
        data: {
            labels: dictOutputServer['eq'],
            datasets: [
                {
                    label: label_success,
                    data: exponentialGraphScale[0],
                    borderColor: 'green',
                    borderWidth: 3,
                    backgroundColor: 'rgba(0, 255, 0, 0.4)',
                    pointRadius: 2,
                    pointBackgroundColor: '#fff',
                    tension: 0,
                    fill: true,
                },
                {
                    label: label_defeat,
                    data: exponentialGraphScale[1],
                    borderColor: 'red',
                    backgroundColor: 'rgba(255, 0, 0, 0.2)',
                    pointRadius: 2,
                    pointBackgroundColor: '#fff',
                    borderWidth: 3,
                    tension: 0,
                    fill: true,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    suggestedMin: 0,
                    suggestedMax: dictOutputServer['eq'].length,
                    pointLabels: {
                        display: false
                    }
                }
            }
        }
    });

    const bubbleGraphScale = bubbleScale(counter_eq_input, count_eq, bubbleDampingCoefficient);
    let myBubble = new Chart(document.getElementById('myBubble'), {
        type: 'bubble',
        data: {
            datasets: [
                {
                    label: label_success,
                    data: bubbleGraphScale[0],
                    backgroundColor: 'rgba(0, 255, 0, 0.8)'
                },
                {
                    label: label_defeat,
                    data: bubbleGraphScale[1],
                    backgroundColor: 'rgba(255, 0, 0, 0.4)'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            x: {
                min: 0,
                max: (count_eq - 1) * 2,
                ticks: {
                    stepSize: Math.floor(count_eq / counter_eq_input) / (10 ** 2),
                },
                title: {
                    display: true,
                    text: text,
                }
            },
            y: {
                min: -maxTime * 2,
                max: maxTime * 2,
                ticks: {
                    stepSize: Math.floor(count_eq / counter_eq_input) / 2,
                },
                title: {
                    display: true,
                    text: text_time,
                }
            }
        }
    })
}


function documentDeveloper(){
    document.body.style.overflow = 'auto';
    document.body.style.backgroundRepeat = "repeat";
    const divFinish = document.createElement('div');
    const ButtonGoBack = document.createElement('button');

    ButtonGoBack.id = 'ButtonGoBack';
    divFinish.classList.add('divFinishContent')
    elementAlignment(divFinish, true);

    for(let i = 0; i < dictFeedBackTexts['contents'].length; i++){
        const divContent = document.createElement('div');
        const divLabelSQl = document.createElement('div');
        const divDataSQl = document.createElement('div');

        elementAlignment(divContent);
        divContent.classList.add('divContent');
        divLabelSQl.innerText = `Текст повідомлення:\n ${dictFeedBackTexts['contents'][i][0]}`;
        divDataSQl.innerText = `Дата повідомлення:\n ${dictFeedBackTexts['contents'][i][1]}`;
        divContent.appendChild(divLabelSQl);
        divContent.appendChild(divDataSQl);
        divFinish.appendChild(divContent);
    }

    if (is_ukrainian){
        ButtonGoBack.innerText = 'Повернутись назад';
    }else{
        ButtonGoBack.innerText = 'Go back';
    }
    divFinish.appendChild(ButtonGoBack);
    container.appendChild(divFinish);
}


function NextSlideTutorial(){
    if (is_ukrainian){
        switch (counterTutorial){
            case 1:
                tutorial.src = '/static/tutorialPng_uk/tutorial_slide_2_uk.png';
                break;
            case 2:
                tutorial.src = '/static/tutorialPng_uk/tutorial_slide_3_uk.png';
                break;
            case 3:
                tutorial.src = '/static/tutorialPng_uk/tutorial_slide_4_uk.png';
                break;
            default:
                counterTutorial = 0;
                tutorial.src = '/static/tutorialPng_uk/tutorial_slide_1_uk.png';
                break;
        }
    }else{
        switch (counterTutorial){
            case 1:
                tutorial.src = '/static/tutorialPng_en/tutorial_slide_2_en.png';
                break;
            case 2:
                tutorial.src = '/static/tutorialPng_en/tutorial_slide_3_en.png';
                break;
            case 3:
                tutorial.src = '/static/tutorialPng_en/tutorial_slide_4_en.png';
                break;
            default:
                counterTutorial = 0;
                tutorial.src = '/static/tutorialPng_en/tutorial_slide_1_en.png';
                break;
        }
    }
}


/*
* +----------------------------------------------------------------------+
* //--------------------------- 14.09.2025 -----------------------------//
* | Вхідна точка: Два маркера -> (flagGameDescription, flagGlobalButton) |
* +----------------------------------------------------------------------+
* */
function onClick(){
    if(!container){
        console.warn("Помилка: контейнер 'CARD-container' не знайдено");
        return false;
    }
    document.body.style.height = "100vh";

    if(flagGameDescription) {
        removeElement()
        updateBackgroundImage();
        if (document.querySelector('header')) { document.querySelector('header').remove(); }

        const ButtonStart = document.createElement('button');
        const divButtonTutorial = document.createElement('div');
        const ButtonNextSlide = document.createElement('button');
        const ButtonPreviousSlide = document.createElement('button');
        const ButtonDeveloperSql = document.createElement('button');

        container.style.left = '0';
        elementAlignment(container, false);
        elementAlignmentRow(divButtonTutorial, false);


        function buttonLanguage_1(arrayLabels){
            ButtonNextSlide.id = 'ButtonNextSlide';
            ButtonPreviousSlide.id = 'ButtonPreviousSlide';
            ButtonDeveloperSql.id = 'btnDeveloperSql';
            ButtonNextSlide.innerText = arrayLabels[0];
            ButtonPreviousSlide.innerText = arrayLabels[1];
            ButtonDeveloperSql.innerText = arrayLabels[2];
        }


        tutorial.id = 'tutorial';
        ButtonStart.id = 'ButtonStart';
        elementAlignment(ButtonStart, true);

        if(is_ukrainian){
            ButtonStart.innerText = 'Почати';
            buttonLanguage_1(['Вперед', 'Назад', 'Розробникy']);
            tutorial.src = 'static/tutorialPng_uk/tutorial_slide_1_uk.png';
        }else{
            ButtonStart.innerText = 'Begin';
            buttonLanguage_1(['Next', 'Back', 'Developers']);
            tutorial.src = 'static/tutorialPng_en/tutorial_slide_1_en.png';
        }

        btnAppend.appendChild(ButtonDeveloperSql);
        container.appendChild(tutorial);
        divButtonTutorial.appendChild(ButtonPreviousSlide);
        divButtonTutorial.appendChild(ButtonNextSlide);
        container.appendChild(divButtonTutorial);
        container.appendChild(ButtonStart);
        flagGameDescription = false;
    }else if(!flagGameDescription && flagGlobalButton){
        removeElement();
        removeElement('btnDeveloperSql');

        const easyButton = document.createElement('button');
        const mediumButton = document.createElement('button');
        const hardButton = document.createElement('button');
        const newForm = document.createElement('form');


        function buttonLanguage_2(arrayLabels){
            easyButton.id = 'Initial-1';
            mediumButton.id = 'Initial-2';
            hardButton.id = 'Advanced';
            easyButton.innerText = arrayLabels[0];
            mediumButton.innerText = arrayLabels[1];
            hardButton.innerText = arrayLabels[2];
        }


        if (is_ukrainian){
            buttonLanguage_2(['Початковий - 1', 'Початковий - 2', 'Продвинутий']);
        }else{
            buttonLanguage_2(['Initial - 1', 'Initial - 2', 'Advanced']);
        }

        newForm.id = 'newForm'
        newForm.style.gap = '10px';
        newForm.style.marginTop = '0';
        newForm.appendChild(easyButton);
        newForm.appendChild(mediumButton);
        newForm.appendChild(hardButton);
        elementAlignment(newForm, false);

        container.style.left = '0';
        container.style.top = '150px';
        container.style.paddingBottom = '120px';
        container.appendChild(newForm);
        elementAlignment(container, false);
        flagGlobalButton = false;
    }
}

/*
* +----------------------+
* | Початок відліку часу |
* +----------------------+
* */
function startTimer(){
    console.log('maxTime: ' + maxTime);
    if(intervalTime) clearInterval(intervalTime);
    let oldTimer = document.getElementById('timerDisplay');
    if(oldTimer) oldTimer.remove();

    const timer = document.createElement('div');
    const timeImage = document.createElement('img');
    const timeText = document.createElement('span');

    timer.id = 'timerDisplay';
    timer.classList.add('card-Time');
    timer.style.color = '#66BAB0';
    timeImage.src = '/static/img/clockRes.png'
    timer.appendChild(timeImage);
    timer.appendChild(timeText);
    elementAlignmentRow(timer, false);
    container.appendChild(timer)

    minutes = 0;
    seconds = 0;
    counterTime = 0;

    intervalTime = setInterval(function(){
        counterTime++;
        remainingTime = maxTime - counterTime;
        minutes = Math.floor(remainingTime / 60);
        seconds = remainingTime % 60;
        timeText.innerText = minutes + ':' + seconds;

        if(counterTime >= maxTime){
            clearInterval(intervalTime);
            elDivEquationResult.innerHTML = '';
            removeSlider();
            removeElement();

            const audio = new Audio('/static/audio/gameOver.mp3');
            const gameOver = document.createElement('div');
            const ButtonStartTheGame = document.createElement('button');
            const ButtonEndTheGame = document.createElement('button');
            const ButtonDiv = document.createElement('div');

            audio.volume = 0.8;
            elementAlignmentRow(ButtonDiv, true);
            elementAlignment(gameOver, false);
            gameOver.classList.add('fontStylesBold');
            gameOver.classList.add('stopTimer')
            gameOver.innerText = 'Час вичерпано! Спробуйте знову.';
            ButtonDiv.style.margin = '40px';


            function buttonLanguage(arrayLabels){
                ButtonStartTheGame.id = 'ButtonStartTheGame';
                ButtonEndTheGame.id = 'ButtonEndTheGame';
                ButtonStartTheGame.innerText = arrayLabels[0];
                ButtonEndTheGame.innerText = arrayLabels[1];
            }


            if (is_ukrainian){
                buttonLanguage(['Почати з початку?', 'Вийти з гри']);
            }else{
                buttonLanguage(['Start from the beginning?', 'Exit the game']);
            }

            ButtonDiv.appendChild(ButtonStartTheGame);
            ButtonDiv.appendChild(ButtonEndTheGame);
            container.appendChild(gameOver);
            container.appendChild(ButtonDiv);
            audio.play().then(() =>{console.log('Play sound game over.')});
            adaptationUpdate().then(() =>{console.log('Adaption was successful!');});
        }
    }, 1000);
}

function stopTimer(){
    clearInterval(intervalTime);
}
