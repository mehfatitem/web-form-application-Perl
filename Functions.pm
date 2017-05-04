package Functions;

use utf8;
use Encode;

sub new {
	my ($class, %args) = @_;
	return bless \%args, $class;
}

sub isValExist{
	my ($self , $val) = @_;
	my $returnResult ;
	my $length = length $val;
	if($length>0){
		$returnResult = "true";
	}else{
		$returnResult = "false";
	}
	return $returnResult;
}

sub isPositiveInteger{
	my ($self , $val) = @_;
	my $returnResult;
	if($val =~ /^\d+?$/ && $val>0){
		$returnResult = "true";
	}else{
		$returnResult = "false";
	}		
	return $returnResult;
}

sub decodeUTF8{
	my ($self , $val) = @_;
	return decode("utf8" , $val);
}

sub encodeUTF8{
	my ($self , $val) = @_;
	return encode("utf8" , $val);
}

sub  trim { 
	my ($self , $s) = @_;
	$s =~ s/^\s+|\s+$//g; 
	return $s 
};

sub displayMessage{
	my ($self , $messageType , $messageText) = @_;
	my $messageTemplate = "<div class='alert alert-".$messageType." alert-dismissable'><a href='#'' class='close' data-dismiss='alert' aria-label='close'>×</a>".$messageText."</div>";
	print $messageTemplate;
}
1;