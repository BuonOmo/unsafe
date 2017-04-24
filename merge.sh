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
    tail -n +2 $current > $threats_merged
  else
    headless_list=mktemp
    tail -n +2 $current > $headless_list
    comm -12 <(sort $threats_merged) <(sort $headless_list) > $tmp_file
    cat $tmp_file > $threats_merged
  fi
done
rm $headless_list

rm $tmp_file
