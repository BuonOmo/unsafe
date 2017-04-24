#!/bin/zsh

cd data
tmp_file=`mktemp`

list_merged=list-merged.txt
rm $list_merged

first=true
for current in list*; do
  if $first; then
    first=false
    cat $current > $list_merged
  else
    comm -12 <(sort $list_merged) <(sort $current) > $tmp_file
    cat $tmp_file > $list_merged
  fi
done

threats_merged=threats-merged.csv
rm $threats_merged

first=true
for current in threats*; do
  if $first; then
    first=false
    cat $current > $threats_merged
  else
    comm -12 <(sort $threats_merged) <(sort $current) > $tmp_file
    cat $tmp_file > $threats_merged
  fi
done

rm $tmp_file
