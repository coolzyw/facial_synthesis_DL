function changepic(obj) {   
	var newsrc=getObjectURL(obj.files[0]);
    document.getElementById('img_id').src=newsrc;
}

function submitpic() {
    var hair_color = document.getElementById("hair").value;
    var gender = document.getElementById("gender").value;
    var aged = document.getElementById("aging").checked;
    console.log(hair_color)
    console.log(gender);
    console.log(aged);
    var image = document.getElementById("output_img_id");

    dir = "./crop/person0/";
    if (hair_color === "black") {
        image.src = dir+"style1.jpg";
    }
    else if (hair_color === "blond") {
        image.src = dir+"style2.jpg";
    }
    else {
        image.src = dir+"style3.jpg";
    }

    if (gender === "male") {
        image.src = dir +"style4.jpg";
    }

    if (aged === true) {
        image.src = dir + "style5.jpg";
    }

    console.log(image.src);
}

function getObjectURL(file) {
    var url = null ;
    if (window.createObjectURL!=undefined) { // basic
        url = window.createObjectURL(file) ;
    } else if (window.URL!=undefined) { // mozilla(firefox)
       url = window.URL.createObjectURL(file) ;
    } else if (window.webkitURL!=undefined) { // webkit or chrome
       url = window.webkitURL.createObjectURL(file) ;
    }
    return url ;
}


