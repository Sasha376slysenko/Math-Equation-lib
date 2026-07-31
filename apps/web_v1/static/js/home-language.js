document.addEventListener('DOMContentLoaded', () => {
    modalLanguage();

    document.addEventListener('click', (event) => {
        if (event.target.closest('#language')){
            language_change();
        }else if (event.target.closest('#color-theme')) {
            color_change();
        }else if (event.target.closest('#sound')){
            soundTrackChange();
        }else if (event.target.closest('#info')) {
            info_abut_us_open();
        }else{
            info_abut_us_close();
        }
    });
});

let is_ukrainian = true;
let is_colorTheme = true;
let is_soundTrack = true;
const audio = new Audio('/static/audio/background.mp3');

// AUDION WHILE TRUE
audio.addEventListener('ended', () => {
    audio.currentTime = 0;
    audio.play().then(() => { console.log('Background music') });
})


function modalLanguage(marker= true){
    const modal_3 = document.getElementById('modal-3');
    if (!modal_3) { return; }

    if (marker){
        modal_3.innerHTML = 'Ласкаво просимо до "Рівняння пам\'яті" - веб-гра, яка допомагає тренувати ваш мозок і покращувати пам\'ять.\n' +
            '                Ця гра розроблена для всіх - як молодих, так і старших, хто хоче підтримувати свою робочу пам\'ять у хорошій формі.<br>\n' +
            '                <br>\n' +
            '                У грі вам дається випадкове число, і ваше завдання - скласти математичне рівняння, використовуючи числа та оператори,\n' +
            '                щоб отримати рівність. Не хвилюйтеся, якщо ви новачок - у грі є зручний навчальний посібник, який все пояснює.<br>\n' +
            '                <br>\n' +
            '                У грі є три рівні:<br>\n' +
            '                <br>\n' +
            '                Початковий – 1: дозволяється використання додавання, віднімання та дужок.<br>\n' +
            '                Початковий – 2: дозволяється використання множення, ділення та дужок.<br>\n' +
            '                Продвинутий: доступні всі основні дії – додавання, віднімання, множення, ділення та дужки.<br>\n' +
            '                <br>\n' +
            '                Це головна особливість нашої гри – не просто розв’язування прикладу, а побачити, скільки різних підходів може бути для одного завдання.<br>\n' +
            '                <br>\n' +
            '                Ідея створення гри належить людині, яка хотіла зробити корисний, цікавий та доступний інструмент для тренування мозку.<br>\n' +
            '                <br>\n' +
            '                Ми плануємо розвивати проект далі – додавати нові рівні, покращувати інтерфейс та робити гру ще зручнішою.<br>\n' +
            '                <br>\n' +
            '                «Рівняння пам’яті» доступна на комп’ютерах, смартфонах, але найзручніше грати на комп’ютері.\n' +
            '                Вам не потрібно нічого встановлювати – просто відкрийте сайт у браузері та почніть грати.<br>\n' +
            '                <br>\n' +
            '                Наша мета – щоб уже за кілька днів ви помітили покращення швидкості ментальної арифметики та пам’яті.\n' +
            '                Приєднуйтесь до гри – і дозвольте своєму мозку активно працювати!<br>';
    }else{
        modal_3.innerHTML = 'Welcome to "Memory equation" – a web game designed to train your brain and improve memory.\n' +
            '                This game is made for everyone – both young and older players who want to keep their working memory sharp.<br>\n' +
            '                <br>\n' +
            '                In the game, you are given a random number, and your task is to create a mathematical equation using numbers and operators\n' +
            '                to achieve equality. Don’t worry if you are new – the game includes a helpful tutorial that explains everything.<br>\n' +
            '                <br>\n' +
            '                The game has three levels:<br>\n' +
            '                <br>\n' +
            '                Beginner – 1: addition, subtraction, and parentheses are allowed.<br>\n' +
            '                Beginner – 2: multiplication, division, and parentheses are allowed.<br>\n' +
            '                Advanced: all basic operations are available – addition, subtraction, multiplication, division, and parentheses.<br>\n' +
            '                <br>\n' +
            '                The main feature of our game is not just solving a single example, but discovering how many different ways of thinking can exist for one task.<br>\n' +
            '                <br>\n' +
            '                The idea for the game came from someone who wanted to create a useful, fun, and accessible tool for brain training.<br>\n' +
            '                <br>\n' +
            '                We plan to continue developing the project – adding new levels, improving the interface, and making the game even more convenient.<br>\n' +
            '                <br>\n' +
            '                "Memory Equations" is available on computers and smartphones, but it is most comfortable to play on a computer.\n' +
            '                There’s nothing to install – just open the website in your browser and start playing.<br>\n' +
            '                <br>\n' +
            '                Our goal is that within just a few days you will notice improvements in mental arithmetic speed and memory.\n' +
            '                Join the game – and let your brain stay active!<br>';
    }
}


