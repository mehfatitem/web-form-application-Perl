package Database;

use warnings;
use strict;

use DBI;

my $db="sample";
my $host="localhost";
my $user="root";
my $password=""; 

sub new {
	my ($class, %args) = @_;
	return bless \%args, $class;
}

sub openConn{
	my $dbh   = DBI->connect ("DBI:mysql:database=$db:host=$host",$user, $password)  or die "Can't connect to database: $DBI::errstr\n";
	$dbh->do("set NAMES 'utf8'");
	$dbh->do("SET CHARACTER SET utf8");
	$dbh->do("SET COLLATION_CONNECTION='utf8_general_ci'");
	return $dbh;
}

sub runSql{
	my ($self , $sql) = @_;
	my $conn = openConn();
	my $sth = $conn->prepare($sql);
	$sth->execute;
	return $sth;
}
1;

