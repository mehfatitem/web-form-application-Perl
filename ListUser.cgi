#!"c:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use utf8;
use Encode;
use CGI qw(:standart);
use Database;
use Functions;

my $cgi = new CGI();
my $db = Database->new;
my $func = Functions->new;

if($cgi->param('operation') eq "listUser"){
	print $cgi->header(-content_type => 'text/plain' ,  -charset => 'utf-8');

	my $gender = "";
	my $name = "";
	my $surname = "";
	my $age = "";
	my $class = "";
	my $counter = 0;

	my $template = "<table id='listUser' class='table table-striped table-bordered' cellspacing='0' width='100%'><caption><b>KULLANICI LİSTESİ</b></caption><thead><tr><th>Ad</th><th>Soyad</th><th>Yaş</th><th>Cinsiyet</th></tr></thead><tbody>";

	my $sth = $db->runSql("SELECT * FROM person ORDER BY id DESC");

	while (my $result = $sth->fetchrow_hashref){
		$name = $func->decodeUTF8($result->{name});
		$surname = $func->decodeUTF8($result->{surname});
		$age = $result->{age};
		if($result->{gender} == 1){
			$gender = "Bay";
		}else{
			$gender = "Bayan";
		}
		
		if($counter % 5 == 0){
			$class = "active";
		}elsif($counter % 5 == 1){
			$class = "success";
		}elsif($counter % 5 == 2 ){
			$class = "danger";
		}elsif($counter % 5 == 3){
			$class = "info";
		}elsif($counter % 5 == 4){
			$class = "warning";
		}

		$template .= "<tr class='".$class."'>";
		$template .= "<td>".$name."</td><td>".$surname."<td>".$age."</td><td>".$gender."</td>";
		$template .= "</tr>";
		$counter++;
	}
	$template .= "</tbody>";
	$template .= "</table>";

	if($counter > 0){  
		print $template;
	}else{
		$func->displayMessage("warning" , "Herhangi bir kayıt bulunamadı!");
	}
}else{
	print "<img src='http://www.404errorpages.com/images/image003.png' alt='404' Error Pages'>";
}