function language_change(){
    const modal_1 = document.getElementById('modal-1');
    const feedback_inp = document.getElementById('feedBack-input');
    const ButtonFeedbackInput = document.getElementById('ButtonFeedbackInput');
    const modal_2 = document.getElementById('modal-2');
    const inp_1 = document.getElementById('username');
    const inp_2 = document.getElementById('password');
    const btnFeedBackSql = document.getElementById('btnFeedBackSql');
    const h_1_game_txt = document.getElementById('animated-h1');
    const p_1_game_txt = document.getElementById('p-game-content');
    const btn_1_game_txt = document.getElementById('button_js');

    if (is_ukrainian){
        if (btn_1_game_txt) { btn_1_game_txt.innerText = 'Learn more'; }
        if (h_1_game_txt) { h_1_game_txt.innerText = 'Memory equation'; }
        if (p_1_game_txt) { p_1_game_txt.innerText = 'Train your memory - no one will solve the equation for you!'; }

        if (modal_1) {
            modal_1.innerHTML = `Hello, welcome to the modal window.<br>
            Describe the equation with which you encountered a problem, if any.
            Or evaluate the work if you liked everything.`;
        }
        if (feedback_inp) {
            feedback_inp.placeholder = 'Leave a review';
            feedback_inp.setCustomValidity('Fill in the field');
        }
        if (ButtonFeedbackInput) { ButtonFeedbackInput.innerText = 'Send'; }

        if (modal_2) { modal_2.innerText = 'Hello, this is the developer window. If you are a developer, please enter.'; }
        if (inp_1) { inp_1.setCustomValidity('Fill in the field'); }
        if (inp_2) { inp_2.setCustomValidity('Fill in the field'); }
        if (btnFeedBackSql) { btnFeedBackSql.innerText = 'Confirm'; }

        modalLanguage(false);
    }else{
        if (btn_1_game_txt) { btn_1_game_txt.innerText = 'Дізнатись більше'; }
        if (h_1_game_txt) { h_1_game_txt.innerText = 'Pівняння памʼяті'; }
        if (p_1_game_txt) { p_1_game_txt.innerText = 'Тренуй памʼять - рівняння за тебе не вирішить ніхто!'; }

        if (modal_1) {
            modal_1.innerHTML = `Привіт, вас вітає модальне вікно.<br>
            Опишіть рівність з якою сталась проблема, якщо вона є.
            Або оценіть роботу, якщо все сподобалось.`;
        }
        if (feedback_inp) {
            feedback_inp.placeholder = 'Залишити відгук';
            feedback_inp.setCustomValidity('заповніть поле');
        }
        if (ButtonFeedbackInput) { ButtonFeedbackInput.innerText = 'Надіслати'; }

        if (modal_2) { modal_2.innerText = 'Привіт, це вікно розробника. Якщо ти розробник зайди.'; }
        if (inp_1) { inp_1.setCustomValidity('Заповніть поле'); }
        if (inp_2) { inp_2.setCustomValidity('Заповніть поле'); }
        if (btnFeedBackSql) { btnFeedBackSql.innerText = 'Підтвердити'; }

        modalLanguage();
    }

    if (inp_1) { inp_1.addEventListener('input', () => {inp_1.setCustomValidity('');}); }
    if (inp_2) { inp_2.addEventListener('input', () => {inp_2.setCustomValidity('');}) }
    if (feedback_inp){
        feedback_inp.addEventListener('input', () => {
            feedback_inp.setCustomValidity('');
        });
    }
    is_ukrainian = !is_ukrainian;
}


