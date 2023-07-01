document.addEventListener('DOMContentLoaded', function() {

    let github_button = document.querySelector("#github");
    github_button.addEventListener('click', function() {
        window.open('https://github.com/nashira26')
    });


    let linkedin_button = document.querySelector("#linkedin");
    linkedin_button.addEventListener('click', function() {
        window.open("https://www.linkedin.com/in/nashira-nasrudeen/" )
    });

    let email_button = document.querySelector("#email");
    email_button.addEventListener('click', function() {
        window.open("https://mail.google.com/mail/?view=cm&source=mailto&to=fathimanashira@gmail.com")
    });
});

