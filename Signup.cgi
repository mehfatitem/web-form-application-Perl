#!"c:\xampp\perl\bin\perl.exe"

use strict;
use warnings;
use utf8;
use Encode;
no warnings;
use CGI qw(:standart);
use Database;
use Functions;

my $cgi = new CGI();
my $db = Database->new;
my $func = Functions->new;


my $name    = $cgi->param('name');
my $surname = $cgi->param('surname');
my $age     = $cgi->param('age');
my $gender  = $cgi->param('gender');

my $errorMessage = "";

print $cgi->header(-content_type => 'text/plain' ,  -charset => 'utf-8');

if($func->isValExist($name) eq "false"){
	$errorMessage .= "<li>Ad alanı zorunludur!</li>";
}

if($func->isValExist($surname) eq "false"){
	$errorMessage .= "<li>Soyad alanı zorunludur!</li>";
}

if($func->isValExist($age) eq "false"){
	$errorMessage .= "<li>Yaş alanı zorunludur!</li>";
}

if($func->isPositiveInteger($age) eq "false"){
	$errorMessage .= "<li>Yaş değeri pozitif bir tam sayı değeri olmalıdır!</li>";
}

if($gender ne "1" && $gender ne 2){
	$errorMessage .= "<li>Yanlış cinsiyet seçimi yaptınız!</li>";
}

if($func->isValExist($errorMessage) eq "true"){
	$func->displayMessage("danger" , $errorMessage);
}else{
	my $sth = $db->runSql("Select * from person where name = '".$func->trim($name)."' and surname = '".$func->trim($surname)."'");
	my $rows = $sth->rows;
	my $contact = "<b>".$func->trim($name)." ".$func->trim($surname)."</b>";
	$contact = $func->decodeUTF8($contact);
	if($rows>0){
		$func->displayMessage("warning" , $contact." isimli kullanıcı sistemde mevcuttur!");
	}else{
	    my $sth = $db->runSql("INSERT INTO person (name,surname,age,gender) VALUES('$name','$surname','$age', '$gender')");
	    if($sth){
	    	$func->displayMessage("success" , "Kayıt başarıyla eklendi.");
	    }else{
	    	$func->displayMessage("danger" , "Kayıt ekleme esnasında bir hata oluştu!");
	    }
	}
}

