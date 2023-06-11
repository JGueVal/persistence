#!/bin/bash

proc() {
  resul=$(echo $1 | awk -F '' '{
    conta = 1
    ORS="*"
    do {
      print $conta
      conta++
    } while (conta <= NF)
  }')

  echo $(($resul 1))
  exit 0

}

main() {
  while [ $num -ge 10 ]; do
    step=$(proc $num)
    num=$step
    echo $num
  done
  exit 0
}


read num
main $num

# IVLIVS mppr.
