


$(".open-menu-signup").click(function(){
$(".contain-register").removeClass('d-none');
$(".contain-login").addClass("d-none");
});

$(".open-menu-login").click(function(){
        console.log("Click");
$(".contain-register").addClass('d-none');
$(".contain-login").removeClass("d-none");
});