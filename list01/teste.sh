#!/bin/bash


for ((i = 0; i <= 400; i++)); do
    f1=$i
    f2=$((400-$i))
    f3=$(($RANDOM % 400))
    echo "$f1 $f2 $f3" > file
    out1=$(python gerson.py < file)
    out2=$(python ionesio.py < file)
    if [ $out1 != $out2 ]; then
        echo "Saida esperada  = $out1 | Saida ionesio = $out2"
        cat file 
    fi

done
