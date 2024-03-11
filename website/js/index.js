const signinURL = './signin';
const signupURL = './signup';
const homeURL = './home';
const libraryURL = './library';
const aboutURL = './about';
const searchURL = './search';

function signup_style(){
    document.getElementById("signup").style.display = "flex"
    document.getElementById("signin").style.display = "none"
}

function signin_style(){
    document.getElementById("signin").style.display = "flex"
    document.getElementById("signup").style.display = "none"
}

function login(){
    document.getElementById("home").style.display = "none"
    document.getElementById("login-register").style.display = "flex"
    document.getElementById("signin").style.display = "flex"
    document.getElementById("signup").style.display = "none"
    document.getElementById("about_section").style.display = "none"
    document.getElementById("library"),style.display = "none"
    document.getElementById("search_section").style.display = "none"
}

function Home(){
    document.getElementById("home").style.display = "block"
    document.getElementById("library_section").style.display = "none"
    document.getElementById("login-register").style.display = "none"
    document.getElementById("about_section").style.display = "none"
    document.getElementById("search_section").style.display = "none"
}

function library(){
    document.getElementById("library_section").style.display = "block"
    document.getElementById("home").style.display = "none"
    document.getElementById("login-register").style.display = "none"
    document.getElementById("about_section").style.display = "none"
    document.getElementById("search_section").style.display = "none"
}

function about(){
    document.getElementById("home").style.display = "none"
    document.getElementById("login-register").style.display = "none"
    document.getElementById("library_section").style.display = "none"
    document.getElementById("about_section").style.display = "block"
    document.getElementById("search_section").style.display = "none"
}

function search(){
    document.getElementById("home").style.display = "none"
    document.getElementById("login-register").style.display = "none"
    document.getElementById("library_section").style.display = "none"
    document.getElementById("search_section").style.display = "block"
    document.getElementById("about_section").style.display = "none"
}