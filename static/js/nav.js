$(".open-menu-signup").click(function () {
  $(".contain-register").removeClass("d-none").addClass("d-block");
  $(".contain-login").removeClass("d-block").addClass("d-none");
});

$(".open-menu-login").click(function () {
  console.log("Click");
  $(".contain-register").removeClass("d-block").addClass("d-none");
  $(".contain-login").addClass("d-block").removeClass("d-none");
});

$(".show-following-menu-button").click(function () {
  console.log("click");
  $(".contain-find-users").addClass("d-none");
  $(".show-following-menu-button").removeClass("not-selected");
  $(".show-following-menu-button").addClass("underline");
  $(".find-users-menu-button").addClass("not-selected");
  $(".find-users-menu-button").removeClass("underline");
  $(".contain-following-users").removeClass("d-none");
});

$(".find-users-menu-button").click(function () {
  console.log("click");
  $(".contain-find-users").removeClass("d-none");
  $(".show-following-menu-button").addClass("not-selected");
  $(".show-following-menu-button").removeClass("underline");
  $(".find-users-menu-button").removeClass("not-selected");
  $(".find-users-menu-button").addClass("underline");
  $(".contain-following-users").addClass("d-none");
});

$(".big-find-users").click(function () {
  console.log("click");
  $(".contain-find-users").removeClass("d-none");
  $(".show-following-menu-button").addClass("not-selected");
  $(".show-following-menu-button").removeClass("underline");
  $(".find-users-menu-button").removeClass("not-selected");
  $(".find-users-menu-button").addClass("underline");
  $(".contain-following-users").addClass("d-none");
});

/* This code will be used for news posting to set the value of the url in the modal */

$(".post-about-news").click(function () {
  /* get the value of the url in that news card and set it to the value of the url in the modal */
  $("#content_link").attr("value", $(this).attr("id"));
});

/* Validation of register form */
let validate_user = false;
let validate_pass = false;
let letter_check;

function validateUsername() {
  $(".username-messages").removeClass("d-none");

  console.log("clicked");
  let username = $(".validate_username").val();
  let u = username.split("");

  // Check that each character is either a letter or a number
  for (i = 0; i < username.length; i++) {
    if (
      (u[i] >= "a" && u[i] <= "z") ||
      (u[i] >= "A" && u[i] <= "Z") ||
      !isNaN(u[i])
    ) {
      letter_check = true;
      console.log("Letter check is " + letter_check);
    } else {
      console.log("bad character");
      letter_check = false;
      break;
      console.log("Letter check is " + letter_check);
    }
  }

  if (username.length < 4 || username.length > 10) {
    $(".validate_username").css("border", "1px solid red");
    validate_user = false;
    $(".invalid-username-length").removeClass("d-none");
    $(".valid-username-length").addClass("d-none");
  } else if (username.length >= 4 && username.length <= 10) {
    $(".invalid-username-length").addClass("d-none");
    $(".valid-username-length").removeClass("d-none");
  }

  if (letter_check == false) {
    $(".invalid-username-chars").removeClass("d-none");
    $(".valid-username-chars").addClass("d-none");
  } else if (letter_check == true) {
    $(".invalid-username-chars").addClass("d-none");
    $(".valid-username-chars").removeClass("d-none");
  }

  if (username.length >= 4 && username.length <= 10 && letter_check == true) {
    validate_user = true;
    $(".validate_username").css("border", "1px solid green");
  } else {
    validate_user = false;
    $(".validate_username").css("border", "1px solid red");
  }

  // Reset border and messages if nothing is typed
  if (username.length == 0) {
    $(".validate_username").css("border", "1px solid lightgrey");
    $(".username-messages").addClass("d-none");
  }

  enableButton();
}

function validatePassword() {
  $(".password-messages").removeClass("d-none");

  let password = $(".validate_password").val();
  let confirm = $("#password-confirm").val();
  let p = password.split("");

  if (password != confirm) {
    $(".validate_password").css("border", "1px solid red");
    $(".valid-password-match").addClass("d-none");
    $(".invalid-password-match").removeClass("d-none");
    validate_pass = false;
  }
  else {
    $(".invalid-password-match").addClass("d-none");
    $(".valid-password-match").removeClass("d-none");
  }

  if (password.length < 6 && password.length != 0) {
    $(".validate_password").css("border", "1px solid red");
    validate_pass = false;
  } else {
    validate_pass = true;
  }

  let contains_int = false;

  for (i = 0; i < password.length; i++) {
    if (!isNaN(p[i])) {
      contains_int = true;
    }
  }

  if (password.length < 6) {
    $(".invalid-password-length").removeClass("d-none");
    $(".valid-password-length").addClass("d-none");
  } else {
    $(".invalid-password-length").addClass("d-none");
    $(".valid-password-length").removeClass("d-none");
  }

  if (contains_int == true) {
    $(".invalid-password-chars").addClass("d-none");
    $(".valid-password-chars").removeClass("d-none");
  } else {
    $(".invalid-password-chars").removeClass("d-none");
    $(".valid-password-chars").addClass("d-none");
  }

  if (password.length >= 6 && contains_int == false && password.length != 0) {
    $(".validate_password").css("border", "1px solid red");
    validate_pass = false;
  }

  if (password.length >= 6 && contains_int == true && password == confirm) {
    $(".validate_password").css("border", "1px solid green");
    validate_pass = true;
  } else {
    validate_pass = false;
  }
  // Reset border and messages if nothing is typed
  if (password.length == 0) {
    $(".validate_password").css("border", "1px solid lightgrey");
    $(".password-messages").addClass("d-none");
  }
  enableButton();
}

function enableButton() {
  if (validate_user == true && validate_pass == true) {
    $(".register-button").prop("disabled", false);
  } else {
    $(".register-button").prop("disabled", true);
  }
}