function info_abut_us_open(){
    const modalAbutUs = document.getElementById('modal-abut-us');
    modalAbutUs.style.display = 'flex';
}
function info_abut_us_close(){
    const modalAbutUs = document.getElementById('modal-abut-us');
    modalAbutUs.style.display = 'none';
}


function color_change(){
    const headerColor = document.getElementById('header');
    const btnLanguage = document.getElementById('language');
    const btnInfo = document.getElementById('info');
    const modalWindow = document.getElementById('modal-feedback');
    const modalWindowContent = document.querySelector('.modal-window-content');
    const modalDeveloper = document.getElementById('modal-developer');
    const modalDeveloperContent = document.querySelector('.modal-content-developer');

    const colorBlack = 'black';
    const colorDarkTheme = "#243447";
    const colorLightTheme = "#ffffff";

    if (is_colorTheme){
        document.body.style.backgroundColor = colorDarkTheme;
        if (headerColor) { headerColor.style.backgroundColor = colorDarkTheme; }
        if (btnLanguage) {btnLanguage.style.color = colorLightTheme; }
        if (btnInfo) {btnInfo.style.color = colorLightTheme; }

        if (modalWindow) {
            modalWindow.style.background = 'linear-gradient(135deg, #0b132b, #1c2d5a, #3a6ea5)';
            modalWindowContent.style.border = '2px solid #3b82f6';
        }
        if (modalDeveloper) {
            modalDeveloper.style.background = 'linear-gradient(0deg, #1f1f2e, #312b4e, #4d3b6f)';
            modalDeveloperContent.style.border = '2px solid rgba(120, 90, 190, 0.4)';
        }
    }else{
        document.body.style.backgroundColor = colorLightTheme;
        if (headerColor) { headerColor.style.backgroundColor = colorLightTheme; }
        if (btnLanguage) { btnLanguage.style.color = colorBlack; }
        if (btnInfo) {btnInfo.style.color = colorBlack; }

        if (modalWindow) {
            modalWindow.style.background = 'linear-gradient(135deg, #e6f4ef, #e2f0fa, #f8f9f5)';
            modalWindowContent.style.border = '3px solid black';
        }
        if (modalDeveloper) {
            modalDeveloper.style.background = 'linear-gradient(135deg, #d3ede2, #b8d9cc, #a2c6bb)';
            modalDeveloperContent.style.border = '3px solid black';
        }
    }
    is_colorTheme = !is_colorTheme;
    soundTrackColorChange();
}


function soundTrackColorChange(){
    const sound = document.getElementById('sound');
    const imgSound = document.createElement('img');

    if (sound && is_soundTrack){
        sound.innerHTML = '';
        imgSound.src= '/static/img/turn_off_music.png';
        imgSound.width = 30;
        imgSound.height = 30;
        sound.appendChild(imgSound);
    }else if (sound && !is_soundTrack){
        sound.innerHTML = '';
        imgSound.src= '/static/img/turn_on_the_music.png';
        imgSound.width = 30;
        imgSound.height = 30;
        sound.appendChild(imgSound);
    }
}


function soundTrackChange(){
    const sound = document.getElementById('sound');
    const imgSound = document.createElement('img');

    if (is_soundTrack){
        sound.innerHTML = '';
        imgSound.src= '/static/img/turn_on_the_music.png';
        imgSound.width = 30;
        imgSound.height = 30;
        sound.appendChild(imgSound);

        if (audio.paused || audio.ended){
            audio.volume = 0.5;
            audio.play().then(() => { console.log('Background music') });
        }
    }else{
        sound.innerHTML = '';
        imgSound.src= '/static/img/turn_off_music.png';
        imgSound.width = 30;
        imgSound.height = 30;
        sound.appendChild(imgSound);
        audio.pause();
    }
    is_soundTrack = !is_soundTrack;
    soundTrackColorChange();
}