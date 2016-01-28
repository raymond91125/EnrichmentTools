#!/usr/bin/perl

use strict;
open(my $fh, '>', 'output.txt');
my (@files) = <../input/genesets_golden/*>;
my $dict = "./dictionary_complete100.csv";
my $alpha = "0.01";
foreach my $file (@files) {
  print $fh qq($file\n);
  my $pyreturn = `python hgt_tmp.py $file $dict $alpha 2>&1`;
  print $fh qq($pyreturn\n);
  print $fh qq(#####\n);
  print qq($file\n);
}

close $fh;
