
$(".open-menu-signup").click(function(){
$(".contain-register").removeClass('d-none');
$(".contain-login").addClass("d-none");
});

$(".open-menu-login").click(function(){
        console.log("Click");
$(".contain-register").addClass('d-none');
$(".contain-login").removeClass("d-none");
});

$(".show-following-menu-button").click(function(){
        console.log("click");
$(".contain-find-users").addClass("d-none");
$(".show-following-menu-button").removeClass("not-selected")
$(".show-following-menu-button").addClass("underline")
$(".find-users-menu-button").addClass("not-selected")
$(".find-users-menu-button").removeClass("underline")
$(".contain-following-users").removeClass("d-none"); 
});



$(".find-users-menu-button").click(function(){
        console.log("click");
$(".contain-find-users").removeClass("d-none");
$(".show-following-menu-button").addClass("not-selected")
$(".show-following-menu-button").removeClass("underline")
$(".find-users-menu-button").removeClass("not-selected")
$(".find-users-menu-button").addClass("underline")
$(".contain-following-users").addClass("d-none"); 
});

$(".big-find-users").click(function(){
        console.log("click");
$(".contain-find-users").removeClass("d-none");
$(".show-following-menu-button").addClass("not-selected")
$(".show-following-menu-button").removeClass("underline")
$(".find-users-menu-button").removeClass("not-selected")
$(".find-users-menu-button").addClass("underline")
$(".contain-following-users").addClass("d-none"); 
});



/* This code will be used for news posting to set the value of the url in the modal */ 
$(".post-about-news").click(function(){
/* get the value of the url in that news card and set it to the value of the url in the modal */
$("#content_link").attr("value", $(this).attr('id'));
});