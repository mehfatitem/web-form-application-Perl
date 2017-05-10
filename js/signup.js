var warningMessage = "";

function isExist(val){
	if(val.length == 0)
		return true;
	else
		return false;
}

function parseContent(div , content){
	$("#" + div).html(content);
}

function clearDiv(div){
	$("#" + div).empty();
	makeHidden(div);
}

function makeVisible(div){
	$("#"+div).css("visibility" , "visible");
}

function makeHidden(div){
	$("#"+div).css("visibility" , "hidden");
}

function isInt(n) {
	return n % 1 === 0;
}

function postUrl(url , data , result){
	$.ajax({
		url : url,
		type: "POST",
		data : data,
		success: function(data, textStatus, jqXHR) {
			$("#"+result).html(data);
			$('#listUser').dataTable( {
				"language":{
					"url":"//cdn.datatables.net/plug-ins/1.10.12/i18n/Turkish.json"
				}
		    });
		},
		error: function (jqXHR, textStatus, errorThrown) {
			console.log("Error : " + errorThrown);
		}
    });
}

function displayMessage(messageType , messageText){
	var messageTemplate = "<div class='alert alert-"+messageType+" alert-dismissable'><a href='#'' class='close' data-dismiss='alert' aria-label='close'>×</a>"+messageText+"</div>";
	return messageTemplate;
}

$(document).ready(function(){
	clearDiv("result");
	$("#save").click(function(){
		clearDiv("result");
		
		var name 	= $("#name").val().trim();
		var surname = $("#surname").val().trim();
		var surname = $("#surname").val().trim();
		var age  	= $("#age").val().trim();
		var gender	= $('#gender').val().trim();
		
		if(isExist(name))
			warningMessage += "<li>Ad alanı zorunludur!</li>";
		if(isExist(surname))
			warningMessage += "<li>Soyad alanı zorunludur!</li>";
		if(isExist(age))
			warningMessage += "<li>Yaş alanı zorunludur!</li>";
		if(!isInt(age) || parseInt(age)<=0)
			warningMessage += "<li>Yaş değeri pozitif bir tam sayı değeri olmalıdır!</li>";

		makeVisible("result");

		if(!isExist(warningMessage)){
			messageTemplate = displayMessage("danger" , warningMessage);
			parseContent("result" , messageTemplate);
			warningMessage = "";
		}else{
			var data = {name : name , surname : surname , age : age , gender : gender};
			var url = "/sample_perl_application/Signup.cgi";
			var result = "result";

			postUrl(url, data , result);
		}	
	});
	$("#list-user").click(function(){
		makeVisible("result");
		postUrl("/sample_perl_application/ListUser.cgi" , {operation : "listUser"} , "result");
	});
});
	
